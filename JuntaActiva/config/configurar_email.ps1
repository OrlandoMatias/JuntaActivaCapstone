# Script PowerShell para configurar email en Django

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CONFIGURACION DE EMAIL PARA DJANGO" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Este script te ayudara a configurar el envio de emails reales." -ForegroundColor Yellow
Write-Host ""
Write-Host "IMPORTANTE: Necesitas una contrasena de aplicacion de Gmail" -ForegroundColor Red
Write-Host "(no tu contrasena normal)" -ForegroundColor Red
Write-Host ""
Write-Host "Como obtener una contrasena de aplicacion:" -ForegroundColor Green
Write-Host "1. Ve a https://myaccount.google.com/" -ForegroundColor White
Write-Host "2. Seguridad > Verificacion en dos pasos (activala)" -ForegroundColor White
Write-Host "3. Contrasenas de aplicaciones > Generar" -ForegroundColor White
Write-Host "4. Copia la contrasena de 16 caracteres" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$EMAIL_USER = Read-Host "Ingresa tu email de Gmail"
$EMAIL_PASS = Read-Host "Ingresa tu contrasena de aplicacion (sin espacios)" -AsSecureString
$EMAIL_PASS_PLAIN = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($EMAIL_PASS))

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Configurando variables de entorno..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

$env:EMAIL_HOST_USER = $EMAIL_USER
$env:EMAIL_HOST_PASSWORD = $EMAIL_PASS_PLAIN

Write-Host ""
Write-Host "Variables configuradas:" -ForegroundColor Green
Write-Host "- EMAIL_HOST_USER=$env:EMAIL_HOST_USER" -ForegroundColor White
Write-Host "- EMAIL_HOST_PASSWORD=********** (oculta)" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "IMPORTANTE: Estas variables solo funcionan en esta ventana" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para que funcionen, debes iniciar el servidor desde ESTA MISMA VENTANA:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  cd config" -ForegroundColor White
Write-Host "  python manage.py runserver" -ForegroundColor White
Write-Host ""
Write-Host "Si cierras esta ventana, tendras que configurar de nuevo." -ForegroundColor Yellow
Write-Host ""
Write-Host "Para configuracion permanente, lee: CONFIGURAR_EMAIL.md" -ForegroundColor Green
Write-Host ""
Write-Host "Presiona Enter para continuar..." -ForegroundColor Cyan
Read-Host
