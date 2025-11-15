# 📧 Cómo Enviar Emails Reales

## Estado Actual
✅ Los emails se ven en la consola (modo desarrollo)  
❌ Los emails NO se envían a los destinatarios reales

## Para Enviar Emails Reales

### Opción 1: Gmail (Más Fácil) 🎯

#### Paso 1: Obtener Contraseña de Aplicación de Gmail

1. **Habilita la verificación en 2 pasos:**
   - Ve a: https://myaccount.google.com/security
   - Busca "Verificación en dos pasos"
   - Actívala si no está activada

2. **Genera una contraseña de aplicación:**
   - Ve a: https://myaccount.google.com/apppasswords
   - Selecciona "Correo" y "Otro (nombre personalizado)"
   - Escribe "Django Junta Vecinos"
   - Haz clic en "Generar"
   - **Copia la contraseña de 16 caracteres** (ej: `abcd efgh ijkl mnop`)

#### Paso 2: Configurar Variables de Entorno

**En PowerShell (antes de iniciar el servidor):**

```powershell
# Reemplaza con tu email y contraseña de aplicación
$env:EMAIL_HOST_USER="tu_email@gmail.com"
$env:EMAIL_HOST_PASSWORD="abcd efgh ijkl mnop"
$env:DEFAULT_FROM_EMAIL="tu_email@gmail.com"

# Ahora inicia el servidor
python manage.py runserver
```

#### Paso 3: Verificar

Cuando inicies el servidor, deberías ver:
```
✓ Email configurado: Usando SMTP (smtp.gmail.com) con usuario tu_email@gmail.com
```

Si ves esto, los emails se enviarán realmente.

---

### Opción 2: Configuración Permanente con Archivo .env

#### Paso 1: Instalar python-decouple

```bash
pip install python-decouple
```

#### Paso 2: Crear archivo .env

Crea un archivo llamado `.env` en la carpeta `config/` con:

```env
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
DEFAULT_FROM_EMAIL=tu_email@gmail.com
```

#### Paso 3: Actualizar settings.py

Agrega al inicio de `settings.py`:

```python
from decouple import config

# Luego reemplaza os.environ.get por config:
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
```

---

## 🧪 Probar el Envío de Emails

### Método 1: Desde la Aplicación

1. Inicia el servidor con las variables configuradas
2. Inicia sesión como admin
3. Ve a "Gestión Certificados"
4. Aprueba un certificado
5. Verifica:
   - En la consola: Deberías ver "✓ Email enviado exitosamente"
   - En el email del vecino: Debería llegar el correo

### Método 2: Desde Django Shell

```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
from django.conf import settings

# Enviar email de prueba
send_mail(
    'Prueba de Email',
    'Este es un email de prueba desde Django.',
    settings.DEFAULT_FROM_EMAIL,
    ['destinatario@example.com'],  # Cambia por un email real
    fail_silently=False,
)
```

Si no hay errores, el email se envió correctamente.

---

## ⚠️ Solución de Problemas

### Error: "SMTPAuthenticationError"

**Causa:** Usuario o contraseña incorrectos

**Solución:**
- Verifica que estés usando la **contraseña de aplicación** (16 caracteres)
- NO uses tu contraseña normal de Gmail
- Verifica que la verificación en 2 pasos esté habilitada

### Error: "SMTPServerDisconnected"

**Causa:** Configuración de puerto o TLS incorrecta

**Solución:**
- Verifica que uses puerto 587
- Verifica que EMAIL_USE_TLS esté en True

### Los emails no llegan

**Posibles causas:**
1. Revisa la carpeta de spam del destinatario
2. Verifica que el email del destinatario sea correcto
3. Mira la consola para ver si hay errores
4. Verifica que las variables de entorno estén configuradas

### Mensaje: "Usando console backend"

**Causa:** Las variables de entorno no están configuradas

**Solución:**
- Configura EMAIL_HOST_USER y EMAIL_HOST_PASSWORD
- Reinicia el servidor después de configurar las variables

---

## 📋 Checklist Rápido

Antes de iniciar el servidor, verifica:

- [ ] Verificación en 2 pasos habilitada en Gmail
- [ ] Contraseña de aplicación generada (16 caracteres)
- [ ] Variables de entorno configuradas en PowerShell
- [ ] Servidor reiniciado después de configurar variables
- [ ] Mensaje "✓ Email configurado" aparece al iniciar servidor

---

## 🎯 Comandos Completos (Copia y Pega)

**PowerShell (reemplaza con tus datos):**

```powershell
# Configurar variables
$env:EMAIL_HOST_USER="tu_email@gmail.com"
$env:EMAIL_HOST_PASSWORD="tu contraseña de aplicacion"
$env:DEFAULT_FROM_EMAIL="tu_email@gmail.com"

# Verificar configuración
echo "Email: $env:EMAIL_HOST_USER"

# Iniciar servidor
cd config
python manage.py runserver
```

---

## 💡 Recomendaciones

### Para Desarrollo:
- Usa el modo consola (configuración actual)
- No necesitas configurar nada
- Los emails se ven en la terminal

### Para Pruebas:
- Usa Gmail con contraseña de aplicación
- Envía emails a tu propio correo para probar
- Verifica que lleguen correctamente

### Para Producción:
- Usa un servicio profesional como:
  - SendGrid (12,000 emails gratis/mes)
  - Mailgun (5,000 emails gratis/mes)
  - Amazon SES (muy económico)
- No uses Gmail para producción (límites de envío)

---

## 🔒 Seguridad

⚠️ **IMPORTANTE:**

- ❌ NUNCA subas tu contraseña al repositorio
- ❌ NUNCA compartas tu contraseña de aplicación
- ✅ Usa variables de entorno
- ✅ Agrega `.env` al `.gitignore`
- ✅ Revoca contraseñas de aplicación si las expones

---

## 📞 ¿Necesitas Ayuda?

Si sigues teniendo problemas:

1. Verifica que las variables estén configuradas:
   ```powershell
   echo $env:EMAIL_HOST_USER
   echo $env:EMAIL_HOST_PASSWORD
   ```

2. Mira los logs en la consola del servidor

3. Prueba con el shell de Django (método 2 arriba)

4. Verifica que tu cuenta de Gmail no tenga restricciones

---

## ✅ Resumen

**Modo Actual:** Console (emails en consola)  
**Para emails reales:** Configura EMAIL_HOST_USER y EMAIL_HOST_PASSWORD  
**Más fácil:** Gmail con contraseña de aplicación  
**Para producción:** Usa un servicio profesional

¡Una vez configurado, los emails se enviarán automáticamente! 📧
