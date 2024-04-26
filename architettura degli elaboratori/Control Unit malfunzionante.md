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

1) quali istruzioni sono affette?
 
![[istr affette regwrite branch.png|center|400]]
- tutte le istruzioni che modificano un registro (tipo `r` e `lw`) lo lasceranno invece invariato
- branch - oltre a saltare, modificherà uno dei registri:
	- `rt` verrà sovrascritto (perché `RegDst` = 0)
	- il valore scritto sarà la differenza tra i due registri confrontati dalla ALU (assumiamo `MemToReg = 0`)

2) programma per mostrarlo

scriviamo un programma che lasci il valore 0 nel registro `$s0` se la CPU è malfunzionante, e scriva 1 se funziona correttamente.
- ricordiamo che non possiamo caricare un valore in un registro perché `RegWrite = 0`




