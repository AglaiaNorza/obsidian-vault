---
sticker: lucide//database
---
oggetti e tipi primitivi hanno una diversa rappresentazione in memoria:

| tipi primitivi                                                   | oggetti                                                                       |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| memoria allocata automaticamente <br>a **tempo di compilazione** | memoria allocata durante <br>l'**esecuzione del programma** (operatore `new`) |
***
- i **riferimenti** sono la versione di Java dei puntatori di C.
- sono indirizzi di memoria, il cui valore numerico è però sconosciuto.
<br/>
- gli oggetti quindi sono memorizzati nelle variabili attraverso il loro riferimento (e non direttamente)
***
esistono due (tre) tipi di memoria:
- **heap** - memoria per la creazione dinamica (oggetti)
- **stack** - variabili locali
 
>[!example]- esempio
>![[heap e stack.png]]

***
##### rappresentare la memoria
![[rappresentare memoria.png]]



>[!example]- esempio di codice da analizzare
> ```java
> public class Tornello
> {
> 	static private int passaggi;
> 	
> 
> }
> 
>```
>![[codice da rappresentare.png]]
che fare?
1) analizzare i **campi statici** 
	- (qui, nel metaspace inserisco "passaggi = 0", perché Java inizializza gli interi automaticamente a 0)
2) analizzare il **main**
	- si fa una barra nello stack per dare uno spazio al metodo `main` 
	- si crea il vettore args che contiene Stringhe (che deve puntare dal main allo heap perché le Stringhe e gli Array sono oggetti)
	- anche il Tornello t1 deve puntare allo heap, perché i Tornelli sono oggetti (Tornello non ha campi che non siano statici - se li avesse avuti, avremmo dovuto mettere le variabili nel rettangolo nello heap) 
3) analizzare le **chiamate ai metodi**:
	- si crea lo spazio per ogni chiamata nello stack (e si modificano eventuali campi che queste chiamate modificano)
	- ogni chiamata si sovrappone a quella precedente - se chiamo `passa()` e poi `Tornello()`, sullo stack si vede solo `Tornello()`, che prende il posto di `passa()`, e crea un nuovo Tornello t2
	>[!tip] indici dei loop
	>gli indici dei loop sono variabili temporaneamente allocate nello stack
	>>[!example]- visualizzazione
	>>![[loop nello stack.png]]

>[!example]- rappresentazione finale tornello
>![[rappr tornello.png]]

*** 
##### i campi static
I campi di una classe possono essere dichiarati *static*.
- Un campo static è relativo all'**intera classe**, non al singolo oggetto istanziato - esiste in una singola locazione di memoria, allocata in una zona speciale chiamata MetaSpace.
- per ogni campo non static c'è invece **una locazione di memoria per ogni oggetto** (collocata dopo `new`)

***




