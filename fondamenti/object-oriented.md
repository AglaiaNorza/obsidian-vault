![[Screen Shot 2023-11-28 at 10.10.25.png |300]]   
una classe sta a un'istanza-oggetto come humankind sta a una persona x.
#### ereditarietà
si possono far derivare classi da altre classi 
le classi derivate ereditano metodi e attributi, ma si possono estendere aggiungendone di nuovi.
![[Screen Shot 2023-11-28 at 16.47.40.png |250]]

es. da Color (che ha r,g,b), se voglio anche alpha, eredito e aggiungo alpha
```python
Class ColorAlpha(Color):
	def __init__(self, r, g, b, a):
	super().__init__(r,g,b) #stiamo riutilizzando il codice di Color (super)
	self._a = a #Alpha

	def __repr__(self):
	return super().__repr__()[:-1] + f'{self._a} 
	#anche qui richiamiamo con super Color
```

###### attributi di classe vs di oggetto
- attributi di classe: condivisi fra tutti gli oggetti di quella classe
- attributi di istanza oggetto: relativi a quell'oggetto

#### decoratori
modificano le funzionalità alle funzioni (they "decorate") senza modificarne il codice.

per esemipo, per modificare una funzione senza cambiarla:
```python
def before_and_after_decorator(func):
		def my_wrapping_function():
		print("> decorator: before")
		func()
		print(">my_wrapping_function")
	return my_wrapping_function

def my_locked_func():
	print("main code of the locked function")

dec = before_and_after_decorator(my_locked_func)
#dec è una FUNZIONE. per avere l'output devo ecocarla:
value = dec()
```

si può fare così:
```python
@before_and_after_decorator
def my_locked_function_two():
	print("main code of locked function")
```

#### overloading degli operatori
si overloadano gli operatori così che facciano una cosa diversa per alcune classi.

es. in color, invece di concatenare tuple, sommo i valori rgb
```python
def __add__(self, other_color):
	return Color(self._r + other_col._r,
				 self._g + other_col._g,
				 self._b + other_col._b)
``` 

moltiplicazione:
```python
def __mul__(self, k):
	if isinstance(k, int):
	
	elif isinstance(k, color):
```
### oggetti "callable"
quali oggetti sono callable?
callable() ritorna vero se un oggetto  è chiamabile
```python
[callable(x) for x in [int, str, list]]
# True, True, True
```
int, stringhe e liste sono tutte chiamabili
##### rendere un nuovo tipo chiamabile:
si aggiunge call ai suoi metodi
```python
class Foobar():
	def __init__(self):
		pass
		
	def __call__(self, param=str()):
		printf(f'called {param}'')

fb = Foobar() #così abbiamo definito l'oggetto fb, che è callable
```
ma la classe Foobar stessa è callable?  sì
