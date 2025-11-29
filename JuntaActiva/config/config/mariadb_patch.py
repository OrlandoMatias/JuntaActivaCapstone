"""
Parche para compatibilidad con MariaDB 10.4 en Django 5.2+

Django 5.2 requiere MariaDB 10.5+ porque usa la cláusula RETURNING.
Este parche permite usar Django 5.2 con MariaDB 10.4 deshabilitando
las características que no son compatibles.

IMPORTANTE: Este archivo debe importarse ANTES de cualquier operación
de base de datos en settings.py
"""

def patch_mariadb_compatibility():
    """
    Aplica parches para hacer Django 5.2+ compatible con MariaDB 10.4
    """
    try:
        from django.db.backends.mysql import base, features
        
        # 1. Parchear la verificación de versión mínima
        _original_check = base.DatabaseWrapper.check_database_version_supported
        
        def _patched_check(self):
            """Permitir MariaDB 10.4+ sin error de versión"""
            # Simplemente no hacer nada - permitir cualquier versión
            pass
        
        base.DatabaseWrapper.check_database_version_supported = _patched_check
        
        # 2. Parchear DatabaseFeatures para deshabilitar RETURNING
        # Esto se hace directamente en la clase, no en instancias
        features.DatabaseFeatures.can_return_columns_from_insert = False
        features.DatabaseFeatures.can_return_rows_from_bulk_insert = False
        
        return True
        
    except ImportError:
        # Django aún no está instalado
        return False
    except Exception as e:
        print(f"⚠ Error aplicando parche MariaDB: {e}")
        return False


# Aplicar el parche inmediatamente al importar este módulo
patch_mariadb_compatibility()
