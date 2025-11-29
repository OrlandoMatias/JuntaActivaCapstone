from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
import uuid
from datetime import datetime, date
import locale
from .models import Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia, EspacioComunitario, ReservaEspacio
from .forms import VecinoForm, ProyectoForm, CertificadoForm, ActividadForm, NoticiaForm

# Configurar locale para fechas en español
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
    except:
        pass  # Si no se puede configurar, usar el locale por defecto


def home(request):
    """Vista de página principal con últimas noticias y próximas actividades"""
    # Obtener últimas 5 noticias ordenadas por fecha
    ultimas_noticias = Noticia.objects.all().order_by('-fecha_publicacion')[:5]
    
    # Obtener próximas 5 actividades ordenadas por fecha
    proximas_actividades = Actividad.objects.all().order_by('fecha')[:5]
    
    context = {
        'ultimas_noticias': ultimas_noticias,
        'proximas_actividades': proximas_actividades,
    }
    
    return render(request, 'gestion/home.html', context)


def login_view(request):
    """Vista personalizada de login con notificaciones pop-up"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor, intenta nuevamente.')
            return redirect('login')
    
    return render(request, 'gestion/login.html')


def registrar_vecino(request):
    """Vista para registro de nuevos vecinos con creación de usuario"""
    if request.method == 'POST':
        form = VecinoForm(request.POST)
        if form.is_valid():
            # Crear usuario de Django
            user = User.objects.create_user(
                username=form.cleaned_data['rut'],  # Usar RUT como username
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['nombre'],
                last_name=form.cleaned_data['apellido']
            )
            
            # Crear vecino y vincular con usuario
            vecino = form.save(commit=False)
            vecino.user = user
            vecino.save()
            
            # Iniciar sesión automáticamente
            login(request, user)
            
            messages.success(request, '¡Registro exitoso! Bienvenido a la comunidad.')
            return redirect('home')
    else:
        form = VecinoForm()
    
    return render(request, 'gestion/vecinos/registrar.html', {'form': form})


@login_required
def lista_vecinos(request):
    """Vista administrativa para listar todos los vecinos y gestionar membresías (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('home')
    
    # Obtener todos los vecinos
    vecinos = Vecino.objects.all().order_by('-fecha_registro')
    
    return render(request, 'gestion/vecinos/lista.html', {'vecinos': vecinos})


@login_required
def cambiar_estado_miembro(request, id):
    """Vista administrativa para cambiar el estado de membresía de un vecino (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    vecino = get_object_or_404(Vecino, id=id)
    
    # Cambiar estado de membresía
    vecino.es_miembro = not vecino.es_miembro
    vecino.save()
    
    # Mensaje de confirmación
    if vecino.es_miembro:
        messages.success(request, f'{vecino.nombre} {vecino.apellido} ahora es miembro de la junta de vecinos.')
        
        # Enviar email de bienvenida
        try:
            asunto = '🎉 ¡Bienvenido a la Junta de Vecinos!'
            mensaje = f"""
Estimado/a {vecino.nombre} {vecino.apellido},

¡Felicitaciones! Su solicitud ha sido APROBADA y ahora es miembro oficial de nuestra Junta de Vecinos.

Como miembro, ahora puede:
✅ Reservar espacios comunitarios
✅ Solicitar certificados de residencia
✅ Postular proyectos vecinales
✅ Inscribirse en actividades
✅ Participar en las decisiones de la comunidad

Datos de su cuenta:
- RUT: {vecino.rut}
- Email: {vecino.email}
- Dirección: {vecino.direccion}

Puede acceder al sistema en: http://127.0.0.1:8000/

¡Bienvenido a nuestra comunidad!

Saludos cordiales,
Junta de Vecinos
"""
            
            send_mail(
                asunto,
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [vecino.email],
                fail_silently=False,
            )
            messages.success(request, 'Email de bienvenida enviado al vecino.')
        except Exception as e:
            print(f"❌ Error al enviar email: {e}")
            messages.warning(request, 'Vecino aprobado, pero no se pudo enviar el email de notificación.')
    else:
        messages.info(request, f'{vecino.nombre} {vecino.apellido} ya no es miembro de la junta de vecinos.')
    
    return redirect('lista_vecinos')


@login_required
def solicitar_certificado(request):
    """Vista para solicitar certificado de residencia (requiere login)"""
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('home')
    
    if request.method == 'POST':
        form = CertificadoForm(request.POST)
        if form.is_valid():
            certificado = form.save(commit=False)
            certificado.vecino = vecino
            certificado.aprobado = False
            certificado.save()
            messages.success(request, 'Solicitud de certificado enviada. Será revisada por un administrador.')
            return redirect('home')
    else:
        form = CertificadoForm()
    
    return render(request, 'gestion/certificados/solicitar.html', {'form': form, 'vecino': vecino})


def listar_noticias(request):
    """Vista para listar todas las noticias"""
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    
    return render(request, 'gestion/noticias/lista.html', {'noticias': noticias})


@login_required
def listar_actividades(request):
    """Vista para listar todas las actividades con cupos disponibles (requiere login)"""
    actividades = Actividad.objects.all().order_by('fecha')
    
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        vecino = None
    
    # Calcular cupos disponibles para cada actividad
    actividades_con_cupos = []
    for actividad in actividades:
        esta_inscrito = vecino and actividad.inscritos.filter(id=vecino.id).exists()
        actividades_con_cupos.append({
            'actividad': actividad,
            'cupos_disponibles': actividad.cupos_disponibles(),
            'esta_inscrito': esta_inscrito,
        })
    
    return render(request, 'gestion/actividades/lista.html', {
        'actividades_con_cupos': actividades_con_cupos,
        'vecino': vecino
    })


@login_required
def inscribirse_actividad(request, id):
    """Vista para inscribirse en una actividad (requiere login)"""
    actividad = get_object_or_404(Actividad, id=id)
    
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('listar_actividades')
    
    # Verificar que existan cupos disponibles
    if not actividad.tiene_cupos_disponibles():
        messages.error(request, f'Lo sentimos, la actividad "{actividad.nombre}" no tiene cupos disponibles.')
        return redirect('listar_actividades')
    
    # Verificar si el vecino ya está inscrito
    if actividad.inscritos.filter(id=vecino.id).exists():
        messages.warning(request, f'Ya estás inscrito en la actividad "{actividad.nombre}".')
        return redirect('listar_actividades')
    
    # Agregar vecino a inscritos
    actividad.inscritos.add(vecino)
    messages.success(request, f'¡Inscripción exitosa en "{actividad.nombre}"!')
    
    return redirect('listar_actividades')


# ============================================
# VISTAS ADMINISTRATIVAS
# ============================================

@login_required
def lista_vecinos(request):
    """Vista administrativa para listar todos los vecinos (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('home')
    
    vecinos = Vecino.objects.all().order_by('apellido', 'nombre')
    
    return render(request, 'gestion/vecinos/lista.html', {'vecinos': vecinos})


@login_required
def cambiar_estado_miembro(request, id):
    """Vista administrativa para cambiar el estado de miembro de un vecino (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    vecino = get_object_or_404(Vecino, id=id)
    
    # Cambiar el estado de miembro (toggle)
    vecino.es_miembro = not vecino.es_miembro
    vecino.save()
    
    # Enviar email de notificación al vecino
    try:
        if vecino.es_miembro:
            asunto = '✅ Bienvenido como Miembro de la Junta de Vecinos'
            mensaje = f"""
Estimado/a {vecino.nombre} {vecino.apellido},

¡Felicitaciones! Ha sido registrado como MIEMBRO de la Junta de Vecinos.

Como miembro, ahora puede:
✅ Postular proyectos vecinales
✅ Participar en actividades exclusivas
✅ Acceder a beneficios especiales

Puede acceder a su cuenta en el sistema para comenzar a postular proyectos.

¡Bienvenido a la comunidad!

Saludos cordiales,
Junta de Vecinos
            """
        else:
            asunto = '⚠️ Estado de Membresía Actualizado'
            mensaje = f"""
Estimado/a {vecino.nombre} {vecino.apellido},

Le informamos que su estado de membresía en la Junta de Vecinos ha sido actualizado.

Actualmente NO es miembro activo de la junta.

Si tiene alguna consulta, por favor contacte a la administración.

Saludos cordiales,
Junta de Vecinos
            """
        
        # Crear y enviar email
        email = EmailMessage(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [vecino.email],
        )
        
        resultado = email.send(fail_silently=False)
        
        if resultado > 0:
            estado_texto = "miembro" if vecino.es_miembro else "no miembro"
            print(f"✓ Email enviado exitosamente a {vecino.email} - Estado: {estado_texto}")
    except Exception as e:
        # Log error pero no bloquear la operación
        import traceback
        print(f"❌ Error al enviar email: {e}")
        print(f"❌ Traceback completo:")
        traceback.print_exc()
    
    estado_texto = "miembro" if vecino.es_miembro else "no miembro"
    messages.success(request, f'{vecino.nombre} {vecino.apellido} ahora es {estado_texto} de la junta. Email enviado.')
    return redirect('lista_vecinos')


@login_required
def listar_certificados(request):
    """Vista para listar certificados (admin ve todos, vecino ve solo los suyos)"""
    if request.user.is_staff:
        # Admin ve todos los certificados
        certificados = CertificadoResidencia.objects.all().order_by('-fecha_solicitud')
    else:
        # Vecino ve solo sus certificados
        try:
            vecino = request.user.vecino
            certificados = CertificadoResidencia.objects.filter(vecino=vecino).order_by('-fecha_solicitud')
        except Vecino.DoesNotExist:
            messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
            return redirect('home')
    
    return render(request, 'gestion/certificados/lista.html', {
        'certificados': certificados,
        'is_admin': request.user.is_staff
    })


def generar_pdf_certificado(certificado):
    """Función auxiliar para generar el PDF del certificado"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    elements = []
    
    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Título
    elements.append(Paragraph("JUNTA DE VECINOS", title_style))
    elements.append(Paragraph("CERTIFICADO DE RESIDENCIA", subtitle_style))
    elements.append(Spacer(1, 0.5*inch))
    
    # Información del certificado
    elements.append(Paragraph(f"<b>Código de Certificado:</b> {certificado.codigo_certificado}", normal_style))
    elements.append(Paragraph(f"<b>Fecha de Emisión:</b> {certificado.fecha_solicitud.strftime('%d de %B de %Y')}", normal_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Cuerpo del certificado
    # Construir dirección completa con comuna
    direccion_completa = certificado.vecino.direccion
    if certificado.vecino.comuna:
        direccion_completa += f", {certificado.vecino.comuna}"
    
    texto_certificado = f"""
    Por medio del presente documento, la Junta de Vecinos certifica que:
    <br/><br/>
    <b>{certificado.vecino.nombre} {certificado.vecino.apellido}</b><br/>
    RUT: <b>{certificado.vecino.rut}</b><br/>
    Email: {certificado.vecino.email}<br/>
    Teléfono: {certificado.vecino.telefono}<br/>
    <br/>
    Reside en la dirección:<br/>
    <b>{direccion_completa}</b>
    <br/><br/>
    Este certificado se emite a solicitud del interesado para los fines que estime conveniente.
    """
    elements.append(Paragraph(texto_certificado, normal_style))
    elements.append(Spacer(1, 0.5*inch))
    
    # Fecha y firma
    elements.append(Spacer(1, 1*inch))
    elements.append(Paragraph(f"Fecha: {datetime.now().strftime('%d de %B de %Y')}", normal_style))
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("_" * 40, normal_style))
    elements.append(Paragraph("Firma y Timbre<br/>Junta de Vecinos", normal_style))
    
    # Construir el PDF
    doc.build(elements)
    
    # Obtener el valor del buffer
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data


@login_required
def aprobar_certificado(request, id):
    """Vista administrativa para aprobar un certificado de residencia (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    certificado = get_object_or_404(CertificadoResidencia, id=id)
    
    # Actualizar aprobado=True
    certificado.aprobado = True
    
    # Generar código único de certificado
    certificado.codigo_certificado = f"CERT-{uuid.uuid4().hex[:8].upper()}"
    certificado.save()
    
    # Generar PDF del certificado
    try:
        pdf_data = generar_pdf_certificado(certificado)
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        messages.error(request, 'Error al generar el certificado PDF.')
        return redirect('listar_certificados')
    
    # Enviar email con PDF adjunto
    try:
        asunto = 'Certificado de Residencia Aprobado'
        mensaje = f"""
Estimado/a {certificado.vecino.nombre} {certificado.vecino.apellido},

Su solicitud de certificado de residencia ha sido aprobada.

Código de certificado: {certificado.codigo_certificado}
Fecha de solicitud: {certificado.fecha_solicitud.strftime('%d/%m/%Y')}

Adjunto encontrará su certificado en formato PDF.
También puede descargarlo desde su cuenta en el sistema.

Saludos cordiales,
Junta de Vecinos
        """
        
        # Crear email con adjunto
        email = EmailMessage(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [certificado.vecino.email],
        )
        
        # Adjuntar PDF
        email.attach(
            f'certificado_{certificado.codigo_certificado}.pdf',
            pdf_data,
            'application/pdf'
        )
        
        # Enviar email
        resultado = email.send(fail_silently=False)
        
        if resultado > 0:
            print(f"✓ Email con PDF adjunto enviado exitosamente a {certificado.vecino.email}")
        else:
            print(f"⚠ No se pudo enviar el email a {certificado.vecino.email}")
    except Exception as e:
        # Log error pero no bloquear la operación
        import traceback
        print(f"❌ Error al enviar email: {e}")
        print(f"❌ Traceback completo:")
        traceback.print_exc()
        messages.warning(request, f'Certificado aprobado, pero no se pudo enviar el email de notificación. Error: {str(e)}')
        messages.success(request, f'Certificado aprobado exitosamente. Código: {certificado.codigo_certificado}')
        return redirect('listar_certificados')
    
    messages.success(request, f'Certificado aprobado exitosamente. Código: {certificado.codigo_certificado}. Email enviado con PDF adjunto.')
    return redirect('listar_certificados')


@login_required
def rechazar_certificado(request, id):
    """Vista administrativa para rechazar un certificado de residencia (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    certificado = get_object_or_404(CertificadoResidencia, id=id)
    
    # Mantener aprobado=False (ya está así por defecto)
    certificado.aprobado = False
    certificado.save()
    
    # Enviar email de notificación al vecino
    try:
        asunto = 'Certificado de Residencia Rechazado'
        mensaje = f"""
Estimado/a {certificado.vecino.nombre} {certificado.vecino.apellido},

Lamentamos informarle que su solicitud de certificado de residencia ha sido rechazada.

Fecha de solicitud: {certificado.fecha_solicitud.strftime('%d/%m/%Y')}

Para más información, por favor contacte a la junta de vecinos.

Saludos cordiales,
Junta de Vecinos
        """
        resultado = send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [certificado.vecino.email],
            fail_silently=False,
        )
        if resultado > 0:
            print(f"✓ Email enviado exitosamente a {certificado.vecino.email}")
    except Exception as e:
        # Log error pero no bloquear la operación
        print(f"❌ Error al enviar email: {e}")
        messages.warning(request, 'Certificado rechazado, pero no se pudo enviar el email de notificación.')
    
    messages.success(request, 'Certificado rechazado. Se ha notificado al vecino.')
    return redirect('listar_certificados')


@login_required
def listar_proyectos(request):
    """Vista para listar proyectos (admin ve todos, vecino ve solo los suyos)"""
    if request.user.is_staff:
        # Admin ve todos los proyectos
        proyectos = ProyectoVecinal.objects.all().order_by('-fecha_postulacion')
    else:
        # Vecino ve solo sus proyectos
        try:
            vecino = request.user.vecino
            proyectos = ProyectoVecinal.objects.filter(vecino=vecino).order_by('-fecha_postulacion')
        except Vecino.DoesNotExist:
            messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
            return redirect('home')
    
    return render(request, 'gestion/proyectos/lista.html', {
        'proyectos': proyectos,
        'is_admin': request.user.is_staff
    })


@login_required
def cambiar_estado_proyecto(request, id):
    """Vista administrativa para cambiar el estado de un proyecto vecinal (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    proyecto = get_object_or_404(ProyectoVecinal, id=id)
    
    # Recibir nuevo estado desde POST
    nuevo_estado = request.POST.get('estado')
    
    if nuevo_estado not in ['pendiente', 'aprobado', 'rechazado']:
        messages.error(request, 'Estado inválido.')
        return redirect('listar_proyectos')
    
    # Actualizar estado del proyecto
    proyecto.estado = nuevo_estado
    proyecto.save()
    
    # Enviar email de notificación al vecino
    try:
        # Personalizar el mensaje según el estado
        if nuevo_estado == 'aprobado':
            asunto = '✅ Proyecto Vecinal Aprobado'
            mensaje = f"""
Estimado/a {proyecto.vecino.nombre} {proyecto.vecino.apellido},

¡Excelentes noticias! Su proyecto vecinal "{proyecto.nombre}" ha sido APROBADO.

📋 Detalles del Proyecto:
- Nombre: {proyecto.nombre}
- Descripción: {proyecto.descripcion}
- Fecha de postulación: {proyecto.fecha_postulacion.strftime('%d de %B de %Y')}
- Estado: Aprobado ✅

Puede ver más detalles de su proyecto en su cuenta del sistema.

¡Felicitaciones por su iniciativa!

Saludos cordiales,
Junta de Vecinos
            """
        elif nuevo_estado == 'rechazado':
            asunto = '❌ Proyecto Vecinal Rechazado'
            mensaje = f"""
Estimado/a {proyecto.vecino.nombre} {proyecto.vecino.apellido},

Lamentamos informarle que su proyecto vecinal "{proyecto.nombre}" ha sido RECHAZADO.

📋 Detalles del Proyecto:
- Nombre: {proyecto.nombre}
- Fecha de postulación: {proyecto.fecha_postulacion.strftime('%d de %B de %Y')}
- Estado: Rechazado ❌

Para más información sobre los motivos del rechazo o para presentar un nuevo proyecto, 
por favor contacte a la junta de vecinos.

Puede ver el estado de sus proyectos en su cuenta del sistema.

Saludos cordiales,
Junta de Vecinos
            """
        else:  # pendiente
            asunto = '⏳ Proyecto Vecinal en Revisión'
            mensaje = f"""
Estimado/a {proyecto.vecino.nombre} {proyecto.vecino.apellido},

Su proyecto vecinal "{proyecto.nombre}" está en estado de REVISIÓN.

📋 Detalles del Proyecto:
- Nombre: {proyecto.nombre}
- Fecha de postulación: {proyecto.fecha_postulacion.strftime('%d de %B de %Y')}
- Estado: Pendiente ⏳

Le notificaremos cuando haya una actualización sobre su proyecto.

Puede ver el estado de sus proyectos en su cuenta del sistema.

Saludos cordiales,
Junta de Vecinos
            """
        
        # Crear y enviar email
        email = EmailMessage(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [proyecto.vecino.email],
        )
        
        resultado = email.send(fail_silently=False)
        
        if resultado > 0:
            print(f"✓ Email enviado exitosamente a {proyecto.vecino.email} - Estado: {nuevo_estado}")
        else:
            print(f"⚠ No se pudo enviar el email a {proyecto.vecino.email}")
    except Exception as e:
        # Log error pero no bloquear la operación
        import traceback
        print(f"❌ Error al enviar email: {e}")
        print(f"❌ Traceback completo:")
        traceback.print_exc()
        messages.warning(request, f'Estado actualizado, pero no se pudo enviar el email de notificación. Error: {str(e)}')
        messages.success(request, f'Estado del proyecto actualizado a "{nuevo_estado}".')
        return redirect('listar_proyectos')
    
    messages.success(request, f'Estado del proyecto actualizado a "{nuevo_estado}". Email enviado al vecino.')
    return redirect('listar_proyectos')


@login_required
def crear_noticia(request):
    """Vista administrativa para crear una nueva noticia (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('home')
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Noticia publicada exitosamente.')
            return redirect('listar_noticias')
    else:
        form = NoticiaForm()
    
    return render(request, 'gestion/noticias/crear.html', {'form': form})


@login_required
def postular_proyecto(request):
    """Vista para postular un proyecto vecinal (requiere login y ser miembro)"""
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('home')
    
    # Validar que el vecino sea miembro de la junta
    if not vecino.es_miembro:
        messages.error(request, '❌ Usted no es miembro de la Junta de Vecinos. Solo los miembros pueden postular proyectos vecinales. Por favor, contacte a la administración para más información.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.vecino = vecino
            proyecto.estado = 'pendiente'
            proyecto.save()
            messages.success(request, 'Proyecto postulado exitosamente. Será revisado por un administrador.')
            return redirect('home')
    else:
        form = ProyectoForm()
    
    return render(request, 'gestion/proyectos/postular.html', {'form': form, 'vecino': vecino})


# ============================================
# VISTAS DE AUTENTICACIÓN
# ============================================

def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')


@login_required
def descargar_certificado_pdf(request, id):
    """Vista para descargar certificado de residencia en PDF"""
    certificado = get_object_or_404(CertificadoResidencia, id=id)
    
    # Verificar permisos: admin o el vecino dueño del certificado
    if not request.user.is_staff:
        try:
            if certificado.vecino != request.user.vecino:
                messages.error(request, 'No tienes permisos para descargar este certificado.')
                return redirect('listar_certificados')
        except Vecino.DoesNotExist:
            messages.error(request, 'No tienes permisos para descargar este certificado.')
            return redirect('home')
    
    # Verificar que el certificado esté aprobado
    if not certificado.aprobado:
        messages.error(request, 'Este certificado aún no ha sido aprobado.')
        return redirect('listar_certificados')
    
    # Generar PDF usando la función auxiliar
    pdf_data = generar_pdf_certificado(certificado)
    
    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{certificado.codigo_certificado}.pdf"'
    response.write(pdf_data)
    
    return response


@login_required
def desinscribirse_actividad(request, id):
    """Vista para desinscribirse de una actividad"""
    actividad = get_object_or_404(Actividad, id=id)
    
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('listar_actividades')
    
    # Verificar si el vecino está inscrito
    if not actividad.inscritos.filter(id=vecino.id).exists():
        messages.warning(request, f'No estás inscrito en la actividad "{actividad.nombre}".')
        return redirect('listar_actividades')
    
    # Remover vecino de inscritos
    actividad.inscritos.remove(vecino)
    messages.success(request, f'Te has desinscrito exitosamente de "{actividad.nombre}". El cupo ha sido liberado.')
    
    return redirect('listar_actividades')



# ============================================
# VISTAS DE RESERVAS DE ESPACIOS
# ============================================

@login_required
def listar_espacios(request):
    """Vista para listar espacios comunitarios disponibles"""
    espacios = EspacioComunitario.objects.filter(activo=True).order_by('tipo', 'nombre')
    
    return render(request, 'gestion/reservas/espacios.html', {'espacios': espacios})


@login_required
def solicitar_reserva(request):
    """Vista para solicitar reserva de un espacio comunitario"""
    # Obtener vecino del usuario actual
    try:
        vecino = request.user.vecino
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('home')
    
    if request.method == 'POST':
        from .forms import ReservaEspacioForm
        form = ReservaEspacioForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.vecino = vecino
            reserva.estado = 'pendiente'
            reserva.save()
            messages.success(request, 'Solicitud de reserva enviada exitosamente. Será revisada por un administrador.')
            return redirect('mis_reservas')
    else:
        from .forms import ReservaEspacioForm
        form = ReservaEspacioForm()
    
    return render(request, 'gestion/reservas/solicitar.html', {'form': form, 'vecino': vecino})


@login_required
def mis_reservas(request):
    """Vista para que el vecino vea sus propias reservas"""
    try:
        vecino = request.user.vecino
        reservas = ReservaEspacio.objects.filter(vecino=vecino).order_by('-fecha_solicitud')
    except Vecino.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de vecino asociado a tu usuario.')
        return redirect('home')
    
    return render(request, 'gestion/reservas/mis_reservas.html', {'reservas': reservas})


@login_required
def gestionar_reservas(request):
    """Vista administrativa para gestionar todas las reservas (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('home')
    
    reservas = ReservaEspacio.objects.all().order_by('-fecha_solicitud')
    
    return render(request, 'gestion/reservas/gestionar.html', {'reservas': reservas})


@login_required
def aprobar_reserva(request, id):
    """Vista administrativa para aprobar una reserva (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    reserva = get_object_or_404(ReservaEspacio, id=id)
    
    # Verificar que no exista otra reserva aprobada para el mismo espacio, fecha y horario
    reservas_conflicto = ReservaEspacio.objects.filter(
        espacio=reserva.espacio,
        fecha=reserva.fecha,
        horario=reserva.horario,
        estado='aprobada'
    ).exclude(id=reserva.id)
    
    if reservas_conflicto.exists():
        messages.error(request, f'No se puede aprobar. Ya existe una reserva aprobada para {reserva.espacio.nombre} el {reserva.fecha.strftime("%d/%m/%Y")} en horario {reserva.get_horario_display()}.')
        return redirect('gestionar_reservas')
    
    # Aprobar reserva
    reserva.estado = 'aprobada'
    reserva.fecha_respuesta = datetime.now()
    reserva.save()
    
    # Enviar email de notificación
    try:
        asunto = '✅ Reserva de Espacio Aprobada'
        mensaje = f"""
Estimado/a {reserva.vecino.nombre} {reserva.vecino.apellido},

¡Excelentes noticias! Su solicitud de reserva ha sido APROBADA.

📋 Detalles de la Reserva:
- Espacio: {reserva.espacio.nombre} ({reserva.espacio.get_tipo_display()})
- Fecha: {reserva.fecha.strftime('%d de %B de %Y')}
- Horario: {reserva.get_horario_display()}
- Motivo: {reserva.motivo}
- Cantidad de personas: {reserva.cantidad_personas}

Por favor, recuerde:
✅ Llegar puntualmente
✅ Respetar el horario asignado
✅ Dejar el espacio limpio y ordenado
✅ Cumplir con las normas de uso del espacio

Puede ver los detalles de su reserva en su cuenta del sistema.

¡Que disfrute del espacio!

Saludos cordiales,
Junta de Vecinos
        """
        
        email = EmailMessage(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [reserva.vecino.email],
        )
        
        resultado = email.send(fail_silently=False)
        
        if resultado > 0:
            print(f"✓ Email de aprobación enviado a {reserva.vecino.email}")
    except Exception as e:
        import traceback
        print(f"❌ Error al enviar email: {e}")
        traceback.print_exc()
        messages.warning(request, 'Reserva aprobada, pero no se pudo enviar el email de notificación.')
        messages.success(request, f'Reserva aprobada exitosamente.')
        return redirect('gestionar_reservas')
    
    messages.success(request, f'Reserva aprobada exitosamente. Email enviado al vecino.')
    return redirect('gestionar_reservas')


@login_required
def rechazar_reserva(request, id):
    """Vista administrativa para rechazar una reserva (solo admin)"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    reserva = get_object_or_404(ReservaEspacio, id=id)
    
    # Rechazar reserva
    reserva.estado = 'rechazada'
    reserva.fecha_respuesta = datetime.now()
    reserva.save()
    
    # Enviar email de notificación
    try:
        asunto = '❌ Reserva de Espacio Rechazada'
        mensaje = f"""
Estimado/a {reserva.vecino.nombre} {reserva.vecino.apellido},

Lamentamos informarle que su solicitud de reserva ha sido RECHAZADA.

📋 Detalles de la Solicitud:
- Espacio: {reserva.espacio.nombre} ({reserva.espacio.get_tipo_display()})
- Fecha: {reserva.fecha.strftime('%d de %B de %Y')}
- Horario: {reserva.get_horario_display()}
- Motivo: {reserva.motivo}

Para más información sobre los motivos del rechazo o para realizar una nueva solicitud,
por favor contacte a la junta de vecinos.

Puede ver el estado de sus reservas en su cuenta del sistema.

Saludos cordiales,
Junta de Vecinos
        """
        
        email = EmailMessage(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [reserva.vecino.email],
        )
        
        resultado = email.send(fail_silently=False)
        
        if resultado > 0:
            print(f"✓ Email de rechazo enviado a {reserva.vecino.email}")
    except Exception as e:
        import traceback
        print(f"❌ Error al enviar email: {e}")
        traceback.print_exc()
        messages.warning(request, 'Reserva rechazada, pero no se pudo enviar el email de notificación.')
    
    messages.success(request, 'Reserva rechazada. Se ha notificado al vecino.')
    return redirect('gestionar_reservas')


@login_required
def cancelar_reserva(request, id):
    """Vista para que el vecino cancele su propia reserva"""
    reserva = get_object_or_404(ReservaEspacio, id=id)
    
    # Verificar permisos: admin o el vecino dueño de la reserva
    if not request.user.is_staff:
        try:
            if reserva.vecino != request.user.vecino:
                messages.error(request, 'No tienes permisos para cancelar esta reserva.')
                return redirect('mis_reservas')
        except Vecino.DoesNotExist:
            messages.error(request, 'No tienes permisos para cancelar esta reserva.')
            return redirect('home')
    
    # Solo se pueden cancelar reservas pendientes o aprobadas
    if reserva.estado not in ['pendiente', 'aprobada']:
        messages.error(request, 'Esta reserva no puede ser cancelada.')
        return redirect('mis_reservas')
    
    reserva.estado = 'cancelada'
    reserva.save()
    
    messages.success(request, 'Reserva cancelada exitosamente.')
    return redirect('mis_reservas')


@login_required
def calendario_reservas(request):
    """Vista para mostrar calendario de reservas disponibles"""
    from datetime import timedelta
    from django.db.models import Q
    
    # Obtener espacios activos
    espacios = EspacioComunitario.objects.filter(activo=True)
    
    # Obtener fecha seleccionada o usar hoy
    fecha_str = request.GET.get('fecha', date.today().isoformat())
    try:
        fecha_seleccionada = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    except:
        fecha_seleccionada = date.today()
    
    # Obtener reservas aprobadas para la fecha seleccionada
    reservas_dia = ReservaEspacio.objects.filter(
        fecha=fecha_seleccionada,
        estado='aprobada'
    ).select_related('espacio', 'vecino')
    
    # Crear diccionario de disponibilidad
    disponibilidad = {}
    for espacio in espacios:
        disponibilidad[espacio.id] = {
            'espacio': espacio,
            'horarios': {}
        }
        for horario_code, horario_nombre in ReservaEspacio.HORARIO_CHOICES:
            reserva_existente = reservas_dia.filter(espacio=espacio, horario=horario_code).first()
            disponibilidad[espacio.id]['horarios'][horario_code] = {
                'nombre': horario_nombre,
                'disponible': not reserva_existente,
                'reserva': reserva_existente
            }
    
    context = {
        'espacios': espacios,
        'fecha_seleccionada': fecha_seleccionada,
        'disponibilidad': disponibilidad,
        'horarios': ReservaEspacio.HORARIO_CHOICES,
    }
    
    return render(request, 'gestion/reservas/calendario.html', context)
