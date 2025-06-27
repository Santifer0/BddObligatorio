@echo off
echo Iniciando Backend y Frontend...
echo.
echo Presiona Ctrl+C para detener los servidores
echo.

start "Backend Flask" cmd /k "cd /d \"c:\Users\juanm\OneDrive\Documentos\ucu\Base de datos\BddObligatorio\" && \"c:/Users/juanm/OneDrive/Documentos/ucu/Base de datos/BddObligatorio/.venv/Scripts/python.exe\" app.py"

timeout /t 3 /nobreak > nul

start "Frontend React" cmd /k "cd /d \"c:\Users\juanm\OneDrive\Documentos\ucu\Base de datos\BddObligatorio\Frontend\obligatorioBasesDeDatos\" && npm run dev"

echo Servidores iniciados:
echo - Backend: http://localhost:5000
echo - Frontend: http://localhost:5173
echo.
pause
