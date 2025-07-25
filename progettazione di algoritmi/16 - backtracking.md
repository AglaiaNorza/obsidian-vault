---
{}
---
>[!info] backtracking
>Il **backtracking** è una tecnica algoritmica utilizzata tipicamente per risolvere problemi in cui devono essere soddisfatti dei vincoli. Costruisce progressivamente una soluzione, scartando i percorsi che violano i vincoli e tornando indietro quando una scelta porta a un vicolo cieco o quando una soluzione parziale è stata completata.
>- il backtracking ha una complessità esponenziale, quindi è poco efficiente nell'affrontare problemi che non siano NP-completi [[15 - programmazione dinamica#problema dei file su disco|(problemi NP-completi)]]

Un algoritmo di backtracking userà quindi una *funzione di taglio* (che verifica una certa condizione prima di effetuare alcune scelte) per evitare le chiamate ricorsive non necessarie, "potando" quindi l'albero di ricorsione.
## calcolare la complessità
Si consideri un algoritmo di enumerazione basato sul backtracking dove l'albero di ricorsione ha **altezza** $h$, il **costo di una foglia** è $g(n)$ e il **costo di un nodo interno** è $O(f(n))$.

Sappiamo, per come funziona il backtracking, che *un nodo viene generato solo se ha la possibilità di portare ad una foglia da stampare*.

Quindi:
- si generano solo le foglie che vanno stampate, quindi il costo totale dei **nodi foglia** è $O(S(n) \cdot g(n))$ 
- i **nodi interni** che verranno generati saranno $O(S(n) \cdot h)$, in quanto ogni nodo interno generato apparterrà ad un cammino che parte dalla radice ed arriva ad una delle $S(n)$ foglie da enumerare (non si generano nodi che portano a "vicoli ciechi")

La complessità totale sarà quindi:
$$O(S(n)\cdot h \cdot f(n) + S(n) \cdot g(n))$$
## esercizi
### stringhe binarie

> [!example] stringhe binarie (senza vincoli)
> Dato un parametro intero $n$, stampare tutte le stringhe binarie lunghe $n$.

> [!tip] osservazioni
> - le stringhe da stampare sono $2^n$
> - stampare una stringa lunga $n$ costa $\Theta(n)$
> 
> quindi, il meglio che ci si può aspettare da un algoritmo è $\Omega (2^n\cdot n)$

```python
def strbin(n, sol = []):
	if len(sol) == n:
		print(''.join(sol))
		return
		
	sol.append('0')
	strbin(n, sol)
	sol.pop()
	
	sol.append('1')
	strbin(n, sol)
	sol.pop()
```

- questo algoritmo genera un albero di chiamate ricorsive alto $n$
- l'albero ha quindi $\sum_{i=o}^h 2^i=2^{h+1}-1$ nodi, che $\in \Theta(2^n)$
- ogni nodo esegue solo operazioni in $\Theta(1)$, tranne per il `print()`, che costa $\Theta(n)$ e viene eseguito solo dalle foglie 

quindi, i nodi interni lavorano per $\Theta(1) \cdot \Theta(2^n) = \Theta(2^n)$, mentre i nodi foglia per $2^n \cdot \Theta(n)$, per un totale di:

$$
\Theta(2^n) + 2^n \cdot \Theta(n) = \Theta(2^n \cdot n)
$$

> [!example] vincolo sugli zeri
> Si vogliono stampare solo le stringhe che contengono massimo $k$ uni, con $k\leq n$.

>[!error] soluzione ottimizzabile
>Una soluzione in $\Theta(2^n \cdot n)$ è quella per cui si creano tutte le stringhe, ma si stampano solo quelle ammissibili:
> ```python
> def strbinkLame(n, k, tot1 = 0, sol = []):
> 	if len(sol) == n:
> 		if sol.count('1') <= k:
> 			print(''.join(sol))
> 	return
> 	
> 	sol.append('0')
> 	strbinkLame(n, k, tot1, sol)
> 	sol.pop()
> 	sol.append('1')
> 	bk2(n, k, tot1+1, sol)
> 	sol.pop()
> ```
> - questo algoritmo non è però ottimale: infatti, è inutile generare nell'albero di ricorsione nodi che non possono portare a soluzioni (foglie) da stampare.

Con la tecnica del backtracking, si può risolvere questo problema: si implementa un **controllo** sul numero di uni presenti nella stringa composta fino a quel momento, e si verifica se se ne possano aggiungere altri.

```python
def strbink(n, k, tot1 = 0, sol = []):
	if len(sol) == n:
		print(''.join(sol))
	return
	
	sol.append('0')
	strbink(n, k, tot1, sol)
	sol.pop()
	 
	if tot1 < k:
		sol.append('1')
		bk2(n, k, tot1+1, sol)
		sol.pop()
```

- uno `0` si può sempre aggiungere (non ci sono vincoli sugli zeri)
- un  `1` si può aggiungere solo se non si è ancora raggiunto il numero massimo (`k`)

Grazie a questa **funzione di taglio**, le chiamate ricorsive sono ridotte e l'algoritmo risulta molto più efficiente.

### matrici binarie

> [!example] matrici binarie
> Progettare un algoritmo che prende come parametro un intero $n$ e stampa tutte le matrici binarie $n \times n$.

- le matrici binarie lunghe $n$ sono $2^{n^2}$

Invece di gestire la matrice con `append()` e `pop()` come faremmo con una stringa, conviene crearla e gestirla andando avanti e indietro con gli indici.

```python
def printmatr(n, sol, i=0, j=0):
	if i == n: # saremmo ad una riga n+1 che non esiste
		for row in sol:
			print(row)
		print()
		return
		
	i1, j1 = i, j+1
	
	if j1 == n: # prossima riga
		i1, j1 = i+1, 0
		
	sol[i][j] = 0
	es1(n, sol, i1, j1)
	
	sol[i][j] = 1
	es1(n, sol, i1, j)

def matrbin():
	sol = [[0]*n for _ in range(n)]
	printmatr(n, sol)
```

- l'albero di ricorsione generato da questo algoritmo è binario di altezza $n^2$, e ha quindi $2^{n^2}-1$  nodi interni e $2^{n^2}$ foglie.
- ciascun nodo interno richiede $O(1)$ e ciascuna foglia $O(n^2)$

L'algoritmo ha quindi complessità $O(2^{n^2}n^2)$.
- poiché le matrici da stampare sono $2^{n^2}$ e la stampa di una matrice richiede $\Theta(n^2)$, l'algoritmo è ottimo.

### partizioni (senza ordine)

> [!example] partizioni
> Dato un numero intero positivo $n$, definiamo come partizioni di tutte le sequenze di elementi inferiori o uguali ad $n$ la cui somma è esattamente $n$. Vogliamo stampare solo quelle senza ordine (ovvero, se per esempio $n=4$, se stampiamo $2,\,1,\,1$, non dobbiamo stampare anche $1,\,2,\,1$).

```python
def partizioni(n, l, s=0):
    if s == n:
        print(l)
        return

    # ordine decrescente
    # se la lista è vuota, scelgo n come primo elemento
    last = l[-1] if l else n 
    
    for i in range(last, 0, -1):
        if s + i <= n: # se si può aggiungere
            l.append(i)
            partizioni(n,l,s+i)
            l.pop()

l = []
partizioni(n, l)
```

- con `for i in range(last, 0, -1)` faccio sì che ogni numero che viene aggiunto sia minore o uguale al precedente, così da forzare un ordine decrescente (eliminando i duplicati con la stessa somma ma diverso ordine)
