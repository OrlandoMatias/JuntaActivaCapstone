# Configuración de Base de Datos

Este documento explica cómo configurar la base de datos del sistema.

## SQLite (Por Defecto)

SQLite es la opción por defecto y no requiere configuración adicional.

**Ventajas:**
- Sin instalación adicional
- Ideal para desarrollo
- Archivo único portable

**Desventajas:**
- No recomendado para producción
- Limitado en concurrencia

## MySQL con XAMPP (Recomendado para Windows)

### Instalación de XAMPP

1. Descargar XAMPP 8.2.12 o superior:
   - Link: https://www.apachefriends.org/
   - Link directo: https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.2.12/

2. Instalar XAMPP:
   - Marcar: MySQL, phpMyAdmin, Apache
   - Carpeta de instalación: C:\xampp

3. Iniciar servicios:
   - Abrir XAMPP Control Panel
   - Click en "Start" junto a MySQL
   - Click en "Start" junto a Apache

### Crear Base de Datos

**Opción A: Usando phpMyAdmin (Recomendado)**

1. Abrir: http://localhost/phpmyadmin
2. Click en "Nueva" o "New"
3. Nombre: `junta_vecinos`
4. Cotejamiento: `utf8mb4_unicode_ci`
5. Click en "Crear"

**Opción B: Usando línea de comandos**

```cmd
cd C:\xampp\mysql\bin
mysql -u root
```

```sql
CREATE DATABASE junta_vecinos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### Configurar Django

1. Crear archivo `config/.env`:

```env
DB_ENGINE=mysql
DB_NAME=junta_vecinos
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

Nota: En XAMPP, el usuario root no tiene contraseña por defecto.

2. Ejecutar migraciones:

```cmd
cd config
python manage.py migrate
```

3. Verificar conexión:

```cmd
python verificar_mysql.py
```

### Crear Usuario MySQL (Opcional pero Recomendado)

Para mayor seguridad, crear un usuario específico:

1. En phpMyAdmin, ir a "Cuentas de usuario"
2. Click en "Agregar cuenta de usuario"
3. Completar:
   - Usuario: `junta_user`
   - Host: `localhost`
   - Contraseña: (elegir una segura)
4. Marcar: "Otorgar todos los privilegios para la base de datos junta_vecinos"
5. Click en "Continuar"

6. Actualizar `config/.env`:

```env
DB_USER=junta_user
DB_PASSWORD=tu_contraseña
```

## MySQL Server (Sin XAMPP)

### Instalación

1. Descargar MySQL Community Server:
   - Link: https://dev.mysql.com/downloads/mysql/

2. Instalar siguiendo el asistente

3. Crear base de datos:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE junta_vecinos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'junta_user'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON junta_vecinos.* TO 'junta_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

4. Configurar `config/.env` como se indicó anteriormente

## Verificación

Para verificar que la conexión funciona correctamente:

```bash
cd config
python verificar_mysql.py
```

Deberías ver:
```
Conexión exitosa
Versión de MySQL: 10.x.x-MariaDB
Base de datos actual: junta_vecinos
```

## Backup y Restauración

### Hacer Backup

**Usando phpMyAdmin:**
1. Seleccionar base de datos `junta_vecinos`
2. Click en "Exportar"
3. Click en "Continuar"
4. Se descarga archivo `junta_vecinos.sql`

**Usando línea de comandos:**
```bash
mysqldump -u root junta_vecinos > backup.sql
```

### Restaurar Backup

**Usando phpMyAdmin:**
1. Seleccionar base de datos `junta_vecinos`
2. Click en "Importar"
3. Seleccionar archivo `.sql`
4. Click en "Continuar"

**Usando línea de comandos:**
```bash
mysql -u root junta_vecinos < backup.sql
```

## Cambiar entre SQLite y MySQL

### De SQLite a MySQL

1. Hacer backup de datos (opcional):
```bash
python manage.py dumpdata > backup.json
```

2. Configurar MySQL en `.env`

3. Ejecutar migraciones:
```bash
python manage.py migrate
```

4. Restaurar datos (opcional):
```bash
python manage.py loaddata backup.json
```

### De MySQL a SQLite

1. Hacer backup de datos:
```bash
python manage.py dumpdata > backup.json
```

2. Eliminar o comentar variables MySQL en `.env`

3. Ejecutar migraciones:
```bash
python manage.py migrate
```

4. Restaurar datos:
```bash
python manage.py loaddata backup.json
```

## Solución de Problemas

### MySQL no inicia en XAMPP

**Causa:** Puerto 3306 ocupado

**Solución:**
1. En XAMPP Control Panel, click en "Config" junto a MySQL
2. Seleccionar "my.ini"
3. Buscar `port=3306` y cambiar a `port=3307`
4. Guardar y reiniciar MySQL
5. Actualizar `.env`: `DB_PORT=3307`

### Error: Access denied for user

**Verificar:**
- Usuario y contraseña en `.env` sean correctos
- Usuario tenga permisos en la base de datos
- No haya espacios extra en `.env`

### Error: Can't connect to MySQL server

**Verificar:**
- MySQL esté corriendo (verde en XAMPP)
- Puerto correcto en `.env`
- Firewall no bloquee la conexión

### Error: No module named 'pymysql'

**Solución:**
```bash
pip install pymysql cryptography
```

## Requisitos de Versión

- **Django 5.0+:** Requiere MariaDB 10.5+ o MySQL 8.0+
- **Django 4.2:** Compatible con MariaDB 10.4+ o MySQL 5.7+

Si tienes XAMPP antiguo con MariaDB 10.4, el sistema incluye un parche de compatibilidad automático.

## Rendimiento

Para mejorar el rendimiento en producción:

1. Configurar índices en campos frecuentemente consultados
2. Usar conexión persistente en `settings.py`:
```python
DATABASES = {
    'default': {
        ...
        'CONN_MAX_AGE': 600,
    }
}
```

3. Configurar pool de conexiones
4. Optimizar consultas con `select_related()` y `prefetch_related()`
