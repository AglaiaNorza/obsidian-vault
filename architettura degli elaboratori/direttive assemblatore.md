---
sticker: lucide//hammer
---
Le direttive non corrispondono in modo diretto ad una particolare istruzione in linguaggio macchina, bensì vengono interpretate esclusivamente dall’assemblatore, il quale si occuperà poi di tradurre il tutto in istruzioni più complesse.

- danno etichette ai vettori - come se fossero "tipi"
- descrivono come mettere queste "variabili" nella *RAM* (ma sta a noi tenere traccia di quanto spostarci)
 
le direttive principali sono:
- **`.data`** -> definizione dei dati statici
- **`.text`** -> definizione del programma
- **`.asciiz`** -> stringa terminata da \0
- **`.byte`** -> sequenza di byte
- **`.double`** -> sequenza di double
- **`.float`** -> sequenza di float
- **`.half`** -> sequenza di half words
- **`.word`** -> sequenza di words

per le etichette vere e proprie, vedi [[etichette]]