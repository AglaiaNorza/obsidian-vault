## mutua esclusione: soluzioni software
Proviamo ora a gestire la mutua esclusione senza aiuto dal parte dell’hardware o dal Sistema Operativo. Tenteremo quindi di gestire tutto nel codice (senza la sicurezza di avere operazioni atomiche).

>[!tip] le soluzioni che vedremo valgono per 2 processi
>fare il passaggio a n processi è possibile ma non semplice
### tentativi
> [!summary] tentativo 1
> ![[me-tentativo-1.png|center|400]]
> 
> implementa la mutua esclusione MA
> - c'è busy-waiting
> - se ci fosse solo un processo, non funzionerebbe

> [!summary] tentativo 2
> ![[me-tentativo-2.png|center|400]]
> 
> uso un array per indicare se uno dei due processi è in sezione critica (P1 legge il valore di P2 e viceversa)
> - all'inizio sono tutti e due inizializzati a 0, quindi, se lo scheduler interrompesse P1 una volta entrato nel while ma prima che setti la variabile, anche P2 entrerebbe nella sezione critica (race condition)

> [!summary] tentativo 3
> ![[me-tentativo-3.png|center|400]]
> 
> si utilizza una flag per comunicare l'intenzione di entrare in una sezione critica
> - anche qui, se lo scheduler interrompe subito dopo l'impostazione della `flag`, i due processi rimangono bloccati nel while (deadlock)

> [!summary] tentativo 4
> ![[me-tentativo-4.png|center|400]]
> 
>si tenta di risolvere il problema del tentativo precedente modificando nuovamente la `flag` dentro il while, ma anche in questo caso non funziona sempre.
>può avvenire *livelock*: 
>![[livelock-es.png|200]]

### algoritmo di Dekker
![[dekker-algo.png|center|550]]

Qui fin dall’inizio dichiaro di voler entrare nella sezione critica. Se il `wants_to_enter` dell’altro processo è `false` entro nella sezione critica. Nel caso in cui invece il valore è `true`, si ha una variabile `turn` condivisa. Per il `P0` se `turn` è `0` (non tocca a me), rimetto a falso il fatto che voglio entrare e faccio un’attesa attiva finché il `turn` è `1`. Una volta finita l’attesa reimposto il fatto che voglio entrare a `true`.
- se il dispatcher è fair, funziona
- garantisce il **bounded-waiting** - un processo può aspettarne un altro al massimo una volta
- non c'è deadlock, ma c'è busy-waiting
- non richiede nessun supporto dal Sistema Operativo (bisogna disattivare le ottimizzazioni dei sistemi operativi moderni)
- vale solo per 2 processi - l'estensione a N è possibile ma non banale

### algoritmo di Peterson
![[peterson-algo.png|center|350]]

Il processo "fa passare" l’altro processo - si entra nel `while` solamente se è il turno dell’altro processo e si vuole entrare (non si hanno problemi se in esecuzione si ha un solo processo). Anche qui, facendo un interleaving perfetto, non si avrebbero problemi in quanto viene mandato in esecuzione il penultimo processo che ha impostato `turn`

- ha le stesse caratteristiche dell'algoritmo di dekker
## passaggio di messaggi
Quando un processo interagisce con un altro, devono essere soddisfatti due requisiti fondamentali:
- **sincronizzazione** (mutua esclusione) --> il mittente deve inviare prima che il ricevente riceva
- **comunicazione**

Il *message passing* è una soluzione al secondo requisito, e:
- funziona sia con memoria condivisa che distribuita
- può essere usata anche per la sincronizzazione

Funziona con due primitive:
- `send(destination, message)` - qui `message` è il messaggio da mandare`
- `receive(source, message)` - qui `message` è la zona di memoria in cui vogliamo ricetvere il messaggio
- + a volte, il test di ricezione

>[!tip] send e receive sono sempre atomiche
>

- possono essere bloccanti oppure no (mentre il test di ricezione è sempre bloccante)
### send e receive bloccanti
Se `send` e `receive` sono bloccanti, il processo che invia il messaggio sarà `BLOCKED` fino a che qualcuno non effettuerà un `receive`, e allo stesso modo un processo che chiama `receive` prima di avere un messaggio da ricevere sarà `BLOCKED` fino alla ricezione di un messaggio.
- quindi che un processo si blocchi o no dipende da che funzione è stata chiamata prima
- questo tipo di comunicazione viene tipicamente chiamato *rendevouz*
### send non bloccante
è una scelta più naturale per molti programmi concorrenti.
- la chiameremo `nbsend`

nel caso più comune è abbinata comunque ad una ricezione bloccante:
- il mittente continua, mentre il destinatario è bloccato fino alla ricezione del mesaggio

ma è possibile abbinarla anche alla ricezione non bloccante (`nbreceive`)
- se il messaggio c'è, viene ricevuto, altrimenti si va avanti
- può settare un bit dentro il messaggio per dire se la ricezione è avvenuta o no
- (non si usa l'accoppiata ricezione non bloccante-invio bloccante di solito)
### indirizzamento
Il mittente deve sapere a quali processi vuole inviare il messaggio (e lo stesso vale per il destinatario, anche se non sempre).
Si possono usare:
- **indirizzamento diretto**
- **indirizzamento indiretto**
#### indirizzamento diretto
`send` include uno specifico identificatore per il destinatario (o gruppo di destinatari)
- per la `receive`, ci può essere oppure no
	- `receive(sender, msg)` riceve solo se il mittente coincide con il sender
	- `receive(null, msg)` riceve da chiunque
	- (dentro `msg` c'è anche il mittente)

>[!tip] ogni processo ha una sua coda - una volta piena, solitamente il processo si perde o viene ritrasmesso
#### indirizzamento indiretto
I messaggi sono inviati ad una particolare zona di memoria condivisa (**mailbox**) - il mittente li manda lì, e il destinatario se li prende.
- se la ricezione è bloccante e ci sono più processi in attesa su una ricezione, un solo processo viene svegliato
- ci sono evidenti analogie con producer/consumer (nello specifico, se la mailbox è piena allora `nbsend` si deve bloccare)

>[!example] esempi di comunicazione indiretta
>![[comunicazione-indiretta.png|center|450]]
### formato dei messaggi

> [!info] questo è il tipico formato dei messaggi:
> ![[formato-messaggi.png|center|300]]

### mutua esclusione con i messaggi
```C
const message null = /* null message */
mailbox box;

void P(int i) {
	message msg;
	while(true) {
		receive(box, msg);
		/* critical section */
		nbsend(box, msg);
		/* remainder */
	}
}

void main() {
	box = create_mailbox();
	nbsend(box, null);
	parbegin (P(1),P(2),...,P(n));
}
```
- si usano i messaggi per comunicare la situazione della sezione critica
- è necessario creare la mailbox con un messaggio al suo interno, altrimenti nessun processo entrerebbe mai nella sezione critica
- è necessario usare `nbsend(box,msg)`, altrimenti il processo che è stato nella sezione critica non può andare avanti fino a quando un altro processo non ci entri
### producer/consumer con messaggi
(le premesse sono le stesse di prima)

> [!summary]- premesse
> La situazione è questa:
> - uno o più processi creano dati e li mettono in un buffer - consumer prende i dati dal buffer (a cui può accedere un solo processo, che sia producer o consumer)
> 
> I problemi:
> - assicurare che i producer non inseriscano quando il buffer è pieno e che il consumer non legga quando il buffer è vuoto
> - mutua esclusione sul buffer

```C
const int capacity = /* buffering capacity */;
mailbox mayproduce, mayconsume;
const message null = /* null message */;

void main() {
	mayproduce = crate_mailbox();
	mayconsume = create_mailbox();
	for(int i=1; i<=capacity; i++) {
		nbsend(mayproduce, null);
	}
	parbegin(producer, consumer);
}

void producer() {
	message pmsg;
	while(true) {
		receive(mayproduce, pmsg);
		pmsg = produce();
		// append al buffer !
		nbsend(mayconsume, pmsg);
	}
}

void consumer() {
	message cmsg;
	while(true) {
		receive(mayconsume, cmsg);
		consume(cmsg);
		nbsend(mayproduce, null);
	}
}
```

- riempiendo `mayproduce` con `capacity` elementi, mi assicuro che nessun producer aggiunga al buffer se esso è già pieno (se `mayproduce` non ha messaggi, il producer diventa `BLOCKED`)
- `mayconsume` è usato per assicurarsi che il consumer non legga un buffer vuoto

Questa soluzione assicura:
- mutua esclusione
- no deadlock
- no starvation - solo se le code di processi bloccati su una receive sono gestite in modo "forte" (FIFO)