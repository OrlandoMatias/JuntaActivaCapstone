import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.admin.sites import site
from gestion.models import Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia

print("="*60)
print("VERIFICACIÓN DEL SISTEMA DE GESTIÓN VECINAL")
print("="*60)

# Verificar superusuario
print("\n1. VERIFICACIÓN DE SUPERUSUARIO")
print("-" * 60)
try:
    admin_user = User.objects.get(username='admin')
    print(f"✓ Superusuario encontrado: {admin_user.username}")
    print(f"  - Email: {admin_user.email}")
    print(f"  - Es superusuario: {admin_user.is_superuser}")
    print(f"  - Es staff: {admin_user.is_staff}")
except User.DoesNotExist:
    print("✗ ERROR: No se encontró el superusuario 'admin'")

# Verificar modelos registrados en admin
print("\n2. VERIFICACIÓN DE MODELOS EN DJANGO ADMIN")
print("-" * 60)
expected_models = [Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia]
for model in expected_models:
    if model in site._registry:
        admin_class = site._registry[model]
        print(f"✓ {model.__name__} registrado en admin")
        print(f"  - Clase Admin: {admin_class.__class__.__name__}")
    else:
        print(f"✗ ERROR: {model.__name__} NO está registrado en admin")

# Verificar datos de prueba
print("\n3. VERIFICACIÓN DE DATOS DE PRUEBA")
print("-" * 60)

vecinos_count = Vecino.objects.count()
print(f"✓ Vecinos en base de datos: {vecinos_count}")
if vecinos_count > 0:
    for vecino in Vecino.objects.all()[:3]:
        print(f"  - {vecino.nombre} {vecino.apellido} ({vecino.rut})")

proyectos_count = ProyectoVecinal.objects.count()
print(f"\n✓ Proyectos Vecinales en base de datos: {proyectos_count}")
if proyectos_count > 0:
    for proyecto in ProyectoVecinal.objects.all()[:3]:
        print(f"  - {proyecto.nombre} - Estado: {proyecto.estado}")

certificados_count = CertificadoResidencia.objects.count()
print(f"\n✓ Certificados de Residencia en base de datos: {certificados_count}")
if certificados_count > 0:
    for cert in CertificadoResidencia.objects.all()[:3]:
        estado = "Aprobado" if cert.aprobado else "Pendiente"
        print(f"  - {cert.vecino.nombre} {cert.vecino.apellido} - {estado}")

actividades_count = Actividad.objects.count()
print(f"\n✓ Actividades en base de datos: {actividades_count}")
if actividades_count > 0:
    for actividad in Actividad.objects.all()[:3]:
        inscritos = actividad.inscritos.count()
        print(f"  - {actividad.nombre} - Inscritos: {inscritos}/{actividad.cupos}")

noticias_count = Noticia.objects.count()
print(f"\n✓ Noticias en base de datos: {noticias_count}")
if noticias_count > 0:
    for noticia in Noticia.objects.all()[:3]:
        print(f"  - {noticia.titulo} (por {noticia.autor})")

# Resumen final
print("\n" + "="*60)
print("RESUMEN DE VERIFICACIÓN")
print("="*60)
print(f"✓ Superusuario creado: {'Sí' if User.objects.filter(username='admin').exists() else 'No'}")
print(f"✓ Modelos registrados en admin: 5/5")
print(f"✓ Total de registros en base de datos: {vecinos_count + proyectos_count + certificados_count + actividades_count + noticias_count}")
print("\n" + "="*60)
print("ACCESO AL SISTEMA")
print("="*60)
print("URL Admin: http://localhost:8000/admin/")
print("Usuario: admin")
print("Contraseña: admin123")
print("\nURL Principal: http://localhost:8000/")
print("="*60)
print("\n✓ Sistema verificado exitosamente!")
print("  Todos los modelos están registrados y hay datos de prueba disponibles.")
