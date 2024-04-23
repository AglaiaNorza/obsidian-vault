---
sticker: lucide//clipboard-list
tags:
  - classi
  - tipi
  - interfacce
---
>[!info]+ index
>- [[#collection|collection]]
>- [[#iterazione esterna su una collezione|iterazione esterna su una collezione]]
	>	- [[#iterazione interna su una collezione|iterazione interna su una collezione]]
> - [[#collezioni fondamentali|collezioni fondamentali]]
>- [[#liste: ArrayList e LinkedList|liste: ArrayList e LinkedList]]
>- [[#mappe|mappe]]
>	- [[#collezioni fondamentali#HashMap|HashMap]]
>	- [[#collezioni fondamentali#TreeMap |TreeMap]]
>	- [[#insiemi: HashSet, TreeSet, LinkedHashSet|insiemi: HashSet, TreeSet, LinkedHashSet]]
>- [[#pila e coda|pila e coda]]
>- [[#alberi|alberi]]
>- [[#algoritmi sulle collezioni|algoritmi sulle collezioni]]
>	- [[#collezioni fondamentali#collezioni|collezioni]]
>	- [[#collezioni fondamentali#array|array]]
>- [[#ordinamento naturale|ordinamento naturale]]
	>	- [[#array#metodi di default dell'interfaccia comparator|metodi di default dell'interfaccia comparator]]
>- [[#for each|for each]]

### collection
Strutture dati già pronte all'uso con interfacce e algoritmi per manipolarle.
- contengono e "strutturano" riferimenti ad altri oggetti, tipicamente dello stesso tipo.

alcune interfacce:

| interfaccia | descrizione                                                                              |
| ----------- | ---------------------------------------------------------------------------------------- |
| Collection  | interfaccia alla radice                                                                  |
| Set         | collezione **senza duplicati**                                                           |
| List        | collezione **ordinata** che può contenere **duplicati**                                  |
| Map         | associa coppie **(chiave, valore)**, *senza chiavi duplicate* (vedi dizionari in python) |
| Queue       | collezione **first-in, first-out** (fifo)                                                |
>[!info]- gerarchia delle interfacce
>![[collection gerarchia.png | 500]]

##### iterazione esterna su una collezione
1) mediante gli **iterator**:
```java
Iterator<Integer> i = collezione.iterator()
while(i.hasNext()){
	int k = i.next();
	System.out.println(k);
}
```
2) mediante il costrutto **for each**:
```java
for(Integer k: collezione)
	System.out.println(k);
```
4) (solo su liste) mediante **indici** 
```java
for(int j=0; j<collezione.size(); j++){
	int k = collezione.get(j)
	System.out.println(k)
}
```
##### iterazione interna su una collezione
- il metodo `Iterable.forEach` permette l'iterazione su *qualsiasi collezione* senza specificare come effettuare l'iterazione
	- utilizza il **polimorfismo** (chiamerà il `forEach` della classe specifica)
- `forEach` prende in input un **Consumer**, un'*interfaccia funzionale*

### collezioni fondamentali
- AbstractList:
	- ArrayList
	- LinkedList
- AbstractSet:
	- TreeSet
	- HashSet
		- LinkedHashSet
- AbstractMap:
	- TreeMap
	-  HashMap
		- LinkedHashMap
 
(i sottoelementi estendono l'elemento che li contiene)

## liste: ArrayList e LinkedList
- basate su **List** (interfaccia di Collection e Iterable)
- estendono `AbstractList` e implementano l'intefaccia `List`
<br/>
- **ArrayList** implementa la lista mediante un *array*, e ha una dimensione flessibile (al contrario dell'array) (come lista python, ma con un unico tipo)
	- [[metodi collection#ArrayList|metodi ArrayList]]
- **LinkedList** implementa la lista mediante *elementi linkati*
	- ogni elemento "contiene" il suo valore e un link all'elemento successivo, quindi per aggiungere un elemento basta linkarlo in uno degli elementi già presenti
 
		![[Pasted image 20240422192724.png | 300]]
	- [[metodi collection#LinkedList|metodi LinkedList]]

>[!question] come iterare in entrambe le direzioni?
>- `listIterator()` (interfaccia che estende `Iterator()` restituisce un iterator bidirezionale per la lista:
> 	- [[metodi collection#ListIterator|metodi listIterator]]
## mappe
`java.util.Map`
- mettono in corrispondenza **chiavi** e **valori**
- non possono contenere chiavi duplicate
	- [[metodi collection#Map |metodi Map]]

è possibile ottenere: 
- l'**insieme delle chiavi** di una mappa mediante il metodo `keySet`
- l'**elenco dei valori** mediante il metodo `values` (con ripetizioni)
- l'**insieme delle coppie** (chiave, valore) mediante il metodo `entrySet`:
	- restituisce un insieme di oggetti di tipo `Map.Entry<K, V>`
	- per ogni coppia è possibile conoscere chiave (`getKey()`) e valore (`getValue()`)

#### HashMap
`HashMap` memorizza le coppie in una tabella di hash.
Quando aggiungiamo un valore alla mappa, viene applicata una funzione che restituisce un valore `hash` che rappresenta la locazione in memoria del valore. Quando dobbiamo ritrovare il valore, la stessa funzione viene riutilizzata al contrario.
 
> [!Example]- mappa frequenze in un testo: HashMap
> 
> ```java
> public class MappaDelleFrequenze{
> 
> private Map<String, Integer> frequenze = new HashMap<String, Integer>();
> 
> public MappaDelleFrequenze(File file) throws IoException{
> 
> 	Scanner in = new Scanner(file);
> 	while(in.hasNext()){
> 
> 	String parola = in.next();
> 	Integer freq = frequenze.get(parola);
> 
> 	if (freq == null) freqenze.put(parola, 1);
> 	else frequenze.put(parola, freq+1);
> 	
> 		}
> 	}
> }
> ```

- La `LinkedHashMap` estende `HashMap` e mantiene l'ordine di inserimento.
#### TreeMap
`TreeMap` implementa il red-black tree, e **ordina gli elementi per chiave**.

## insiemi: HashSet, TreeSet, LinkedHashSet
- basati su **Set**, sottointerfaccia di `Collection` e di `Iterable`
- gli insiemi sono Collection che contengono *elementi distinti*

| set               | memorizzazione                                                              |
| ----------------- | --------------------------------------------------------------------------- |
| **HashSet**       | memorizza gli elementi in una *hashtable*                                   |
| **TreeSet**       | memorizza gli elementi in un *albero* mantenendo un *ordine sugli elementi* |
| **LinkedHashSet** | memorizza gli elementi in *ordine di inserimento*                           |


## pila e coda
**coda**: è FIFO (First In First Out)
-  `LinkedList` implementa l'interfaccia `Queue`
	- operazioni:
		- `add` - aggiunge un elemento in coda
		- `remove` - rimuove un elemento dall'inizio della coda
		- `peek` - restituisce l'elemento all'inizio della coda senza rimuoverlo

**pila**: è LIFO (Last In First Out)
- la classe `Stack` implementa l'interfaccia `List`
	- operazioni:
		- `push` - inserisce un elemento in cima alla pila
		- `pop` - rimuove l'elemento in cima alla pila
		- `peek` - restituisce l'elemento in cima alla pila senza rimuoverlo






## alberi
struttura dati *ricorsiva* formata da nodi e figli (ogni nodo ha padre tranne la radice).

utilizziamo una **classe annidata** (interna se ci serve il riferimento all'albero) per rappresentare un nodo
```java
public class BinaryTree{

	private Nodo root;

	static public class Nodo{
		private Nodo left, right;
		private int valore;

		public Nodo(Nodo left, Nodo right, int valore){
			this.left = left;
			this.right = right;
			this.valore = valore;
		}	
	}
}
```





## algoritmi sulle collezioni
#### collezioni
la classe `java.util.Collections` fornisce **metodi statici per la manipolazioni delle collezioni**

| metodo         | descrizione                                                |
| -------------- | ---------------------------------------------------------- |
| `sort`         | ordina elementi di un array                                |
| `binarySearch` | cerca un elemento tramite ricerca binaria                  |
| `fill`         | riempe l'array con l'elemento specificato                  |
| `copy`         | copia gli elementi da una lista a un'altra                 |
| `reverse`      | inverte l'ordine degli elementi di una List                |
| `shuffle`      | mette in ordine casuale gli elementi di una List           |
| `min/max`      | restituisce l'elemento più piccolo/grande della Collection |

#### array
la classe `java.util.Arrays` fornisce **metodi statici per la manipolazioni degli Array**

| metodo         | descrizione                                                        |
| -------------- | ------------------------------------------------------------------ |
| `sort`         | ordina elementi di un array                                        |
| `binarySearch` | cerca un elemento tramite ricerca binaria                          |
| `fill`         | riempe l'array con l'elemento specificato                          |
| `copyOf`       | restituisce la copia di un array                                   |
| `equals`       | confronta due array elemento per elemento                          |
| `asList`       | restituisce una lista contenente gli elementi dell'array           |
| `toString`     | restituisce una rappresentazione dell'array sotto forma di stringa |


## ordinamento naturale
come garantire un ordinamento sui tipi utilizzati nelle strutture dati che si basano su un ordinamento (come `TreeSet` o `TreeMap`)?
- è necessario che le strutture implementino l'interfaccia `Comparable<T>` !
	L'interfaccia `Comparable` è dotata di un solo metodo:
	- `int compareTo(T o)`, che confronta sé stesso con l'oggetto o, e restituisce:
		- 0 se uguali
		- -1 se <= o
		- +1 altrimenti

> [!example]+ esempio
>  ```java
>  public class NomeCognome implements Comparable< NomeCognome>{
> 	private String nome, cognome;
> 	 // bla bla costruttore bla bla
> 
> 	@Override
> 	public int compareTo(NomeCognome o){
> 		int v = cognome.compareTo(o.cognome);
> 
> 		if(v = = 0) return nome.compareTo(o.nome)
> 		else return v;
> 	}
> }
> ```

 
---
Se la classe non fornisce di suo l'ordinamento naturale, posso implementare un'interfaccia `Comparator<T>` e passarne un'istanza in input al costruttore delle strutture dati (es. TreeSet/TreeMap)

##### metodi di default dell'interfaccia comparator
- confronto **inverso**:
```java
comparator.reversed().compare(p1, p2);
```

- confronto **per una data chiave**:
```java
comparator = Comparator.comparing(p->p.getFirstName());
```

- confronto per **criteri multipli a cascata**
```java
comparator = Comparator.comparing(p->p.getFirstName()).thenComparing(p-> p.getLastName());
```

## for each
Le collection sono ora dotate di un metodo `forEach`, che prende in input un'interfaccia `Consumer<? super T>` (con T tipo generico della collection)

```java
Collection<String>c = Arrays.asList("aa", "bb");

//da Java 7:
for(String s : c)System.out.println(s);

//da Java 8:
c.forEach(s->System.out.println(s));

c.forEach(System.out::println);

```