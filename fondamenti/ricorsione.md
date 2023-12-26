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

fibonacci con for:
```python
def fibonacci_iter(n):
	f = [1,1] + [None] * (n-1)
	for k in range(2, n)
```

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
# generica per ricorsione

 1) **<font color="#31859b">riduzione</font>** del problema
 2) **<font color="#31859b">caso base</font>** - esiste un problema (una parte del problema) con soluzione elementare
 3) **<font color="#31859b">convergenza</font>** - applicando la riduzione  è sempre possibile arrivare al caso base
 4) **<font color="#8064a2">conquer</font>** - unire le soluzioni delle riduzioni per risolvere il problema principale


##### sommare ricorsivamente all'andata:
ragioniamo in maniera inversa: invece che ridurre, incrementiamo fino ad arrivare alla soluzione

1. incremento i -> i+1
2. finisco quando i= n+1 (convergenza e risultato)
3. in partenza la somma e' 0, ad ogni passo incremento
```python
def sumrp(i, n, partial_sum=0):
    if i == n:
        return partial_sum + n 
    return sumrp(i+1, n, partial_sum=partial_sum+i)
```

### ricorsione sugli alberi
[[alberi]]

in maniera ricorsiva, dobbiamo aprire tutte le directory e "vedere" tutti i file.
###### esempio: trovare file con una certa estensione in una directory 
- serve il modulo os (per cartelle/sottocartelle/file)
	- os.listdir(cartella) dà tutti i file presenti nella cartella 
- il path assoluto si trova con:
```python
f'{folder}/{fname}'
#che sarebbe:
folder + "/" + fname
#oppure:
os.path.join(folder, fname)
```
- stringa.endswith(end) - controlla se una stringa finisce in un certo modo

```python
import os

def find_file_with_ext(folder, ext):
	rez = [] #lista che conterrà i risultati

	#si fa un for su quanti items abbiamo, e per ogni item,
	#se è un file okay, sennò richiamiamo la funzione
	#con quella directory invece di quella iniziale

	for fname in os.listdir(folder):
		#ricalcolo il percorso assoluto
		full_path = f'{folder}/{fname}'
		#full path può essere un file o una directory

		if os.path.isfile(full_path):
		
			if fname.endswith(ext):
				rez.append(full_path)
				#se è un file e finisce con 
				#l'estensione che voglio, lo aggiungo
		else:
			#se è una directory: vado in ricorsione
			L_files = find_file_with_ext(full_path, ext)
			#L_files sarà la lista di file in quella
			#directory che finiscono con l'ext richiesta
			#(perché la funzione ritorna una lista

			rez = rez + L_files

	return rez
```

la parte ricorsiva è difficile perché, quando stiamo scrivendo la parte ricorsiva ("else"), non abbiamo ancora scritto il return (quindi dobbiamo immaginare che la funzione restituirà la lista con i path dei file con estensione ext *in quella directory*).

###### ritornare un dizionario con chiave percorso e valore dimensione del file
- serve os per trovare la dimensione del file: 
	- os.stat(file).st_size 

```python
import os

def find_file_with_ext(folder, ext):
	rez = {} 
	
	for fname in os.listdir(folder):
		full_path = f'{folder}/{fname}'

		if os.path.isfile(full_path):
		
			if fname.endswith(ext):
				rez[fullpath] = os.stat(full_path).st_size 

		else:
			D_files = find_file_with_ext(full_path, ext)
			
			rez.update(D_files)
			#oppure, con unpack:
			# rez = {**rez, **D_files}
	return rez
```

#### search orders
**pre-order**:
ricerca prima se stesso, poi tutti quelli a sinistra e poi tutti quelli a destra
```python
def find_pre(self, f_value):
	if self.value == value:
		return True
		
	elif self.sx and find_pre(self, value):
		return True
		
	elif self.dx and find_pre(self, value):
		return True
		
	else: return False
```

**in order:**
prima sinistra, poi se stesso, poi destra
```python
def print_tree_in(self):
	if self.sx:
		self.s
	print(self.value)
	if self.dx:
	

```

**post-order**
prima sinistra, poi destra, poi se stesso