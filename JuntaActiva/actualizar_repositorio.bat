@echo off
echo ========================================
echo Actualizando repositorio en GitHub
echo Repositorio: ProyectoJuntaActiva
echo ========================================
echo.

REM Verificar si ya esta inicializado
if not exist .git (
    echo Inicializando repositorio...
    git init
    git remote add origin https://github.com/OrlandoMatias/ProyectoJuntaActiva.git
    echo.
)

REM Agregar cambios
echo Agregando cambios...
git add .
echo.

REM Hacer commit
set /p mensaje="Ingresa el mensaje del commit (o presiona Enter para usar mensaje por defecto): "
if "%mensaje%"=="" set mensaje=Actualizacion del sistema

echo.
echo Creando commit: %mensaje%
git commit -m "%mensaje%"
echo.

REM Subir cambios
echo Subiendo a GitHub...
git push -u origin main
echo.

echo ========================================
echo Actualizacion completada!
echo ========================================
pause
