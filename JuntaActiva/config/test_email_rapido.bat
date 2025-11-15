@echo off
echo ========================================
echo PRUEBA RAPIDA DE EMAIL
echo ========================================
echo.
echo Este script probara el envio de emails
echo.
set /p EMAIL="Ingresa tu email para recibir la prueba: "
echo.
echo Enviando email de prueba a %EMAIL%...
echo.
python probar_email.py %EMAIL%
echo.
pause
