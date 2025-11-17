#!/usr/bin/env python
"""
Script para crear datos de prueba en el sistema.
Crea espacios comunitarios, actividades, noticias y vecinos de ejemplo.
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from gestion.models import (
    Vecino, EspacioComunitario, Actividad, Noticia
)

def crear_espacios_comunitarios():
    """Crear espacios comunitarios de ejemplo"""
    print("\n=== Creando Espacios Comunitarios ===")
    
    espacios = [
        {
            'nombre': 'Cancha de Fútbol',
            'tipo': 'cancha',
            'descripcion': 'Cancha de fútbol con pasto sintético, iluminación nocturna y graderías para 50 personas.',
            'capacidad': 30,
            'activo': True
        },
        {
            'nombre': 'Cancha de Básquetbol',
            'tipo': 'cancha',
            'descripcion': 'Cancha techada de básquetbol con piso de madera y tableros profesionales.',
            'capacidad': 20,
            'activo': True
        },
        {
            'nombre': 'Sala Multiuso',
            'tipo': 'sala',
            'descripcion': 'Sala amplia con sillas, mesas, proyector y sistema de audio. Ideal para reuniones y eventos.',
            'capacidad': 50,
            'activo': True
        },
        {
            'nombre': 'Sala de Reuniones',
            'tipo': 'sala',
            'descripcion': 'Sala pequeña con mesa de conferencias para 12 personas, pizarra y aire acondicionado.',
            'capacidad': 12,
            'activo': True
        },
        {
            'nombre': 'Plaza Central',
            'tipo': 'plaza',
            'descripcion': 'Plaza principal con áreas verdes, juegos infantiles y zona de parrillas.',
            'capacidad': 100,
            'activo': True
        },
        {
            'nombre': 'Quincho Comunitario',
            'tipo': 'plaza',
            'descripcion': 'Quincho techado con parrillas, mesas y baños. Perfecto para celebraciones.',
            'capacidad': 40,
            'activo': True
        },
    ]
    
    creados = 0
    for espacio_data in espacios:
        espacio, created = EspacioComunitario.objects.get_or_create(
            nombre=espacio_data['nombre'],
            defaults=espacio_data
        )
        if created:
            print(f"✓ Creado: {espacio.nombre} ({espacio.get_tipo_display()})")
            creados += 1
        else:
            print(f"- Ya existe: {espacio.nombre}")
    
    print(f"\nTotal espacios creados: {creados}")
    return EspacioComunitario.objects.count()

def crear_actividades():
    """Crear actividades de ejemplo"""
    print("\n=== Creando Actividades ===")
    
    hoy = datetime.now().date()
    
    actividades = [
        {
            'nombre': 'Taller de Reciclaje - Sala Multiuso 10:00',
            'descripcion': 'Aprende a reciclar y crear compost casero. Trae tus residuos orgánicos y te enseñaremos cómo transformarlos en abono natural. Lugar: Sala Multiuso. Hora: 10:00 hrs.',
            'fecha': hoy + timedelta(days=7),
            'cupos': 25
        },
        {
            'nombre': 'Clase de Yoga - Plaza Central 18:00',
            'descripcion': 'Sesión de yoga para todos los niveles. Trae tu mat y ropa cómoda. Instructor certificado. Lugar: Plaza Central. Hora: 18:00 hrs.',
            'fecha': hoy + timedelta(days=3),
            'cupos': 30
        },
        {
            'nombre': 'Campeonato de Fútbol - Cancha de Fútbol 09:00',
            'descripcion': 'Torneo de fútbol 7 para vecinos. Inscribe tu equipo. Habrá premios para los ganadores. Lugar: Cancha de Fútbol. Hora: 09:00 hrs.',
            'fecha': hoy + timedelta(days=14),
            'cupos': 60
        },
        {
            'nombre': 'Taller de Cocina Saludable - Sala Multiuso 15:00',
            'descripcion': 'Aprende a preparar comidas nutritivas y económicas. Chef profesional enseñará recetas fáciles. Lugar: Sala Multiuso. Hora: 15:00 hrs.',
            'fecha': hoy + timedelta(days=10),
            'cupos': 20
        },
        {
            'nombre': 'Cine al Aire Libre - Plaza Central 20:00',
            'descripcion': 'Noche de cine familiar bajo las estrellas. Trae tu silla o manta. Habrá palomitas gratis. Lugar: Plaza Central. Hora: 20:00 hrs.',
            'fecha': hoy + timedelta(days=5),
            'cupos': 100
        },
        {
            'nombre': 'Feria de Emprendedores - Plaza Central 10:00',
            'descripcion': 'Espacio para que vecinos emprendedores muestren y vendan sus productos. Inscripciones abiertas. Lugar: Plaza Central. Hora: 10:00 hrs.',
            'fecha': hoy + timedelta(days=21),
            'cupos': 50
        },
        {
            'nombre': 'Taller de Primeros Auxilios - Sala de Reuniones 14:00',
            'descripcion': 'Curso básico de primeros auxilios dictado por paramédicos. Certificado incluido. Lugar: Sala de Reuniones. Hora: 14:00 hrs.',
            'fecha': hoy + timedelta(days=12),
            'cupos': 15
        },
        {
            'nombre': 'Zumba para Todos - Cancha de Básquetbol 19:00',
            'descripcion': 'Clase de zumba con música latina. Para todas las edades. No se requiere experiencia. Lugar: Cancha de Básquetbol. Hora: 19:00 hrs.',
            'fecha': hoy + timedelta(days=4),
            'cupos': 25
        },
    ]
    
    creados = 0
    for actividad_data in actividades:
        actividad, created = Actividad.objects.get_or_create(
            nombre=actividad_data['nombre'],
            defaults=actividad_data
        )
        if created:
            print(f"✓ Creada: {actividad.nombre} - {actividad.fecha.strftime('%d/%m/%Y')}")
            creados += 1
        else:
            print(f"- Ya existe: {actividad.nombre}")
    
    print(f"\nTotal actividades creadas: {creados}")
    return Actividad.objects.count()

def crear_noticias():
    """Crear noticias de ejemplo"""
    print("\n=== Creando Noticias ===")
    
    noticias = [
        {
            'titulo': 'Nueva Iluminación en la Plaza Central',
            'contenido': '''La junta de vecinos informa que se ha completado la instalación de nueva iluminación LED en la Plaza Central. 
            
Este proyecto, gestionado durante los últimos 3 meses, mejorará significativamente la seguridad y permitirá el uso del espacio durante las noches.

Las nuevas luminarias son de bajo consumo energético y tienen una vida útil de 10 años. Agradecemos a todos los vecinos que apoyaron esta iniciativa.'''
        },
        {
            'titulo': 'Horario de Recolección de Basura',
            'contenido': '''Se informa a todos los vecinos que el horario de recolección de basura ha cambiado:

- Lunes, Miércoles y Viernes: Basura domiciliaria (19:00 hrs)
- Martes y Jueves: Reciclaje (19:00 hrs)
- Sábados: Residuos voluminosos (09:00 hrs)

Por favor, sacar los contenedores después de las 18:00 hrs del día correspondiente.'''
        },
        {
            'titulo': 'Reunión Mensual de Vecinos',
            'contenido': '''Los invitamos a la reunión mensual de vecinos que se realizará el próximo sábado a las 11:00 hrs en la Sala Multiuso.

Temas a tratar:
- Informe financiero del mes
- Nuevos proyectos comunitarios
- Propuestas de mejoras
- Varios

Su participación es importante. Los esperamos!'''
        },
        {
            'titulo': 'Mantención de Áreas Verdes',
            'contenido': '''Durante esta semana se realizará mantención de las áreas verdes del sector.

El equipo de jardinería estará trabajando en:
- Poda de árboles y arbustos
- Corte de pasto
- Riego de plantas
- Limpieza de hojas secas

Agradecemos su comprensión si hay alguna molestia temporal.'''
        },
        {
            'titulo': 'Nuevo Sistema de Reservas Online',
            'contenido': '''Tenemos buenas noticias! Ya está disponible el nuevo sistema de reservas online para espacios comunitarios.

Ahora puedes:
- Ver disponibilidad en tiempo real
- Solicitar reservas desde tu casa
- Recibir confirmación por email
- Gestionar tus reservas

Ingresa al sistema con tu usuario y contraseña. Si tienes dudas, contacta a la administración.'''
        },
    ]
    
    creados = 0
    for noticia_data in noticias:
        noticia, created = Noticia.objects.get_or_create(
            titulo=noticia_data['titulo'],
            defaults=noticia_data
        )
        if created:
            print(f"✓ Creada: {noticia.titulo}")
            creados += 1
        else:
            print(f"- Ya existe: {noticia.titulo}")
    
    print(f"\nTotal noticias creadas: {creados}")
    return Noticia.objects.count()

def crear_vecinos_prueba():
    """Crear vecinos de prueba"""
    print("\n=== Creando Vecinos de Prueba ===")
    
    vecinos = [
        {
            'rut': '12345678-9',
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'direccion': 'Calle Principal 123',
            'telefono': '+56912345678',
            'email': 'juan.perez@example.com',
            'es_miembro': True
        },
        {
            'rut': '98765432-1',
            'nombre': 'María',
            'apellido': 'González',
            'direccion': 'Avenida Central 456',
            'telefono': '+56987654321',
            'email': 'maria.gonzalez@example.com',
            'es_miembro': True
        },
        {
            'rut': '11223344-5',
            'nombre': 'Pedro',
            'apellido': 'Rodríguez',
            'direccion': 'Pasaje Los Aromos 789',
            'telefono': '+56911223344',
            'email': 'pedro.rodriguez@example.com',
            'es_miembro': False
        },
        {
            'rut': '55667788-9',
            'nombre': 'Ana',
            'apellido': 'Martínez',
            'direccion': 'Calle Las Flores 321',
            'telefono': '+56955667788',
            'email': 'ana.martinez@example.com',
            'es_miembro': True
        },
        {
            'rut': '99887766-5',
            'nombre': 'Carlos',
            'apellido': 'López',
            'direccion': 'Avenida Los Pinos 654',
            'telefono': '+56999887766',
            'email': 'carlos.lopez@example.com',
            'es_miembro': False
        },
    ]
    
    creados = 0
    for vecino_data in vecinos:
        # Crear usuario si no existe
        username = f"{vecino_data['nombre'].lower()}.{vecino_data['apellido'].lower()}"
        user, user_created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': vecino_data['email'],
                'first_name': vecino_data['nombre'],
                'last_name': vecino_data['apellido']
            }
        )
        if user_created:
            user.set_password('vecino123')
            user.save()
        
        # Crear vecino
        vecino_data['user'] = user
        vecino, created = Vecino.objects.get_or_create(
            rut=vecino_data['rut'],
            defaults=vecino_data
        )
        if created:
            estado = "Miembro" if vecino.es_miembro else "No miembro"
            print(f"✓ Creado: {vecino.nombre} {vecino.apellido} ({estado})")
            print(f"  Usuario: {username} / Contraseña: vecino123")
            creados += 1
        else:
            print(f"- Ya existe: {vecino.nombre} {vecino.apellido}")
    
    print(f"\nTotal vecinos creados: {creados}")
    return Vecino.objects.count()

def main():
    print("=" * 60)
    print("CREACIÓN DE DATOS DE PRUEBA")
    print("=" * 60)
    
    try:
        # Crear datos
        total_espacios = crear_espacios_comunitarios()
        total_actividades = crear_actividades()
        total_noticias = crear_noticias()
        total_vecinos = crear_vecinos_prueba()
        
        # Resumen
        print("\n" + "=" * 60)
        print("RESUMEN")
        print("=" * 60)
        print(f"Espacios Comunitarios: {total_espacios}")
        print(f"Actividades: {total_actividades}")
        print(f"Noticias: {total_noticias}")
        print(f"Vecinos: {total_vecinos}")
        print("\n" + "=" * 60)
        print("DATOS DE PRUEBA CREADOS EXITOSAMENTE")
        print("=" * 60)
        
        print("\nPuedes iniciar sesión con:")
        print("- Admin: admin / [tu contraseña]")
        print("- Vecinos: juan.perez / vecino123")
        print("           maria.gonzalez / vecino123")
        print("           pedro.rodriguez / vecino123")
        print("           ana.martinez / vecino123")
        print("           carlos.lopez / vecino123")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
