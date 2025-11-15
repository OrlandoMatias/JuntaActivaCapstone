# 🚀 Inicio Rápido

## Iniciar el Sistema

```bash
cd config
python manage.py runserver
```

Luego abre: **http://localhost:8000/**

---

## 🔐 Credenciales

### Administrador
- **Usuario:** `admin`
- **Contraseña:** `admin123`

### Vecinos Existentes
- **Usuario:** `12345678-9` (o cualquier RUT de vecino)
- **Contraseña:** `vecino123`

---

## ✨ Nuevas Funcionalidades

### 1. 📄 Descargar Certificados en PDF
1. Inicia sesión como vecino
2. Ve a "Mis Certificados"
3. Haz clic en "📄 Descargar PDF" (solo certificados aprobados)

### 2. 🚪 Desinscribirse de Actividades
1. Inicia sesión como vecino
2. Ve a "Actividades"
3. Si estás inscrito, haz clic en "Desinscribirse"

### 3. 📧 Notificaciones por Email
- En desarrollo: Los emails se imprimen en la consola del servidor
- Mira la terminal donde corre `runserver` para ver los emails

---

## 📚 Documentación Completa

- **INSTRUCCIONES_LOGIN.md** - Sistema de autenticación
- **CONFIGURACION_EMAIL.md** - Configurar emails reales
- **MEJORAS_IMPLEMENTADAS.md** - Todas las mejoras en detalle

---

## 🧪 Prueba Rápida

### Como Vecino:
1. Login: http://localhost:8000/login/ (`12345678-9` / `vecino123`)
2. Solicitar certificado
3. Ver mis certificados
4. Inscribirse en actividad
5. Desinscribirse de actividad

### Como Admin:
1. Login: http://localhost:8000/login/ (`admin` / `admin123`)
2. Aprobar certificado (mira la consola para ver el email)
3. Ver que el vecino puede descargar el PDF
4. Gestionar proyectos y actividades

---

## ⚡ Comandos Útiles

```bash
# Crear superusuario adicional
python manage.py createsuperuser

# Verificar sistema
python manage.py check

# Crear datos de prueba
python populate_test_data.py

# Vincular vecinos con usuarios
python crear_usuarios_vecinos.py

# Acceder a shell de Django
python manage.py shell
```

---

## 🎯 Flujo Típico de Uso

### Vecino Nuevo:
1. Registrarse → http://localhost:8000/vecinos/registrar/
2. Crear contraseña
3. Iniciar sesión automáticamente
4. Solicitar certificado
5. Postular proyecto
6. Inscribirse en actividades

### Administrador:
1. Iniciar sesión
2. Revisar solicitudes de certificados
3. Aprobar/rechazar (se envía email automático)
4. Revisar proyectos vecinales
5. Aprobar/rechazar proyectos
6. Crear noticias
7. Gestionar vecinos

---

## 🐛 Solución Rápida de Problemas

### El servidor no inicia
```bash
python manage.py migrate
python manage.py runserver
```

### No puedo iniciar sesión
- Verifica las credenciales
- Admin: `admin` / `admin123`
- Vecino: `[RUT]` / `vecino123`

### No veo los emails
- Los emails se imprimen en la consola donde corre el servidor
- Mira la terminal, no el navegador

### Error al descargar PDF
- Verifica que reportlab esté instalado: `pip install reportlab`
- Verifica que el certificado esté aprobado

---

## 📞 ¿Necesitas Ayuda?

1. Revisa la documentación en los archivos `.md`
2. Ejecuta `python manage.py check` para ver errores
3. Mira los logs en la consola del servidor
4. Verifica que todas las dependencias estén instaladas

---

## 🎉 ¡Listo!

El sistema está completamente funcional con:
- ✅ Autenticación personalizada
- ✅ Vistas diferenciadas (admin/vecino)
- ✅ Descarga de certificados en PDF
- ✅ Sistema de notificaciones por email
- ✅ Gestión de inscripciones en actividades
- ✅ Interfaz amigable y responsive

¡Disfruta usando el Sistema de Gestión Vecinal! 🏘️
