# Regole scritte prima del test - 22/10/2026: zona di rumore

Francesco mi ha lasciato libero di scegliere strumento e tipo di strategia, purché
intraday. Ho scelto la strategia di momentum intraday pubblicata da Zarattini,
Aziz e Barbon ("Beat the Market: An Effective Intraday Momentum Strategy for
S&P500 ETF (SPY)", Swiss Finance Institute, paper 24-97, 2024).

Perché questa: è pubblicata, ha regole semplici e senza parametri da inseguire,
e l'effetto che sfrutta ha una spiegazione. Nel pomeriggio americano chi
deve coprire posizioni (market maker in opzioni, fondi a leva) compra quando il
mercato sale e vende quando scende, e questo allunga i movimenti già iniziati.

## Regole

- Apertura di riferimento: 03:00 NY (Londra) oppure 09:30 NY (Wall Street).
- Ogni 30 minuti si confronta il prezzo con l'apertura. La "zona di rumore" a
  quell'ora è apertura × (1 ± k × media di quanto il prezzo si era allontanato
  dall'apertura alla stessa ora nelle 14 giornate precedenti), con k = 1 o 1,5.
- Sopra la zona si compra, sotto si vende. Ultimo controllo 15:30 NY, tutto
  chiuso alle 16:00 NY. Al massimo 3 trade al giorno, uno alla volta.
- Stop a 0,5 o 1 volta la larghezza della zona. Due uscite:
  "rr" = take profit a 2,5 volte lo stop (regola di Francesco);
  "segui" = stop che segue il prezzo a quella distanza, come nello studio.
- Rischio 1% a trade, costi veri, stesso esame di sempre: walk-forward,
  cassetto chiuso dal 01/04/2025, PF >= 1,20, t-stat >= 2,5, >= 150 trade,
  >= 60% anni in utile, >= metà griglia con PF > 1. 16 combinazioni.

Strumenti: oro e i 4 cambi che abbiamo; poi S&P 500 e Nasdaq 100 (gli indici
dove lo studio è stato fatto) appena arriva l'esportazione.
