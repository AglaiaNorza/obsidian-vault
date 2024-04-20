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