"""
Script para probar el envío de emails

Uso:
    python probar_email.py destinatario@example.com
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("=" * 60)
print("PRUEBA DE ENVÍO DE EMAIL")
print("=" * 60)
print()

# Verificar configuración
if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
    print("⚠️  MODO CONSOLA ACTIVO")
    print("   Los emails se imprimirán en la consola, no se enviarán realmente.")
    print()
    print("   Para enviar emails reales, configura:")
    print("   $env:EMAIL_HOST_USER='tu_email@gmail.com'")
    print("   $env:EMAIL_HOST_PASSWORD='tu_contraseña_de_aplicacion'")
    print()
else:
    print("✓ MODO SMTP ACTIVO")
    print(f"  Servidor: {settings.EMAIL_HOST}")
    print(f"  Usuario: {settings.EMAIL_HOST_USER}")
    print(f"  Puerto: {settings.EMAIL_PORT}")
    print()

# Obtener destinatario
if len(sys.argv) > 1:
    destinatario = sys.argv[1]
else:
    destinatario = input("Ingresa el email de destino: ").strip()

if not destinatario or '@' not in destinatario:
    print("❌ Error: Email inválido")
    sys.exit(1)

print()
print(f"Enviando email de prueba a: {destinatario}")
print()

try:
    resultado = send_mail(
        subject='Prueba de Email - Sistema de Gestión Vecinal',
        message='''
Hola,

Este es un email de prueba del Sistema de Gestión Vecinal.

Si recibes este mensaje, significa que el sistema de emails está funcionando correctamente.

Saludos,
Junta de Vecinos
        ''',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[destinatario],
        fail_silently=False,
    )
    
    if resultado > 0:
        print("✓ Email enviado exitosamente!")
        print()
        if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
            print("  (El email se imprimió arriba en la consola)")
        else:
            print(f"  Revisa la bandeja de entrada de {destinatario}")
            print("  Si no lo ves, revisa la carpeta de spam")
    else:
        print("⚠️  No se pudo enviar el email")
        
except Exception as e:
    print(f"❌ Error al enviar email: {e}")
    print()
    print("Posibles causas:")
    print("- Credenciales incorrectas")
    print("- Contraseña de aplicación no configurada")
    print("- Verificación en 2 pasos no habilitada")
    print("- Problemas de conexión")
    sys.exit(1)

print()
print("=" * 60)
