---
tags: 
sticker: lucide//file-question
---
#### if/else
per eseguire un semplice if/else del tipo 
`if (x>0) <istruzione>
`else <istruzione>` 

si utilizza l'istruzione `blez`(branch at less than or equal to zero) - e si scrive il codice per la condizione falsa (se x <= 0) 
```
.text

blez $t0, else

#codice se la cond. è vera
#(se non branch-o)

j endIF #esco dall'if

else:
#codice se la cond. è falsa

endIf:
#codice per dopo
```

1) `blez` - branch-a, se il contenuto del registro $t0 è minore o uguale a 0, alla riga con scritto "else"
2) dopo `blez` si scrive il codice se non si va nel branch
3) `j endIF` - (jump) salta al punto "`endIF`", uscendo così dall'if che abbiamo creato
4) `else` qui c'è il codice a cui si branch-a se la condizione è falsa
5) `endIF` - punto a cui si salta dal codice per la condizione vera (e a cui si arriva senza dover saltare se la condizione è falsa)

altro esempio:

`if(i==j): f = g+h
`else: f = g-h`

```
.text

bneq $s3, $s4, else
add $s0, $s1, $s2
j endIf

else:
sub $s0, $s1, $s2

endIF:

```

#### loop
per ricreare un **do while** (x!=0)
```
.text

do:
#codice da ripetere

bnez $t0, do
```

- se x è diversa da 0, branch-a all'inizio del codice da ripetere (a `do`)

invece, per un **while do** (x!=0)
```
.text

while:
beqz $t0, endWhile

#codice da ripetere

j while #loop

endWhile:
#codice seguente
```
- se x è uguale a zero, branch-a (esce quindi dal while)

invece, per ricreare un **for**(i=0; i<N; i++)
```
.text
#t0 contiene l'indice, t1 il valore limite N

xor $t0, $t0, $t0 

li $t1, N #load-o N

cicloFor:
bge $t0, $t1, endFor

#codice da ripetere

addi $t0, $t0, 1
j cicloFor

endFor
#codice seguente
```

- `xor $t0, $t0, $t0` fa uno xor tra $t0 e se stesso e lo colloca in $t0 - serve per azzerare il valore di $t0, visto che uno xor tra due cose uguali darà sempre 0.
- `li` load immediato di un valore in un registro
- `bge` - branch if greater than or equal to, va a `endFor` se le condizioni del for non valgono più, quindi se l'indice `t0` è diventato maggiore di o uguale a `N`
- `addi` a "fine for" aggiunge uno all'indice (ricordo che è `addi` e non `add` perché si aggiunge un numero e non il contenuto di un registro)