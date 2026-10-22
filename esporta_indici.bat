@echo off
title Eatrading - esporta_indici
rem Doppio clic per esportare lo storico degli indici USA (S&P 500 e Nasdaq 100).
cd /d "%~dp0"
echo Eatrading - esporta_indici. Cartella: %CD%
call prepara_python.bat || goto fine
.venv\Scripts\python.exe fase1_esporta_forex.py "US500|SP500|SPX500|US500.cash" "NAS100|US100|USTEC|NDX100|NAS100.cash"
:fine
echo.
pause
