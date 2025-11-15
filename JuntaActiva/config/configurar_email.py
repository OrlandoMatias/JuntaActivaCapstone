"""
Script para configurar el envío de emails reales usando Gmail

IMPORTANTE: Para usar Gmail necesitas:
1. Habilitar la verificación en 2 pasos en tu cuenta de Gmail
2. Generar una "Contraseña de aplicación" en: https://myaccount.google.com/apppasswords
3. Usar esa contraseña de aplicación (16 caracteres) en lugar de tu contraseña normal
"""

import os
import sys

print("=" * 60)
print("CONFIGURACIÓN DE EMAIL PARA ENVÍO REAL")
print("=" * 60)
print()
print("Este script te ayudará a configurar el envío de emails reales.")
print()
print("⚠️  IMPORTANTE: Para usar Gmail necesitas:")
print("   1. Habilitar verificación en 2 pasos")
print("   2. Generar una 'Contraseña de aplicación'")
print("   3. Ir a: https://myaccount.google.com/apppasswords")
print()

respuesta = input("¿Ya tienes una contraseña de aplicación de Gmail? (s/n): ").lower()

if respuesta != 's':
    print()
    print("Por favor, sigue estos pasos:")
    print("1. Ve a: https://myaccount.google.com/apppasswords")
    print("2. Selecciona 'Correo' y 'Otro (nombre personalizado)'")
    print("3. Escribe 'Django App' como nombre")
    print("4. Copia la contraseña de 16 caracteres que te dan")
    print("5. Vuelve a ejecutar este script")
    print()
    sys.exit(0)

print()
print("Ingresa tus credenciales de Gmail:")
print()

email = input("Email de Gmail: ").strip()
password = input("Contraseña de aplicación (16 caracteres): ").strip()

if not email or not password:
    print()
    print("❌ Error: Debes ingresar email y contraseña")
    sys.exit(1)

if '@' not in email:
    print()
    print("❌ Error: Email inválido")
    sys.exit(1)

print()
print("Configurando variables de entorno...")
print()

# Configurar variables de entorno para la sesión actual
os.environ['EMAIL_HOST_USER'] = email
os.environ['EMAIL_HOST_PASSWORD'] = password
os.environ['DEFAULT_FROM_EMAIL'] = email

print("✓ Variables de entorno configuradas para esta sesión")
print()
print("=" * 60)
print("CONFIGURACIÓN COMPLETADA")
print("=" * 60)
print()
print(f"Email configurado: {email}")
print()
print("IMPORTANTE: Esta configuración es temporal (solo para esta sesión)")
print()
print("Para hacer la configuración permanente, tienes 2 opciones:")
print()
print("OPCIÓN 1 - PowerShell (Recomendado para Windows):")
print("-" * 60)
print(f"$env:EMAIL_HOST_USER='{email}'")
print(f"$env:EMAIL_HOST_PASSWORD='{password}'")
print(f"$env:DEFAULT_FROM_EMAIL='{email}'")
print()
print("Ejecuta estos comandos en PowerShell antes de iniciar el servidor")
print()
print("OPCIÓN 2 - Archivo .env (Permanente):")
print("-" * 60)
print("Crea un archivo llamado '.env' en la carpeta config con:")
print(f"EMAIL_HOST_USER={email}")
print(f"EMAIL_HOST_PASSWORD={password}")
print(f"DEFAULT_FROM_EMAIL={email}")
print()
print("Luego instala python-decouple: pip install python-decouple")
print()
print("=" * 60)
print()
print("Ahora puedes iniciar el servidor:")
print("python manage.py runserver")
print()
print("Los emails se enviarán realmente a los destinatarios.")
print("=" * 60)
