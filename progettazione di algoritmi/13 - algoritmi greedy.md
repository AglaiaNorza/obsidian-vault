---
created: 2025-04-30T17:16
updated: 2025-05-04T18:30
---
> [!info] greedy
> Un algoritmo si dice **greedy** se, ad ogni passaggio, opta per la *soluzione ottimale a livello locale*.

Per analizzare il paradigma greedy, consideriamo un problema chiamato selezione di attività.
### selezione di attività
Abbiamo una lista di $n$ attività da eseguire:
- ciascuna attività è caratterizzata da una coppia $(\text{tempo di inizio, tempo di fine})$
- due attività sono *compatibili* se non si sovrappongono

Si vuole trovare un sottoinsieme massimale di attività compatibili.

>[!example] esempio 
>
>![[greedy-att-es.png|center|450]]

Per usare il paradigma greedy occorre trovare una regola semplice da calcolare che permetta di effettuare ogni volta la scelta giusta.

Ci sono diverse potenziali regole di scelta:
- prendere l'attività compatibile che *inizia prima*
- prendere l'attività compatibile che *dura di meno*
- prendere l'attività compatibile che ha *meno conflitti* con le rimanenti

Ma la regola giusta in questo caso sta nel prendere sempre l'attività compatibile che **finisce prima**.

>[!note] dimostrazione
>Supponiamo per assurdo che la soluzione greedy $SOL$ trovata con questa regola non sia ottima. Le soluzioni ottime differiscono quindi da $SOL$. 
>
>Nel caso ci siano più soluzioni ottime, prendiamo quella che differisce nel minor numero di attività da $SOL$: chiamiamola $SOL^*$. Dimostreremo ora che esiste un'altra soluzione ottima $SOL'$ che differisce ancora di meno da $SOL$, il che è assurdo.
>
>Siano $A_{1},\,A_{2},\,\dots$ le attività nell'ordine in cui sono state selezionate dal greedy. Sia $A_{i}$ la prima attività scelta dal greedy e non dall'ottimo (ce ne deve essere almeno una, perché tutte le attività scartate dal greedy erano incompatibili con quelle già prese e, se la soluzione avesse preso tutte le attività scelte dal greedy, non potrebbe averne prese di più). Nell'ottimo deve esserci un'altra attività $A'$ che va in conflitto con $A_{i}$ (altrimenti $SOL^*$ non sarebbe ottima).
>
>Si può quindi sostituire in $SOL^*$ l'attività $A'$ con l'attività $A_{i}$ senza creare conflitti (perché in base alla regola del greedy, $A_{i}$ termina prima di $A'$, quindi se $A'$ non creava conflitti, neanche $A_{i}$ lo farà). Si ottiene così una soluzione ottima $SOL'$ (le attività in $SOL'$ sono tutte compatibili, e la sua cardinalità è uguale a quella di $SOL^*$). 
>
>Ma $SOL'$ differisce da $SOL$ di un'attività in meno rispetto a $SOL^*$ (abbiamo sostituito un'attività con una di $SOL$)
>
>![[greedy-sol-es.png|center|500]]

#### implementazione
Le idee alla base dell'implementazione sono:
- ordinare le attività in `lista` per tempo di fine crescente - si paga $O(n \log n)$ per l'ordinamento, ma ogni estrazione costerà $\Theta(1)$ (invece di $O(n)$ necessario per cercare l'attività che finisce prima)
- per controllare se le attività vanno in conflitto, conviene mantenere una variabile con il tempo di fine dell'ultima attività inserita 

```python
def selezione_a(lista):
	lista.sort(key = lambda x : x[1])
	libero = 0
	sol = []
	for inizio, fine in lista:
		if libero < inizio:
			sol.append((inizio, fine))
			libero = fine
	return sol
```

### assegnazione di attività
Abbiamo una lista di attività, ciascuna caratterizzata da un tempo di inizio e un tempo di fine. Le attività vanno eseguite tutte, e si vuole assegnare il minor numero di aule tenendo conto del fatto che in una stessa aula non possono eseguirsi più attività in parallelo.

>[!bug] possibile soluzione greedy (errata)
>Un possibile algoritmo greedy si basa sull'idea di occupare aule finché ci sono attività da assegnare, assegnando ad ogni aula inaugurata il maggior numero di attività non ancora assegnate che è in grado di contenere.
>
>Ma non è una soluzione ottima. Per esempio, nel caso di `lista = [(1,4), (1,6), (7,8), (5,10)]`, propone una soluzione che utilizza tre aule, mentre la soluzione ottima ne utilizza 2:
>
>![[att-es-1.png|center|400]]

La soluzione corretta consiste invece nel selezionare ogni volta l'attività che **inizia prima**: se può essere posizionata in un'aula già esistente, gliela si assegna, altrimenti si alloca una nuova aula.

>[!note] dimostrazione di correttezza
>Sia $k$ il numero di aule utilizzate dalla soluzione. Fremo vedere che nella lista ci sono $k$ attività incompatibili a coppie, ovvero che si sovrappongono nel tempo (il che implica che sono necessarie $k$ aule).
>
>- Sia $(a,b)$ l’attività che ha portato all’introduzione nella soluzione della $k$-esima aula. 
>
>In quel momento, tutte le $k-1$ aule precedentemente allocate erano occupate da attività che si sovrappongono temporalmente con $(a,b)$ (nessuna era ancora terminata all’istante $a$ in cui inizia l’attività $(a,b)$). Poiché l’algoritmo sceglie le attività in ordine di inizio e assegna aule solo se necessario, significa che al tempo $a$ le $k-1$ aule erano tutte occupate.
>
>Quindi, le $k$ attività (le $k+1$ e $a$) sono a due a due incompatibili, perché tutte risultano "attive" nello stesso istante. Quindi, qualsiasi soluzione valida deve usare almeno $k$ aule. La soluzione greedy ne usa esattamente $k$ ed è quindi ottima.

#### implementazione
- per individuare in maniera efficiente l'attività che inizia prima, si effettua un pre-processing in cui si ordinano le attività per tempo di inizio.
- per individuare efficientemente (in $O(1)$) quale aula si liberi prima, si costruisce un *heap minimo* con le coppie $(\text{libera},\,i)$ dove $\text{libera}$ indica il tempo in cui si libera l'aula $i$ 
- se l'attività può essere eseguita nell'aula che si libera prima, allora bisogna assegnargliela e aggiornare il valore $\text{libera}$ della coppia che rappresenta l'aula nella heap; se invece l'attività non può essere eseguita in quell'aula, allora non saraà possibile farlo in nessuna delle altre: bisognerà allocare una nuova aula ed inserirla nella heap.
	- inserimenti, estrazioni e cancellazioni in una heap costano $O(\log n)$

```python
def assegnazioneAule(lista):
	from heapq import heappop, heappush
	f = [[]]
	H = [(0,0)]
	lista.sort()
	
	for inizio, fine in lista:
		libera, aula = H[0]
		if libera<inizio:
			f[aula].append((inizio, fine))
			heappop(H)
			heappush(H, (fine, aula))
		else:
			f.append([(inizio, fine)])
			heappush(H, (fine, len(f)-1))
	return f
```

- ordinare la lista costa $\Theta(n \log n)$
- il `for` viene eseguito $n$ volte e, al suo interno, nel caso peggiore può essere eseguita un'estrazione da heap seguita da un inserimento (entrambe di costo $O(\log n)$); il `for` costerà quindi $O(n \log n)$

La complessità dell'algoritmo è $\Theta(n \log n)$.
### file su disco
Abbiamo $n$ file di dimensioni $d_{0},\,d_{1},\,\,\dots,\, d_{n-1}$ che vogliamo memorizzare su un disco di capacità $k$. Tuttavia, la somma delle dimensioni di questi file eccede la capacità del disco. Si vuole selezionare un sottoinsieme dei file che abbia *cardinalità massima* e che possa essere memorizzato sul disco.

- un algoritmo greedy per questo problema è questo: si considerano i file per *dimensione crescente* e, se c'è spazio per memorizzare un file su disco, lo si memorizza.

>[!note] dimostrazione di correttezza
>Assumiamo per assurdo che la soluzione $sol$ prodotta dal greedy non sia ottima. Devono quindi esistere insiemi con più file di $sol$ che rispettano la capacità del disco.
>
>Tra questi insiemi, prendiamo quello con più elementi in comune con $sol$: chiamiamolo $sol^*$.
>
>- Esiste necessariamente un file $a$ che appartiene a $sol^*$ e non a $sol$ e occupa più spazio di qualunque file in $sol$ (per il criterio di scelta greedy, tutti gli elementi in $sol$ occupano meno spazio di quelli non presenti). 
>- Esiste necessariamente anche un file $b$ che appartiene a $sol$ e non a $sol^*$ (perché $sol \not\subset sol^*$ - l'aggiunta di un qualsiasi elemento a $sol$ porterebbe a superare la capacità del disco)
>
>Possiamo quindi eliminare da $sol^*$ il file $a$ e inserire il file $b$ (che ha quindi dimensione $\leq a)$ ottenendo un nuovo insieme di file che rispetta ancora le capacità del disco ed ha un elemento in più in comune con sol, contraddicendo l'ipotesi per cui $sol^*$ è quello con più elementi in comune con $sol$.

```python
def file(D, k):
	n = len(D)
	lista = [(D[i], i) for i in range(n)]
	lista.sort()
	spazio, sol = []

	for p, i in lista:
		if spazio + p <= k:
			sol.append(i)
			spazio += d
		else:
			return sol 
```

Questo algoritmo ha complessità $O(n+m)$ (causata dal `sort()`).