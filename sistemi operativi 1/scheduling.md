Un sistema operativo deve allocare risorse tra diversi processi che ne fanno richiesta contemporaneamente: tra le risorse, c'è il processore (e quindi il tempo di esecuzione). Questa risorsa viene allocata tramite lo **scheduling**.

>[!question] qual è lo scopo dello scheduling?
>- *assegnare ad ogni processore i processi* da eseguire, man mano che questi vengono creati e distrutti
>- va fatto *ottimizzando* vari aspetti:
>	- tempo di risposta
>	- throughput (portare a termine più processi nella stessa unità di tempo)
>	- efficienza del processore
>- non fare favoritismi tra processi (con stessa priorità) ma *gestire la priorità* dei processi quando necessario
>- evitare la starvation dei processi
>- usare il processore in modo efficiente
>- avere un **overhead** basso (overhead = lavoro fatto in più - lo scheduler deve essere veloce ed efficiente)

#### tipi di scheduling
Ci sono diversi tipi di scheduling (a seconda di quanto spesso vengono eseguiti)
- **long-term** (eseguito molto di rado) - decide l'aggiunta ai processi da essere eseguiti
- **medium-term** (eseguito ogni tanto)- decide l'aggiunta ai processi in memoria principale
- **short-term** - decide quale processo va eseguito tra quelli pronti
- **I/O** - decide a quale processo assegnare un dispositivo I/O, tra quelli che lo stanno richiedendo

### stati dei processi e scheduling
molte delle transizioni del [[processi#stato di un processo|modello a sette stati]] sono dovute a uno scheduler.
 
![[transizioni-scheduler.png|500]]

![[code-scheduling.png]] 

#### long-term scheduling
spesso è **FIFO**. 
Altrettanto spesso, è FIFO con delle condizioni: pirorità, requisiti I/O, o tempo di esecuzione atteso.
- controlla il grado di multiprogrammazione (e decide se mettere un processo in RAM o su disco)
- può essere chiamato in causa anche quando non ci sono nuovi processi (es. quando termina un processo o quando processi sono idle da troppo tempo)

tipiche strategie:
- i lavori *batch* (non interattivi) vengono accodati e il LTS li prende man mano che ritiene giusto
- i lavori *interattivi* vengono ammessi fino a che non si satura il sistema
- se si sa quali sono *I/O-bound* e quali *CPU-bound* (usano molto I/O o CPU), può mantenere un mix tra i due tipi

#### medium-term scheduling
è parte della funzione di **swapping** dei processi (passaggio da memoria secondaria a principale e viceversa)
- l'obiettivo principale è gestire il grado di multiprogrammazione

#### short-term scheduler
chiamato anche **dispatcher**.
Eseguito più frequentemente, sulla base di eventi (interruzioni di clock o I/O, syscalls, segnali).
Il suo scopo è *allocare tempo di esecuzione* su un processore per ottimizzare il comportamento dell'intero sistema, in base a determinati indici prestazionali.

>[!tip] criteri utente e sistema
>Occorre distinguere i criteri per lo short term scheduling in utente e di sistema.
>
>I criteri per l'*utente* sono quelli che un singolo utente può apprezzare (es. tempo di risposta), mentre quelli per il *sistema* sono legati all'uso efficiente di un procesore.

>[!bug] criteri prestazionali e non
>Un'altra distinzione che occorre fare è tra criteri correlati e non correlati alle *prestazioni*.
>Quelli prestazionali sono quelli **quantitativi** e facili da misurare.
>Quelli non prestazionali sono **qualitativi** e molto più difficili da misurare.

##### criteri utente:
*prestazionali*:
- **turnaround time** (tempo di ritorno) - tempo tra la creazione di un processo e il suo completamento. (di solito si parla di batch)
- **response time** -  tempo tra la sottomissione di una richiesta e l'inizio della risposta (processi interattivi) - duplice obiettivo dello scheduler: minimizzare il tempo medio, o massimizzare il numero di utenti con un buon tempo di risposta.
- **deadline** - massimizzare il numero di scadenze rispettate

*non prestazionali*:
- **predictability** - non deve esserci troppa variabilità nei tempi di risposta e/o ritorno

##### criteri di sistema:
*prestazionali*:
- **throughput** (volume di lavoro nel tempo) - massimizzare il numero di processi completati per unità di tempo
- **processor utilization** - percentuale di tempo in cui il processore viene utilizzato - il processore deve essere idle il minor tempo possibile

*non prestazionali*:
- **fairness** - se non ci sono indicazioni dall'utente o dal sistema, tutti i processi devono essere trattati allo stesso modo
- **enforcing priorities** - se ci sono priorità, lo scheduler deve favorire processi a priorità più alta
- **balancing resources** - lo scheduler deve far sì che le risorse del sistema siano usate il più possibile - dovranno essere favoriti processi che useranno meno le risorse attualmente più usate

>[!warning] priorità e starvation
>Un processo a bassa priorità potrebbe soffrire di starvation a causa di un altro processo a priorità più alta.
>- Soluzione: man mano che l'"età" aumenta (o anche sulla base di quante volte sarebbe potuto andare in esecuzione), la priorità cresce

### politiche di scheduling
![[scheduling-politics.png]]

#### funzione di selezione
è quella che sceglie il processo da mandare in esecuzione.

Si basa tipicamente su alcuni parametri:
- w(ait) = tempo trascorso in attesa
- e(xecution) = tempo trascorso in esecuzione 
- s = tempo totale richiesto (incluso quello già servito - e) (viene o stimato, o fornito come input)

#### modalità di decisione
specifica in quali istanti di tempo la funzione di selezione viene invocata.
Può essere:
- **non-preemptive** - se un processo è in esecuzione, o arriva fino a terminazione, o fa una richiesta bloccante (quindi resta in esecuzione se non fa chiamate bloccanti)
- **preemptive** - il dispatcher può interrompere un processo in esecuzione "liberamente" - (se non è terminato o blocked), il processo diventa `ready` 
	- la preemption può avvenire per diversi motivi: o sono arrivati *nuovi processi* appena creati, o per un *interrupt* (di I/O, o di clock, per evitare che un processo monopolizzi il sistema)

#### esempi classici su un esempio comune
Abbiamo 5 processi batch, ABCDE, che arrivano a distanza di due unità di tempo.

![[es-scheduling.png]]

##### first come first served (FIFO)
- non-preemptive
- tutti i processi vengono aggiunti alla coda dei `ready`
- quando un processo smette di essere eseguito, si passa al processo che ha aspettato di più nella coda

![[FCFS.png|400]]

problemi:
- un processo corto potrebbe attendere molto prima di essere eseguito (es. E)
- favorisce i processi molto CPU-bound (che non verranno rilasciati fino alla loro terminazione)

##### round-robin 
- preemptive, si basa su un *clock*
- ogni processo ha una fetta di tempo - in ordine di arrivo (FIFO), hanno un'unità di clock a testa 

![[round-robin.png|400]]

- un'interruzione di clock viene generata periodicamente - quando arriva, il processo attualmente in esecuzione viene rimesso nella coda dei `ready` e il prossimo viene selezionato tra quelli già ready (se la coda è vuota, il processo rimane in esecuzione)

>[!question] Quanto lungo deve essere il quanto di tempo?
> - Il round robin funziona bene se il quanto è non troppo più grande del tipico tempo di interazione di un processo:
> 	- ![[quantum-robin.png|200]]
> 
> - invece, se il quanto di tempo è minore del tempo di risposta, diventa non ottimale:
> 	- al processo viene sottratto il processore prima che riesca a computare la risposta, e il tempo di risposta per il processo si allunga
> 	- ![[quanto-robin2.png|300]]
> 	  
> ma:
> - se il quanto è troppo lungo, si rischia di degenerare in FCFS

quindi, quando si sceglie il round robin, è necessario studiare i tempi di risposta e scegliere bene il quanto.

>[!tip] CPU-bound vs IO-bound
>anche il round-robin *favorisce i processi CPU-bound*: il quanto di tempo di un processo viene usato del tutto (o quasi) - mentre i processi I/O-bound ne usano solo la porzione fino alla richiesta di I/O
>
>- soluzione: **round-robin virtuale**
>se un processo fa una richiesta bloccante (es. I/O), quando la richiesta viene esaudita, il processo non va in una coda di ready - ma esiste un'altra coda, la *conda ausiliare*, usata per i processi per i quali una richiesta bloccante è appena stata esaurita. Il dispatcher sceglie quindi prima dalla auxiliary queue (mandando in esecuzione solo per il tempo che rimaneva al quanto di quei processi), e, solo se questa è vuota, passa alla ready queue.

##### shortest process next
- richiede che i processi forniscano la propria *durata*, o che questa venga stimata
- il prossimo processo da mandare in esecuzione è quello più breve = il cui tempo di esecuzione stimato è minore
- senza preemption

![[SPN-es.png|400]]
 
- i processi lunghi potrebbero soffrire di starvation 
- il tempo di esecuzione è stimato, e se viene stimato erroneamente il sistema operativo può abortire il processo

>[!info] come stimare il tempo di esecuzione?
>- in alcuni sistemi ci sono processi che sono eseguiti svariate volte
>- si può usare il passato ($T_{i}$) per predire il futuro ($S_{i}$):
>$$S_{n+1}=\frac{1}{n} \sum_{i=1}^n T_{i}$$
>questa è una media - ma per calcolarla, servirebbe mantenere n valori. ma si può fare anche:
>$$S_{n+1}=\frac{1}{n}T_{n}+\frac{n-1}{n}S_{N}$$
>così basta tenere l'ultimo valore e la stima precedente.
>
>- ma sarebbe meglio far pesare di più le istanze più recenti:
>(se chiamo alpha 1/n noto che:)
>$$S_{n+1} = \alpha \,T_{n}+(1-\alpha )S_{n}, \,\,\,0<\alpha <1$$ 
>e notiamo che è equivalente a:
>$$S_{n+1} = \alpha \,T_{n}+\dots+ \alpha (1-\alpha )^iT_{n-i}+\dots +(1-\alpha )^n S_{1}$$ 
>che è l'*exponential averaging*