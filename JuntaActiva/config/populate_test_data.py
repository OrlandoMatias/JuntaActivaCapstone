import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gestion.models import Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia

# Limpiar datos existentes (opcional)
print("Creando datos de prueba...")

# Crear Vecinos
vecinos_data = [
    {
        'rut': '12345678-9',
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'email': 'juan.perez@email.cl',
        'telefono': '+56912345678',
        'direccion': 'Calle Principal 123',
        'es_miembro': True
    },
    {
        'rut': '98765432-1',
        'nombre': 'María',
        'apellido': 'González',
        'email': 'maria.gonzalez@email.cl',
        'telefono': '+56987654321',
        'direccion': 'Avenida Central 456',
        'es_miembro': True
    },
    {
        'rut': '11223344-5',
        'nombre': 'Pedro',
        'apellido': 'Silva',
        'email': 'pedro.silva@email.cl',
        'telefono': '+56911223344',
        'direccion': 'Pasaje Los Aromos 789',
        'es_miembro': False
    }
]

vecinos = []
for data in vecinos_data:
    vecino, created = Vecino.objects.get_or_create(
        rut=data['rut'],
        defaults=data
    )
    vecinos.append(vecino)
    if created:
        print(f"✓ Vecino creado: {vecino.nombre} {vecino.apellido}")
    else:
        print(f"- Vecino ya existe: {vecino.nombre} {vecino.apellido}")

# Crear Proyectos Vecinales
proyectos_data = [
    {
        'nombre': 'Plaza Comunitaria',
        'descripcion': 'Construcción de una plaza con juegos infantiles y áreas verdes para la comunidad',
        'estado': 'pendiente',
        'vecino': vecinos[0]
    },
    {
        'nombre': 'Mejoramiento de Iluminación',
        'descripcion': 'Instalación de nuevas luminarias LED en las calles del sector',
        'estado': 'aprobado',
        'vecino': vecinos[1]
    },
    {
        'nombre': 'Ciclovía Vecinal',
        'descripcion': 'Creación de una ciclovía que conecte el barrio con el metro',
        'estado': 'rechazado',
        'vecino': vecinos[2]
    }
]

for data in proyectos_data:
    proyecto, created = ProyectoVecinal.objects.get_or_create(
        nombre=data['nombre'],
        vecino=data['vecino'],
        defaults=data
    )
    if created:
        print(f"✓ Proyecto creado: {proyecto.nombre}")
    else:
        print(f"- Proyecto ya existe: {proyecto.nombre}")

# Crear Certificados de Residencia
certificados_data = [
    {
        'vecino': vecinos[0],
        'aprobado': True,
        'codigo_certificado': 'CERT-2024-001'
    },
    {
        'vecino': vecinos[1],
        'aprobado': False,
        'codigo_certificado': ''
    },
    {
        'vecino': vecinos[2],
        'aprobado': True,
        'codigo_certificado': 'CERT-2024-002'
    }
]

for data in certificados_data:
    # Verificar si ya existe un certificado para este vecino
    existing = CertificadoResidencia.objects.filter(vecino=data['vecino']).first()
    if not existing:
        certificado = CertificadoResidencia.objects.create(**data)
        print(f"✓ Certificado creado para: {certificado.vecino.nombre}")
    else:
        print(f"- Certificado ya existe para: {existing.vecino.nombre}")

# Crear Actividades
hoy = date.today()
actividades_data = [
    {
        'nombre': 'Taller de Reciclaje',
        'descripcion': 'Aprende a reciclar y crear compost en casa',
        'fecha': hoy + timedelta(days=7),
        'cupos': 20
    },
    {
        'nombre': 'Feria Gastronómica',
        'descripcion': 'Feria de comida típica chilena con emprendedores locales',
        'fecha': hoy + timedelta(days=14),
        'cupos': 50
    },
    {
        'nombre': 'Clase de Yoga Comunitaria',
        'descripcion': 'Sesión de yoga gratuita para todos los vecinos',
        'fecha': hoy + timedelta(days=3),
        'cupos': 15
    }
]

for data in actividades_data:
    actividad, created = Actividad.objects.get_or_create(
        nombre=data['nombre'],
        defaults=data
    )
    if created:
        # Inscribir algunos vecinos
        if actividad.nombre == 'Taller de Reciclaje':
            actividad.inscritos.add(vecinos[0], vecinos[1])
        elif actividad.nombre == 'Clase de Yoga Comunitaria':
            actividad.inscritos.add(vecinos[2])
        print(f"✓ Actividad creada: {actividad.nombre}")
    else:
        print(f"- Actividad ya existe: {actividad.nombre}")

# Crear Noticias
noticias_data = [
    {
        'titulo': 'Bienvenidos al Sistema de Gestión Vecinal',
        'contenido': 'Nos complace anunciar el lanzamiento de nuestro nuevo sistema de gestión vecinal. Aquí podrán registrarse, solicitar certificados, inscribirse en actividades y estar al tanto de todas las novedades de nuestra comunidad.',
        'autor': 'Directorio Junta Vecinal'
    },
    {
        'titulo': 'Próxima Asamblea General',
        'contenido': 'Les recordamos que la próxima asamblea general se realizará el día 20 de este mes a las 19:00 hrs en la sede vecinal. Se tratarán temas importantes sobre los proyectos comunitarios en curso.',
        'autor': 'Secretaría'
    },
    {
        'titulo': 'Horarios de Atención',
        'contenido': 'La sede vecinal estará abierta de lunes a viernes de 10:00 a 18:00 hrs. Para solicitudes de certificados, por favor utilizar el sistema en línea o acercarse en horario de atención.',
        'autor': 'Administración'
    }
]

for data in noticias_data:
    noticia, created = Noticia.objects.get_or_create(
        titulo=data['titulo'],
        defaults=data
    )
    if created:
        print(f"✓ Noticia creada: {noticia.titulo}")
    else:
        print(f"- Noticia ya existe: {noticia.titulo}")

print("\n" + "="*50)
print("Resumen de datos de prueba:")
print("="*50)
print(f"Vecinos: {Vecino.objects.count()}")
print(f"Proyectos: {ProyectoVecinal.objects.count()}")
print(f"Certificados: {CertificadoResidencia.objects.count()}")
print(f"Actividades: {Actividad.objects.count()}")
print(f"Noticias: {Noticia.objects.count()}")
print("="*50)
print("\n✓ Datos de prueba creados exitosamente!")
print("\nCredenciales de acceso al admin:")
print("Usuario: admin")
print("Contraseña: admin123")
print("URL: http://localhost:8000/admin/")
