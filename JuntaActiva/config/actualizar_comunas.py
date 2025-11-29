"""
Script para actualizar el campo comuna de todos los vecinos existentes
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gestion.models import Vecino
from django.contrib.auth.models import User

def actualizar_comunas():
    """Actualiza el campo comuna de todos los vecinos excepto el admin"""
    
    # Obtener el usuario admin
    try:
        admin_user = User.objects.get(username='admin')
        print(f"✓ Usuario admin encontrado: {admin_user.username}")
    except User.DoesNotExist:
        admin_user = None
        print("⚠ No se encontró usuario 'admin'")
    
    # Obtener todos los vecinos
    vecinos = Vecino.objects.all()
    
    if not vecinos.exists():
        print("❌ No hay vecinos en la base de datos")
        return
    
    print(f"\n📊 Total de vecinos encontrados: {vecinos.count()}")
    
    # Actualizar vecinos
    actualizados = 0
    omitidos = 0
    
    for vecino in vecinos:
        # Verificar si el vecino es el admin
        if admin_user and vecino.user == admin_user:
            print(f"⏭  Omitiendo admin: {vecino.nombre} {vecino.apellido}")
            omitidos += 1
            continue
        
        # Actualizar comuna
        vecino.comuna = "San Joaquín"
        vecino.save()
        print(f"✓ Actualizado: {vecino.nombre} {vecino.apellido} - Comuna: {vecino.comuna}")
        actualizados += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Proceso completado:")
    print(f"   - Vecinos actualizados: {actualizados}")
    print(f"   - Vecinos omitidos (admin): {omitidos}")
    print(f"{'='*50}")

if __name__ == '__main__':
    print("🏘️  Actualizando comunas de vecinos...")
    print("="*50)
    actualizar_comunas()
