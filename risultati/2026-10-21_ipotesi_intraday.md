# Tre idee intraday su XAUUSD, regole fissate PRIMA del test

Scritte il 21/10/2026, dopo il fallimento della strategia MVP e prima di
guardare qualsiasi risultato di queste tre idee. Le regole non si cambiano
dopo aver visto i numeri: si possono solo scegliere, nel walk-forward, i
valori della piccola griglia indicata, usando solo gli anni passati.

Orari in ora italiana salvo dove indicato. Costi come nel test MVP
(spread minimo e slittamento in proporzione al prezzo, 0,07 $/oncia di commissione).

## Idea A: rottura del range notturno all'apertura di Londra

- Range: massimo e minimo delle barre dalle 01:00 alle 08:00.
- Si salta il giorno se l'altezza del range supera l'ATR giornaliero (14 giorni, fino a ieri).
- Dalle 09:00 alle 12:00: long alla chiusura M5 sopra il massimo, short sotto il minimo. Solo la prima rottura, 1 trade al giorno.
- Stop: lato opposto del range (griglia: lato opposto | meta' del range).
- Target: 1 volta l'altezza del range dall'entrata (griglia: 1 | 1,5 | 2).
- Uscita comunque alle 21:00.

## Idea B: momentum all'apertura di New York

- Alle 09:45 di New York si misura il movimento dalle 03:00 di New York (apertura di Londra).
- Se il movimento supera 0,5 volte l'ATR giornaliero (griglia: 0,3 | 0,5 | 0,7), si entra nella stessa direzione.
- Stop: 0,5 volte l'ATR giornaliero (griglia: 0,3 | 0,5 | 0,7). Nessun target.
- Uscita alle 13:30 di New York (chiusura del COMEX), 1 trade al giorno.

## Idea C: rottura su H1 nella direzione del trend giornaliero

- Trend: chiusura di ieri sopra la media a 50 giorni = solo long, sotto = solo short.
- Entrata alla chiusura di una barra H1 tra le 09:00 e le 18:00 che supera il massimo (long) o il minimo (short) delle 20 barre H1 precedenti (griglia: 10 | 20 | 40).
- Stop: 2 ATR H1 (griglia: 1,5 | 2 | 3). Target: 3 ATR H1. Uscita alle 21:00. Massimo 2 trade al giorno.

## Soglia per passare alla demo (Fase 2)

Nel walk-forward (3 anni di allenamento, 1 di prova, solo anni di prova contati):
- almeno 100 trade;
- profit factor almeno 1,15 con tutti i costi;
- anni di prova in utile almeno 6 su 10 (o il 60%);
- drawdown del Monte Carlo al 95% sotto il 25% con rischio 0,75% a trade.

Con tre idee provate insieme, una puo' sembrare buona per caso: se ne passa
solo una e di poco, la consideriamo "da confermare" in demo, non promossa.
