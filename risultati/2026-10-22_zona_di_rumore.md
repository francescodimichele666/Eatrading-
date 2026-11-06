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

# Risultati (22/10/2026)

Costi: spread di ogni barra del broker (S&P 500 circa 0,4 punti, Nasdaq circa
1,2 punti all'apertura di Wall Street), più mezzo spread di slittamento.

| Strumento | Trade | PF fuori campione | t-stat | Anni in utile | Griglia PF>1 | Esame di sviluppo |
|---|---|---|---|---|---|---|
| Oro | 1272 | 0,88 | -1,9 | 1/6 | 0% | no |
| EURUSD / USDCHF / AUDUSD / USDCAD | 1215-1563 | 0,80-0,93 | negativi | 0-2/6 | 0% | no |
| S&P 500 | 1517 | **1,22** | 2,98 | 6/6 | 38% | no (solo la griglia) |
| Nasdaq 100 | 1135 | **1,27** | 3,22 | 4/5 | 50% | **sì** |

Sugli indici tutte le 8 combinazioni con apertura alle 09:30 NY hanno PF > 1
nello sviluppo, e tutte quelle con apertura alle 03:00 NY sono sotto 1: il
risultato sta proprio dove lo studio dice che deve stare. Con costi doppi il
PF scende di 0,01-0,04; long e short guadagnano in modo simile; entrando 5
minuti in ritardo il PF scende di circa 0,07 ma resta sopra 1.

## Cassetto degli ultimi 18 mesi (aperto una volta, 01/04/2025 - 21/10/2026)

Nasdaq 100, parametri scelti dalla regola (k 1, stop 1, take profit 2,5):
**483 trade, PF 0,98, t-stat -0,19**. Non supera l'esame finale.

Solo a titolo informativo (non conta per la decisione): le 8 combinazioni con
apertura 09:30 nel cassetto vanno da 0,94 a 1,22 sul Nasdaq e da 0,86 a 1,14
sull'S&P 500, cioè in media circa a zero. L'effetto c'era dal 2017 al 2025 e si
è indebolito negli ultimi 18 mesi, proprio dopo la pubblicazione dello studio
(2024): è quello che succede di solito quando una strategia diventa famosa.
