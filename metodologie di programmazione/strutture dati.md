---
sticker: lucide//clipboard-list
---
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
- **ArrayList** implementa la lista mediante un *array*
	- [[metodi collection#ArrayList|metodi ArrayList]]
- **LinkedList** implementa la lista mediante *elementi linkati*
	- [[metodi collection#LinkedList|metodi LinkedList]]

>[!question] come iterare in entrambe le direzioni?
>- `listIterator()` (interfaccia che estende `Iterator()` restituisce un iterator bidirezionale per la lista:
> 	- [[metodi collection#ListIterator|metodi listIterator]]

## insiemi: HashSet, TreeSet, LinkedHashSet
- basati su **Set**, sottointerfaccia di `Collection` e di `Iterable`
- gli insiemi sono Collection che contengono *elementi distinti*

| set               | memorizzazione                                                              |
| ----------------- | --------------------------------------------------------------------------- |
| **HashSet**       | memorizza gli elementi in una *hashtable*                                   |
| **TreeSet**       | memorizza gli elementi in un *albero* mantenendo un *ordine sugli elementi* |
| **LinkedHashSet** | memorizza gli elementi in *ordine di inserimento*                           |

## mappe
`java.util.Map`
- mettono in corrispondenza **chiavi** e **valori**
- non possono contenere chiavi duplicate
	- [[metodi collection#Map |metodi Map]]
 
> [!Example]- mappa frequenze in un testo
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

è possibile ottenere: 
- l'**insieme delle chiavi** di una mappa mediante il metodo `keySet`
- l'**elenco dei valori** mediante il metodo `values` (con ripetizioni)
- l'**insieme delle coppie** (chiave, valore) mediante il metodo `entrySet`:
	- restituisce un insieme di oggetti di tipo `Map.Entry<K, V>`
	- per ogni coppia è possibile conoscere chiave (`getKey()`) e valore (`getValue()`)

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
