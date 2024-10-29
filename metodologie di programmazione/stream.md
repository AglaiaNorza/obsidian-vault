
> [!Info]+ index
> - [[#ottenere uno stream|ottenere uno stream]]
> - [[#stream vs collection|stream vs collection]]
> - [[#metodi delle stream|metodi delle stream]]
> 	- [[#metodi delle stream#min e max|min e max]]
> 	- [[#metodi delle stream#filter, forEach|filter, forEach]]
> 	- [[#metodi delle stream#count|count]]
> 	- [[#metodi delle stream#sorted|sorted]]
> 	- [[#metodi delle stream#map|map]]
> 	- [[#metodi delle stream#collect|collect]]
> 	- [[#metodi delle stream#Collectors.toMap|Collectors.toMap]]
> 		- [[#Collectors.toMap#raggruppamento di elementi|raggruppamento di elementi]]
> 	- [[#metodi delle stream#creare il proprio collector|creare il proprio collector]]
> 	- [[#metodi delle stream#partizionamento di elementi|partizionamento di elementi]]
> 	- [[#metodi delle stream#distinct|distinct]]
> 	- [[#metodi delle stream#reduce|reduce]]
> 	- [[#metodi delle stream#limit e skip|limit e skip]]
> 	- [[#metodi delle stream#takeWhile/dropWhile|takeWhile/dropWhile]]
> 	- [[#metodi delle stream#anyMatch/allMatch/noneMatch|anyMatch/allMatch/noneMatch]]
> 	- [[#metodi delle stream#findFirst e findAny|findFirst e findAny]]
> 	- [[#metodi delle stream#mapToInt e IntStream.summaryStatistics|mapToInt e IntStream.summaryStatistics]]
> 	- [[#metodi delle stream#flatMap|flatMap]]
> 	- [[#metodi delle stream#ottenere uno stream infinito|ottenere uno stream infinito]]
> 	- [[#metodi delle stream#fare copie di stream|fare copie di stream]]
> - [[#stream paralleli|stream paralleli]]
> - [[#mappe|mappe]]

abbiamo già iniziato a parlare di *stream* in riferimento ai [[file]].

`java.util.stream.Stream` è un'interfaccia che rappresenta una sequenza di elementi su cui possono essere effettuate una o più operazioni.
- supporta operazioni *sequenziali* e *parallele*
- viene creato a partire da una sorgente di dati (come una `java.util.Collection`)
- al contrario delle Collection, uno Stream *non memorizza né modifica* i dati della sorgente, ma opera su di essi

le operazioni possono essere:
- **intermedie** - restituiscono un *altro stream* su cui continuare a lavorare
- **terminali** - restituiscono il *tipo atteso* - una volta che uno stream è stato usato, <font color="#b7dde8">non può essere riutilizzato</font>

si segue un **builder pattern**: si impostano una serie di operazioni (intermedie) per configurare e infine si costruisce l'oggetto (operazione terminale)

le Stream hanno un **comportamento pigro**: le operazioni non vengono eseguite immediatamente, ma solo quando si richiede l'esecuzione di un'*operazione terminale*.

le operazioni possono essere:
- **<font color="#c3d69b">stateless</font>**: l'elaborazione degli elementi può procedere in modo *<font color="#d7e3bc">indipendente</font>* (non c'è ordine)
- **<font color="#fbd5b5">stateful</font>**: l'elaborazione di un elemento potrebbe *<font color="#fbd5b5">dipendere</font>* da quella di altri elementi

>[!Abstract]- IntStream, DoubleStream, LongStream
>poiché Stream opera su oggetti, esistono analoghe versioni ottimizzate per lavorare con 3 tipi primitivi:
>- int (`IntStream`), double (`DoubleStream`), long (`LongStream`)
> 
>tutte queste estendono l'interfaccia di base `BaseStream`
> 
>- si ottengono da uno stream con i metodi `mapToInt`, `mapToLong`, `mapToDouble`
>- dispongono di due metodi statici: 
>	- `range(inizio, fine)` - intervallo aperto a destra
>	- `rangeClosed(inizio, fine)` - intervallo chiuso a destra 
>>[!Example] IntStream ottenuto da stream di array di interi
>>```java
>>Arrays.stream(new int[]{1,2,3}) //restituisce un IntStream
>>	.map(n->2 * n+1)
>>	.average()
>>	.ifPresent(System.out::println);
>>```


#### ottenere uno stream
1) direttamente *dai dati* con il metodo statico generico
	- `Stream.of(elenco di dati)` 

 
1) da Java8, dalle *Collection*:
	- `default Stream<E> stream()`
	- `default Stream<E> parallelStream()` - restituisce uno stream parallelo se possibile (altrimenti sequenziale)

2) da un array:
	- `Stream<T> Arrays.stream(T[] array)`

3) uno stream di testo da BufferedReader.lines()
 **FINISICI**
---

#### stream vs collection

| stream                                                                                               | collection                                                                                           |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| permette di usare uno **stile dichiarativo** - iterazione interna sui dati                           | impone l'utilizzo di uno **stile imperativo** - iterazione esterna sui dati (tranne che per ForEach) |
| impone l'utilizzo di uno **stile imperativo** - iterazione esterna sui dati (tranne che per ForEach) |                                                                                                      |

#### metodi delle stream
>[!Tip] `java.util.stream.Stream<T>`
>![[metodi Stream.png|center|500]]
##### min e max
- restituiscono il minimo e il massimo di uno stream sotto forma di *Optional*
- prendono in input un *Comparator* sul tipo degli elementi dello stream

##### filter, forEach
- `filter` accetta un `Predicate` per filtrare gli elementi dello stream, ed è un'*operazione intermedia* che restituisce lo stream filtrato
- `forEach` prende in input un `Consumer` e lo applica ad ogni elemento dello stream, ed è un'*operazione terminale*
 
>[!Example]- esempi
>filtra gli elementi di una lista di interi mantenendo solo quelli dispari e stampa ciascun elemento rimanente:
>```java
>List< Integer> l = Arrays.asList(4,8,15,16,23,42)
>l.stream()
>.filter(k-> k%2 = = 1)
>.forEach(Sysyem.out::println);
>```

##### count 
- operazione terminale che restituisce il numero *long* di elementi nello stream

##### sorted
- operazione intermedia che restituisce una *vista ordinata* senza modificare la collezione sottostante

##### map
- operazione intermedia sugli stream che restituisce un nuovo stream in cui *ciascun elemento dello stream di origine è convertito* in un altro oggetto attraverso la `Function` passata in input
```java
l.stream().map(String::toUpperCase)
.sorted(Comparator<String>.naturalOrder()
.reversed())
.forEach(System.out::println);
```

##### collect
- operazione terminale che permette di raccogliere gli elementi dello stream in un qualche oggetto (es. collection, stringa, intera)

> [!Example]- esempio
> stringa che concatena stringhe in un elenco, rese maiuscole e separate da virgola
> 
> ```java
> List< String> l = Arrays.asList("RoMa", "milano", "Torino");
> String s = "";
> 
> // in Java 7:
> for (String e : l) s += e.toUpperCase()+", ";
> s = s.substring(0, s.length()-2);
> 
> // in Java 8:
> s = l.stream().map(e -> e.toUpperCase())
> .collect(Collectors.joining(", "));
> ```

- `java.util.stream.Collectors` contiene i metodi che raccolgono gli elementi di uno stream
 
>[!Tip] tip
>per rendere più leggibile il codice, si può fare
>`import static java.util.stream.Collectors.*`
>- permette di scrivere il nome del metodo senza "Collectors" (`toList() vs Collectors.toList())`


| metodo                                                                                  | cosa fa                                                                                         |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `counting()`                                                                            | restituisce un collector con un solo elemento: il numero di elementi nello stream (con un long) |
| `maxBy/minBy(comparator)`                                                               | ... con il minimo o il massimo                                                                  |
| `summingInt(lambda che mappa elementi a intero)`                                        | ... con somma in int                                                                            |
| `summingDouble()`                                                                       | somma in double                                                                                 |
| `averagingInt()`                                                                        | media                                                                                           |
| `averagingDouble()`                                                                     | media come double                                                                               |
| `joining()` e <br>`joining(separatore)` e <br>`joining(separatore, prefisso, suffisso)` | concatena gli elementi stringa dello stream                                                     |

##### Collectors.toMap
- prende in input fino a 4 argomenti:
	1) la *funzione* per mappare l'oggetto dello stream nella *chiave* della mappa
	2) la *funzione* per mappare l'oggetto dello stream nel *valore* della mappa
	3) [<font color="#a5a5a5">opzionale</font>]:  la funzione da utilizzare per *unire* il valore preesistente nella mappa con quello nuovo nel caso la chiave esista già
	4) [<font color="#a5a5a5">opzionale</font>]: il `Supplier`

###### raggruppamento di elementi

| metodo                                                                                                      | che fa                             |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `groupingBy(lambda che mappa gli elementi di tipo T in bucket rappresentati da oggetti di un altro tipo S)` | restituisce una `Map<S, List<T>>`  |
| `groupingBy(lambda, downStreamCollector)`                                                                   | per il raggruppamento multilivello |
- essenzialmente fa una mappa (chiave -> mappa/lista/set)

in raccolte multilivello, `Collectors.mapping` è utile per mappare il valore di raggruppamento a un altro tipo.
```java
Map<City, Set<String>> peopleSurnamesByCity =
people.stream().collect(
	groupingBy(Person::getCity,
		 mapping(Person::getLastName, toSet())));
```

##### creare il proprio collector
con il metodo statico `Collector.of`, che prende in input 4 argomenti:
1) un **supplier** per creare la rappresentazione interna
2) un **accumulator** che aggiorna la rappresentazione con il nuovo elemento
3) un **combiner**, che "fonde" due rappresentazioni ottenute in modo parallelo 
4) un **finisher**, che trasforma tutto nel tipo finale

```java
Collector<Person, StringJoiner, String> personNameCollector
= Collector.of(
	()-> new StringJoiner("|"), //supplier
	(j,p) -> j.add(p.name.toUpperCase()), //accumulator
	(j1,j2) -> j1.merge(j2), //combiner
	StringJoiner::toString); //finisher

String names = people.stream()
		.collect(personNameCollector);
//darebbe MAX|PETER|PAMELA|DAVID
```

##### partizionamento di elementi
`partitioningBy(predicato)` raggruppa in una `Map<Boolean, List<T>>`
- crea una mappa da booleano a lista di interi che soddisfano quel criterio di predicato in input (quindi una mappa a "due" elementi: le cose che rispettano la condizione e quelle che non la rispettano)

##### distinct
- restituisce un nuovo stream senza ripetizione di elementi (gli elementi sono tutti distinti tra loro)

> [!Tip] quindi, per creare una lista con solo elementi distinti
> ```java
> List< Integer> distinti = l.stream().
> distinct().collect(toList());
> ```


##### reduce
operazione *terminale* che effettua una riduzione sugli elementi dello stream utilizzando la funzione data in input.

- prende due input: 
	1) elemento di identità: l' "accumulatore" su cui si reduce
	2) la funzione con cui ridurre

```java
//invece di fare:
for(int k : lista)
	somma +=k;

//fai
lista.stream().reduce(0, (a,b)->a+b);
//oppure
lista.stream().reduce(0, Integer::sum);
```

**<font color="#31859b">versione con un parametro solo</font>**
esiste anche una versione di `reduce` con un solo parametro - senza elemento di identità - che restituisce un `Optional<T>` perché, se lo stream è vuoto, non avendo l'elemento identità non si sa cosa restituire

> [!Example]+ esempi
> ```java
> Optional< String> reduced = l.stream().sorted()
> 	.reduce((s1,s2)->s1+"#"+s2);
> ```
> calcolare la somma del doppio dei valori pari di una lista
>- con fiilter, map, reduce
>```java
>l.stream().filter(e-> e%2= = 0)
>	.map(e-> e * 2)
>	.reduce(0, Integer::sum)
>```
>- con filter, mapToInt e IntStream.sum
> ```java
>l.stream().filter(e-> e%2= = 0)
>	.mapToInt(e-> e * 2)
>	.sum();
>```
> 

##### limit e skip
- `limit` (intermedia) limita lo stream a k elementi (k long in input)
 
`List<String> reduced = l.stream().limit(2).collect(toList());`

- `skip` (intermedia) salta k elementi (k long passato in input)
 
 `List<String> reduced = l.stream().skip(2).collect(toList());` (non contiene i primi due elementi della stream)

##### takeWhile/dropWhile
- `takeWhile` (intermedio) prende elementi finché si verifica la condizione del predicato
- `dropWhile` (intermedio) salta elementi finché si verifica la condizione del predicato

##### anyMatch/allMatch/noneMatch
restituiscono un booleano relativo all'esito del matching (se gli elementi rispettano una condizione)
 
`boolean anySwA = l.stream().anyMatch(s->s.startsWith("a");`

##### findFirst e findAny
operazioni terminali per ottenere il primo elemento e un qualsiasi elemento dello stream

`Optiona<String>v = l2.stream().sorted().findFirst()`

##### mapToInt e IntStream.summaryStatistics
- è possibile convertire uno `Stream` in un `IntStream`
- `IntStream` possiede il metodo `summaryStatistics` che restituisce un oggetto di `IntSummaryStatistics` con informazioni su min, max, media, conteggio

```java
IntSummaryStatistics stats = p.stream()
	.mapToInt(x->x).summaryStatistics();
	
System.out.println(stats.getMin());
```

##### flatMap
permette di "unire" gli stream in un unico stream
- essenzialmente, "appiattisce" le collection (collection di collection -> collection di elementi dalle collection)
```java
Map<String, Long> letterToCount =
words.map(w->w.split("")) //restituisce String[]
//passi a flatmap il supplier che 
//rende la collection uno stream
	.flatMap(Arrays::stream)
	.collect(groupingBy(identity(), counting()));
```

> [!Example] stampare i token (distinti) da file
> ```java
> Files.lines(Paths.get("stuff.txt"))
> 
> .map(line -> line.split("\\s+")) // Stream<String[]>
> .flatMap(Arrays::stream) // Stream< String>
> .distinct() // Stream< String>
> .forEach(System.out::println);
> ```
##### ottenere uno stream infinito

con il metodo `iterate()` che, partendo dal primo argomento, restituisce uno stream infinito con **valori successivi** applicando la funzione passata come secondo argomento
 
```java
Stream<Integer> numbers = Stream.iterate(0, n->n+10)
```

- è possibile **limitare** uno stream infinito con il metodo `limit`

##### fare copie di stream
gli stream non sono riutilizzabili, ma è possibile creare un builder di stream tramite una **lambda**.

```java
Supplier<Stream<String>> streamSupplier = () ->
Stream.of("d2", "a2", "b1", "b3", "c")
.filter(s -> s.startsWith("a"));
```
- ha più senso se, invece di un Supplier, abbiamo una funzione che prende in input una Collection e restituisce uno stream su tale collection

#### stream paralleli
- le operazioni su stream sequenziali sono effettuate in un *singolo thread*.
- le operazioni su stream paralleli sono effettuate contemporaneamente su **thread multipli**

lo stream parallelo è più veloce di quello sequenziale, ma non nel caso in cui le operazioni sono *bloccanti*.

>[!Question] quando usare uno stream parallelo?
>- quando il problema è parallelizzante
>- quando posso permettermi di usare più risorse
>- quando la dimensione del problema è tale da giustificare il sovraccarico dato dalla parallelizzazione

#### mappe
le mappe non supportano gli stream, ma, da Java8, forniscono numerose funzioni aggiuntive

```java
map.of() //da Java9

map.computeIfPresent(3, (key, val) -> val + key); 
//se l'elemento 3 è presente, modifica il valore 
//associatogli utilizzando la bifunction in input

map.merge(9, "val9", (value, newValue) -> value.concat(newValue));

map.containsKey(9);

map.computeIfAbsent(23, key -> "val" + key);

map.remove(3, "val3"); map.get(3);
```
