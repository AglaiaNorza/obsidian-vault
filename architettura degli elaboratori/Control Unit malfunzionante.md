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
2) 



