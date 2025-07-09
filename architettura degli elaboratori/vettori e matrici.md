---
{}
---
in assembly non esistono i tipi.

### vettori
**vettore**
- sequenza di n elementi di dimensioni uguali
- consecutivi in memoria
- indirizzabili per indice (da 0 a N-1)
- dimensione totale = N * dim. elemento
 
SI definiscono staticamente nella sezione `data` usando un'etichetta (indirizzo del primo elemento del vettore)

Per **indirizzare** l'elemento i-esimo, bisogna aggiungere l'offset `i * dimensione elemento`.

>[!example]- esempio
>- vettore di word a partire da `0x00001004`:
la prima word si trova a  `0x00001004`, la seconda a  `0x00001008` (offset di 4 byte)
>- vettore di half word a partire da `0x0001000`:
prima word a `0x0001000`, seconda a `0x0001002` (metà di 4 byte)

##### vettori di byte in memoria
- vettore di *byte* (valori da 0 a 255)
`label1: .byte 1,2,3,4`
 <br/>
- vettore di *caratteri* (byte) seguiti da \0 (carattere codificato con zero, 0x0)
`label2: .asciiz "sopra la panca"` - ogni lettera occupa un byte
###### vettori di word
numeri a 32 bit in CA2 codificati in 4 byte

`label13: .word 1,2,3,4,5,6`

per mettere 100 valori a 0:
`label4: .word 0:100`

il processore MIPS permette l'ordinamento dei byte di una word in due modi:
- **Big-endian** - byte memorizzati dal MSB al LSB
- **Little-endian** - dal LSB al MSB
 
L'ordine delle word è lo stesso, ma l'insieme dei singoli byte è specchiato.
 
![[little e big endian.png]]

##### cicli
due stili di scansione di un vettore:

1) **scansione per indice**

| pro                                                                          | contro                                                                     |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| comoda se l'*indice serve* <br>per controlli o altro                         | *convertire* ogni volta <br>l'indice nel corrispondente <br>offset in byte |
| l'incremento dell'indice *non<br>dipende dalla dimensione*<br>degli elementi |                                                                            |
| comoda se il vettore è allocato<br>staticamente in `.data`                   |                                                                            |
|                                                                              |                                                                            |

> [!example]- codice
> ```
> .data
> vector: 10, 123, 33
>  
> .text
> main:
> 	la $s0, vector # Carico in $s0 l'indirizzo del vettore
> 	li $t0, 2      # Carico in $t0 il valore 2, indice dell'elemento
> 	sll $t1, $t0, 2  # Carico in $t1 il valore $t0 * 4 (shifto di 2)
> 	add $s0, $s0, $t1 # Sommo $s0 e $t1 (sposto il puntatore)
> ```

2) **scansione per puntatore**

| pro                                               | contro                                                                     |
| ------------------------------------------------- | -------------------------------------------------------------------------- |
| si lavora direttamente su<br>indirizzi di memoria | *non si ha l'indice*<br>dell'elemento                                      |
| *meno calcoli* nel ciclo                          | l'incremento del puntatore<br>*dipende dalla dimensione degli<br>elementi* |
|                                                   | bisogna calcolare l'indirizzo<br>successivo all'ultimo elemento            |
>[!example]- codice
>```
>.data
>vector: 10, 123, 33 
>
>.text
>main:
>li $t0, 2          # Carico 2 in $t0
>sll $t1, $t0, 2         # Moltiplico per 4 e carico in $t1
>lw $s0, vector($t1)       # Leggo l'indirzzo vettore+$t1
>```

### matrici
una matrice MxN è una successione di M vettori, ciascuno di N elementi.
(la struttura bidimensionale è mentale, in realtà è solo una lunga serie di bit)
- numero di elementi totali = `M x N`
- dimensione totale in byte = `M x N x dimensione elemento`

Si definisce staticamente come un vettore contenente M x N elementi uguali
`Matrice: .word 0:91` - spazio per 7 x 13

trovare la posizione di un elemento:
![[posizione in matrice.png]]

##### matrici 3D
![[matrici3d.png]]