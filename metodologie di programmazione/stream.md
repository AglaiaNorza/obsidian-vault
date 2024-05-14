---
sticker: lucide//align-left
---
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


| metodo                                                                                  | cosa fa                                                      |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `counting()`                                                                            | restituisce il numero di elementi nello stream (con un long) |
| `maxBy/minBy(comparator)`                                                               | restituisce un Optional con il minimo o il massimo           |
| `summingInt(lambda che mappa elementi a intero)`                                        | somma in int                                                 |
| `summingDouble()`                                                                       | somma in double                                              |
| `averagingInt()`                                                                        | media                                                        |
| `averagingDouble()`                                                                     | media come double                                            |
| `joining()` e <br>`joining(separatore)` e <br>`joining(separatore, prefisso, suffisso)` | concatena gli elementi stringa dello stream                  |

##### Collectors.toMap
- prende in input fino a 4 argomenti:
	1) la *funzione* per mappare l'oggetto dello stream nella *chiave* della mappa
	2) la *funzione* per mappare l'oggetto dello stream nel *valore* della mappa
	3) [<font color="#a5a5a5">opzionale</font>]:  la funzione da utilizzare per *unire* il valore preesistente nella mappa con quello nuovo nel caso la chiave esista già
	4) [<font color="#a5a5a5">opzionale</font>]: il `Supplier`