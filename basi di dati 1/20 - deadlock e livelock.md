## deadlock
Un **deadlock** si verifica quando:
- ogni transazione in un insieme $T$ è in attesa di ottenere un lock su un item sul quale qualche altra transazione dell'insieme detiene un lock, 
- quindi ogni transazione rimane bloccata, non rilascia i propri lock, e può bloccare anche transazioni che non sono in $T$

### soluzioni risolutive
Per verificare il sussistere di una situazione di stallo, si mantiene il **grafo d'attesa**, che ha come
- **nodi**: le transazioni
- **archi**: c'è un arco $T_{1}\to T_{2}$ quando la transazione $T_{1}$ è in attesa di ottenere un lock su un item su cui $T_{2}$ mantiene un lock

#### roll-back
Per risolvere il sussistere di una situazione di stallo, una transazione nel ciclo viene *rolled-back* e successivamente fatta ripartire.

- la transazione è abortita
- i suoi effetti sulla base di dati vengono annullati, ripristinando i valori dei dati precedenti all'inizio della sua esecuzione
- tutti i lock mantenuti dalla transazione vengono rilasciati

### approcci preventivi
In genere, si cerca di evitare il verificarsi di situazioni di stallo adottando opportuni protocolli.

Per esempio, si possono ordinare gli item e imporre alle transazioni di richiedere i lock necessari seguendo tale ordine.
- così non ci possono essere cicli nel grafo di attesa

![[prevenire-deadlock.png|center|350]]

## livelock
Un livelock si verifica quando una transazione aspetta indefinitamente che gli venga garantito un lock su un certo item.

### soluzioni
Il problema dell'attesa indefinita può essere risolto:
- con una strategia **first come-first served**
- eseguendo le transazioni in base alla loro **priorità** e aumentando la priorità di una transazione all'aumentare del tempo in cui rimane in attesa

#### abort di una transazione





