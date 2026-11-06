# Apprendimento dagli errori: quattro metodi provati - 22/10/2026

Francesco ha chiesto un metodo che impari dagli errori e faccia tornare la
zona di rumore profittevole. Ho provato quattro metodi sugli anni passati,
ognuno usando solo le informazioni disponibili fino a quel momento.
Variante di partenza: apertura 09:30 NY, k 1, stop 1, take profit 2,5.

Nota onesta: gli ultimi 18 mesi li avevo già visti (cassetto aperto per il
Nasdaq), quindi il confronto su quel periodo non è "pulito" al 100%.

| Metodo | S&P 2020-03/2025 | S&P ultimi 18 mesi | Nasdaq 2020-03/2025 | Nasdaq ultimi 18 mesi |
|---|---|---|---|---|
| fisso (nessun apprendimento) | PF 1,21 | 1,04 | 1,24 | 0,98 |
| ricalibra ogni mese (sceglie la variante migliore degli ultimi 36 mesi) | 1,23 | 0,99 | 1,25 | 1,08 |
| pausa se gli ultimi 30 trade sono in perdita | 1,15 | 0,96 | 1,22 | 0,97 |
| pausa se gli ultimi 60 trade sono in perdita | 1,22 | 1,07 | 1,17 | 1,01 |
| scarta i gruppi in perdita (fascia oraria, lato, volatilità) | 1,20 | 1,05 | 1,23 | 0,95 |

## Cosa vuol dire

- Nessun metodo fa tornare la strategia chiaramente profittevole negli ultimi
  18 mesi: le differenze (da 0,95 a 1,08) sono nel margine della fortuna.
- "Scartare i gruppi che hanno perso" è il metodo più intuitivo ma il più
  pericoloso: impara dal rumore e a volte toglie proprio i trade buoni.
- Ricalibrare e mettere in pausa non aumentano molto il guadagno, ma servono a
  **seguire il mercato** e a **fermarsi** se la strategia smette di funzionare.

## Cosa fa il bot (ogni sabato)

1. Ricalibra: tra k 1 / 1,5 e stop 0,5 / 1 sceglie la variante con il
   risultato più solido negli ultimi 36 mesi.
2. Pausa: se gli ultimi 60 trade (anche quelli non fatti) sono in perdita,
   l'indice va in pausa finché non torna positivo.
3. Errori: rapporto con le perdite raggruppate per fascia oraria, lato e
   volatilità (solo informativo, non cambia le regole), e confronto tra i
   trade veri del bot e quelli del backtest della settimana, per trovare gli
   errori di esecuzione (trade mancati, slittamenti).
