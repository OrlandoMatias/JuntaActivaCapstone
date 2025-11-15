"""
Script para verificar la configuración de email
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.conf import settings
from django.core.mail import send_mail

print("=" * 60)
print("VERIFICACIÓN DE CONFIGURACIÓN DE EMAIL")
print("=" * 60)

print(f"\n1. Backend de email: {settings.EMAIL_BACKEND}")
print(f"2. Host SMTP: {settings.EMAIL_HOST if hasattr(settings, 'EMAIL_HOST') else 'No configurado'}")
print(f"3. Puerto: {settings.EMAIL_PORT if hasattr(settings, 'EMAIL_PORT') else 'No configurado'}")
print(f"4. Usuario: {settings.EMAIL_HOST_USER}")
print(f"5. Contraseña: {'*' * len(settings.EMAIL_HOST_PASSWORD) if settings.EMAIL_HOST_PASSWORD else 'No configurada'}")
print(f"6. From email: {settings.DEFAULT_FROM_EMAIL}")

if settings.EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    print("\n✓ Configuración SMTP detectada - Los emails se enviarán realmente")
    
    print("\n¿Deseas enviar un email de prueba? (s/n): ", end='')
    respuesta = input().lower()
    
    if respuesta == 's':
        print("\nIngresa el email de destino para la prueba: ", end='')
        email_destino = input()
        
        print(f"\nEnviando email de prueba a {email_destino}...")
        try:
            resultado = send_mail(
                'Email de Prueba - Sistema Junta de Vecinos',
                'Este es un email de prueba del sistema.\n\nSi recibes este mensaje, la configuración es correcta.\n\nSaludos,\nSistema Junta de Vecinos',
                settings.DEFAULT_FROM_EMAIL,
                [email_destino],
                fail_silently=False,
            )
            
            if resultado > 0:
                print(f"✓ Email enviado exitosamente a {email_destino}")
                print("\nRevisa la bandeja de entrada (o spam) del destinatario.")
            else:
                print(f"⚠ No se pudo enviar el email")
        except Exception as e:
            print(f"✗ Error al enviar email: {e}")
    else:
        print("\nPrueba cancelada.")
else:
    print("\n⚠ Usando console backend - Los emails se imprimirán en consola")

print("\n" + "=" * 60)
