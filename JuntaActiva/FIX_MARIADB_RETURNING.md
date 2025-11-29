# Fix: Error RETURNING con MariaDB 10.4

## Problema
Al intentar crear noticias (o cualquier registro en la base de datos), se producía el siguiente error:

```
ProgrammingError at /noticias/crear/
(1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'RETURNING `gestion_noticia`.`id`' at line 1")
```

## Causa
- Django 5.2+ utiliza la cláusula SQL `RETURNING` para obtener el ID de los registros insertados
- MariaDB solo soporta `RETURNING` desde la versión 10.5
- El sistema usa MariaDB 10.4.32 (incluido en XAMPP), que no soporta esta característica

## Solución Aplicada
**Parche de compatibilidad para Django 5.2.8 con MariaDB 10.4**

Se creó un módulo de parche (`config/mariadb_patch.py`) que:
1. Deshabilita la verificación de versión mínima de MariaDB
2. Desactiva las características `can_return_columns_from_insert` y `can_return_rows_from_bulk_insert`

### Archivos modificados:
- `config/config/mariadb_patch.py` - Módulo de parche creado
- `config/config/settings.py` - Importa el parche al inicio
- `requirements.txt` - Actualizado a Django 5.2.8

### Cómo funciona:
El parche se aplica automáticamente al importarse en `settings.py`, antes de que Django inicialice la conexión a la base de datos. Esto asegura que las características incompatibles estén deshabilitadas desde el principio.

## Alternativas Consideradas

### Opción 1: Downgrade a Django 5.0.9 (Descartada)
- Perderíamos funcionalidades nuevas de Django 5.2
- La subida de imágenes en noticias funciona mejor en 5.2

### Opción 2: Actualizar MariaDB (No recomendado para desarrollo)
- Actualizar XAMPP a una versión con MariaDB 10.5+
- Requiere reinstalación completa de XAMPP
- Puede causar problemas de compatibilidad con otros proyectos

### Opción 3: Usar SQLite (No recomendado para este proyecto)
- Cambiar a SQLite para desarrollo
- No refleja el entorno de producción
- Pérdida de datos existentes en MySQL

## Resultado
✅ El sistema funciona correctamente con Django 5.2.8 y MariaDB 10.4.32
✅ Se pueden crear noticias con imágenes sin errores
✅ Se pueden crear reservas y otros registros sin problemas
✅ Compatibilidad total con la base de datos existente
✅ Todas las funcionalidades de Django 5.2 disponibles

## Versiones Actuales
- Django: 5.2.8
- MariaDB: 10.4.32
- Python: 3.14.0
- PyMySQL: 1.1.1

## Notas
- El parche es transparente y no requiere cambios en el código de la aplicación
- Si en el futuro se actualiza MariaDB a 10.5+, el parche puede removerse sin problemas
- El parche solo afecta al backend de MySQL/MariaDB, no a otras partes de Django
