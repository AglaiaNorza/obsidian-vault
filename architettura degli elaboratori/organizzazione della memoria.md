---
{}
---
[fonti varie ma molto appunti exyss]
- La memoria può contenere sia istruzioni che dati.
- La memoria delle architetture MIPS è **indicizzata al byte** (ogni indice punta a un byte).
- - Ad ogni byte è associato un **indirizzo**, rappresentato da 8 cifre esadecimali.
- Ogni **word** è composta da **4 byte**, ovvero 32 bit, quindi le parole sono separate da 4 byte (se la prima è all'indirizzo 0x00000000, la seconda sarà a 0x00000004).
- Quindi, il k-esimo byte sarà all'indirizzo(k-1), mentre la j-esima word a 4 * (j-1)
 
 Ci sono 2^30 parole di memoria (32 registri, ma 2^32/4 perché ogni word sono 4 byte), ovvero 4 Giga-byte.

La memoria può essere immaginata come una tabella da 4 colonne (un byte per colonna) e 2^30 righe (una word per riga).

![[mips memory.png| 450]]

Nel linguaggio MIPS, per leggere il contenuto di una word si usa la notazione `offset($indirizzo)`, dove `$indirizzo` è un registro contenente un valore interpretato come indirizzo di memoria da cui prendere la word, e `offset` il numero di byte successivi all'indirizzo.

### componenti
![[mips memory components.png | 350]]

La memoria è divisa in:
- **Stack** - operazioni legate alle funzioni(/procedure), salva le chiamate ricorsive e le variabili locali. Non ha dimensione fissa. Al suo interno opera il registro `$sp`, Stack Pointer.
- **Heap o Dynamic Data** - contiene i dati dinamici immagazzinati durante l'esecuzione.
- **Static Data** - contiene i dati statici definiti all'avvio del programma (etichette sotto `.data`). Il registro  `$gp`, Global Pointer, viene usato dall'assemblatore per gestire gli indicizzamenti all'interno di questa zona.
- **Program Instructions** - contiene le istruzioni del programma (etichetta `.text`). Al suo interno opera il *Program Counter*, il registro che memorizza la posizione in memoria dell'istruzione successiva da eseguire.
- **Kernel-reserved memory** - spazio di memoria inutilizzabile riservato al Kernel del sistema operativo.

