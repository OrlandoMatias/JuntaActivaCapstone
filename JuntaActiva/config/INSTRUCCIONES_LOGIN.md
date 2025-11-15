# Sistema de Autenticación - Instrucciones de Uso

## 🔐 Credenciales de Acceso

### Administrador
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **URL Login:** http://localhost:8000/login/

### Vecinos Existentes
- **Usuario:** [RUT del vecino] (ej: `12345678-9`)
- **Contraseña:** `vecino123`
- **URL Login:** http://localhost:8000/login/

## 📋 Funcionalidades por Tipo de Usuario

### 👤 Vecinos (Usuarios Normales)
Cuando un vecino inicia sesión, puede:
- ✅ Ver noticias y actividades
- ✅ Inscribirse en actividades (automáticamente con su usuario)
- ✅ Solicitar certificados de residencia (automáticamente a su nombre)
- ✅ Postular proyectos vecinales (automáticamente a su nombre)
- ✅ Ver el estado de sus propios certificados
- ✅ Ver el estado de sus propios proyectos

**Menú del Navbar para Vecinos:**
- Inicio
- Noticias
- Actividades
- Solicitar Certificado
- Postular Proyecto
- Mis Certificados
- Mis Proyectos
- Cerrar Sesión

### 👨‍💼 Administradores
Cuando un administrador inicia sesión, puede:
- ✅ Ver todas las funcionalidades públicas
- ✅ Gestionar todos los vecinos
- ✅ Aprobar/rechazar certificados de residencia
- ✅ Aprobar/rechazar proyectos vecinales
- ✅ Crear noticias
- ✅ Ver todas las solicitudes y proyectos de todos los vecinos

**Menú del Navbar para Administradores:**
- Inicio
- Noticias
- Actividades
- Gestión Vecinos
- Gestión Certificados
- Gestión Proyectos
- Crear Noticia
- Cerrar Sesión

## 🆕 Registro de Nuevos Vecinos

### Proceso de Registro
1. Ir a: http://localhost:8000/vecinos/registrar/
2. Completar el formulario con:
   - RUT (será el nombre de usuario)
   - Nombre
   - Apellido
   - Email
   - Teléfono
   - Dirección
   - **Contraseña** (mínimo 6 caracteres)
   - **Confirmar Contraseña**
3. Al registrarse, el sistema:
   - Crea un usuario de Django
   - Crea el perfil de vecino
   - Vincula ambos
   - Inicia sesión automáticamente

## 🔒 Restricciones de Acceso

### Páginas que Requieren Login
- Inscribirse en actividades
- Solicitar certificados
- Postular proyectos
- Ver mis certificados
- Ver mis proyectos

### Páginas Solo para Administradores
- Gestión de vecinos
- Gestión de certificados (aprobar/rechazar)
- Gestión de proyectos (aprobar/rechazar)
- Crear noticias

### Páginas Públicas (Sin Login)
- Inicio
- Ver noticias
- Ver lista de actividades (sin poder inscribirse)

## 🎯 Cambios Implementados

### 1. Modelo Vecino
- ✅ Agregado campo `user` (OneToOneField con User de Django)
- ✅ Cada vecino está vinculado a un usuario del sistema

### 2. Formulario de Registro
- ✅ Agregados campos de contraseña y confirmación
- ✅ Validación de contraseñas coincidentes
- ✅ Validación de email único
- ✅ Validación de RUT único

### 3. Vistas Actualizadas
- ✅ `registrar_vecino`: Crea usuario y vecino, inicia sesión automáticamente
- ✅ `solicitar_certificado`: Usa el vecino del usuario actual (requiere login)
- ✅ `postular_proyecto`: Usa el vecino del usuario actual (requiere login)
- ✅ `inscribirse_actividad`: Usa el vecino del usuario actual (requiere login)
- ✅ `listar_certificados`: Admin ve todos, vecino ve solo los suyos
- ✅ `listar_proyectos`: Admin ve todos, vecino ve solo los suyos
- ✅ `listar_actividades`: Requiere login para inscribirse

### 4. Plantillas Actualizadas
- ✅ Navbar dinámico según tipo de usuario
- ✅ Eliminado menú desplegable de vecinos en formularios
- ✅ Actividades muestran botón de inscripción directo
- ✅ Certificados y proyectos se solicitan automáticamente al nombre del usuario
- ✅ Vistas diferenciadas para admin y vecinos

### 5. Formularios Simplificados
- ✅ `CertificadoForm`: Sin campo vecino (se usa el usuario actual)
- ✅ `ProyectoForm`: Sin campo vecino (se usa el usuario actual)
- ✅ Inscripción en actividades: Sin selector de vecino (se usa el usuario actual)

## 🚀 Cómo Iniciar el Sistema

1. **Activar el entorno virtual:**
   ```bash
   cd config
   ..\venv\Scripts\Activate.ps1
   ```

2. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

3. **Abrir en el navegador:**
   - http://localhost:8000/

4. **Iniciar sesión:**
   - Como admin: http://localhost:8000/login/ (admin / admin123)
   - Como vecino: http://localhost:8000/login/ (RUT / vecino123)

## 📝 Notas Importantes

- Los vecinos existentes tienen la contraseña por defecto: `vecino123`
- Los nuevos vecinos crean su propia contraseña al registrarse
- El RUT se usa como nombre de usuario
- Solo los administradores pueden aprobar/rechazar solicitudes
- Los vecinos solo ven sus propias solicitudes y proyectos
- Las actividades requieren login para inscribirse
- El sistema envía emails de notificación (si está configurado)

## 🔧 Mantenimiento

### Crear Usuario Admin Adicional
```bash
python manage.py createsuperuser
```

### Vincular Vecinos Existentes con Usuarios
```bash
python crear_usuarios_vecinos.py
```

### Cambiar Contraseña de Usuario
```bash
python manage.py changepassword [username]
```
