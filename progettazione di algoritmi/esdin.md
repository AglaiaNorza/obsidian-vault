---
created: 2025-05-08T16:11
updated: 2025-05-08T17:58
---

> [!example] cifre decimali decrescenti
> Dato un intero $n$, vogliamo sapere quante sono le sequenze di cifre decimali non decrescenti lunghe $n$.

- per $n=1$, le cifre sono $10$
- per $n=2$ ⟶ $55$ cifre

Infatti, alla prima cifra $x$ possono seguire $10-x$ cifre diverse. Si ha quindi 
$$
\sum_{x=0}^9(10-x) = \sum_{i=1}^{10} i = \frac{10 \cdot 11}{2}=55
$$

Per risolvere questo problema con la programmazione dinamica non basta una tabella monodimensionale - serve una matrice definita così:
- $T[i][j]=$ numero di sequenze decimali non decrescenti lunghe $i$ che terminano con la cifra $j$

Quindi, la soluzione al problema sarà data dalla somma degli elementi dell'ultima riga.

> [!tip] ragionamento
> Le stringhe lunghe $i$ che terminano con $j$ saranno formate da stringhe lunghe $i-1$ che terminano con qualunque cifra $k\leq j$.

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
Data una matrice quadrata binaria $M$ di dimensione $n\times n$, si vuole sapere, in $O(n^2)$, qual è la dimensione massima per le sottomatrici quadrate di soli uni contenute in $M$.

Si può utilizzare una tabella bidimensionale $n \times n$ dove:
- $T[i][j]=$ il lato della matrice quadrata più grande contenente tutti uni e con cella in basso a destra $M[i][j]$

>[!tip] ragionamento
>Il ragionamento è questo:
>- se $M[i][j]=0$ 

$$
T[i][j] = \begin{cases} 0 & M[i][j]=0 \\
min( T[i][j-1],\,T[i-1][j-1],\,T[i-1][j])+1 & \text{altrimenti}

\end{cases}
$$
### knapsack problem
Dato uno zaino di capacità $c$ ed $n$ oggetti, ognuno con un peso $p_{i}$ e un valore $v_{i}$. Si vuole sapere il valore massimo che si può inserire nello zaino.
- questo problema 