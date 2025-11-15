# Configuración de Email

## 📧 Estado Actual

El sistema está configurado para **imprimir los emails en la consola** durante el desarrollo (modo DEBUG=True). Esto significa que:

- ✅ Los emails se "envían" pero aparecen en la terminal donde corre el servidor
- ✅ No necesitas configurar nada para probar el sistema
- ✅ Puedes ver el contenido completo de los emails en la consola

## 🔍 Cómo Ver los Emails en Desarrollo

1. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

2. Realiza una acción que envíe email (aprobar certificado, aprobar proyecto, etc.)

3. Mira la consola donde corre el servidor, verás algo como:
   ```
   Content-Type: text/plain; charset="utf-8"
   MIME-Version: 1.0
   Content-Transfer-Encoding: 7bit
   Subject: Certificado de Residencia Aprobado
   From: noreply@juntavecinos.cl
   To: juan.perez@email.cl
   Date: Thu, 13 Nov 2025 12:00:00 -0000
   Message-ID: <...>

   Estimado/a Juan Pérez,

   Su solicitud de certificado de residencia ha sido aprobada.
   ...
   ```

## 📨 Configurar Email Real (Producción)

Si quieres enviar emails reales (por ejemplo, usando Gmail):

### Opción 1: Gmail con App Password (Recomendado)

1. **Habilita la verificación en 2 pasos** en tu cuenta de Gmail

2. **Genera una contraseña de aplicación:**
   - Ve a: https://myaccount.google.com/apppasswords
   - Selecciona "Correo" y "Otro (nombre personalizado)"
   - Copia la contraseña generada (16 caracteres)

3. **Configura las variables de entorno:**
   
   En Windows (PowerShell):
   ```powershell
   $env:EMAIL_HOST_USER="tu_email@gmail.com"
   $env:EMAIL_HOST_PASSWORD="tu_contraseña_de_aplicacion"
   $env:DEFAULT_FROM_EMAIL="noreply@juntavecinos.cl"
   ```

4. **Cambia DEBUG a False** en `config/settings.py` (solo para producción):
   ```python
   DEBUG = False
   ```

### Opción 2: Otro Proveedor SMTP

Edita `config/settings.py` y cambia:

```python
EMAIL_HOST = 'smtp.tu-proveedor.com'
EMAIL_PORT = 587  # o 465 para SSL
EMAIL_USE_TLS = True  # o False si usas SSL
EMAIL_HOST_USER = 'tu_usuario'
EMAIL_HOST_PASSWORD = 'tu_contraseña'
```

## 🧪 Probar el Envío de Emails

### Método 1: Desde la Aplicación

1. Inicia sesión como admin
2. Ve a "Gestión Certificados"
3. Aprueba un certificado
4. Verifica:
   - En desarrollo: Mira la consola
   - En producción: Revisa el email del vecino

### Método 2: Desde Django Shell

```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Prueba de Email',
    'Este es un email de prueba.',
    settings.DEFAULT_FROM_EMAIL,
    ['destinatario@example.com'],
    fail_silently=False,
)
```

## ⚠️ Solución de Problemas

### "SMTPAuthenticationError"
- Verifica que el usuario y contraseña sean correctos
- Si usas Gmail, asegúrate de usar una "App Password"
- Verifica que la verificación en 2 pasos esté habilitada

### "SMTPServerDisconnected"
- Verifica el puerto (587 para TLS, 465 para SSL)
- Verifica que EMAIL_USE_TLS esté configurado correctamente

### "Connection refused"
- Verifica que tu firewall permita conexiones SMTP
- Verifica que el servidor SMTP esté accesible

### Los emails no llegan
- Revisa la carpeta de spam
- Verifica que el email del destinatario sea correcto
- Mira los logs en la consola para ver errores

## 📋 Emails que Envía el Sistema

El sistema envía emails en las siguientes situaciones:

1. **Certificado Aprobado**
   - Destinatario: Vecino solicitante
   - Contenido: Código de certificado y enlace de descarga

2. **Certificado Rechazado**
   - Destinatario: Vecino solicitante
   - Contenido: Notificación de rechazo

3. **Proyecto Aprobado**
   - Destinatario: Vecino postulante
   - Contenido: Confirmación de aprobación

4. **Proyecto Rechazado**
   - Destinatario: Vecino postulante
   - Contenido: Notificación de rechazo

## 💡 Recomendaciones

- **Desarrollo:** Usa el backend de consola (configuración actual)
- **Pruebas:** Usa un servicio como Mailtrap.io
- **Producción:** Usa un servicio profesional como SendGrid, Mailgun, o Amazon SES

## 🔒 Seguridad

- ❌ **NUNCA** subas las credenciales de email al repositorio
- ✅ Usa variables de entorno para las credenciales
- ✅ Usa contraseñas de aplicación en lugar de tu contraseña real
- ✅ Considera usar un servicio de email transaccional para producción
