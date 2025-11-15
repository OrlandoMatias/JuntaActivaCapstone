# Comandos para subir a GitHub

## 1. Inicializar repositorio local
```bash
git init
```

## 2. Agregar todos los archivos
```bash
git add .
```

## 3. Hacer el primer commit
```bash
git commit -m "Sistema completo de gestión vecinal con reservas, certificados y proyectos"
```

## 4. Conectar con tu repositorio de GitHub
Reemplaza <tu-usuario> y <tu-repositorio> con tus datos:
```bash
git remote add origin https://github.com/<tu-usuario>/<tu-repositorio>.git
```

## 5. Verificar la conexión
```bash
git remote -v
```

## 6. Subir los cambios
```bash
git branch -M main
git push -u origin main
```

---

## Para actualizaciones futuras:

### 1. Ver cambios
```bash
git status
```

### 2. Agregar cambios
```bash
git add .
```

### 3. Hacer commit
```bash
git commit -m "Descripción de los cambios"
```

### 4. Subir a GitHub
```bash
git push
```

---

## Comandos útiles:

### Ver historial de commits
```bash
git log --oneline
```

### Ver diferencias
```bash
git diff
```

### Descartar cambios locales
```bash
git checkout -- <archivo>
```

### Actualizar desde GitHub
```bash
git pull
```

---

## Si ya existe un repositorio en GitHub:

### Opción 1: Clonar y copiar archivos
```bash
git clone https://github.com/<tu-usuario>/<tu-repositorio>.git
# Copiar tus archivos al directorio clonado
cd <tu-repositorio>
git add .
git commit -m "Actualización del sistema"
git push
```

### Opción 2: Forzar push (cuidado, sobrescribe el remoto)
```bash
git init
git add .
git commit -m "Sistema completo"
git remote add origin https://github.com/<tu-usuario>/<tu-repositorio>.git
git push -f origin main
```
