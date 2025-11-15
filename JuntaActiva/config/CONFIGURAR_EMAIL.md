# 📧 Configuración de Email para Envío Real

## 🎯 Objetivo
Configurar el sistema para enviar correos electrónicos reales (no solo imprimirlos en consola).

---

## 📋 Opción 1: Gmail (Recomendado)

### Paso 1: Obtener Contraseña de Aplicación de Gmail

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. En el menú izquierdo, selecciona **Seguridad**
3. En "Cómo inicias sesión en Google", activa la **Verificación en dos pasos** (si no está activada)
4. Una vez activada, busca **Contraseñas de aplicaciones**
5. Selecciona:
   - Aplicación: **Correo**
   - Dispositivo: **Otro (nombre personalizado)** → escribe "Django Junta Vecinos"
6. Haz clic en **Generar**
7. Copia la contraseña de 16 caracteres que aparece (sin espacios)

### Paso 2: Configurar Variables de Entorno

#### En Windows (CMD):
```cmd
set EMAIL_HOST_USER=tu_email@gmail.com
set EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion_sin_espacios
```

#### En Windows (PowerShell):
```powershell
$env:EMAIL_HOST_USER="tu_email@gmail.com"
$env:EMAIL_HOST_PASSWORD="tu_contraseña_de_aplicacion_sin_espacios"
```

#### En Linux/Mac:
```bash
export EMAIL_HOST_USER=tu_email@gmail.com
export EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion_sin_espacios
```

### Paso 3: Iniciar el Servidor

```bash
cd config
python manage.py runserver
```

Deberías ver:
```
✓ Email configurado: Usando SMTP (smtp.gmail.com) con usuario tu_email@gmail.com
```

---

## 📋 Opción 2: Outlook/Hotmail

### Configurar Variables de Entorno

#### En Windows (CMD):
```cmd
set EMAIL_HOST=smtp-mail.outlook.com
set EMAIL_PORT=587
set EMAIL_USE_TLS=True
set EMAIL_HOST_USER=tu_email@outlook.com
set EMAIL_HOST_PASSWORD=tu_contraseña
```

#### En Windows (PowerShell):
```powershell
$env:EMAIL_HOST="smtp-mail.outlook.com"
$env:EMAIL_PORT="587"
$env:EMAIL_USE_TLS="True"
$env:EMAIL_HOST_USER="tu_email@outlook.com"
$env:EMAIL_HOST_PASSWORD="tu_contraseña"
```

---

## 📋 Opción 3: Archivo .env (Permanente)

Para no tener que configurar las variables cada vez que inicias el servidor:

### Paso 1: Instalar python-decouple

```bash
pip install python-decouple
```

### Paso 2: Crear archivo .env

Crea un archivo llamado `.env` en la carpeta `config/` con este contenido:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
DEFAULT_FROM_EMAIL=tu_email@gmail.com
```

### Paso 3: Modificar settings.py

Agrega al inicio de `config/config/settings.py`:

```python
from decouple import config

# Luego reemplaza las líneas de EMAIL_HOST_USER y EMAIL_HOST_PASSWORD por:
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
```

---

## 🧪 Probar el Envío de Emails

### Método 1: Aprobar un Certificado

1. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

2. Inicia sesión como admin

3. Ve a "Gestionar Certificados"

4. Aprueba un certificado pendiente

5. Verifica que el email se envió:
   ```
   ✓ Email con PDF adjunto enviado exitosamente a vecino@email.com
   ```

6. Revisa la bandeja de entrada del vecino

### Método 2: Script de Prueba

```bash
cd config
python test_email_pdf.py
```

---

## ⚠️ Solución de Problemas

### Error: "SMTPAuthenticationError"

**Causa:** Credenciales incorrectas o contraseña de aplicación no configurada.

**Solución:**
- Verifica que usas una **contraseña de aplicación** (no tu contraseña normal de Gmail)
- Verifica que la verificación en dos pasos esté activada en Gmail
- Copia la contraseña sin espacios

### Error: "SMTPServerDisconnected"

**Causa:** Configuración de puerto o TLS incorrecta.

**Solución:**
- Gmail: puerto 587 con TLS
- Outlook: puerto 587 con TLS
- Verifica que `EMAIL_USE_TLS=True`

### Error: "Connection refused"

**Causa:** Firewall o antivirus bloqueando la conexión.

**Solución:**
- Desactiva temporalmente el firewall/antivirus
- Verifica tu conexión a internet
- Intenta con otro proveedor de email

### Los emails no llegan

**Posibles causas:**
1. Revisa la carpeta de **Spam/Correo no deseado**
2. Verifica que el email del vecino sea correcto
3. Algunos proveedores tardan unos minutos en entregar

---

## 📝 Ejemplo Completo (Gmail)

```bash
# 1. Configurar variables de entorno (PowerShell en Windows)
$env:EMAIL_HOST_USER="juntavecinos@gmail.com"
$env:EMAIL_HOST_PASSWORD="abcd efgh ijkl mnop"

# 2. Iniciar servidor
cd config
python manage.py runserver

# Deberías ver:
# ✓ Email configurado: Usando SMTP (smtp.gmail.com) con usuario juntavecinos@gmail.com

# 3. Aprobar un certificado desde el navegador

# 4. Verificar en la consola:
# ✓ Email con PDF adjunto enviado exitosamente a vecino@email.com

# 5. Revisar el correo del vecino
```

---

## 🔒 Seguridad

### ⚠️ IMPORTANTE:

1. **Nunca** subas el archivo `.env` a Git/GitHub
2. **Nunca** compartas tu contraseña de aplicación
3. Agrega `.env` al archivo `.gitignore`:
   ```
   .env
   *.env
   ```

4. Si subes el código a GitHub, usa el archivo `.env.example` (sin datos reales)

---

## ✅ Verificación Final

Cuando todo esté configurado correctamente, al iniciar el servidor verás:

```
✓ Email configurado: Usando SMTP (smtp.gmail.com) con usuario tu_email@gmail.com
```

Y al aprobar un certificado:

```
✓ Email con PDF adjunto enviado exitosamente a vecino@email.com
```

El vecino recibirá un email con:
- ✅ Notificación de aprobación
- ✅ PDF del certificado adjunto
- ✅ Fechas en español
- ✅ Código único del certificado

---

## 🎉 ¡Listo!

Ahora el sistema enviará correos electrónicos reales automáticamente cuando:
- Se apruebe un certificado
- Se rechace un certificado
- Se cambie el estado de un proyecto
