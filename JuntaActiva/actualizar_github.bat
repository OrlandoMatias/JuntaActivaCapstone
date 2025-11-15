@echo off
echo ========================================
echo Actualizando proyecto en GitHub
echo ========================================
echo.

REM Ver estado
echo Estado actual:
git status
echo.

REM Agregar cambios
echo Agregando cambios...
git add .
echo.

REM Pedir mensaje de commit
set /p mensaje="Ingresa el mensaje del commit: "
echo.

REM Hacer commit
echo Haciendo commit...
git commit -m "%mensaje%"
echo.

REM Subir cambios
echo Subiendo a GitHub...
git push
echo.

echo ========================================
echo Actualizacion completada!
echo ========================================
pause
