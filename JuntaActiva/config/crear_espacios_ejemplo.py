"""
Script para crear espacios comunitarios de ejemplo
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from gestion.models import EspacioComunitario

print("=" * 60)
print("CREANDO ESPACIOS COMUNITARIOS DE EJEMPLO")
print("=" * 60)

espacios_ejemplo = [
    {
        'nombre': 'Cancha de Fútbol Principal',
        'tipo': 'cancha',
        'descripcion': 'Cancha de fútbol con pasto sintético, iluminación nocturna y graderías. Ideal para partidos y entrenamientos.',
        'capacidad': 30,
        'activo': True
    },
    {
        'nombre': 'Cancha de Básquetbol',
        'tipo': 'cancha',
        'descripcion': 'Cancha techada de básquetbol con piso de madera. Incluye tableros profesionales y marcador electrónico.',
        'capacidad': 25,
        'activo': True
    },
    {
        'nombre': 'Sala Multiuso',
        'tipo': 'sala',
        'descripcion': 'Sala amplia con sillas, mesas, proyector y sistema de sonido. Perfecta para reuniones, talleres y eventos.',
        'capacidad': 50,
        'activo': True
    },
    {
        'nombre': 'Sala de Reuniones Pequeña',
        'tipo': 'sala',
        'descripcion': 'Sala equipada con mesa de conferencias, pizarra y aire acondicionado. Ideal para reuniones pequeñas.',
        'capacidad': 15,
        'activo': True
    },
    {
        'nombre': 'Plaza Central',
        'tipo': 'plaza',
        'descripcion': 'Plaza comunitaria con áreas verdes, juegos infantiles y zona de parrillas. Perfecta para eventos al aire libre.',
        'capacidad': 100,
        'activo': True
    },
    {
        'nombre': 'Plaza del Barrio Norte',
        'tipo': 'plaza',
        'descripcion': 'Plaza con áreas de picnic, bancas y zona de ejercicios. Ideal para actividades recreativas.',
        'capacidad': 80,
        'activo': True
    },
]

espacios_creados = 0
espacios_existentes = 0

for espacio_data in espacios_ejemplo:
    # Verificar si ya existe
    existe = EspacioComunitario.objects.filter(
        nombre=espacio_data['nombre']
    ).exists()
    
    if existe:
        print(f"⚠ Ya existe: {espacio_data['nombre']}")
        espacios_existentes += 1
    else:
        espacio = EspacioComunitario.objects.create(**espacio_data)
        print(f"✓ Creado: {espacio.nombre} ({espacio.get_tipo_display()}) - Capacidad: {espacio.capacidad}")
        espacios_creados += 1

print("\n" + "=" * 60)
print(f"✓ Espacios creados: {espacios_creados}")
print(f"⚠ Espacios que ya existían: {espacios_existentes}")
print(f"📊 Total de espacios en el sistema: {EspacioComunitario.objects.count()}")
print("=" * 60)

print("\n🎉 ¡Listo! Ahora puedes:")
print("1. Ver los espacios en: http://localhost:8000/reservas/espacios/")
print("2. Ver el calendario en: http://localhost:8000/reservas/calendario/")
print("3. Solicitar una reserva en: http://localhost:8000/reservas/solicitar/")
