> [!info]- index
> - [[#CPU senza pipeline|CPU senza pipeline]]
> 			- [[#fasi di esecuzione di un'istruzione|fasi di esecuzione di un'istruzione]]
> 			- [[#unità funzionali necessarie|unità funzionali necessarie]]
> 	- [[#CPU senza pipeline#ingredienti|ingredienti]]
> 		- [[#ingredienti#memoria istruzioni, PC, adder|memoria istruzioni, PC, adder]]
> 		- [[#ingredienti#registri e ALU|registri e ALU]]
> 		- [[#ingredienti#memoria dati e unità di estensione del segno|memoria dati e unità di estensione del segno]]


La CPU è una *macchina sequenziale* - è formata da:
- uno **stato** (elementi che, se rimessi nella stessa condizione, fanno comportare la macchina allo stesso modo).
- un **circuito combinatorio**.

## CPU senza pipeline
per progettare una CPU senza pipeline, è necessario:
1) definire come viene elaborata un'istruzione - **fasi di esecuzione**
2) scegliere le **istruzioni da realizzare**
3) scegliere le **unità funzionali necessarie**
4) **collegare** le unità funzionali
5) **costruire la Control Unit** (CU), che controlla il funzionamento della CPU
6) calcolare il massimo tempo di esecuzione delle istruzioni - che ci fornisce il **periodo di clock**

##### fasi di esecuzione di un'istruzione
1) **fetch** - *caricamento* di un'istruzione da memoria a Control Unit
2) **decodifica** - *decodifica* dell'istruzione e *lettura argomenti* dai registri
3) **esecuzione** - *attivazione* delle unità necessarie
4) **memoria** - accesso alla memoria
5) **write back** - scrittura dei *risultati nei registri*
6) **aggiornamento program counter** - normale/salti condizionati/salti non condizionati

ci sono diversi *tipi di istruzione* da realizzare**
- accesso alla memoria→ `lw, sw` (tipo I)
- salti condizionati → `beq` (tipo I)
- operazioni aritmetico-logiche → `add, sun, sll, slt` (tipo R)
- salti non condizionati → `j, jal` (tipo J)
- operandi non costanti → `li, addi, subi` (tipo I)**

>[!info] formato delle istruzioni
>![[formato istruzioni mips.png]]

##### unità funzionali necessarie
seguendo l'architettura di Von Neuman, le unità funzionali necessarie per la progettazione di una CPU sono:

| unità                    | descrizione                                             |
| ------------------------ | ------------------------------------------------------- |
| **PC** (Program Counter) | registro che contiene <br>l'*indirizzo dell'istruzione* |
| **memoria istruzioni**   | contiene le *istruzioni*                                |
| **adder**                | per *calcolare il PC* (successivo o salto)              |
| **registri**             | contengono gli *argomenti* delle istruzioni             |
| **ALU**                  | fa *operazioni* aritmetico-logiche, confronti           |
| **memoria dati**         | da cui *leggere/scrivere* i dati                        |

Queste unità sono collegate da **datapath** - interconnessioni che definiscono il flusso delle informazioni nella CPU.
 
Se un'unità funzionale può ricevere *dati da più sorgenti*, è necessario inserire un **MUX** per selezionare la sorgente necessaria.

### ingredienti

#### memoria istruzioni, PC, adder

- come primo elemento, è necessaria un'unità di memoria in cui salvare le istruzioni del programma, che possa **fornire in uscita l'istruzione associata ai dati in ingresso**:
	- input: indirizzo a 32 bit
	- output: istruzione da 32 bit situata nell'indirizzo di input
 
	![[memoria istr.png| 200]]
- abbiamo bisogno anche del **Program Counter (PC)**, per salvare l'indirizzo dell'istruzione corrente:
	- il program counter è un registro a 32 bit e viene riscritto al termine di ogni ciclo di clock
  
	![[pcer.png| 200]]
- e di una **ALU sommatrice**, per sommare l'indirizzo corrente a 4 e ottenere l'indirizzo successivo:
	- input: due valori a 32 bit
	- output: la loro somma
 
	 ![[sommatore.png|200]]

#### registri e ALU
- il **blocco dei registri** (register file) contiene i *32 registri* universali a 32 bit del processore
	- i registri sono indirizzabili con 5 bit (ciascun registro può essere letto o scritto specificando il numero ad esso associato)
	- 4 porte di <u>input</u> a 5 bit:
		- 2 *registri di lettura*, che non richiedono segnali di controllo
		- 1 *registro di scrittura*, che necessita del segnale di controllo **RegWrite** (1- scrivo, 0 - non scrivo)
		- 1 ingresso per il *dato da scrivere*
 
	 ![[register file.png|400]]

- la **ALU**, che riceve due valori interi a 32 bit e svolge un'operazione indicata dai segnali **Op. ALU**
	- output: risultato a 32 bit e segnale *"Zero"*, che indica se il risultato è zero
#### memoria dati e unità di estensione del segno
- l'**unità di memoria dati** scrive o legge dati in memoria
	- input: 
		- segnali **MemWrite** e **MemRead** - indicano lettura o scrittura (sono due ma solo uno può essere attivo)
		- **indirizzo** dato da scrivere o leggere
		- **dato** da scrivere (se MemWrite) 
	- output: **dato letto** (se MemRead) 
 
	![[memoria dati.png| 250]]
- l'**unità di estensione del segno** del campo offset (16 bit meno significativi dell'istruzione) estende 16 bit a 32 (copia il bit del segno nei 16 MSB)
 
	![[estensione segno.png | 200]]