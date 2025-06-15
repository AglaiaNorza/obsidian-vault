---
created: 2025-06-15T15:30
updated: 2025-06-15T15:40
---
## CDMA
Nel protocollo CDMA, un solo canale occupa l'intera ampiezza di banda, e tutte le stazioni possono inviare contemporaneamente - la "suddivisione" della banda avviene via **codici**.

- ogni stazione ha un codice
- ogni codice, se moltiplicato per un altro, dà 0 (sequenze ortogonali)
- ogni codice, se moltiplicato per se stesso, dà il numero di stazioni
- ogni stazione che vuole trasmettere moltiplica i propri dati per il proprio codice e trasmette
- ogni stazione che vuole ricevere moltiplica i dati ricevuti per il codice del mittente e divide per il numero delle stazioni

>[!tip] sequenze ortogonali
>
>Ogni sequenza è composta da $N$ elementi (con $N=$ numero di stazioni, che deve essere una potenza di 2).
>
>- moltiplicando una sequenza per un numero, ogni elemento della sequenza viene moltiplicato per tale numero
>- moltiplicando due sequenze uguali e sommando il risultato, si ottiene $N$
>```
>[+1, +1, +1, +1] x [+1, +1, +1, +1] = 1 + 1 + 1 + 1 = 4
>```
>- moltiplicando due sequenze diverse e sommando i risultati, si ottiene 0
>```
>[+1, +1, -1, -1] x [+1, +1, +1, +1] = 1 + 1 - 1 - 1 = 0
>```
>- per sommare due sequenze, si sommano gli elementi corrispondenti
>```
>[+1, +1, -1, -1] + [+1, +1, +1, +1] = [2 + 2 + 0 + 0]
>```
