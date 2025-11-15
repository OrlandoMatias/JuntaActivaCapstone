# Sistema de Gestión Vecinal - Junta de Vecinos

Sistema web completo para la gestión de una junta de vecinos, desarrollado con Django.

## 🚀 Características

### ✅ Sistema de Membresía
- Registro de vecinos con creación automática de usuario
- Aprobación de miembros por administradores
- Email automático de bienvenida al aprobar

### 📋 Certificados de Residencia
- Solicitud de certificados por vecinos
- Aprobación/rechazo por administradores
- Generación automática de PDF en español
- Envío por email al aprobar

### 🏗️ Proyectos Vecinales
- Postulación de proyectos por vecinos
- Gestión de estados (pendiente, aprobado, rechazado, en progreso, completado)
- Notificaciones por email

### 🏟️ Sistema de Reservas
- Reserva de espacios comunitarios (canchas, salas, plazas)
- Gestión de horarios y disponibilidad
- Aprobación administrativa
- Calendario de reservas
- Emails de confirmación

### 📰 Noticias y Actividades
- Publicación de noticias
- Gestión de actividades con cupos
- Inscripción de vecinos

## 🛠️ Tecnologías

- **Backend:** Django 5.2.8
- **Base de datos:** SQLite
- **PDF:** ReportLab
- **Email:** SMTP (Gmail)
- **Frontend:** HTML, CSS, JavaScript

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd ProyectoJuntaActiva-main
```

2. Crear entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
pip install django reportlab
```

4. Configurar base de datos:
```bash
cd config
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Configurar email en `config/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-contraseña-de-aplicación'
DEFAULT_FROM_EMAIL = 'tu-email@gmail.com'
```

7. Iniciar servidor:
```bash
python manage.py runserver
```

8. Acceder a: http://127.0.0.1:8000/

## 📚 Documentación

- `SISTEMA_MEMBRESIA.md` - Sistema de membresía
- `SISTEMA_RESERVAS.md` - Sistema de reservas
- `GUIA_SISTEMA_RESERVAS.md` - Guía de uso de reservas
- `CONFIGURAR_EMAIL.md` - Configuración de emails
- `EMAILS_PROYECTOS.md` - Sistema de emails para proyectos

## 👥 Usuarios

### Administrador
- Acceso completo al sistema
- Gestión de vecinos, certificados, proyectos y reservas
- Creación de noticias y actividades

### Vecino
- Solicitar certificados
- Postular proyectos
- Reservar espacios
- Inscribirse en actividades

## 🔐 Seguridad

- Autenticación requerida para funciones sensibles
- Permisos por rol (admin/vecino)
- Validación de formularios
- Protección CSRF

## 📧 Contacto

Sistema desarrollado para la gestión eficiente de juntas de vecinos.

## 📄 Licencia

Este proyecto es de código abierto.
