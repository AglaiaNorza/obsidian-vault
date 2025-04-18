---
created: 2025-04-01
updated: 2025-04-18T17:45
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
>Si può quindi sostituire in $SOL^*$ l'attività $A'$ con l'attività $A_{i}$ senza creare conflitti (perché in base alla regola del greedy, $A_{i}$ termina prima di $A'$, quindi se $A'$ non creava conflitti, neanche $A^i$ lo farà). Si ottiene così una soluzione ottima $SOL'$ (le attività in $SOL'$ sono tutte compatibili, e la sua cardinalità è uguale a quella di $SOL^*$). 
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
>
