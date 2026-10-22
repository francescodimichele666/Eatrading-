# Strategie intraday pubblicate - regole scritte prima del test, 22/10/2026

Francesco ha chiesto se esistono altre strategie "certificate". Una
certificazione vera non esiste: il massimo è una strategia pubblicata, con i
dati e le regole controllati da altri ricercatori. Ne ho scelte quattro, tutte
intraday, e le provo con le stesse regole di sempre: costi veri, walk-forward,
cassetto chiuso dal 01/04/2025 (già aperto solo per il Nasdaq con la zona di
rumore), soglie PF >= 1,20, t-stat >= 2,5, >= 150 trade, >= 60% anni in utile,
>= metà griglia con PF > 1. Rischio 1% a trade.

## Indici (S&P 500, Nasdaq 100)

1. **Opening range breakout**: Zarattini e Aziz (2023), "Can Day Trading
   Really Be Profitable?". La prima candela di 5 minuti dopo le 09:30 NY dà
   la direzione. Si entra alle 09:35, con lo stop all'estremo opposto della
   candela. Take profit a 2,5 volte il rischio (regola di Francesco) oppure a
   10 volte (come nello studio); altrimenti si esce alle 16:00.
2. **Momentum dell'ultima mezz'ora**: Gao, Han, Li e Zhou (2018), Journal of
   Financial Economics. Se dalla chiusura di ieri alle 10:00 il mercato è
   salito, si compra alle 15:30 e si vende alle 16:00 (al contrario se è
   sceso). Variante: solo se anche la mezz'ora 15:00-15:30 va nella stessa
   direzione. Lo stop di sicurezza è a 0,5 o 1 ATR giornaliero.

## Forex (EURUSD, USDCHF, AUDUSD, USDCAD)

3. **Ore locali**: Breedon e Ranaldo (Banca Nazionale Svizzera, 2011). Una
   valuta tende a indebolirsi nelle ore del suo mercato. Finestre: europea
   02:00-08:00 NY (euro e franco deboli), americana 10:00-16:00 NY (dollaro
   debole), asiatica 19:00-02:00 NY (dollaro australiano debole).
4. **Fixing di Londra**: Krohn, Mueller e Whelan (Journal of Finance). Il
   dollaro si rafforza nelle ore prima del fixing delle 16:00 di Londra
   (11:00 NY) e si indebolisce dopo. "prima" = dollaro long 08:00-11:00 NY,
   "dopo" = dollaro short 11:00-14:00 NY.

Per 3 e 4 lo stop di sicurezza è a 0,5 o 1 ATR giornaliero e si esce a fine
finestra.

# Risultati (22/10/2026)

Profit factor fuori campione (walk-forward 2020-2025, costi veri):

| Strategia | S&P 500 | Nasdaq 100 | EURUSD | USDCHF | AUDUSD | USDCAD |
|---|---|---|---|---|---|---|
| Opening range breakout (Zarattini-Aziz) | 0,93 | **1,12** (t 1,3) | | | | |
| Ultima mezz'ora (Gao e altri) | 0,88 | 0,83 | | | | |
| Ore locali (Breedon-Ranaldo) | | | 0,98 | 0,82 | 0,84 | non applicabile |
| Fixing di Londra (Krohn e altri) | | | 0,87 | 0,68 | 0,81 | 0,83 |

Nessuna supera l'esame di sviluppo, quindi il cassetto resta chiuso. Il
breakout sul Nasdaq è positivo in entrambe le varianti (target 2,5 e 10), ma
con t-stat 1,3 può ancora essere fortuna. È coerente con una replica
indipendente ("gross reproduced, net zero": prima dei costi funziona, dopo i
costi si va in pari). Gli effetti sul forex sono di pochi centesimi di punto
percentuale al giorno: lo spread di circa 1 pip se li mangia tutti.
