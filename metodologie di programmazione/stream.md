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

>[!Tip] metodi di `java.util.stream.Stream<T>`
>![[metodi Stream.png|center|500]]

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

| stream                                                                                                | collection                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| permette di usare uno **stile dichiarativo** - iterazione interna sui dati                            | impone l'utilizzo di uno **stile imperativo** - iterazione esterna sui dati (tranne che per ForEach) |
|  impone l'utilizzo di uno **stile imperativo** - iterazione esterna sui dati (tranne che per ForEach) |                                                                                                      |

>[!Abstract] metodi min e max delle stream
> - restituiscono il minimo e il massimo di uno stream sotto forma di *Optional*
> - prendono in input un *Comparator* sul tipo degli elementi dello stream



