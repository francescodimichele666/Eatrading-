@echo off
rem Doppio clic per avviare il bot (solo conto DEMO). Se si ferma per un errore, riparte da solo.
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
    echo Prima lancia avvia_controllo.bat almeno una volta.
    pause
    exit /b 1
)
.venv\Scripts\python.exe -m pip install --quiet -r requirements.txt

:riavvia
.venv\Scripts\python.exe -m bot.principale
if errorlevel 2 (
    echo Il bot si e fermato per un motivo di sicurezza: leggi logs\bot.log.
    pause
    exit /b 2
)
echo Il bot si e fermato. Riparto tra 30 secondi (chiudi questa finestra per fermarlo davvero).
timeout /t 30 /nobreak >nul
goto riavvia
