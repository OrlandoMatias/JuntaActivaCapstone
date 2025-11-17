# Guía de Desarrollo

Esta guía está dirigida a desarrolladores que deseen contribuir o extender el sistema.

## Configuración del Entorno de Desarrollo

### Requisitos

- Python 3.11 o superior
- Git
- Editor de código (VS Code, PyCharm, etc.)
- MySQL (XAMPP) o SQLite

### Instalación

1. Clonar repositorio:
```bash
git clone <repositorio>
cd ProyectoJuntaActiva
```

2. Crear entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar base de datos (ver docs/BASE_DE_DATOS.md)

5. Aplicar migraciones:
```bash
cd config
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Cargar datos de prueba (opcional):
```bash
python manage.py loaddata fixtures/datos_prueba.json
```

## Estructura del Proyecto

```
ProyectoJuntaActiva/
├── config/                     # Proyecto Django
│   ├── config/                # Configuración principal
│   │   ├── settings.py       # Configuración de Django
│   │   ├── urls.py           # URLs principales
│   │   └── wsgi.py           # WSGI para producción
│   ├── gestion/              # Aplicación principal
│   │   ├── models.py         # Modelos de datos
│   │   ├── views.py          # Vistas
│   │   ├── forms.py          # Formularios
│   │   ├── admin.py          # Configuración del admin
│   │   ├── urls.py           # URLs de la app
│   │   ├── templates/        # Plantillas HTML
│   │   ├── static/           # Archivos estáticos
│   │   └── migrations/       # Migraciones de BD
│   ├── manage.py             # Comando de gestión
│   ├── verificar_mysql.py    # Script de verificación
│   └── .env                  # Variables de entorno
├── docs/                     # Documentación
├── venv/                     # Entorno virtual
├── requirements.txt          # Dependencias
└── README.md                # Documentación principal
```

## Modelos de Datos

### Vecino
Representa a un vecino registrado en el sistema.

```python
class Vecino(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
```

### Cuota
Gestión de cuotas de vecinos.

```python
class Cuota(models.Model):
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    pagada = models.BooleanField(default=False)
    fecha_pago = models.DateField(null=True, blank=True)
```

### CertificadoResidencia
Solicitudes de certificados.

```python
class CertificadoResidencia(models.Model):
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
```

### ProyectoVecinal
Proyectos propuestos por vecinos.

```python
class ProyectoVecinal(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
```

### EspacioComunitario y ReservaEspacio
Sistema de reservas de espacios.

```python
class EspacioComunitario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

class ReservaEspacio(models.Model):
    espacio = models.ForeignKey(EspacioComunitario, on_delete=models.CASCADE)
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
```

## Crear Nuevas Funcionalidades

### 1. Crear Modelo

Editar `gestion/models.py`:

```python
class NuevoModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Nuevo Modelo"
        verbose_name_plural = "Nuevos Modelos"
    
    def __str__(self):
        return self.campo1
```

### 2. Crear Migración

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Registrar en Admin

Editar `gestion/admin.py`:

```python
from .models import NuevoModelo

@admin.register(NuevoModelo)
class NuevoModeloAdmin(admin.ModelAdmin):
    list_display = ['campo1', 'campo2', 'fecha_creacion']
    list_filter = ['fecha_creacion']
    search_fields = ['campo1', 'campo2']
```

### 4. Crear Formulario

Editar `gestion/forms.py`:

```python
from django import forms
from .models import NuevoModelo

class NuevoModeloForm(forms.ModelForm):
    class Meta:
        model = NuevoModelo
        fields = ['campo1', 'campo2']
        widgets = {
            'campo1': forms.TextInput(attrs={'class': 'form-control'}),
            'campo2': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
```

### 5. Crear Vista

Editar `gestion/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import NuevoModelo
from .forms import NuevoModeloForm

@login_required
def crear_nuevo_modelo(request):
    if request.method == 'POST':
        form = NuevoModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = NuevoModeloForm()
    
    return render(request, 'gestion/nuevo_modelo_form.html', {'form': form})
```

### 6. Crear Template

Crear `gestion/templates/gestion/nuevo_modelo_form.html`:

```html
{% extends 'gestion/base.html' %}

{% block content %}
<h2>Crear Nuevo Modelo</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Guardar</button>
</form>
{% endblock %}
```

### 7. Agregar URL

Editar `gestion/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('nuevo-modelo/crear/', views.crear_nuevo_modelo, name='crear_nuevo_modelo'),
]
```

## Sistema de Emails

El sistema usa Django Email para enviar notificaciones.

### Configuración

En `config/.env`:

```env
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_aplicacion
```

### Enviar Email

```python
from django.core.mail import send_mail
from django.conf import settings

def enviar_notificacion(destinatario, asunto, mensaje):
    send_mail(
        subject=asunto,
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[destinatario],
        fail_silently=False,
    )
```

## Generación de PDFs

El sistema usa ReportLab para generar certificados.

### Ejemplo Básico

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Hola Mundo")
    p.showPage()
    p.save()
    
    return response
```

## Testing

### Crear Tests

Editar `gestion/tests.py`:

```python
from django.test import TestCase
from .models import Vecino

class VecinoTestCase(TestCase):
    def setUp(self):
        Vecino.objects.create(
            rut="12345678-9",
            nombre="Juan",
            apellido="Pérez",
            direccion="Calle 123",
            telefono="912345678",
            email="juan@example.com"
        )
    
    def test_vecino_creado(self):
        vecino = Vecino.objects.get(rut="12345678-9")
        self.assertEqual(vecino.nombre, "Juan")
```

### Ejecutar Tests

```bash
python manage.py test
```

## Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell interactivo
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic

# Verificar problemas
python manage.py check

# Limpiar sesiones expiradas
python manage.py clearsessions
```

## Buenas Prácticas

### Código

- Seguir PEP 8 para estilo de código Python
- Usar nombres descriptivos para variables y funciones
- Comentar código complejo
- Mantener funciones pequeñas y enfocadas

### Git

- Commits descriptivos y atómicos
- Usar ramas para nuevas funcionalidades
- Hacer pull request para revisión de código

### Seguridad

- Nunca commitear `.env` o credenciales
- Validar todos los inputs de usuario
- Usar `@login_required` para vistas protegidas
- Sanitizar datos antes de mostrar en templates

### Performance

- Usar `select_related()` y `prefetch_related()` para optimizar queries
- Implementar paginación en listas largas
- Cachear datos que no cambian frecuentemente
- Optimizar imágenes y archivos estáticos

## Deployment

Para producción, considerar:

1. Cambiar `DEBUG = False` en settings.py
2. Configurar `ALLOWED_HOSTS`
3. Usar servidor web (Nginx + Gunicorn)
4. Configurar HTTPS
5. Usar base de datos robusta (MySQL/PostgreSQL)
6. Configurar backups automáticos
7. Implementar logging
8. Usar variables de entorno para secretos

## Recursos

- Documentación de Django: https://docs.djangoproject.com/
- ReportLab: https://www.reportlab.com/docs/reportlab-userguide.pdf
- Python PEP 8: https://pep8.org/

## Contribuir

1. Fork el proyecto
2. Crear rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -am 'Agregar nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request
