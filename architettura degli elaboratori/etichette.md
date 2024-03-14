---
sticker: lucide//form-input
---
[da appunti exyss]

le etichette vengono poste accanto ad istruzioni e dati statici, e svolgono la funzione di "**segnalibro**" per l'assemblatore, che, in fase di compilazione, le andrà a **tradurre con l'indirizzo di memoria corrispondente** all'istruzione/dato statico associato.

esempio:
```
.data
vettore: 10, 2, 0x12
stringa: .asciiz "Sono una stringa"
vettore_float: .float 10.2, 3.33333

.text

main:
la $s0, vettore //carico in $s0 l’indirizzo del dato "vettore"
lw $s1, 0($s0)
lw $s2, 4($s0)
lw $s3, 8($s0)
add $t0, $s1, $s2 // $t0 = $s1 + $s2 ossia $t0 = 10 + 2
sub $t0, $t0, $s3 // $t0 = $t0 + $s3 ossia $t0 = 12 - 18
```
Analizziamo pezzo per pezzo il codice:
1. Vengono definiti dei dati statici sotto la direttiva `.data`. In particolare, viene
definito un vettore di interi (indicabili sia in decimale sia in esadecimale), una stringa
di caratteri ed un vettore di valori float.
2. Viene utilizzata la direttiva `.text`, indicando l’inizio delle istruzioni del programma
3. Viene usato il comando `Load Address`, che carica in `$s0` l’indirizzo di memoria
associato all’etichetta "vettore"
4. Vengono caricati tutti i valori del vettore utilizzando il comando `Load Word`. Da
tali istruzioni, possiamo notare come un vettore di valori (indipendentemente dal
tipo) corrisponda esattamente ad un insieme di word messe una di fila all’altra,
dunque distanti 4 byte ciascuna in memoria. Lo stesso discorso si applica anche per
le stringhe, poiché esse non sono nient’altro che un vettore di caratteri.
5. Vengono svolte operazioni numeriche tra i registri in cui sono stati caricati i valori
del vettore

