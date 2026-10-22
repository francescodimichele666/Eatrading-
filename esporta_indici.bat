@echo off
rem Doppio clic per esportare lo storico degli indici USA (S&P 500 e Nasdaq 100).
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
    echo Prima lancia avvia_controllo.bat almeno una volta.
    pause
    exit /b 1
)
.venv\Scripts\python.exe -m pip install --quiet -r requirements.txt
.venv\Scripts\python.exe fase1_esporta_forex.py "US500|SP500|SPX500|US500.cash" "NAS100|US100|USTEC|NDX100|NAS100.cash"
pause
