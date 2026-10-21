@echo off
rem Doppio clic per esportare lo storico per il backtest (Fase 1).
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
    echo Prima lancia avvia_controllo.bat almeno una volta.
    pause
    exit /b 1
)

.venv\Scripts\python.exe -m pip install --quiet -r requirements.txt
.venv\Scripts\python.exe fase1_esporta_dati.py
pause
