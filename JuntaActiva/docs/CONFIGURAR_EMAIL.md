# Configuración de Email

Este documento explica cómo configurar el sistema para enviar correos electrónicos reales.

## Configuración con Gmail (Recomendado)

### Paso 1: Obtener Contraseña de Aplicación

1. Ir a: https://myaccount.google.com/
2. Seleccionar "Seguridad"
3. Activar "Verificación en dos pasos" (si no está activada)
4. Buscar "Contraseñas de aplicaciones"
5. Seleccionar:
   - Aplicación: Correo
   - Dispositivo: Otro (nombre personalizado) - "Django Junta Vecinos"
6. Click en "Generar"
7. Copiar la contraseña de 16 caracteres (sin espacios)

### Paso 2: Configurar Variables de Entorno

Editar o crear el archivo `config/.env`:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
DEFAULT_FROM_EMAIL=noreply@juntavecinos.cl
```

### Paso 3: Verificar Configuración

Iniciar el servidor:

```bash
cd config
python manage.py runserver
```

Deberías ver:
```
Email configurado: Usando SMTP (smtp.gmail.com) con usuario tu_email@gmail.com
```

## Configuración con Outlook/Hotmail

Editar `config/.env`:

```env
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@outlook.com
EMAIL_HOST_PASSWORD=tu_contraseña
DEFAULT_FROM_EMAIL=noreply@juntavecinos.cl
```

## Probar el Envío de Emails

### Método 1: Aprobar un Certificado

1. Iniciar sesión como admin
2. Ir a "Gestionar Certificados"
3. Aprobar un certificado pendiente
4. Verificar que el email se envió
5. Revisar la bandeja de entrada del vecino

### Método 2: Script de Prueba

```bash
cd config
python test_email_pdf.py
```

## Solución de Problemas

### Error: SMTPAuthenticationError

Causa: Credenciales incorrectas o contraseña de aplicación no configurada.

Solución:
- Usar contraseña de aplicación (no contraseña normal de Gmail)
- Verificar que la verificación en dos pasos esté activada
- Copiar la contraseña sin espacios

### Error: SMTPServerDisconnected

Causa: Configuración de puerto o TLS incorrecta.

Solución:
- Gmail: puerto 587 con TLS
- Outlook: puerto 587 con TLS
- Verificar que EMAIL_USE_TLS=True

### Error: Connection refused

Causa: Firewall o antivirus bloqueando la conexión.

Solución:
- Desactivar temporalmente el firewall/antivirus
- Verificar conexión a internet
- Intentar con otro proveedor de email

### Los emails no llegan

Posibles causas:
1. Revisar carpeta de Spam/Correo no deseado
2. Verificar que el email del vecino sea correcto
3. Algunos proveedores tardan unos minutos en entregar

## Seguridad

Importante:
1. Nunca subir el archivo `.env` a Git/GitHub
2. Nunca compartir contraseña de aplicación
3. Agregar `.env` al archivo `.gitignore`
4. Usar archivo `.env.example` para documentación (sin datos reales)

## Modo Desarrollo

Sin configuración de email, los mensajes se mostrarán en la consola del servidor (modo desarrollo).

Para habilitar este modo, simplemente no configurar las variables EMAIL_HOST_USER y EMAIL_HOST_PASSWORD.

## Verificación Final

Cuando todo esté configurado correctamente:

Al iniciar el servidor:
```
Email configurado: Usando SMTP (smtp.gmail.com) con usuario tu_email@gmail.com
```

Al aprobar un certificado:
```
Email con PDF adjunto enviado exitosamente a vecino@email.com
```

El vecino recibirá un email con:
- Notificación de aprobación
- PDF del certificado adjunto
- Fechas en español
- Código único del certificado

## Emails Automáticos del Sistema

El sistema envía emails automáticamente cuando:
- Se aprueba o rechaza un certificado
- Se cambia el estado de un proyecto
- Se hace miembro a un vecino
- Se aprueba o rechaza una reserva de espacio
