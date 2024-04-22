### fetch e aggiornamento PC
leggiamo l'istruzione corrente e, in parallelo, aggiorniamo il PC
 
![[fetch.png | 400]]

### operazioni ALU e accesso memoria
I formati delle istruzioni *I* (immediato, come load e store word) ed *R* (aritmetico-logiche) sono quasi uguali:
([[progettare una CPU MIPS - le basi#fasi di esecuzione di un'istruzione |vedi formati]])

- il secondo argomento dell'istruzione è:
	1) registro - formato R
	2) campo immediato (ovvero valore esteso nel segno) - formato I

**<font color="#e5b9b7">Primo MUX</font>**:
Le istruzioni aritmetico-logiche utilizzano la ALU con due registri come ingressi, mentre quelle di memoria utilizzano la ALU per calcolare l'indirizzo della memoria dati, ma prendono il secondo ingresso della ALU dal campo offset a 16 bit (con estensione del segno).
Quindi il MUX con segnale di controllo **ALUSrc** sceglie tra queste due opzioni.

**<font color="#fac08f">Secondo MUX</font>**:
Il valore da scrivere nel registro di destinazione proviene dalla ALU per le istruzioni di tipo R o dalla memoria per l'istruzione load.
Quindi il MUX a destra, con segnale di controllo **MemtoReg**, sceglie tra le due opzioni.

![[architettura 1 mips.png |600]]

>[!info]- esempio - istruzioni formato R
![[istr formato R.png|500]]

#### esercizi
>[!example]- add
>![[MIPS add.png]]

>[!example]- load word
>![[MIPS load word.png]]


>[!example]- store word
>![[MIPS store word.png]]

### salti condizionati (beq)
- `beq` ha come operandi: due registri da comparare, un indirizzo a cui saltare (da sommare al PC)
- visto che l'istruzione calcola già l'istruzione successiva al salto, si usa già **PC+4** come base per il calcolo
- anche il campo offset è **spostato di 2 bit a sinistra** (moltiplicato per 4), perché ci spostiamo di word e non byte.
 
	![[beq.png|350]]

>[!example]- load word con tutto
>![[load word 2.png|400]]

### con control unit
la control unit genera un segnale di controllo a 6 bit - **opcode** e **funct**, che definisce che tipo di operazione verrà svolta dalla ALU

| ALU control line | funzione           |     |
| ---------------- | ------------------ | --- |
| `0000`           | `AND`              |     |
| `0001`           | `OR`               |     |
| `0010`           | `add`              |     |
| `0110`           | `subtract`         |     |
| `0111`           | `set on less that` |     |
| `1100`           | `NOR`              |     |
La logica di controllo della ALU è implementata "a cascata" - in base ai bit della ALUop, ci sono *3 casi*:
1) devo guardare funct
2) somma
3) sottrazione

visto che sono 3 opzioni, si utilizzeranno 2 bit.

Se il MSB della ALUOp è:
- 1 - devo controllare il campo **funct**
- 0:
	- se il secondo bit è 0 - faccio una **somma**
	- se il secondo bit è 1 - faccio una **sottrazione**

il valore dell'ingresso di controllo della ALU viene generato dopo una decodifica basata sulla ALUOp.

| codice istruzione | ALUOp | campo funzione | op. ALU  | ingresso controllo ALU |
| ----------------- | ----- | -------------- | -------- | ---------------------- |
| `lw`              | 00    | `XXXXXX`       | somma    | `0010`                 |
| `sw`              | 00    | `XXXXXX`       | somma    | `0010`                 |
| `beq`             | 01    | `XXXXXX`       | sottraz. | `0110`                 |
| `tipo R`          | 10    | `[10] 0000`    | somma    | `0010`                 |
| `tipo R`          | 10    | `[10] 0010`    | sottraz. | `0110`                 |
| `tipo R`          | 10    | `[10] 0100`    | AND      | `0000`                 |
| `tipo R`          | 10    | `[10] 0101`    | OR       | `0001`                 |
| `tipo R`          | 10    | `[10] 1010`    | slt      | `0111`                 |
>[!info]+ input di controllo e tavola di verità
>![[MIPS tavola verita opcode.png]]


