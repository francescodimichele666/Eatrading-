# Eatrading

Bot di trading intraday su MetaTrader 5, scritto in Python: oro (XAUUSD) e indici USA
(S&P 500 e Nasdaq 100).
Il piano completo è nel documento "Bot trading Gold e Forex: analisi e roadmap".

Stato attuale: **Fase 2 di prova, solo conto demo**. Il bot opera due strategie
come prova sui mesi futuri (nessuna delle due ha ancora superato tutti gli
esami per i soldi veri):

- **oro, idea B**: momentum all'apertura di New York;
- **indici USA, zona di rumore**: momentum intraday dopo l'apertura di Wall
  Street, dallo studio dello Swiss Finance Institute (2024). Dal 2017 al 2025
  ha guadagnato (profit factor 1,22-1,27), negli ultimi 18 mesi è in pari.

Ogni sabato il bot fa l'**apprendimento**: rifà i conti sugli ultimi 4 anni,
ricalibra la zona di rumore, mette in pausa un indice se gli ultimi 60 trade
sono in perdita e confronta i trade veri con quelli attesi. I risultati dei
test sono nella cartella `risultati`.

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

## Fase 1: esportare lo storico per il backtest

Si fa sul server, con MT5 aperto. Serve a dare a Claude i prezzi storici del
tuo broker, con lo spread vero di ogni momento.

1. In MT5 vai su *Strumenti → Opzioni → Grafici* e alla voce
   **Barre massime nel grafico** scegli **Unlimited**. Premi OK,
   poi chiudi e riapri MT5.
2. Scarica di nuovo il progetto da GitHub (*Code → Download ZIP*) e
   sostituisci i file nella cartella di prima. Non cancellare la cartella
   `.venv` né il file `config.toml`.
3. Fai doppio clic su `esporta_dati.bat`. Può impiegare 10-20 minuti la prima
   volta, perché MT5 scarica lo storico dal broker.
4. Alla fine trovi nella cartella `logs` un file `dati_backtest_<data>.zip`.
   **Mandalo a Claude.**

### Storico dei cambi (forex)

Per cercare strategie anche sul forex: con MT5 aperto fai doppio clic su
`esporta_forex.bat`. Crea nella cartella `logs` un file `forex_<CAMBIO>.zip`
per ogni cambio (circa 10 MB l'uno, 20-40 minuti in tutto).
**Mandali tutti a Claude.**

## Fase 2: far girare il bot sul conto demo

Il bot gira giorno e notte. Ogni giorno lavorativo (orari italiani, che di
solito sono quelli di New York + 6 ore):

- **oro**: alle 15:45 decide se aprire un trade e lo chiude entro le 19:30;
- **S&P 500 e Nasdaq 100**: dalle 16:00 alle 21:30, ogni mezz'ora, entra se il
  prezzo è uscito dalla zona di rumore (al massimo 3 trade al giorno per
  indice, rischio 1% ciascuno, stop e take profit sul server del broker), e
  chiude tutto alle 22:00.

**Funziona solo su un conto demo**: se MT5 è collegato a un conto reale si
ferma da solo. Il sabato mattina fa l'apprendimento e ti manda il rapporto su
Telegram (lo trovi anche in `logs/apprendimento_<data>.md`).

### 1. Avvisi su Telegram (consigliato)

1. In Telegram cerca **@BotFather**, scrivi `/newbot`, scegli un nome e un
   nome utente che finisca con `bot`. BotFather ti risponde con un **token**.
2. Cerca il tuo nuovo bot in Telegram e scrivigli un messaggio qualsiasi.
3. Nel browser apri `https://api.telegram.org/bot<TOKEN>/getUpdates`
   (al posto di `<TOKEN>` metti il token). Cerca `"chat":{"id":` e copia
   il numero che segue: è il tuo **chat_id**.
4. Apri `config.toml` con il Blocco note e scrivi token e chat_id nella
   sezione `[telegram]`. Salva.

### 2. Preparare il server

1. **Aggiornamenti di Windows**: *Impostazioni → Windows Update → Opzioni
   avanzate → Orario di attività*: scegli manuale, dalle 8:00 alle 23:00.
   Così Windows non si riavvia mentre il bot lavora.
2. **Sospensione**: *Impostazioni → Sistema → Alimentazione* e metti
   **Mai** alla voce sospensione.
3. **MT5**: quando accedi al conto demo spunta *Salva password*, così dopo un
   riavvio si ricollega da solo.
4. **Avvio automatico**: premi i tasti *Windows + R*, scrivi `shell:startup`
   e premi Invio. Nella cartella che si apre trascina, tenendo premuto *Alt*,
   il file `avvia_bot.bat` e l'icona di MT5: si creano dei collegamenti.
   Così dopo un riavvio partono da soli.

### 3. Avviare il bot

1. Scarica il progetto aggiornato (*Code → Download ZIP*) e sostituisci i
   file come per la Fase 1 (senza cancellare `.venv` e `config.toml`).
2. Con MT5 aperto e *Algo Trading* verde, fai doppio clic su `avvia_bot.bat`.
3. Su Telegram arriva "AVVIO: bot avviato su conto demo...". Poi arriva un
   "sono vivo" ogni ora, e un messaggio per ogni decisione e ogni ordine.
4. Lascia aperta la finestra nera: se la chiudi, il bot si ferma.

### Se il bot si blocca da solo

Se il conto demo perde più del 10% dal suo massimo, o più del 3% in un
giorno, il bot smette di aprire trade e te lo scrive su Telegram. Prima parlane con Claude. Per sbloccarlo,
crea nella cartella `logs` un file vuoto chiamato `SBLOCCA.txt`: il bot lo
legge, riparte e lo cancella.

Tutto quello che il bot fa è scritto in `logs/bot.log` (testo) e
`logs/bot.sqlite` (per le analisi di Claude).

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
| `esporta_dati.bat` | Lancia l'esportazione dello storico con un doppio clic |
| `fase1_esporta_dati.py` | Esporta prezzi MT5 e dati FRED in un file ZIP |
| `esporta_forex.bat`, `fase1_esporta_forex.py` | Esportano lo storico M5 dei cambi principali |
| `esporta_indici.bat` | Esporta lo storico M5 di S&P 500 e Nasdaq 100 |
| `avvia_bot.bat` | Avvia il bot con un doppio clic e lo fa ripartire se si ferma |
| `bot/` | Il bot: strategia, rischio, collegamento a MT5, registro |
| `backtest/` | Il motore di backtest (lo usa Claude) |
| `risultati/` | Regole delle idee e risultati dei test |
| `tests/` | Prove automatiche del bot con un finto MT5 |
| `config.example.toml` | Modello delle impostazioni |
| `requirements.txt` | Librerie Python necessarie |
