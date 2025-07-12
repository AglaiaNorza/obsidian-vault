---
created: 2025-07-12T12:03
updated: 2025-07-12T12:03
---
cosa succede se la CU genera segnali errati?
dobbiamo individuare:
- quale combinazione di segnali venga generate
- **quali istruzioni vengano influenzate** dalle nuove combinazioni, e cosa facciano
e successivamente possiamo scrivere un programma che ci mostri se la CPU è malfunzionante o meno.

>[!info] segnali CU
![[segnali di controllo CU.png|center|500]]

#### RegWrite <- Branch
se ho il dubbio che il segnale `RegWrite` sia determinato dal segnale `Branch` (ossia abbia lo stesso valore)

>[!Tip] tip
>si assumano i delta come: `MemToReg` = 1 solo per la `lw`, `RegDest` = 1 solo per le istruzioni di tipo R (altrimenti zero).

1) quali **istruzioni** sono affette?
 
![[istr affette regwrite branch.png|center|400]]
- tutte le *istruzioni che modificano un registro* (tipo `r` e `lw`) lo lasceranno invece invariato
- *branch* - oltre a saltare, modificherà uno dei registri:
	- `rt` verrà sovrascritto (perché `RegDst` = 0)
	- il valore scritto sarà la differenza tra i due registri confrontati dalla ALU (assumiamo `MemToReg = 0`)
>[!Example]- branch errato
> ![[branch errato regwrite branch.png|500]]

2) **programma** per mostrarlo

scriviamo un programma che lasci il valore 0 nel registro `$s0` se la CPU è malfunzionante, e scriva 1 se funziona correttamente.
- ricordiamo che non possiamo caricare un valore in un registro perché `RegWrite = 0`

basta una qualsiasi istruzione che generi un valore diverso da 0:
`li $s0, 1`
`addi $s0, $zero, 1`

oppure una `beq` che calcoli la differenza tra due valori uguali (`$s0` e se stesso), ma assumendo che inizialmente `$s0 = 1` 
`beq $s0, $s0, ...`
visto che il risultato del confronto tra i due registri (sub della ALU verrà caricato erroneamente nel registro, `$s0` varrà 0).

#### MemWrite <- not(RegWrite)
1) istruzioni affette:
 
![[memwrite not regwrite valori.png|center|400]]

- `j` e `beq` saltano correttamente, ma *scrivono in memoria*
>[!Example]- branch e jump errati
![[branch errato memwrite not regwrite.png|500]]
![[jump errato memwrite not regwrite.png|500]]

2) codice:
 
ci conviene usare la `beq`, perché memorizzerà il valore del registro `$rt` all'indirizzo calcolato dalla ALU come differenza tra `$rs` e `$rt`.
```
move $s0, $zero  // mettiamo 0 dentro $s0
sw $s0, 0  // scriviamo il valore di $s0 (0) all'indirizzo 0
li $s1, 1

beq $s1, $s1, on // *
on:
lw $s0, 0 // caricando il contenuto
```
\* branch apparentemente inutile (compara due registri uguali e salta all'istruzione successiva), ma che serve a vedere se scrive all'indirizzo zero (la ALU fa sub tra due registri uguali, fa 0, e se la CPU è rotta va a scrivere `$s1` (1) in 0, sovrascrivendo lo 0)


