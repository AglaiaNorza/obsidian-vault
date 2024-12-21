>[!info] lock
>Il **lock** è il privilegio di accesso ad un singolo item, realizzato tramite una variabile associata all'item (*variabile lucchetto*), il cui valore descrive lo stato dell'item rispetto alle operazioni che possono essere effettuate su di esso.

(nella sua forma più semplice) un lock:
- viene **richiesto** da una transazione (`locking`) - se il valore è `unlocked`, la transazione può accedere all'item e alla variabile viene assegnato il valore `locked`
- viene **rilasciato** da una transazione (`unlocking`) - assegna alla variabile il valore `unlocked`

quindi
- tra l'esecuzione di un'operazione di locking su un item e un'operazione di unlocking sullo stesso item, si dice che la transazione *mantiene un lock* sull'item
- il locking agisce come *primitiva di sincronizzazione* (se una transazione richiede un lock su un item su cui un'altra transazione mantiene un lock, non può passare finché il lock non viene rilasciato).

## schedule legale
Uno schedule è detto **legale** se:
- una transazione effettua un locking ogni volta che deve leggere o scrivere un item
- ciascuna transazione rilascia ogni lock che ha ottenuto

## lock binario
Un lock binario può assumere solo due valori: `locked` e `unlocked`.

Le transazioni fanno uso di due operazioni:
- `lock(X)` per richiedere accesso all'item`X`
- `unlock(X)` per rilasciare l'item `X`

### vantaggi
Attraverso il lock binario risolviamo il primo dei problemi visti: la *perdita di aggiornamento* (ghost/lost update).

>[!example]- esempio 
>![[lock-binario-es1.png|center|350]]
>![[lock-binario-es2.png|center|350]]
>
>- grazie al locking, $T_{2}$ non riesce a leggere $X$ fino a quando $T_{1}$ non ha finito di scriverla, e non si perde quindi il suo aggiornamento

### equivalenza, serializzabilità
La proprietà di equivalenza degli schedule dipende dal protocollo di locking adottato - vediamo il caso del locking binario.
- serve adottare un modello di transazioni che *sia astragga dalle specifiche operazioni* e si basi su quelle rilevanti, per valutare le *sequenze degli accessi* (lock e unlock)

Una transazione viene quindi interpretata come sequenza di `lock` e `unlock`:
- ogni `lock(X)` implica la lettura di `X`
- ogni `unlock(X)` implica la scrittura di `X`

<small>(tutto quello che succede in mezzo non ci interessa)</small>

![[trans-lockb.png|center|200]]

- in corrispondenza di una scrittura, viene associato un nuovo valore all'item coinvolto, calcolato da una **funzione**, associata in modo univoco ad una coppia lock-unlock
	- questa fuzione ha per argomenti **tutti** gli item letti prima dell'unlock corrente, con il **valore che avevano quando sono stati letti**.

>[!info] equivalenza
>Due schedule si definiscono quindi equivalenti se le formule che danno i valori finali per ciascun item sono le stesse.
>- devono essere uguali, per ogni item, a quelle di almeno uno schedule seriale

>[!summary] serializzabilità
>Uno schedule è **serializzabile** se è equivalente ad uno schedule seriale (come già visto)

>[!example]- esempio
>![[attachments/lockbin-funz-es.PNG|center|350]]
>
>i possibili schedule seriali sono:
>![[es-scheduleseriale1.png|center|300]]
>![[es-scheduleseriale2.png|center|300]]
>
>lo schedule è quindi *non serializzabile*, in quanto produce un valore di $X$ ($f_{4}(f_{1}(X_{0}),\,Y_{0})$) diverso da quello prodotto dai due possibili schedule seriali.
> 
>(lo stesso vale per $Y$)

- basta quindi che le formule siano diverse *anche su un solo item* perché gli schedule non siano equivalenti
	- quindi, per provare che uno schedule non è serializzabile, basta fermarsi appena troviamo un item che ha formule diverse

### testare la serializzabilità
Uno schedule è serializzabile se esiste uno schedule seriale tale che per ogni item, l'ordine in cui le varie transazioni fanno un lock coincide con quello dello schedule seriale.

Esiste un algoritmo per testarla:

**passo 1**
- creare un grafo diretto $G$ formato da:
	- *nodi*: transazioni
	- *archi*: $T_{i}\to T_{j}$ (con etichetta $X$) se $T_{i}$ esegue un `unlock(X)` e $T_{j}$ esegue il SUCCESSIVO `lock(X)` 

![[grafo-serializ.png|center|300]]

**passo 2**
- se $G$ ha un ciclo, allora *non è serializzabile*
- altrimenti, applicando l'ordinamento topologico, si ottiene uno schedule seriale $S'$ equivalente a $S$ (l'ordine di cancellazione dei nodi corrisponde allo schedule seriale)

>[!info] ordinamento topologico
>Si ottiene eliminando ricorsivamente un nodo che non ha archi entranti (e i suoi archi uscenti).
>- c'è più di un ordinamento topologico (ci sono diversi path che posso prendere, in base a quale nodo senza archi entranti decido di eliminare per primo)

![[ord-topologico.png|center|350]]


> [!info] teorema: correttezza dell'algoritmo
> Uno schedule $S$ è serializzabile se e solo se il suo grafo di serializzazione è aciclico.



