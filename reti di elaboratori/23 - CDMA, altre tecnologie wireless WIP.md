---
created: 2025-06-15T15:30
updated: 2025-06-15T15:51
---
## CDMA
Nel protocollo CDMA, un solo canale occupa l'intera ampiezza di banda, e tutte le stazioni possono inviare contemporaneamente - la "suddivisione" della banda avviene via **codici**.

- ogni stazione ha un codice
- ogni codice, se moltiplicato per un altro, dà 0 (sequenze ortogonali)
- ogni codice, se moltiplicato per se stesso, dà il numero di stazioni
- ogni stazione che vuole trasmettere moltiplica i propri dati per il proprio codice e trasmette
- ogni stazione che vuole ricevere moltiplica i dati ricevuti per il codice del mittente e divide per il numero delle stazioni
- la sequenza sul canale è la somma delle sequenze inviate dalle stazioni

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

### generazione di sequenze
Per generare sequenze di chip si usa la tabella di Walsh, una matrice quadrata in cui ogni riga è una sequenza di chip.

![[walsh-creazione.png|center|400]]

## bluetooth
Una LAN bluetooth è una piccola rete ad hoc. Si forma spontaneamente, senza l'aiuto di alcuna base station (AP). La banda è di 2,4GHz, ed è divisa in 79 canali da 1MHz ciascuno.

>[!info] stack protocollare
>Bluetooth definisce uno stack protocollare diverso da TCP/IP.
>
>![[stack-bt.png|center|350]]

### piconet e scatternet
Bluetooth definisce due tipi di reti: 

La rete **piconet** è composta al massimo da 8 dispositivi (1 stazione primaria e 7 secondarie che si sintonizzano con essa)
- possono esserci altre stazioni secondarie ma in stato di parked (sincronizzate con la primaria ma che non possono prendere parte alla comunicazione finchè una stazione attiva non viene spostata nello stato di parked o lascia il sistema)

La rete **scatternet** è una combinazione di Piconet in cui una secondaria fa da primaria per un'altra Piconet, passando messaggi da una rete all'altra.

![[scatternet.png|center|500]]

### protocollo MAC
Bluetooth usa **TDMA** con slot temporali da 625μs.

Stazioni primaria e secondarie inviano e ricevono dati, ma non contemporaneamente (half duplex): la primaria usa solo gli slot pari, mentre la secondaria quelli dispari.