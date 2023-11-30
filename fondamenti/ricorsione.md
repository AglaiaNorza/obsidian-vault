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

1) riduzione del problema
2) caso base - esiste un problema (una parte del problema) con soluzione elementare
3) convergenza - applicando la riduzione  è sempre possibile arrivare al caso base
4) conquer - unire le soluzioni delle riduzioni per risolvere il problema principale



