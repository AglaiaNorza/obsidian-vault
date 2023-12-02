una funzione ricorsiva è una funzione che chiama se stessa.
si basa su <span style="color:#32a9b8">stack</span> e <span style="color:#32a9b8">queue</span>
##### queue
principio "first in first out"
- enqueue() - come append
- dequeue() - come pop(0)
##### stack
![[Screen Shot 2023-11-28 at 17.45.54.png]]
principio "last in first out"
call_c è la prima ad "uscire", e il risultato viene passato a call_b

in realtà ha una dimensione "limitata" (modificabile), ma per l'uso medio non interessa.

usa:
- push()
- pop()

##### fibonacci
```python
def fibonacci(n):
	if n<2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
```

così però fa molto lavoro - sviluppa ogni sottoalbero prima di tornare indietro.
la sintassi conta per il modo in cui l'albero verrà navigato (sviluppa da sinistra a destra).
### caching/memoization
"taglia" la complessità temporale del programma memorizzando i valori già calcolati.

si aggiunge un attributo alla classe che memorizza i valori.
```python
class Fibo:
	stats = Stats()
	memory = {0:1, 1:1} #aggiungo qui i casi base

	def fibonacci_memo(n):
		Fibo.stats.increment("n_calls")
			
		if n in Fibo.memory:
			return Fibo.memory[n]
			
		else:
		Fibo.stats.increment("n_recursion")
		rez = Fibo.fibonaxxi_memo(n-1) + Fibo.fibonacci_memo(n-2)
		Fibo.memory[n] = rez
		return rez
	
```

fibonacci con for:
```python
def fibonacci_iter(n):
	f = [1,1] + [None] * (n-1)
	for k in range(2, n)
```

# generica per ricorsione

1) **<font color="#31859b">riduzione</font>** del problema
2) **<font color="#31859b">caso base</font>** - esiste un problema (una parte del problema) con soluzione elementare
3) **<font color="#31859b">convergenza</font>** - applicando la riduzione  è sempre possibile arrivare al caso base
4) **<font color="#8064a2">conquer</font>** - unire le soluzioni delle riduzioni per risolvere il problema principale


###### per sommare ricorsivamente all'andata:
ragioniamo in maniera inversa: invece che ridurre, incrementiamo fino ad arrivare alla soluzione

1. incremento i -> i+1
2. finisco quando i= n+1 (convergenza e risultato)
3. in partenza la somma e' 0, ad ogni passo incremento
```python
def sumrp(i, n, partial_sum=0):
    if i == n:
        return partial_sum + n # mi ri
    return sumrp(i+1, n, partial_sum=partial_sum+i)
```

