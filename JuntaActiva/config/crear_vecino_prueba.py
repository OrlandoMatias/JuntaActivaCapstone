"""
Script para crear un vecino de prueba que NO es miembro
Para ejecutar: python manage.py shell < crear_vecino_prueba.py
"""
from django.contrib.auth.models import User
from gestion.models import Vecino

# Datos del vecino de prueba
rut = "12.345.678-9"
nombre = "María"
apellido = "González"
email = "maria.gonzalez@example.com"
telefono = "+56912345678"
direccion = "Calle Falsa 123, Santiago"
password = "prueba123"

# Verificar si ya existe
if User.objects.filter(username=rut).exists():
    print(f"❌ Ya existe un usuario con RUT {rut}")
    user = User.objects.get(username=rut)
    vecino = user.vecino
    print(f"   Vecino: {vecino.nombre} {vecino.apellido}")
    print(f"   Es miembro: {vecino.es_miembro}")
else:
    # Crear usuario
    user = User.objects.create_user(
        username=rut,
        email=email,
        password=password,
        first_name=nombre,
        last_name=apellido
    )
    
    # Crear vecino (NO miembro)
    vecino = Vecino.objects.create(
        user=user,
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono,
        direccion=direccion,
        es_miembro=False  # NO es miembro aún
    )
    
    print(f"✅ Vecino creado exitosamente:")
    print(f"   RUT: {vecino.rut}")
    print(f"   Nombre: {vecino.nombre} {vecino.apellido}")
    print(f"   Email: {vecino.email}")
    print(f"   Es miembro: {vecino.es_miembro}")
    print(f"   Password: {password}")
    print()
    print("Este vecino aparecerá en la sección 'Pendientes de Aprobación'")
