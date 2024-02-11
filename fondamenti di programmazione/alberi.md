formati da foglie e nodi.
###### alberi binari
![[Screen Shot 2023-12-05 at 17.43.44.png | 500]]
si può creare una classe per definire i nodes (non serve definire tutto l'albero, basta un node con due figli)
```python
class BinaryNode:

	def __init__(self, value, sx=None, dx=None)
	self.value = value
	self.sx = sx
	self.dx = dx
```
se non ha figli dx e sx sono none (di default)
se ha figli riceve valori di tipo BinaryNode per dx e sx (i figli sono nodi/foglie)

*livelli dell'albero*
![[Screen Shot 2023-12-05 at 17.45.49.png |450]]
per cercare a che livello ci si trova, bisogna definire nella ricorsione una variabile che viene modificata ad ogni chiamata ricorsiva

<font color="#4bacc6">**trovare l'altezza ricorsivamente:**</font>
altezza del primo nodo + max(altezza sottoalbero dx, altezza sottoalbero sx)
```python
#ATTRIBUTO DELLA CLASSE BINARYNODE SOPRA ^
def height(self):
	Hsx = 0 if not.self.sx else self.sx.height()
	Hdx = 0 if not.self.dx else self.dx.height()
	
	return max(Hsx, Hdx) + 1
```
if not ... controlla se ci sono nodi figli

**<font color="#4bacc6">diametro</font>**: percorso massimo da foglia a foglica (non è detto che passi dalla radice)
COPIA DALLE SLIDE

**<font color="#4bacc6">ricerca in un albero</font>** 
un albero, in memoria, alla fine è:

quindi:
caso base - il valore è nel nodo corrente
sennò: ho figli? se sì, li controllo, se no, ho finito e non ho trovato

##### filesystem
il filesystem può essere visto come **albero n-ario**:
- <font color="#c0504d">file </font> - <font color="#c0504d">foglie</font>
- <font color="#4bacc6"> directory</font> - <font color="#4bacc6">nodi</font>
 
per ricorsione su alberi di filesystem:  [[ricorsione#ricorsione sugli alberi |ricorsione sugli alberi]]

### alberi di gioco
###### Tris
- vince chi mette in fila il proprio simbolo.
- pareggio: se la board è piena oppure manca una mossa (che non fa vincere nessuno) per riempirla.
La board è uno <font color="#c0504d">stato</font> - una condizione del gioco.
Una <font color="#4bacc6">mossa</font> ci porta in un altro stato.

![[Screen Shot 2023-12-12 at 16.56.48.png |400]]

possibili mosse/ricorsioni:
![[Screen Shot 2023-12-12 at 16.58.21.png |400]]
fine della ricorsione: vittoria o pareggio.

codice:
![[alberi di gioco.py]]
