@echo off
rem Usato dagli altri file .bat: controlla la cartella e prepara Python (.venv) con le librerie.
rem Esce con errore (exit /b 1) se qualcosa non va, dopo aver spiegato cosa fare.

echo %~dp0 | find /i "\AppData\Local\Temp\" >nul
if not errorlevel 1 (
    echo.
    echo ERRORE: stai aprendo il file da dentro lo ZIP.
    echo Prima estrai lo ZIP: tasto destro sul file .zip, "Estrai tutto", poi apri la cartella estratta.
    exit /b 1
)

if exist .venv\Scripts\python.exe goto librerie
echo Prima installazione: preparo Python nella cartella .venv ...
for %%V in (3.14 3.13 3.12) do (
    if not exist .venv\Scripts\python.exe py -%%V -m venv .venv >nul 2>&1
)
if not exist .venv\Scripts\python.exe py -3 -m venv .venv >nul 2>&1
if not exist .venv\Scripts\python.exe python -m venv .venv >nul 2>&1
if not exist .venv\Scripts\python.exe (
    echo.
    echo ERRORE: Python non trovato.
    echo Installa Python da https://www.python.org/downloads/windows/
    echo e nella prima schermata spunta "Add python.exe to PATH".
    exit /b 1
)

:librerie
echo Controllo le librerie (la prima volta puo' richiedere qualche minuto) ...
.venv\Scripts\python.exe -m pip install --disable-pip-version-check -q -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERRORE: installazione delle librerie fallita. Controlla la connessione a internet
    echo e fai una foto di questa finestra per Claude.
    exit /b 1
)
if not exist config.toml copy config.example.toml config.toml >nul
echo Python pronto.
exit /b 0
