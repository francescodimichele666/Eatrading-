@echo off
title Bot Eatrading - conto DEMO
rem Doppio clic per avviare il bot (solo conto DEMO). Se si ferma per un errore, riparte da solo.
cd /d "%~dp0"
echo ==========================================================
echo  Bot Eatrading - solo conto DEMO
echo  Cartella: %CD%
echo  Per fermarlo chiudi questa finestra.
echo ==========================================================
call prepara_python.bat || goto errore

:riavvia
echo.
echo Avvio il bot ...
.venv\Scripts\python.exe -m bot.principale
if errorlevel 2 (
    echo.
    echo Il bot si e' fermato per un motivo di sicurezza: leggi logs\bot.log
    goto errore
)
echo.
echo Il bot si e' fermato. Riparto tra 30 secondi. Chiudi questa finestra per fermarlo davvero.
timeout /t 30 /nobreak >nul
goto riavvia

:errore
echo.
pause
exit /b 1
