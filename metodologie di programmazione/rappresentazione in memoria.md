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
1) ci sono campi statici?
2) 


*** 
##### i campi static
I campi di una classe possono essere dichiarati *static*.
- Un campo static è relativo all'**intera classe**, non al singolo oggetto istanziato - esiste in una singola locazione di memoria, allocata in una zona speciale chiamata MetaSpace.
- per ogni campo non static c'è invece **una locazione di memoria per ogni oggetto** (collocata dopo `new`)

***





