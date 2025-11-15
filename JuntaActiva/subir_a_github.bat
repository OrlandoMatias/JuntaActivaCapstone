@echo off
echo ========================================
echo Subiendo proyecto a GitHub
echo Repositorio: ProyectoJuntaActiva
echo ========================================
echo.

REM Configurar Git (primera vez)
echo [1/6] Configurando Git...
git config --global user.name "Orlando Matias"
git config --global user.email "elias.lopez.xd2@gmail.com"
echo Configuracion completada.
echo.

REM Inicializar repositorio
echo [2/6] Inicializando repositorio...
git init
echo Repositorio inicializado.
echo.

REM Agregar archivos
echo [3/6] Agregando archivos al repositorio...
git add .
echo Archivos agregados.
echo.

REM Hacer commit
echo [4/6] Creando commit...
git commit -m "Sistema completo de gestion vecinal - Reservas, Certificados, Proyectos y Membresia"
echo Commit creado.
echo.

REM Conectar con GitHub
echo [5/6] Conectando con GitHub...
git remote add origin https://github.com/OrlandoMatias/ProyectoJuntaActiva.git
echo Conexion establecida.
echo.

REM Subir a GitHub
echo [6/6] Subiendo archivos a GitHub...
git branch -M main
git push -u origin main
echo.

echo ========================================
echo COMPLETADO!
echo Tu proyecto esta en GitHub
echo ========================================
echo.
pause
