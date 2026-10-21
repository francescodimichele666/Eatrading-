@echo off
rem Doppio clic per lanciare il controllo della Fase 0.
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
    echo Prima installazione: preparo Python...
    py -3.13 -m venv .venv || python -m venv .venv
)
if not exist .venv\Scripts\python.exe (
    echo ERRORE: Python non trovato. Installa Python 3.13 da python.org spuntando "Add python.exe to PATH".
    pause
    exit /b 1
)

.venv\Scripts\python.exe -m pip install --quiet --upgrade pip
.venv\Scripts\python.exe -m pip install --quiet -r requirements.txt
if not exist config.toml copy config.example.toml config.toml >nul

.venv\Scripts\python.exe fase0_controllo.py
pause
