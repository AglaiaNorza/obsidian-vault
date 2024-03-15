pseudoistruzioni:
- il move in realtà è un comando fittizio - è in realtà un'addizione senza segno fra il registro 16 e quello 0 
`addu $8, $0, $16` == `move $t0, $s0`

anche il `ble` è fittizio: SLIDE

##### trovare il massimo di un vettore 
```C
int vettore[6] = {11, 35, 2, 17, 29, 95}
int N = 6;

int max = vettore[0];

for(i = 1; i<N; i++){
	if (vettore[i]>max):
	max = vettore[i];
}
```

assembly:
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

- `sll` - shift logico a sinistra di 2 per moltiplicare i per 4

##### 