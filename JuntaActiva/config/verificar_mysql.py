#!/usr/bin/env python
"""
Script para verificar la conexión a MySQL antes de ejecutar migraciones.
Uso: python verificar_mysql.py
"""

import os
import sys
from pathlib import Path

# Agregar el directorio del proyecto al path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    import django
    django.setup()
except Exception as e:
    print(f"❌ Error al configurar Django: {e}")
    sys.exit(1)

from django.conf import settings
from django.db import connection

def verificar_pymysql():
    """Verifica que PyMySQL esté instalado"""
    try:
        import pymysql
        print(f"✅ PyMySQL instalado: versión {pymysql.__version__}")
        return True
    except ImportError:
        print("❌ PyMySQL no está instalado")
        print("   Ejecuta: pip install pymysql cryptography")
        return False

def verificar_configuracion():
    """Verifica la configuración de la base de datos"""
    db_config = settings.DATABASES['default']
    engine = db_config['ENGINE']
    
    print("\n📋 Configuración de Base de Datos:")
    print(f"   Motor: {engine}")
    
    if 'mysql' in engine:
        print(f"   Base de datos: {db_config.get('NAME', 'N/A')}")
        print(f"   Usuario: {db_config.get('USER', 'N/A')}")
        print(f"   Host: {db_config.get('HOST', 'N/A')}")
        print(f"   Puerto: {db_config.get('PORT', 'N/A')}")
        return True
    elif 'sqlite' in engine:
        print(f"   Archivo: {db_config.get('NAME', 'N/A')}")
        print("\n⚠️  Estás usando SQLite, no MySQL")
        print("   Para usar MySQL, configura las variables en el archivo .env")
        return False
    else:
        print(f"   Motor desconocido: {engine}")
        return False

def verificar_conexion():
    """Intenta conectarse a la base de datos"""
    try:
        print("\n🔌 Intentando conectar a la base de datos...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            print(f"✅ Conexión exitosa!")
            print(f"   Versión de MySQL: {version}")
            
            # Verificar la base de datos actual
            cursor.execute("SELECT DATABASE()")
            db_name = cursor.fetchone()[0]
            print(f"   Base de datos actual: {db_name}")
            
            # Verificar tablas
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                print(f"   Tablas encontradas: {len(tables)}")
                print("   Primeras 5 tablas:")
                for table in tables[:5]:
                    print(f"     - {table[0]}")
            else:
                print("   ⚠️  No hay tablas. Ejecuta: python manage.py migrate")
            
        return True
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        print("\n💡 Posibles soluciones:")
        print("   1. Verifica que MySQL esté corriendo en XAMPP")
        print("   2. Verifica que la base de datos 'junta_vecinos' exista")
        print("   3. Verifica el usuario y contraseña en el archivo .env")
        print("   4. Verifica que el puerto sea el correcto (3306 por defecto)")
        return False

def main():
    print("=" * 60)
    print("🔍 VERIFICACIÓN DE CONFIGURACIÓN MYSQL")
    print("=" * 60)
    
    # Verificar PyMySQL
    if not verificar_pymysql():
        sys.exit(1)
    
    # Verificar configuración
    if not verificar_configuracion():
        sys.exit(1)
    
    # Verificar conexión
    if not verificar_conexion():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ TODO ESTÁ CONFIGURADO CORRECTAMENTE")
    print("=" * 60)
    print("\n📝 Próximos pasos:")
    print("   1. python manage.py migrate")
    print("   2. python manage.py createsuperuser")
    print("   3. python manage.py runserver")
    print()

if __name__ == '__main__':
    main()
