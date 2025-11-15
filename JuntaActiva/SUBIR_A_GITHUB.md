# 📤 Guía para Subir el Proyecto a GitHub

## Paso 1: Crear Repositorio en GitHub

1. **Ve a GitHub:** https://github.com/
2. **Inicia sesión** en tu cuenta
3. **Haz clic en el botón "+" (arriba derecha)** → "New repository"
4. **Configura el repositorio:**
   - **Repository name:** `sistema-gestion-vecinal` (o el nombre que prefieras)
   - **Description:** "Sistema web para gestión de Junta de Vecinos con Django"
   - **Visibility:** Public o Private (tu elección)
   - **NO marques** "Add a README file" (ya lo tenemos)
   - **NO marques** "Add .gitignore" (ya lo tenemos)
   - **NO marques** "Choose a license" (ya lo tenemos)
5. **Haz clic en "Create repository"**

GitHub te mostrará una página con instrucciones. **Copia la URL del repositorio** (algo como: `https://github.com/tu-usuario/sistema-gestion-vecinal.git`)

---

## Paso 2: Inicializar Git en tu Proyecto

Abre PowerShell en la carpeta raíz del proyecto (donde está la carpeta `config` y `venv`):

```powershell
# Verificar que estás en la carpeta correcta
pwd
# Deberías ver algo como: C:\Users\...\ProyectoJuntaActiva

# Inicializar repositorio Git
git init

# Verificar que se creó
ls -Force
# Deberías ver una carpeta .git
```

---

## Paso 3: Configurar Git (Primera vez)

Si es la primera vez que usas Git en tu computadora:

```powershell
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email (el mismo de GitHub)
git config --global user.email "tu_email@example.com"

# Verificar configuración
git config --global --list
```

---

## Paso 4: Agregar Archivos al Repositorio

```powershell
# Ver el estado actual
git status

# Agregar todos los archivos (excepto los del .gitignore)
git add .

# Verificar qué se agregó
git status
# Deberías ver muchos archivos en verde
```

---

## Paso 5: Hacer el Primer Commit

```powershell
# Crear el commit inicial
git commit -m "Initial commit: Sistema de Gestión Vecinal completo"

# Verificar el commit
git log --oneline
```

---

## Paso 6: Conectar con GitHub

```powershell
# Agregar el repositorio remoto (reemplaza con TU URL)
git remote add origin https://github.com/tu-usuario/sistema-gestion-vecinal.git

# Verificar que se agregó correctamente
git remote -v
```

---

## Paso 7: Subir el Código a GitHub

```powershell
# Cambiar el nombre de la rama a 'main' (si es necesario)
git branch -M main

# Subir el código a GitHub
git push -u origin main
```

Si te pide autenticación:
- **Usuario:** Tu nombre de usuario de GitHub
- **Contraseña:** Usa un **Personal Access Token** (no tu contraseña normal)

### Crear Personal Access Token:
1. Ve a: https://github.com/settings/tokens
2. Click en "Generate new token" → "Generate new token (classic)"
3. Nombre: "Django Project"
4. Selecciona: `repo` (todos los permisos de repositorio)
5. Click en "Generate token"
6. **Copia el token** (solo se muestra una vez)
7. Úsalo como contraseña cuando Git te lo pida

---

## Paso 8: Verificar en GitHub

1. Ve a tu repositorio en GitHub: `https://github.com/tu-usuario/sistema-gestion-vecinal`
2. Deberías ver todos tus archivos
3. El README.md se mostrará automáticamente en la página principal

---

## 🎉 ¡Listo!

Tu proyecto ya está en GitHub. Ahora puedes:

- Compartir el enlace con otros
- Clonar el proyecto en otras computadoras
- Colaborar con otros desarrolladores
- Hacer seguimiento de cambios

---

## 📝 Comandos Útiles para el Futuro

### Hacer cambios y subirlos:

```powershell
# Ver qué archivos cambiaron
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

### Ver historial:

```powershell
# Ver commits
git log --oneline

# Ver cambios en un archivo
git diff nombre_archivo.py
```

### Descargar cambios:

```powershell
# Si trabajas desde otra computadora
git pull
```

---

## ⚠️ Importante: Archivos Ignorados

El `.gitignore` ya está configurado para NO subir:

- ❌ `venv/` - Entorno virtual (muy pesado)
- ❌ `db.sqlite3` - Base de datos (datos sensibles)
- ❌ `.env` - Variables de entorno (contraseñas)
- ❌ `__pycache__/` - Archivos de caché
- ❌ `.kiro/` - Archivos de Kiro IDE

Estos archivos NO se subirán a GitHub, lo cual es correcto por seguridad.

---

## 🔒 Seguridad

**NUNCA subas a GitHub:**
- Contraseñas
- Tokens de API
- Claves secretas
- Datos personales de usuarios
- Base de datos con información real

El `.gitignore` ya protege estos archivos, pero siempre verifica con `git status` antes de hacer commit.

---

## 🆘 Solución de Problemas

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/tu-usuario/sistema-gestion-vecinal.git
```

### Error: "failed to push"
```powershell
# Descargar cambios primero
git pull origin main --rebase
git push
```

### Error: "Authentication failed"
- Usa un Personal Access Token en lugar de tu contraseña
- Verifica que el token tenga permisos de `repo`

---

## 📞 ¿Necesitas Ayuda?

Si tienes problemas:
1. Copia el mensaje de error completo
2. Busca en Google: "git [tu error]"
3. Revisa la documentación de Git: https://git-scm.com/doc

---

## ✅ Checklist Final

Antes de subir, verifica:

- [ ] `.gitignore` está creado
- [ ] `README.md` está completo
- [ ] `requirements.txt` tiene todas las dependencias
- [ ] No hay contraseñas en el código
- [ ] La base de datos NO se sube (está en .gitignore)
- [ ] El entorno virtual NO se sube (está en .gitignore)

---

¡Tu proyecto ya está en GitHub y listo para compartir! 🚀
