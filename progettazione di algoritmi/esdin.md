---
created: 2025-05-08T16:11
updated: 2025-05-17T08:25
---
> [!example] cifre decimali decrescenti
> Dato un intero $n$, vogliamo sapere, in $O(n)$, quante sono le sequenze di cifre decimali non decrescenti lunghe $n$.

- per $n=1$, le cifre sono $10$
- per $n=2$ ⟶ $55$ cifre

Infatti, alla prima cifra $x$ possono seguire $10-x$ cifre diverse. Si ha quindi 
$$
\sum_{x=0}^9(10-x) = \sum_{i=1}^{10} i = \frac{10 \cdot 11}{2}=55
$$
> [!tip] ragionamento
> Visto che dobbiamo considerare il constraint della non-decrescenza, dobbiamo tenere a mente non solo la lunghezza delle sequenze, ma anche con che numero terminano (per poter determinare se un numero possa essere aggiunto alla sequenza o no).
>
> Sappiamo infatti che le stringhe lunghe $i$ che terminano con $j$ saranno formate da stringhe lunghe $i-1$ che terminano con qualunque cifra $k\leq j$ (a cui verrà aggiunto $j$).
> 

 Utilizziamo quindi una matrice definita così:
- $T[i][j]=$ numero di sequenze decimali non decrescenti lunghe $i$ che terminano con la cifra $j$

La soluzione al problema sarà data quindi dalla somma degli elementi dell'ultima riga <small>(sequenze non decrescenti lunghe $n$ che terminano con tutte le cifre possibili)</small>

- il caso base è dato dalle sequenze lunghe $1$ - ogni sequenza lunga $1$ è infatti decrescente

La regola ricorsiva è quindi:

$$
T[i][j] = \begin{cases} 1 & i=1 \\
\sum_{k=0}^j T[i-1][k]& \text{altrimenti}
\end{cases} 
$$

**implementazione**:
```python
def es(n):
	T = [[0]*10 for _ in range(n+1)]
	for j in range(10):
		T[1][j] = 1
	for i in range(2, n+1):
		for j in range(10):
			for k in range(j+1):
				T[i][j] += T[i-1][k]
	return sum(T[n])
```

- inizializzare la tabella costa $\Theta(n)$ (ha $n+1$ righe e $10$ colonne)
- dei 3 `for` annidati:
	- il primo viene iterato $n$ volte
	- il secondo viene iterato $10$ volte
	- il terzo viene iterato al più $10$ volte
- il costo totale dei for è $\Theta(n)$

### matrici
Data una matrice $M$ binaria $n \times n$, si vuole verificare, in $\Theta(n)$, se è possibile raggiungere la cella in basso a destra partendo da quella in alto a sinistra senza mai toccare celle che contengono i numero $1$.
- ad ogni passo ci si può spostare solo di un passo verso destra o un passo verso il basso

>[!tip] ragionamento
>- la cella $M[0][0]$ è raggiungibile
>- se $M[i][j]=1$, non è raggiungibile
>
>Assumendo che $M[i][j]=0$,
>- una cella della prima riga può essere raggiunta solo dalla cella che la precede (non ha una cella sopra di sé)
>- una cella della prima colonna può essere raggiunta solo dalla cella che sopra di sé sulla colonna (non ha una cella alla sua sinistra)
>- una cella "interna" è raggiungibile se può essere raggiunta dalla cella che la precede o dalla cella sopra di sé

La ricorrenza sarà quindi

$$
T[i][j] = \begin{cases} False & M[i][j] = 1 \\
True & i=j=0 \\
T[i][j-1] & i =  0 \\
T[i-1][j] & j=0 \\
T[i][j-1] \;\;or\;\; T[i-1][j] & \text{altrimenti}
\end{cases}
$$

### sottomatrici di soli uni

> [!example] testo
> Data una matrice quadrata binaria $M$ di dimensione $n\times n$, si vuole sapere, in $O(n^2)$, qual è la dimensione massima per le sottomatrici quadrate di soli uni contenute in $M$.

Si può utilizzare una tabella bidimensionale $n \times n$ dove:
- $T[i][j]=$ il lato della matrice quadrata più grande contenente tutti uni e con cella in basso a destra $M[i][j]$

>[!tip] ragionamento
>Il ragionamento è questo:
>- se $M[i][j]=0$, $T[i][j]=0$
>- altrimenti, per avere un quadrato di dimensione $k$, gli elementi della matrice $T[i-1][j]$, $T[i-1][j-1]$ e $T[i][j-1]$ <small>(sopra, diagonale, sinistra)</small> dovranno a loro volta essere gli angoli di un quadrato di dimensione almeno $k-1$
>
>Si può osservare in questo caso:
>
> $$
> \begin{array}{ccccc}
> \textcolor{Goldenrod}{1} & \textcolor{Goldenrod}{1} & \textcolor{red}{1} & 1 & 1 \\
> \textcolor{Goldenrod}{1} & \textcolor{orange}{1} & \textcolor{red}{1} & 1 & 1 \\
> \textcolor{red}{1} & \textcolor{red}{1} & \textcolor{Peach}{1} & 0 & 1 \\
> 1 & 1 & 1 & 1 & 1 \\
> 1 & 1 & 0 & 1 & 1 \\
> \end{array}
> $$
> 
> - per il primo quadrato (giallo, che termina in $[1][1]$), è abbastanza evidente: le celle che lo circondano formano quadrati $1 \times 1$
> - ma si nota anche per $[2][2]$ (rosso): infatti, ai tre quadrati $2\times 2$ formati dalle celle circostanti manca esattamente l'ultima cella per diventare un unico quadrato $3 \times 3$

La ricorrenza è quindi:
$$
T[i][j] = \begin{cases} 0 & M[i][j]=0 \\
1 & i  = 0 \lor j=0 \\
min( T[i][j-1],\,T[i-1][j-1],\,T[i-1][j])+1 & \text{altrimenti} 

\end{cases}
$$

(si prende il minimo lato perché, per poter "fondere" i tre quadrati che terminano in quelle tre celle, essi devono essere della stessa dimensione: se si prendesse il massimo, uno degli altri due quadrati potrebbe essere più piccolo e la figura risultante non sarebbe un quadrato - il minimo, invece, li "copre" sicuramente tutti e tre)

**implementazione**:
```python
def sottomatrice(M):
	T = [[0]*n for _ in range(n)]
	T[0][0] = M[0][0]
	for i in range(1,n):
		for j in range(1, n):
			if M[i][j] == 0:
				T[i][j] = 0
			

```

### knapsack problem
Dato uno zaino di capacità $c$ ed $n$ oggetti, ognuno con un peso $p_{i}$ e un valore $v_{i}$. Si vuole sapere il valore massimo che si può inserire nello zaino.
- questo problema 