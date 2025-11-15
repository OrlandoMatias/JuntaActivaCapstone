import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from gestion.models import Vecino

print("Creando usuarios para vecinos existentes...")
print("=" * 50)

# Obtener vecinos sin usuario
vecinos_sin_usuario = Vecino.objects.filter(user__isnull=True)

if not vecinos_sin_usuario.exists():
    print("✓ Todos los vecinos ya tienen usuario asociado.")
else:
    for vecino in vecinos_sin_usuario:
        # Crear usuario con RUT como username
        username = vecino.rut
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            print(f"⚠ Usuario {username} ya existe, vinculando con vecino...")
            user = User.objects.get(username=username)
        else:
            # Crear nuevo usuario con contraseña por defecto
            user = User.objects.create_user(
                username=username,
                email=vecino.email,
                password='vecino123',  # Contraseña por defecto
                first_name=vecino.nombre,
                last_name=vecino.apellido
            )
            print(f"✓ Usuario creado: {username} (contraseña: vecino123)")
        
        # Vincular usuario con vecino
        vecino.user = user
        vecino.save()
        print(f"  Vinculado con: {vecino.nombre} {vecino.apellido}")

print("\n" + "=" * 50)
print("Proceso completado!")
print("\nCredenciales de acceso:")
print("-" * 50)
print("Admin:")
print("  Usuario: admin")
print("  Contraseña: admin123")
print("\nVecinos existentes:")
print("  Usuario: [RUT del vecino]")
print("  Contraseña: vecino123")
print("=" * 50)
