@echo off
echo ========================================
echo CONFIGURACION DE EMAIL PARA DJANGO
echo ========================================
echo.
echo Este script te ayudara a configurar el envio de emails reales.
echo.
echo IMPORTANTE: Necesitas una contrasena de aplicacion de Gmail
echo (no tu contrasena normal)
echo.
echo Como obtener una contrasena de aplicacion:
echo 1. Ve a https://myaccount.google.com/
echo 2. Seguridad ^> Verificacion en dos pasos (activala)
echo 3. Contrasenas de aplicaciones ^> Generar
echo 4. Copia la contrasena de 16 caracteres
echo.
echo ========================================
echo.

set /p EMAIL_USER="Ingresa tu email de Gmail: "
set /p EMAIL_PASS="Ingresa tu contrasena de aplicacion (sin espacios): "

echo.
echo ========================================
echo Configurando variables de entorno...
echo ========================================

set EMAIL_HOST_USER=%EMAIL_USER%
set EMAIL_HOST_PASSWORD=%EMAIL_PASS%

echo.
echo Variables configuradas:
echo - EMAIL_HOST_USER=%EMAIL_HOST_USER%
echo - EMAIL_HOST_PASSWORD=********** (oculta)
echo.
echo ========================================
echo IMPORTANTE: Estas variables solo funcionan en esta ventana
echo ========================================
echo.
echo Para que funcionen, debes iniciar el servidor desde ESTA MISMA VENTANA:
echo.
echo   cd config
echo   python manage.py runserver
echo.
echo Si cierras esta ventana, tendras que configurar de nuevo.
echo.
echo Para configuracion permanente, lee: CONFIGURAR_EMAIL.md
echo.
pause
