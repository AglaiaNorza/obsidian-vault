 in C, il massimo di un vettore si trova così:
 
```C
int vettore[6] = {11, 35, 2, 17, 29, 95}
int N = 6;

int max = vettore[0];

for(i = 1; i<N; i++){
	if (vettore[i]>max):
	max = vettore[i];
}
```

in assembly, invece:
```
.data

vettore: .word 11, 35, 2, 17, 29, 95
N: .word 6

.text

lw $t0, vettore($zero)   #max -> t0 (offset 0)
lw $t1, N    #n -> t1
li $t2, 1    #i = 1

for: 
bge $t2, $t1, endFor

sll $t3, $t2, 2
lw $t4, vettore($t3)

ble $t4, $t0, else
move $t0, $t4 #copiamo il valore in t0

else:
addi $t2, $t2, 1
j for

endFor:
```

il codice inizia con `.data`, la [[direttive assemblatore |direttiva]] usata per la definizione dei dati statici
- `vettore:` è l'[[etichette |etichetta]] che rappresenta il vettore/array che useremo
- `N` è la lunghezza del vettore

`.text` è la direttiva per la definizione del programma.
- come prima cosa si carica in `$t0` il primo elemento del vettore.
- poi si carica `N` in `$t1`.
- infine, si fa un load immediate di 1 in `$t2` - l'indice (che parte da uno perché abbiamo già lo zeresimo elemento del vettore).

`for:` indica l'inizio del for (a cui si potrà poi saltare)\
- `bge $t2, $t1, endFor` è il controllo dell'indice - se il contenuto di `$t2` (l'indice) è maggiore del contenuto di `$t1`(N), si branch-a a `endFor`
- 



- `sll` - shift logico a sinistra di 2 per moltiplicare i per 4

