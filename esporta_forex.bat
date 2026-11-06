@echo off
title Eatrading - esporta_forex
rem Doppio clic per esportare lo storico dei prezzi da MT5 (lascia MT5 aperto).
cd /d "%~dp0"
echo Eatrading - esporta_forex. Cartella: %CD%
call prepara_python.bat || goto fine
.venv\Scripts\python.exe fase1_esporta_forex.py
:fine
echo.
pause
