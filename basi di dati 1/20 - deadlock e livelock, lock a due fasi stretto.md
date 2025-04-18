## deadlock
Un **deadlock** si verifica quando:
- ogni transazione in un insieme $T$ è in attesa di ottenere un lock su un item sul quale qualche altra transazione dell'insieme detiene un lock, 
- quindi ogni transazione rimane bloccata, non rilascia i propri lock, e può bloccare anche transazioni che non sono in $T$

> [!info] grafo d'attesa
> Per verificare il sussistere di una situazione di stallo, si mantiene il **grafo d'attesa**, che ha come
> - **nodi**: le transazioni
> - **archi**: c'è un arco $T_{1}\to T_{2}$ quando la transazione $T_{1}$ è in attesa di ottenere un lock su un item su cui $T_{2}$ mantiene un lock

### soluzioni risolutive

#### roll-back
Per risolvere il sussistere di una situazione di stallo, una transazione nel ciclo viene *rolled-back* e successivamente fatta ripartire.

- la transazione è abortita
- i suoi effetti sulla base di dati vengono annullati, ripristinando i valori dei dati precedenti all'inizio della sua esecuzione
- tutti i lock mantenuti dalla transazione vengono rilasciati

### approcci preventivi
In genere, si cerca di evitare il verificarsi di situazioni di stallo adottando opportuni protocolli.

Per esempio, si possono *ordinare gli item* e imporre alle transazioni di richiedere i lock necessari seguendo tale ordine.
- così non ci possono essere cicli nel grafo di attesa

![[prevenire-deadlock.png|center|350]]

## livelock
Un livelock si verifica quando una transazione aspetta indefinitamente che gli venga garantito un lock su un certo item.

Il problema dell'attesa indefinita può essere risolto:
- con una strategia **first come-first served**
- eseguendo le transazioni in base alla loro **priorità** e aumentando la priorità di una transazione all'aumentare del tempo in cui rimane in attesa
### abort di una transazione
Avviene quando:
1) la transazione esegue un'operazione non corretta (es. divisione per 0)
2) lo scheduler rileva un deadlock
3) lo scheduler fa abortire la transazione per garantire la serializzabilità
4) si verifica un malfunzionamento hardware o software

### punto di commit
Il punto di commit di una transazione è il punto in cui essa ha ottenuto **tutti i lock** di cui aveva bisogno, e ha **effettuato tutti i calcoli** (quindi sta per fare gli unlock).
In questo caso, non può essere abortita se non per il punto 4).

>[!info] dati sporchi
>I dati sporchi sono quindi i dati scritti da una transazione sulla base di dati prima di raggiungere un punto di commit

### rollback a cascata
Quando una transazione $T$ viene abortita, devono essere annullati gli effetti sulla base di dati prodotti sia da $T$ che da qualsiasi transazione abbia letto dati sporchi.

Abbiamo visto che:
- il [[19 - il meccanismo di lock, lock binario|lock binario]] permette di risolvere il problema del lost update, ma non quello della lettura di un dato sporco o dell'aggregato non corretto.
- il [[19 - il meccanismo di lock, lock binario#locking a due fasi|locking a due fasi]] permette di risolvere il problema dell'aggregato non corretto, ma non quello della lettura del dato sporco

Per risolvere questo problema, quindi, serve che le transazioni obbediscano a regole più restrittive.

## locking a due fasi stretto
Una transazione soddisfa il protocollo di locking a due fasi stretto se:
1) **non scrive** sulla base di dati fino a quando non ha **raggiunto il suo punto di commit** 
	- questo assicura che, se una transazione viene abortita, non ha modificato nessun item nella base di dati
2) **non rilascia** un lock finché non ha **finito di scrivere** sulla base di dati
	- in questo modo, se una transazione legge un item scritto da un'altra transazione, quest'ultima sarà sicuramente una transazione che non può essere abortita

> [!example] esempio
> ![[locking-stretto.png|center|200]]

## protocolli: classificazione 
### protocolli conservativi
I protocolli conservativi cercano di **evitare** le situazioni di stallo.
Ogni transazione richiede *tutti i lock all'inizio* - se ne manca anche uno solo, la transazione viene messa in attesa.
(se ha ricevuto lock, questi vengono rilasciati)

Così si evita il deadlock, ma non il livelock - la transazione rischia di non poter mai partire.
Per *evitare anche il livelock*, una transazione richiede tutti i lock che servono all'inizio e li ottiene se e solo se:
- tutti i lock sono disponibili
- nessuna transazione che precede T nella coda è in attesa di un lock richiesto da T

>[!summary] vantaggi e svantaggi
>**vantaggi**:
>- si evita il verificarsi sia del deadlock che del livelock
>
>**svantaggi**:
>- l'esecuzione di una transizione può essere *ritardata*.
>- una transizione è costretta a richiedere un lock *su ogni item che potrebbe servirle*, anche se poi non lo utilizza.

### protocolli aggressivi
I protocolli aggressivi cercano di processare le transazioni **il più rapidamente possibile** anche se ciò può portare a situazioni di stallo.

Una transazione deve richiedere un lock su un item *immediatamente prima* di leggerlo o scriverlo.
- può verificarsi deadlock

### a confronto
La scelta tra protocolli conservativi e aggressivi si basa principalmente sulla **probabilità che due transazioni richiedano un lock su uno stesso item**.
Se essa è
- **alta** --> conviene un protocollo *conservativo*, che evita il sovraccarico dovuto alla gestione del deadlock (rilevarlo, risolvere lo stallo, eseguire parzialmente transazioni che poi verranno abortite, rilascio dei lock)
- **bassa** --> conviene un protocollo *aggressivo*, che evita il sovraccarico dovuto alla gestione dei lock (decidere se garantire un lock, gestire la tavola dei lock, mettere e togliere transazioni da una coda)
## domande orale
>[!question] possibili domande orale 
>- quando si verifica un deadlock? e un livelock?
>- come si verifica il sussistere di una situazione di stallo?
>- quali sono le soluzioni risolutive e gli approcci preventivi per il deadlock?
>- come si risolve il livelock?
>- quando avviene l'abort di una transazione?
>- come funziona il locking a due fasi stretto?
>- cosa risolve il locking a due fasi stretto?
>- protocolli conservativi e aggressivi