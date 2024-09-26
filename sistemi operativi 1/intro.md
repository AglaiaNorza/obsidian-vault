---
sticker: lucide//git-compare
---
### sistema operativo (e i suoi componenti)
gestisce le risorse hardware di un sistema computerizzato (processori, RAM, i/o) e fornisce un insieme di servizi agli utenti. 

![[PC-components.png]]

1) **processore** - si occupa delle computazioni
2) **memoria principale** - è volatile, se il PC si spegne se ne perde il contenuto (chiamata reale o primaria)
3) **I/O** - memoria secondaria non volatile (dischi), comunicazione (scheda di rete..), tastiera ecc.
4) **"bus" di sistema** - fanno comunicare le parti interne del computer 
5) **registri** 
	1) *visibili all'utente*: usati dai linguaggi non interpretati
	2) *di controllo e di stato*: usati dal processore per controllare il suo utilizzo, e dal sistema operativo per controllare l'esecuzione dei programmi
	3) *interni*: usati dal processore, responsabili della comunicazione con memoria e I/O

#### registri visibili all'utente
- sono gli unici che possono essere *usati direttamente* quando si programma in linguaggio macchina. 
- possono contenere dati o indirizzi (puntatori diretti, registri-indice, puntatori a segmento, puntatori a stack)

#### registri interni
i principali registri interni sono:
- **registro dell'indirizzo di memoria** (MAR): contiene l'indirizzo della prossima operazione di lettura/scrittura
- **registro di memoria temporanea** (Memory Buffer Register): contiene i dati da scrivere in memoria, o lo spazio dove scrivere i dati letti dalla memoria
- **I/O address register** (self explanatory)
- **I/O buffer register**: registro di memoria temporanea per I/O

#### registri di controllo e stato
- **Program Counter**: contiene l'indirizzo dell'istruzione da prelevare dalla memoria
- **Instruction Register**: contiene la più recente istruzione prelevata
- **Program Status Word**: contiene le informazioni di stato
- **Flag** (codici di condizione): singoli bit settati dal processore come risultato di operazioni (es. flag ALU)
 
Questi registri vengono letti e modificati in modo implicito dalle istruzioni assembler.
Nell'architettura x86 sono considerati registri di controllo anche quelli per la gestione della memoria.

### esecuzione di istruzioni
ha due passi:
1) fase di **fetch** delle istruzioni: il processore legge il program counter e preleva le istruzioni dalla memoria principale (il PC è incrementato dopo ogni prelievo, oppure modificato da un jump)
2) fase di **execute**: il processore esegue ogni istruzione prelevata:
	1) l'istruzione prelevata viene caricata nell'Instruction Register 
 
	![[fasi-istruzioni.png]]

#### caratteristiche di una macchina ipotetica
Le istruzioni hanno un formato da 16 bit: 4 sono presi dall'OPcode, e 12 dall'address.
Anche gli interi hanno un formato da 16 bit: 1 bit per il segno, e 15 per la magnitudo

![[formato-istruzioni.png|400]]
#### interruzioni
le interruzioni interrompono la normale esecuzione sequenziale del processore.
- come consequenza, viene eseguito software "di sistema", parte del sistema operativo.

Le cause sono molteplici, e danno luogo a diverse *classi* di interruzioni:
- da programma (sincrone)
- da I/O, da fallimento hardware, da timer (asincrone)

Le interruzioni sincrone interrompono immediatamente l'esecuzione del programma, mentre mentre quelle asincrone vengono sollevate successivamente.

Per le interruzioni asincrone, una volta che l'handler è terminato, si riprende dall'istruzione *successiva a quella interrotta*. Per quanto riguarda le interruzioni sincrone, invece, non è detto.
Esistono infatti diversi tipi di errori:

| errore            | risoluzione                                                       |
| ----------------- | ----------------------------------------------------------------- |
| fault             | errore *corregibile*, viene rieseguita la stessa istruzione       |
| abort             | errore *non corregibile*, si esegue software collegato all'errore |
| trap, system call | si continua dall'istruzione successiva                            |
