Un algoritmo si dice **efficiente** se la sua complessità è di ordine *polinomiale* nella dimensione $n$ dell’output, ovvero se è di complessità $O(n^c)$ per una qualche costante $c$.

Un algoritmo è inefficiente se la sua complessità è di ordine superpolinomiale:
- *esponenziale* -→ $\Theta(c^n)=2^{\Theta(n)}$
- *super-esponenziale* -→ cresce più velocemente di un esponenziale
	- per esempio $2^{\Theta(n^2)}$ o anche $2^{\Theta(n \log n)}$
- *sub-esponenziale* -→ cresce più lentamente di un esponenziale: $2^{o(n)}$ 
	- per esempio: $n^{\Theta(\log n)}=2^{\Theta(\log^2 n)}$

> Problemi di cui si conoscono algoritmi subesponenziali e non polinomiali sono pochi e proprio per questo molto studiati.
