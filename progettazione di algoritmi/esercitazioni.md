---
{}
---
### spessore di un sottovettore
> [!example] spessore di un sottovettore (es. 6 pdf divide et impera)
> In un vettore $V$ di interi, si dice **spessore** del vettore la differenza tra il massimo e il minimo del vettore. Progettare un algoritmo che, preso un vettore $V$ di $n$ interi ed un intero $C$, trovi un sottovettore (una sequenza di elementi consecutivi del vettore) di lunghezza massima tra quelli di spessore al più $C$. La complessità dell’algoritmo deve essere $O(n \log n)$.
> 

- quindi, dato un sottovettore $v[i,j)$, definiamo $\text{spessore}(v[i,j)=max(v[i,j)) - min(v[i,j))$

>[!bug] soluzione in $O(n^2)$
> Una soluzione naïf consiste nel controllare tutti i sottovettori (il che richiederebbe $O(n^3)$), ma può essere ottimizzata se si considera una proprietà:
> - se ho due sottovettori $v[i,\,j)$ e $v[i,\,j+1)$ e conosco il massimo del primo, non mi serve ricontrollare tutto il secondo vettore ⟶ il massimo sarà dato da $max(max(v[i,\,j), v[j+1])$  <small>(tra il massimo che conosciamo già e il nuovo elemento)</small>
> 
> In più, so anche che lo spessore segue il *principio di monotonia*, ovvero che:
> 
> $$\begin{align*}
> [i,j) \subseteq[i',\,j']\implies spess(v[i,j))\leq spess(v[i',\,j'))
> \end{align*}$$
> 
> Infatti, si ha 
>  
 > $$\begin{align*}
 > max(v[i,j))-min(v[i,j)) \leq max(v[i',j'))-min(v[i,j)) \leq max(v[i',j'))-min(v[i',j'))=spess(v[i',j'))
\end{align*}$$
> - $max(v[i,j))-min(v[i,j)) \leq max(v[i',j'))-min(v[i,j))$ perché, 

- un sottovettore di lunghezza 1 ha spessore 0
- $i=0,\,j=1$ ⟶ $spess=0$
- se lo spessore è minore di c, allargo (a destra), se è maggiore di c, stringo da sinistra
- (assumiamo che c sia positivo, quindi la massima lunghezza ha come minimo 1)

```python
maxS = v[0]; minS = v[0]
spess = 0
i = 0; j =  1
maxL = 0; maxi = 0; maxj = 1
# ccontrolla se devi mettere n-1 per evitare out of bounds (v[n] non esiste)
while j < n:
	if spess < c:
		j += 1
		maxS = max(maxS, v[j])
		minS = min(minS, v[j])
		spess = maxS - minS
		if spess < c and j-i > maxL:
			maxL = j-i
			maxi, maxj = i, j
	
	else:
		i += 1
		maxS = max(v[i:j]) # Theta(n)
		minS = min(v[i:j]) 
		spess = maxS - minS
```

questo algoritmo ha complessità $O(n^2)$

Utilizzando maxheap e minheap, si potrebbero estrarre massimi e minimi in log n. 

Ma noi vogliamo usare il divide et impera !
Dato un segmento da $inf$ a $sup$,, lo divido a metà e risolvo i sottoproblemi dati dalle due metà
- il caso base è quello con un sottosegmento di lunghezza 1: lo spessore è 0

ci saranno $spess(v[l_{1},\,r_{1}))<c$ e [ stessa cosa con l2 r2 ]

- in questo caso, basterebbe prendere il massimo tra gli spessori dei segmenti destro e sinistro
- ma se il più grande segmento si trova a cavallo ? (ovvero, se include l'indice $m$ (punto medio))

Per ottenere una ricorrenza in n log n, il tempo di combinazione deve essere $n$
T(n) = 2T(n/2) + ?
con ? = Theta(n)

Questo problema è semplificato dal fatto che il segmento deve passare per $m$

- è quindi un segmento della forma $v[l,m)\cup v[m,\,r)]$
- se conosco i massimi e minimi dei due intervalli, lo spessore è dato dalla differenza tra il massimo tra i massimi e il minimo tra i due minimi
- in n, posso calcolarmi tutti gli spessori di tutti gli intervalli del tipo $l,m$ 
- mi conviene calcolare (e tenere da parte) non lo spessore, ma il vettore dei massimi e dei minimi a partire da 

il candidato deve avere un estremo a sinistra di $m$ e uno a destra

quindi fisso  r = m e l = inf


- parto dall'ultimo ad essere più piccolo di c per ottimizzare
- parte da m ?? m+1 da destra e inf a sinistra, e sposta la finestra



```python
l = inf; r = m; spess = max((maxL(inf), maxR(m))) - min(minL(inf), minL(sup)))
while l < m and r < sup:
	if spess < c:
		r += 1
	else :
		l+=1
	spess = riaggiorna_spessore()
```

### massimo insieme indipendente
dato un grafo $G=(V,E)$, un insieme $U\subseteq V$ è indipendente se, $\forall u,\,v\in U,\,(u,v)\not\in E$

NP completo !

vediamo il caso particolare in cui $G$ è un albero (connesso e aciclico)

algoritmo greedy
- prendiamo tutte le foglie (sicuramente indipendenti tra loro)
- poto l'albero (dai padri delle foglie)
- prendo le foglie

Dimostrazione:
- ha cardinalità massima

è l'unione tra indipendenti di V1 e V2 
v1 è indipendente da v2 per costruzione (non avrà elementi adiacenti alle fogli)

V* è V1* + V2* 

---
Date due sequenze $X=x_{1},\,x_{2}\dots,\,x_{n}$, $Y=y_{1},\,y_{2},\,\dots,\,y_{m}$, trovare la minima sequenza $Z$ che ha come sottosequenze $Y$ e $X$.

alberi
libri

alberilibri
allibberrii

aliberi

(stesso ordine ma non consecutive)

Osserviamo prima la versione ricorsiva e successivamente deriviamo da essa la versione iterativa.






Per ottimizzare la soluzione

```python
def superSeqR(X, i, Y, j):
	if i == len(X): return len(Y)-j-1, y[j:] 
	if j == len(Y): return len(X)-i-1, x[i:]

	if X[i] == Y[j]:
		l, s = superSeqR(X, i+1, Y, j+1)
		return l+1, x[i] + s
		
	lx, sx = superSeqR(X, i+1, Y, j)
	ly, sy = superSeqR(X, i, Y, j+1)

	if lx < ly:
		return lx + 1, x[i]+sx
	return ly + 1, y[j]+sy
```


in cui 
- $L[i][j]$ = lunghezza della supersequenza minima tra $x[i:]$ e $y[j:]$

Con casi base:
- $L[m-1][n-1]=0$
- $L[i][m-1]=m-i-1$
- $L[m-1][j]=n-j-1$

```python
def superSeqR(X, i, Y, j, T):
	if L[i][j] == -1:
		if X[i] == Y[j]:
			T[i][j] = superSeqR(X, i+1, Y, j+;1, T) + 1
		else:
			T[i][j] = 1 
				+ min(superSeqR(X, i+1, Y, j, T), superSeqR(X, i, Y, j+1, T))
	return T[i][j]
```

- il risultato si troverà in $T[0][0]$

