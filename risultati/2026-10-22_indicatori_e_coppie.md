# Regole scritte prima dei test - 22/10/2026

Francesco ha chiesto di provare tre strategie classiche a indicatori, di
lavorare sulle coppie che si muovono al contrario (EURUSD/USDCHF e
AUDUSD/USDCAD), con **rischio 1% a trade** e **take profit a 2,5 volte il
rischio**. Queste regole sono fissate prima di vedere qualsiasi risultato.

## Regole comuni

- Sempre intraday: entrate tra le 18:30 e le 16:00 di New York, tutto chiuso
  entro le 16:00 NY. Al massimo 3 trade al giorno, uno alla volta.
- Segnale letto a barra chiusa (M15 o H1), entrata all'apertura della barra
  M5 successiva, al prezzo ask per i long.
- Stop = 1, 1,5 o 2 volte l'ATR(14) del timeframe; take profit = 2,5 volte lo
  stop; altrimenti uscita dopo 4 ore o a fine giornata.
- Costi: spread vero misurato, slittamento, commissione FP Markets.
- Stesso esame di prima: walk-forward (3 anni per scegliere, 1 anno di prova),
  cassetto chiuso dal 01/04/2025, soglie: almeno 150 trade, profit factor
  >= 1,20, t-stat >= 2,5, almeno il 60% degli anni in utile, almeno metà
  della griglia con profit factor > 1.

## Le tre strategie

1. **trend_ema**: long solo sopra la EMA200, short solo sotto. Entrata quando
   la EMA veloce incrocia la lenta (9/21 oppure 20/50). 24 combinazioni.
2. **bollinger**: ritorno alla media. Il prezzo ha toccato la banda di
   Bollinger (20; 2 oppure 2,5) nelle ultime 3 barre e l'oscillatore esce
   dall'ipervenduto o dall'ipercomprato (Stocastico 14,3 su 20/80, oppure
   RSI 14 su 30/70). 48 combinazioni.
3. **ichimoku** (9/26/52): incrocio Tenkan/Kijun con il prezzo dalla parte
   giusta della nuvola, oppure uscita del prezzo dalla nuvola con Tenkan
   dalla parte giusta di Kijun. 24 combinazioni.

## Il sistema "che apprende"

Ogni anno guarda i 3 anni precedenti, sceglie tra **tutte** le combinazioni
di tutte le famiglie quella che è andata meglio e la usa l'anno dopo. È lo
stesso esame del walk-forward, quindi il risultato che esce è quello che
avrebbe ottenuto davvero, senza conoscere il futuro.

## Coppie opposte (quando arrivano i dati forex)

EURUSD x USDCHF = EURCHF e AUDUSD x USDCAD = AUDCAD. Quindi:

- aprire le due coppie in direzioni opposte equivale a raddoppiare la stessa
  scommessa sul dollaro, pagando due volte i costi: non lo proviamo come
  strategia a sé;
- **divergenza**: quando le due coppie smettono per un po' di muoversi al
  contrario (il cross sintetico si allontana dalla sua media), si scommette
  che tornino normali; si paga il costo di entrambe le coppie;
- **conferma**: si entra su una coppia solo se l'altra si è mossa al
  contrario della stessa misura.
