### aggiungere una nuova istruzione
supponiamo di voler creare una nuova istruzione.
dobbiamo:
- definire la sua **codifica**
- definire **cosa faccia**
- individuare le **unità funzionali necessarie**
- individuare i **flussi di informazione** necessari
- individuare i **segnali di controllo** necessari
- calcolare il **tempo** necessario per la nuova istruzione (e se modifica il tempo totale)

#### aggiungere il jump
supponiamo che la codifica sia:
 
![[codifica jump.png|400]]

il campo da 26 bit rappresenta l'**istruzione di destinazione** del salto ed
- è un indirizzo assoluto.

poiché sono 26 bit e non 32, bisogna svolgere una serie di operazioni:
1) si guadagnano due bit facendo lo **shift logico** a sinistra (moltiplicando quindi per 4) (gli zeri sono presi con la messa a terra)]
2) i 4 bit "mancanti" vanno presi dai MSB di PC+4 (bit che indicano il "blocco" in cui ci si trova, quindi prendendoli da PC+4 ci muoviamo nello stesso blocco di 256mb) - si fa con una sorta di `or` che è in realtà un collegamento di cavetti