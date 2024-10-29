molte istruzioni in realtà sono *pseudoistruzioni*: hanno un significato intuitivo, ma non un corrispondente 1 a 1 con le istruzioni che la macchina esegue effettivamente.

vantaggi [[fonte: ppt università di milano](https://pedersini.di.unimi.it/AER/AE2_14_L3.pdf)]:
- parziale standardizzazione del linguaggio: le pseudoistruzioni vengono tradotte in modi differenti per architetture differenti
- rappresentazione più compatta e intuitiva

alcuni esempi di comandi "fittizi" sono:
- il `move` - è in realtà un'addizione senza segno tra il registro 16 e il registro 0 (che contiene sempre 0)
 
	`addu $t0, $zero, $s0` == `move $t0, $s0`
	o anche
	`add $t0, $zero, $s0`
	o anche
	`or $t0, $zero, $s0`
 
- il `ble` (branch on less than or equal) - è in realtà un `slt` (set if less than), scritto sul registro `$1` (`$at`). viene poi usato `beq` con tutti zero, per decidere se saltare all'indirizzo di memoria del check che si troverebbe nel `ble`![[ble.png]]

