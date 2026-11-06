# AI che impara dagli errori sugli ingressi - 22/10/2026

Modello: gradient boosting (alberi di decisione), allenato sui trade passati
della zona di rumore di S&P 500 e Nasdaq per stimare se un ingresso finirà in
utile. Caratteristiche note al momento dell'ingresso: quanto il prezzo è fuori
dalla zona, ora, volatilità relativa, VIX e VIX rispetto alla mediana,
movimento di ieri e apertura nella direzione del trade, direzione, giorno
della settimana, risultato degli ultimi 20 trade. Ogni anno si allena solo
sugli anni precedenti e prende il 50% dei segnali con la probabilità più alta.

## Primo tentativo: troppo bello per essere vero

PF 1,84, t-stat 12, tutti gli anni in forte utile. Era un errore: una
caratteristica (larghezza della zona rispetto alla media dei segnali della
giornata) usava, senza volerlo, i segnali delle ore successive. Il modello
"vedeva il futuro". È lo stesso errore che fa sembrare perfetti molti bot
venduti online.

## Risultato corretto (fuori campione 2020-2026)

| Selezione | Trade | PF | t-stat | Ultimi 18 mesi |
|---|---|---|---|---|
| tutti i segnali | 4614 | 1,16 | 4,36 | PF 1,01 |
| **filtro VIX semplice** | 2366 | **1,22** | 4,10 | **PF 1,12** |
| AI | 2361 | 1,14 | 2,66 | PF 1,02 |
| AI + filtro VIX | 1199 | 1,20 | 2,61 | PF 1,12 |

L'AI non fa meglio della regola semplice del VIX: con questi dati impara
soprattutto il rumore. Il bot resta con il filtro VIX. Il modello è pronto
(`backtest/ai_ingressi.py`) e si può riprovare quando avremo dati nuovi
(trade veri del demo, dati delle opzioni).
