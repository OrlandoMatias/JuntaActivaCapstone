# 🚀 Inicio Rápido - Envío de Emails Reales

## ⚡ Configuración Rápida (5 minutos)

### Paso 1: Obtener Contraseña de Gmail

1. Ve a: https://myaccount.google.com/security
2. Activa **Verificación en dos pasos**
3. Busca **Contraseñas de aplicaciones**
4. Genera una contraseña para "Correo"
5. Copia la contraseña de 16 caracteres (sin espacios)

### Paso 2: Configurar Email

#### Opción A: Script Automático (Recomendado)

**PowerShell:**
```powershell
cd config
.\configurar_email.ps1
```

**CMD:**
```cmd
cd config
configurar_email.bat
```

Sigue las instrucciones en pantalla.

#### Opción B: Manual

**PowerShell:**
```powershell
$env:EMAIL_HOST_USER="tu_email@gmail.com"
$env:EMAIL_HOST_PASSWORD="tu_contraseña_de_aplicacion"
```

**CMD:**
```cmd
set EMAIL_HOST_USER=tu_email@gmail.com
set EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
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

### Paso 4: Probar

1. Abre http://localhost:8000
2. Inicia sesión como admin
3. Aprueba un certificado
4. Verifica que el email se envió:
   ```
   ✓ Email con PDF adjunto enviado exitosamente a vecino@email.com
   ```
5. Revisa la bandeja del vecino

---

## ✅ ¡Listo!

Ahora los emails se envían automáticamente con:
- ✅ PDF del certificado adjunto
- ✅ Fechas en español
- ✅ Notificaciones automáticas

---

## 📚 Más Información

- **Configuración detallada:** Lee `CONFIGURAR_EMAIL.md`
- **Solución de problemas:** Lee `CONFIGURAR_EMAIL.md` sección "Solución de Problemas"
- **Configuración permanente:** Lee `CONFIGURAR_EMAIL.md` sección "Opción 3: Archivo .env"
