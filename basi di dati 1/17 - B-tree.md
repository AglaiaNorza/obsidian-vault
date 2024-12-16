Il B-tree nasce dalla *generalizzazione della struttura di file con indice*.

Si accede ad un file attraverso una **gerarchia di indici** - l'indice a livello più alto (*radice*) è costituito da un unico blocco e *risiede in memoria principale*.
Ogni blocco di un file indice è costituito da record contenenti una coppia (v,b)
- v -->  valore della chiave del primo record della porzione del file principale a cui fa riferimento la coppia
- b --> puntatore (ad un blocco del file indice a livello più basso, o ad un blocco del file principale)

>[!tip] il primo record indice di ogni blocco contiene **solo un puntatore** (niente chiave) <small>ad un blocco che ha chiavi minori di quelle puntate dal secondo record</small>

- ogni chiave di un record indice *ricopre quelle del suo sottoalbero*
- ogni blocco del file principale è memorizzato come quello di un ISAM

>[!warning] ogni blocco di un B-tree (sia indice che principale, tranne la radice) deve essere **pieno almeno per metà**

(per la radice, logicamente, il minimo è due record: se ce ne fosse uno solo, sarebbe inutile e la "vera" radice sarebbe quindi il blocco a cui il record punta)

![[B-tree.png|center|500]]

### ricerca
(per effettuare una ricerca, si accede agli indici a partire dal livello più alto: scendendo nella gerarchia degli indici, si restringe la porzione del file principale in cui deve trovarsi il record desiderato - fino ad arrivare ad un unico blocco).

Si parte dall'indice a livello più alto, e ad ogni passo si esamina *un unico blocco* (se è del file principale, deve essere quello - se è di un file indice, si cerca la chiave che ricopre la propria)

![[B-tree-ricerca.png|center|500]]

<small>(per me è un po' come il binary search tree ma n-ario)</small>
Il costo della ricerca - che è fisso, perché "so dove andare" - è di **h+1 accessi** (con h altezza dell'albero).

>[!tip] come varia h?
>- più i blocchi sono pieni, più h è piccolo (meno costa la ricerca)
>	- se i blocchi sono completamente pieni, un inserimento può richiedere una modifica dell'indice ad ogni livello

### inserimento
caso limite: voglio inserire un record, ma non ho spazio:
 
![[B-tree-ins1.PNG|center|450]]
![[B-tree-ins2.PNG|center|450]]
![[B-tree-ins3.PNG|center|450]]

### cancellazione
in alcuni casi, la cancellazione stravolge completamente la struttura dell'albero:

![[B-tree-canc1.PNG|center|500]]
![[B-tree-canc2.PNG|center|500]]
![[B-tree-canc3.PNG|center|500]]

### massimo valore di h
Siano:
- $N$ - numero di record nel file principale
- $2e-1$ - numero di reccord del file principale che possono essere memorizzati in un blocco
- $2d-1$ - numero di record del file indice che possono essere memorizzati in un bloicco

e quindi (poiché i blocchi devono essere riempiti a metà):
- $e$ - minimo di record necessari in ogni blocco del file principale
- $d$ - minimo di record necessari in ogni blocco del file indice

L