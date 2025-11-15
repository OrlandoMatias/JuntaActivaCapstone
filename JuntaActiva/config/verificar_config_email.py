"""
Script para verificar la configuración de email
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings

print("=" * 60)
print("VERIFICACIÓN DE CONFIGURACIÓN DE EMAIL")
print("=" * 60)
print()

# Verificar variables de entorno
print("1. Variables de Entorno:")
print("-" * 60)
email_user = os.environ.get('EMAIL_HOST_USER', '')
email_pass = os.environ.get('EMAIL_HOST_PASSWORD', '')

if email_user:
    print(f"   ✓ EMAIL_HOST_USER: {email_user}")
else:
    print("   ❌ EMAIL_HOST_USER: No configurado")

if email_pass:
    print(f"   ✓ EMAIL_HOST_PASSWORD: {'*' * len(email_pass)} (configurado)")
else:
    print("   ❌ EMAIL_HOST_PASSWORD: No configurado")

print()

# Verificar configuración de Django
print("2. Configuración de Django:")
print("-" * 60)
print(f"   Backend: {settings.EMAIL_BACKEND}")
print(f"   Host: {settings.EMAIL_HOST}")
print(f"   Port: {settings.EMAIL_PORT}")
print(f"   Use TLS: {settings.EMAIL_USE_TLS}")
print(f"   Host User: {settings.EMAIL_HOST_USER}")
print(f"   From Email: {settings.DEFAULT_FROM_EMAIL}")
print()

# Diagnóstico
print("3. Diagnóstico:")
print("-" * 60)

if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
    print("   ⚠️  MODO CONSOLA ACTIVO")
    print()
    print("   Los emails se imprimen en consola, NO se envían realmente.")
    print()
    print("   Para enviar emails reales:")
    print("   1. Configura las variables de entorno:")
    print("      $env:EMAIL_HOST_USER='tu_email@gmail.com'")
    print("      $env:EMAIL_HOST_PASSWORD='tu_contraseña'")
    print()
    print("   2. REINICIA el servidor:")
    print("      Ctrl+C para detener")
    print("      python manage.py runserver para iniciar")
    print()
elif settings.EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    print("   ✓ MODO SMTP ACTIVO")
    print()
    print("   Los emails se enviarán realmente a los destinatarios.")
    print(f"   Servidor SMTP: {settings.EMAIL_HOST}")
    print(f"   Usuario: {settings.EMAIL_HOST_USER}")
    print()
    print("   ✓ Configuración correcta!")
else:
    print(f"   ⚠️  Backend desconocido: {settings.EMAIL_BACKEND}")

print()
print("=" * 60)
