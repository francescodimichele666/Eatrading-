# Eatrading

Bot di trading intraday per XAUUSD (oro) su MetaTrader 5, scritto in Python.
Il piano completo è nel documento "Bot trading Gold e Forex: analisi e roadmap".

Stato attuale: **Fase 0**, controllo che server, MT5 e broker funzionino insieme.
Nessuna strategia è ancora attiva.

## Fase 0: come lanciare il controllo sul server

Si fa una volta sola, sul server Windows 11.

1. **Installa MT5 di FP Markets** e accedi al conto **demo**.
   In MT5 premi il pulsante **Algo Trading** in alto: deve diventare verde.
   Poi vai su *Strumenti → Opzioni → Expert Advisor* e spunta
   *Consenti il trading algoritmico*.
2. **Installa Python 3.13** da [python.org](https://www.python.org/downloads/windows/).
   Nella prima schermata spunta **"Add python.exe to PATH"**, poi *Install Now*.
3. **Scarica questo progetto**: sulla pagina GitHub premi il pulsante verde
   *Code → Download ZIP* ed estrai la cartella, ad esempio in `C:\Eatrading`.
4. **Lascia MT5 aperto** e fai doppio clic su `avvia_controllo.bat`.
   La prima volta impiega un paio di minuti perché installa le librerie.
5. Il controllo dura circa un minuto e mezzo. Alla fine trovi un rapporto
   nella cartella `logs`. **Copia il suo contenuto e mandalo a Claude.**

Il programma apre e chiude subito 0,01 lotti per provare l'esecuzione,
**solo se il conto è demo**. Su un conto reale quel test non parte mai.

## Impostazioni (facoltative)

Al primo avvio viene creato `config.toml`, copia di `config.example.toml`.
Si apre con il Blocco note. Serve solo se:

- MT5 non è già collegato al conto: inserisci login, password e server;
- vuoi ricevere il rapporto su Telegram: inserisci token e chat_id.

`config.toml` contiene le tue password e **non viene mai caricato su GitHub**.

## File

| File | A cosa serve |
| --- | --- |
| `avvia_controllo.bat` | Prepara Python e lancia il controllo con un doppio clic |
| `fase0_controllo.py` | Il programma di controllo |
| `config.example.toml` | Modello delle impostazioni |
| `requirements.txt` | Librerie Python necessarie |
