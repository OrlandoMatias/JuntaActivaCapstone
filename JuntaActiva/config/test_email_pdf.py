"""
Script para probar el envío de email con PDF adjunto
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.mail import EmailMessage
from django.conf import settings
from gestion.models import CertificadoResidencia
from gestion.views import generar_pdf_certificado

print("=" * 60)
print("PRUEBA DE ENVÍO DE EMAIL CON PDF ADJUNTO")
print("=" * 60)

# Buscar un certificado aprobado
certificados = CertificadoResidencia.objects.filter(aprobado=True)

if not certificados.exists():
    print("\n⚠ No hay certificados aprobados en la base de datos.")
    print("  Primero debes aprobar un certificado desde el panel de administración.")
    sys.exit(1)

certificado = certificados.first()

print(f"\n1. Certificado seleccionado:")
print(f"   - Código: {certificado.codigo_certificado}")
print(f"   - Vecino: {certificado.vecino.nombre} {certificado.vecino.apellido}")
print(f"   - Email: {certificado.vecino.email}")

print(f"\n2. Generando PDF del certificado...")
try:
    pdf_data = generar_pdf_certificado(certificado)
    print(f"   ✓ PDF generado exitosamente ({len(pdf_data)} bytes)")
except Exception as e:
    print(f"   ✗ Error al generar PDF: {e}")
    sys.exit(1)

print(f"\n3. Preparando email con PDF adjunto...")
asunto = 'Certificado de Residencia Aprobado - PRUEBA'
mensaje = f"""
Estimado/a {certificado.vecino.nombre} {certificado.vecino.apellido},

Este es un email de PRUEBA del sistema de certificados.

Su solicitud de certificado de residencia ha sido aprobada.

Código de certificado: {certificado.codigo_certificado}
Fecha de solicitud: {certificado.fecha_solicitud.strftime('%d/%m/%Y')}

Adjunto encontrará su certificado en formato PDF con fechas en español.

Saludos cordiales,
Junta de Vecinos
"""

email = EmailMessage(
    asunto,
    mensaje,
    settings.DEFAULT_FROM_EMAIL,
    [certificado.vecino.email],
)

email.attach(
    f'certificado_{certificado.codigo_certificado}.pdf',
    pdf_data,
    'application/pdf'
)

print(f"   ✓ Email preparado")
print(f"   - De: {settings.DEFAULT_FROM_EMAIL}")
print(f"   - Para: {certificado.vecino.email}")
print(f"   - Asunto: {asunto}")
print(f"   - Adjunto: certificado_{certificado.codigo_certificado}.pdf")

print(f"\n4. Enviando email...")
try:
    resultado = email.send(fail_silently=False)
    if resultado > 0:
        print(f"   ✓ Email enviado exitosamente")
        print(f"\n   NOTA: En modo desarrollo, el email se imprime en la consola")
        print(f"         del servidor Django, no se envía realmente.")
    else:
        print(f"   ⚠ No se pudo enviar el email")
except Exception as e:
    print(f"   ✗ Error al enviar email: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ PRUEBA COMPLETADA")
print("=" * 60)
print("\nRevisa la consola del servidor Django para ver el email.")
