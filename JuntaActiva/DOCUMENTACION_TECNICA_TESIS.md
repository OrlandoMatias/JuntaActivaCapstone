# Documentación Técnica del Sistema de Gestión Vecinal

## Información del Proyecto

**Nombre:** Sistema de Gestión Vecinal - Junta de Vecinos  
**Tipo:** Aplicación Web  
**Propósito:** Sistema integral para la gestión administrativa y comunitaria de juntas de vecinos  
**Arquitectura:** Monolítica basada en patrón MVC (Model-View-Controller)

---

## 1. Stack Tecnológico

### 1.1 Backend

**Framework Principal:**
- Django 5.0.9
  - Framework web de alto nivel escrito en Python
  - Patrón MTV (Model-Template-View)
  - ORM (Object-Relational Mapping) permite trabajar con la base de datos usando Python en vez de SQL.
  - Sistema de autenticación y autorización incorporado

**Lenguaje de Programación:**
- Python 3.14.0
  - Lenguaje interpretado (el código se ejecuta línea por línea, no necesitas compilarlo.) de alto nivel
  - Tipado dinámico (No tienes que decir qué tipo de dato es cada variable.)
  - Orientado a objetos (permite crear clases, objetos, métodos, etc.
Es útil para organizar código en estructuras más limpias.)

**Librerías Python:**
```
Django==5.0.9              # Framework web
reportlab==4.4.4           # Generación de PDFs
pillow==12.0.0             # Procesamiento de imágenes
charset-normalizer==3.4.4  # Normalización de caracteres
python-decouple==3.8       # Gestión de variables de entorno
pymysql==1.1.1             # Conector MySQL para Python
cryptography==44.0.0       # Funciones criptográficas
```

### 1.2 Base de Datos

**Sistema de Gestión de Base de Datos:**
- MySQL / MariaDB 10.4.32+
  - Base de datos relacional (la información se guarda en tablas que pueden relacionarse entre sí mediante claves (primarias y foráneas).
Esto permite mantener datos organizados, consistentes y fáciles de consultar mediante SQL.)
  - Soporte para transacciones ACID (A – Atomicity (Atomicidad):
Una transacción se completa totalmente o no se hace nada.

C – Consistency (Consistencia):
La base de datos siempre pasa de un estado válido a otro válido.

I – Isolation (Aislamiento):
Varias transacciones pueden ejecutarse al mismo tiempo sin interferirse.

D – Durability (Durabilidad):
Una vez que se confirman los cambios, quedan guardados incluso si ocurre un fallo.)

  - Motor de almacenamiento InnoDB (Es responsable de cómo se guardan físicamente los datos.)

  - Charset: utf8mb4 (soporte completo Unicode Permite almacenar todo tipo de caracteres, incluidos: emojis, caracteres asiáticos, símbolos especiales)

**Alternativa de Desarrollo:**
- SQLite 3
  - Base de datos embebida
  - Archivo único
  - Ideal para desarrollo local

**Conector:**
- PyMySQL 1.1.1
  - Cliente MySQL puro Python
  - Compatible con Python 3.x
  - No requiere compilación

### 1.3 Frontend

**Lenguajes:**
- HTML5
- CSS3
- JavaScript (Vanilla)

**Framework CSS:**
- Bootstrap 5.x (inferido del uso común en Django)
- Diseño responsive
- Componentes predefinidos

### 1.4 Servidor de Desarrollo

**Servidor Web:**
- Django Development Server
  - Servidor HTTP integrado
  - Recarga automática de código
  - Solo para desarrollo

### 1.5 Herramientas de Desarrollo

**Control de Versiones:**
- Git
- GitHub (repositorio remoto)

**Entorno Virtual:**
- venv (Python Virtual Environment)
- Aislamiento de dependencias

**IDE/Editor:**
- Compatible con cualquier editor (VS Code, PyCharm, etc.)

---

## 2. Arquitectura del Sistema

### 2.1 Patrón de Diseño

**MTV (Model-Template-View):**
- **Model:** Capa de datos y lógica de negocio
- **Template:** Capa de presentación (HTML)
- **View:** Capa de lógica de aplicación y controladores

### 2.2 Estructura de Directorios

```
ProyectoJuntaActiva/
│
├── config/                          # Proyecto Django principal
│   ├── config/                      # Configuración del proyecto
│   │   ├── __init__.py             # Inicialización (configuración PyMySQL)
│   │   ├── settings.py             # Configuración global
│   │   ├── urls.py                 # Enrutamiento principal
│   │   ├── wsgi.py                 # Interfaz WSGI para producción
│   │   └── asgi.py                 # Interfaz ASGI para async
│   │
│   ├── gestion/                     # Aplicación principal
│   │   ├── migrations/             # Migraciones de base de datos
│   │   ├── templates/              # Plantillas HTML
│   │   │   └── gestion/           # Templates de la app
│   │   ├── static/                 # Archivos estáticos
│   │   │   └── gestion/           # CSS, JS, imágenes
│   │   ├── __init__.py
│   │   ├── admin.py               # Configuración del admin
│   │   ├── apps.py                # Configuración de la app
│   │   ├── models.py              # Modelos de datos
│   │   ├── views.py               # Vistas/Controladores
│   │   ├── urls.py                # Enrutamiento de la app
│   │   ├── forms.py               # Formularios
│   │   └── tests.py               # Pruebas unitarias
│   │
│   ├── manage.py                   # Utilidad de línea de comandos
│   ├── verificar_mysql.py          # Script de verificación BD
│   ├── crear_datos_prueba.py       # Script de datos de prueba
│   ├── .env                        # Variables de entorno (no en Git)
│   └── .env.example                # Ejemplo de configuración
│
├── docs/                            # Documentación técnica
│   ├── README.md                   # Índice de documentación
│   ├── BASE_DE_DATOS.md           # Configuración de BD
│   ├── CONFIGURAR_EMAIL.md        # Configuración de emails
│   ├── DESARROLLO.md              # Guía de desarrollo
│   ├── SISTEMA_MEMBRESIA.md       # Sistema de membresía
│   └── SISTEMA_RESERVAS.md        # Sistema de reservas
│
├── venv/                           # Entorno virtual Python
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación principal
├── .gitignore                      # Archivos ignorados por Git
└── LICENSE                         # Licencia del proyecto
```

### 2.3 Flujo de Datos

```
Usuario (Navegador)
    ↓
Django URLs (urls.py)
    ↓
Views (views.py) ← Forms (forms.py)
    ↓
Models (models.py)
    ↓
Base de Datos (MySQL)
    ↓
Models (ORM)
    ↓
Views (procesamiento)
    ↓
Templates (HTML)
    ↓
Usuario (Navegador)
```

---

## 3. Modelos de Datos

### 3.1 Diagrama Entidad-Relación

```
User (Django Auth)
  ↓ 1:1
Vecino
  ↓ 1:N
  ├── ProyectoVecinal
  ├── CertificadoResidencia
  └── ReservaEspacio
      ↓ N:1
    EspacioComunitario

Actividad
  ↓ N:N
Vecino (inscritos)

Noticia (independiente)
```

### 3.2 Modelos Principales

**Vecino**
```python
- id: AutoField (PK)
- user: OneToOneField(User)
- rut: CharField(12) UNIQUE
- nombre: CharField(100)
- apellido: CharField(100)
- email: EmailField UNIQUE
- telefono: CharField(15)
- direccion: CharField(200)
- es_miembro: BooleanField
- fecha_inscripcion: DateField
```

**ProyectoVecinal**
```python
- id: AutoField (PK)
- nombre: CharField(200)
- descripcion: TextField
- fecha_postulacion: DateField
- estado: CharField(20) [pendiente, aprobado, rechazado]
- vecino: ForeignKey(Vecino)
```

**CertificadoResidencia**
```python
- id: AutoField (PK)
- vecino: ForeignKey(Vecino)
- fecha_solicitud: DateField
- aprobado: BooleanField
- codigo_certificado: CharField(50)
- pdf_generado: BooleanField
```

**EspacioComunitario**
```python
- id: AutoField (PK)
- nombre: CharField(100)
- tipo: CharField(20) [cancha, sala, plaza]
- descripcion: TextField
- capacidad: IntegerField
- activo: BooleanField
```

**ReservaEspacio**
```python
- id: AutoField (PK)
- vecino: ForeignKey(Vecino)
- espacio: ForeignKey(EspacioComunitario)
- fecha: DateField
- horario: CharField(20) [manana, tarde, noche, dia_completo]
- motivo: TextField
- cantidad_personas: IntegerField
- estado: CharField(20) [pendiente, aprobada, rechazada, cancelada]
- fecha_solicitud: DateTimeField
- fecha_respuesta: DateTimeField
- observaciones_admin: TextField
- CONSTRAINT: UNIQUE(espacio, fecha, horario, estado='aprobada')
```

**Actividad**
```python
- id: AutoField (PK)
- nombre: CharField(200)
- descripcion: TextField
- fecha: DateField
- cupos: IntegerField
- inscritos: ManyToManyField(Vecino)
```

**Noticia**
```python
- id: AutoField (PK)
- titulo: CharField(200)
- contenido: TextField
- fecha_publicacion: DateField
```

---

## 4. Funcionalidades del Sistema

### 4.1 Módulo de Autenticación

**Tecnología:** Django Authentication System

**Características:**
- Registro de usuarios
- Login/Logout
- Gestión de sesiones
- Permisos por rol (Admin/Vecino)
- Recuperación de contraseña

**Roles:**
- **Administrador:** Acceso completo al sistema
- **Vecino:** Acceso limitado a funciones de usuario

### 4.2 Módulo de Membresía

**Funcionalidades:**
- Gestión de miembros por administrador
- Cambio de estado de membresía
- Restricción de acceso a funciones según membresía
- Notificaciones por email

**Flujo:**
1. Admin visualiza lista de vecinos
2. Admin cambia estado de membresía
3. Sistema envía email automático
4. Vecino obtiene/pierde permisos

### 4.3 Módulo de Certificados

**Funcionalidades:**
- Solicitud de certificados de residencia
- Aprobación/rechazo por administrador
- Generación automática de PDF
- Envío por email con adjunto

**Tecnología:**
- ReportLab 4.4.4 para generación de PDFs
- Django Email para envío

**Flujo:**
1. Vecino solicita certificado
2. Admin revisa y aprueba/rechaza
3. Sistema genera PDF con código único
4. Sistema envía email con PDF adjunto

### 4.4 Módulo de Proyectos Vecinales

**Funcionalidades:**
- Postulación de proyectos (solo miembros)
- Gestión de estados
- Notificaciones por email

**Estados:**
- Pendiente
- Aprobado
- Rechazado

### 4.5 Módulo de Reservas

**Funcionalidades:**
- Visualización de espacios disponibles
- Calendario de disponibilidad
- Solicitud de reservas
- Aprobación/rechazo por administrador
- Gestión de reservas propias

**Validaciones:**
- No duplicación de reservas
- Fechas futuras únicamente
- Capacidad máxima del espacio
- Horarios predefinidos

**Horarios:**
- Mañana: 08:00 - 13:00
- Tarde: 13:00 - 18:00
- Noche: 18:00 - 22:00
- Día Completo: 08:00 - 22:00

### 4.6 Módulo de Actividades

**Funcionalidades:**
- Publicación de actividades
- Gestión de cupos
- Inscripción de vecinos
- Control de disponibilidad

### 4.7 Módulo de Noticias

**Funcionalidades:**
- Publicación de noticias
- Visualización cronológica
- Gestión por administrador

### 4.8 Sistema de Notificaciones

**Tecnología:** Django Email + SMTP

**Configuración:**
- Servidor SMTP: Gmail/Outlook
- Puerto: 587
- Seguridad: TLS

**Eventos que generan emails:**
- Aprobación/rechazo de certificados
- Cambio de estado de proyectos
- Cambio de estado de membresía
- Aprobación/rechazo de reservas

---

## 5. Seguridad

### 5.1 Autenticación y Autorización

**Mecanismos:**
- Autenticación basada en sesiones
- Decoradores @login_required
- Verificación de permisos por rol
- Protección CSRF (Cross-Site Request Forgery)

### 5.2 Validación de Datos

**Backend:**
- Validación de formularios Django
- Validación de modelos
- Sanitización de inputs

**Base de Datos:**
- Constraints UNIQUE
- Foreign Keys con ON DELETE CASCADE
- Validación de tipos de datos

### 5.3 Gestión de Secretos

**Variables de Entorno:**
- SECRET_KEY de Django
- Credenciales de base de datos
- Credenciales de email
- Archivo .env excluido de Git

### 5.4 Protección de Datos

**Medidas:**
- Contraseñas hasheadas (PBKDF2)
- Validación de RUT único
- Email único por vecino
- Sesiones con timeout

---

## 6. Configuración del Sistema

### 6.1 Variables de Entorno

**Base de Datos:**
```env
DB_ENGINE=mysql
DB_NAME=junta_vecinos
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

**Email:**
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=contraseña_aplicacion
DEFAULT_FROM_EMAIL=noreply@juntavecinos.cl
```

### 6.2 Configuración de Django

**settings.py - Configuraciones Clave:**
```python
DEBUG = True  # False en producción
ALLOWED_HOSTS = []  # Configurar en producción
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True
```

---

## 7. Instalación y Despliegue

### 7.1 Requisitos del Sistema

**Software:**
- Python 3.11 o superior
- MySQL 8.0+ o MariaDB 10.4+
- Git

**Hardware Mínimo:**
- CPU: 2 cores
- RAM: 2 GB
- Disco: 1 GB libre

### 7.2 Proceso de Instalación

```bash
# 1. Clonar repositorio
git clone <repositorio>
cd ProyectoJuntaActiva

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crear archivo config/.env

# 5. Aplicar migraciones
cd config
python manage.py migrate

# 6. Crear superusuario
python manage.py createsuperuser

# 7. Cargar datos de prueba (opcional)
python crear_datos_prueba.py

# 8. Iniciar servidor
python manage.py runserver
```

### 7.3 Despliegue en Producción

**Pasos Adicionales:**
1. Configurar DEBUG = False
2. Configurar ALLOWED_HOSTS
3. Configurar servidor web (Nginx/Apache)
4. Configurar WSGI (Gunicorn)
5. Configurar archivos estáticos
6. Configurar HTTPS
7. Configurar backups automáticos

---

## 8. Testing y Calidad

### 8.1 Pruebas Implementadas

**Scripts de Verificación:**
- verificar_mysql.py: Verifica conexión a base de datos
- crear_datos_prueba.py: Crea datos de prueba

**Pruebas Manuales:**
- Flujos de usuario completos
- Validación de formularios
- Generación de PDFs
- Envío de emails

### 8.2 Datos de Prueba

**Incluye:**
- 6 espacios comunitarios
- 8 actividades programadas
- 5 noticias
- 5 vecinos de ejemplo
- Usuarios con diferentes roles

---

## 9. Rendimiento y Escalabilidad

### 9.1 Optimizaciones Implementadas

**Base de Datos:**
- Índices en campos únicos (RUT, email)
- Foreign Keys para integridad referencial
- Queries optimizadas con ORM

**Backend:**
- Uso de select_related() y prefetch_related()
- Paginación en listas largas
- Caché de sesiones

### 9.2 Limitaciones Actuales

**Concurrencia:**
- Servidor de desarrollo monohilo
- No implementado sistema de caché
- No implementado balanceo de carga

**Escalabilidad:**
- Base de datos única (no replicación)
- Archivos estáticos servidos por Django
- No implementado CDN

---

## 10. Mantenimiento

### 10.1 Backups

**Base de Datos:**
```bash
# Backup
mysqldump -u root junta_vecinos > backup.sql

# Restaurar
mysql -u root junta_vecinos < backup.sql
```

**Archivos:**
- Backup de archivos estáticos
- Backup de archivos media (si aplica)
- Backup de configuración (.env)

### 10.2 Logs

**Django:**
- Logs de errores en consola
- Logs de acceso en servidor web
- Logs de base de datos

### 10.3 Actualizaciones

**Dependencias:**
```bash
pip list --outdated
pip install --upgrade <paquete>
pip freeze > requirements.txt
```

---

## 11. Documentación

### 11.1 Documentación Técnica

**Ubicación:** carpeta `docs/`

**Documentos:**
- BASE_DE_DATOS.md: Configuración de BD
- CONFIGURAR_EMAIL.md: Configuración de emails
- DESARROLLO.md: Guía para desarrolladores
- SISTEMA_MEMBRESIA.md: Sistema de membresía
- SISTEMA_RESERVAS.md: Sistema de reservas

### 11.2 Documentación de Usuario

**Ubicación:** README.md principal

**Contenido:**
- Características del sistema
- Guía de instalación
- Guía de uso básico
- Solución de problemas

---

## 12. Métricas del Proyecto

### 12.1 Estadísticas de Código

**Líneas de Código (aproximado):**
- Python (models, views, forms): ~2000 líneas
- HTML (templates): ~1500 líneas
- CSS: ~500 líneas
- JavaScript: ~300 líneas

**Archivos:**
- Modelos: 7 principales
- Vistas: ~30 funciones
- Templates: ~20 archivos
- Formularios: ~8 clases

### 12.2 Funcionalidades

**Módulos:** 7 principales
**Roles de Usuario:** 2 (Admin, Vecino)
**Tipos de Notificaciones:** 4
**Espacios Comunitarios:** Ilimitados
**Usuarios Concurrentes:** Depende del servidor

---

## 13. Conclusiones Técnicas

### 13.1 Fortalezas

1. **Arquitectura Sólida:** Uso de Django con patrón MTV bien implementado
2. **Seguridad:** Implementación de buenas prácticas de seguridad
3. **Escalabilidad:** Base sólida para crecimiento futuro
4. **Mantenibilidad:** Código organizado y documentado
5. **Funcionalidad Completa:** Sistema integral para gestión vecinal

### 13.2 Áreas de Mejora

1. **Testing:** Implementar pruebas unitarias y de integración
2. **Performance:** Implementar sistema de caché
3. **UI/UX:** Mejorar interfaz de usuario
4. **API:** Implementar API REST para integración
5. **Móvil:** Desarrollar aplicación móvil

### 13.3 Tecnologías Futuras

**Posibles Mejoras:**
- Django REST Framework para API
- React/Vue.js para frontend
- PostgreSQL para mejor rendimiento
- Redis para caché
- Docker para containerización
- CI/CD con GitHub Actions

---

## 14. Referencias

**Documentación Oficial:**
- Django: https://docs.djangoproject.com/
- Python: https://docs.python.org/
- MySQL: https://dev.mysql.com/doc/
- ReportLab: https://www.reportlab.com/docs/

**Estándares:**
- PEP 8: Guía de estilo Python
- HTML5: Estándar W3C
- REST: Architectural Style

---

## Información de Contacto

**Desarrollador:** [Tu Nombre]  
**Email:** [Tu Email]  
**Repositorio:** [URL del repositorio]  
**Fecha:** Noviembre 2025  
**Versión:** 1.0.0

---

**Nota:** Este documento técnico está diseñado para proporcionar una visión completa del sistema para propósitos académicos y de defensa de tesis.
