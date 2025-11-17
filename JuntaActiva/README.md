# Sistema de Gestión Vecinal - Junta de Vecinos

Sistema web completo para la gestión de una junta de vecinos, desarrollado con Django.

## Características

### Sistema de Membresía
- Registro de vecinos con creación automática de usuario
- Aprobación de miembros por administradores
- Email automático de bienvenida al aprobar

### Certificados de Residencia
- Solicitud de certificados por vecinos
- Aprobación/rechazo por administradores
- Generación automática de PDF en español
- Envío por email al aprobar

### Proyectos Vecinales
- Postulación de proyectos por vecinos
- Gestión de estados (pendiente, aprobado, rechazado, en progreso, completado)
- Notificaciones por email

### Sistema de Reservas
- Reserva de espacios comunitarios (canchas, salas, plazas)
- Gestión de horarios y disponibilidad
- Aprobación administrativa
- Calendario de reservas
- Emails de confirmación

### Noticias y Actividades
- Publicación de noticias
- Gestión de actividades con cupos
- Inscripción de vecinos

## Tecnologías

- **Backend:** Django 5.0.9
- **Base de datos:** MySQL (MariaDB 10.4+) / SQLite
- **PDF:** ReportLab
- **Email:** SMTP (Gmail)
- **Frontend:** HTML, CSS, JavaScript

## Instalación Rápida

### Requisitos Previos
- Python 3.11 o superior
- MySQL (XAMPP recomendado para Windows) o SQLite

### Pasos de Instalación

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd ProyectoJuntaActiva
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar base de datos (ver sección Base de Datos)

5. Aplicar migraciones:
```bash
cd config
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar servidor:
```bash
python manage.py runserver
```

8. Acceder a: http://127.0.0.1:8000/

## Configuración de Base de Datos

El sistema soporta SQLite (por defecto) y MySQL.

### Opción 1: SQLite (Desarrollo)

No requiere configuración adicional. Ideal para desarrollo local.

### Opción 2: MySQL (Producción)

1. Instalar XAMPP o MySQL Server
2. Crear base de datos `junta_vecinos`
3. Crear archivo `config/.env`:

```env
DB_ENGINE=mysql
DB_NAME=junta_vecinos
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

Para más detalles, ver `docs/BASE_DE_DATOS.md`

## Configuración de Email

Para habilitar el envío de emails:

1. Editar `config/.env`:
```env
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@juntavecinos.cl
```

2. Para Gmail, generar una "Contraseña de aplicación" en la configuración de seguridad de Google

Sin configuración de email, los mensajes se mostrarán en la consola (modo desarrollo).

## Estructura del Proyecto

```
ProyectoJuntaActiva/
├── config/                 # Configuración de Django
│   ├── config/            # Settings y URLs principales
│   ├── gestion/           # Aplicación principal
│   ├── manage.py          # Comando de gestión de Django
│   └── .env               # Variables de entorno (crear)
├── docs/                  # Documentación
├── venv/                  # Entorno virtual
├── requirements.txt       # Dependencias
└── README.md             # Este archivo
```

## Usuarios del Sistema

### Administrador
- Acceso completo al panel de administración
- Gestión de vecinos, certificados, proyectos y reservas
- Creación de noticias y actividades
- Acceso: http://localhost:8000/admin

### Vecino
- Solicitar certificados de residencia
- Postular proyectos vecinales
- Reservar espacios comunitarios
- Inscribirse en actividades
- Acceso: http://localhost:8000/

## Documentación

Toda la documentación técnica se encuentra organizada en la carpeta `docs/`:

- **docs/README.md** - Índice completo de documentación
- **docs/BASE_DE_DATOS.md** - Configuración de MySQL/SQLite
- **docs/CONFIGURAR_EMAIL.md** - Configuración de emails
- **docs/DESARROLLO.md** - Guía para desarrolladores
- **docs/SISTEMA_MEMBRESIA.md** - Sistema de membresía
- **docs/SISTEMA_RESERVAS.md** - Sistema de reservas

## Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor de desarrollo
python manage.py runserver

# Verificar conexión a base de datos
python verificar_mysql.py

# Ejecutar shell de Django
python manage.py shell
```

## Solución de Problemas

### Error de conexión a MySQL
- Verificar que MySQL esté corriendo
- Revisar credenciales en `.env`
- Ejecutar: `python verificar_mysql.py`

### Error de migraciones
- Eliminar archivos de migración en `gestion/migrations/` (excepto `__init__.py`)
- Ejecutar: `python manage.py makemigrations`
- Ejecutar: `python manage.py migrate`

### Emails no se envían
- Verificar configuración en `.env`
- Verificar contraseña de aplicación de Gmail
- En desarrollo, los emails se muestran en consola

## Seguridad

- Autenticación requerida para funciones sensibles
- Permisos por rol (admin/vecino)
- Validación de formularios
- Protección CSRF
- Variables sensibles en archivo `.env` (no incluido en repositorio)

## Contribuir

1. Fork el proyecto
2. Crear rama para nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## Licencia

Este proyecto es de código abierto.

## Contacto

Sistema desarrollado para la gestión eficiente de juntas de vecinos.
