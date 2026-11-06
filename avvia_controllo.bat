@echo off
title Eatrading - controllo MT5
rem Doppio clic per lanciare il controllo della Fase 0 (prepara anche Python).
cd /d "%~dp0"
echo Eatrading - controllo di MT5 e del conto. Cartella: %CD%
call prepara_python.bat || goto fine
.venv\Scripts\python.exe fase0_controllo.py
:fine
echo.
pause
