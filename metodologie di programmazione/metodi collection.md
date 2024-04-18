## ArrayList

| metodo                                      | descrizione |
| ------------------------------------------- | ----------- |
| `boolean add(E, e)`                         |             |
| `void add(int index, E element)`            |             |
| `boolean addAll(Collection<? extends E> c)` |             |

|               Tipo | Metodo                                                                                                                                                                                                        |
| -----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `boolean add(E,e)` | <br>Appends the specific element to the end of the list                                                                                                                                                       |
|             `void` | **`add(int index, E element)`**  <br>Inserts the specific element at the specific position in the list                                                                                                        |
|          `boolean` | **`addAll(Collection<? extends E> c)`**  <br>Appends all of the elements in the specified collection to the end of this list, in the order that they are returned by the specified collection’s Iterator      |
|           `boolan` | **`addAll (int index, Collection<? extends E> c)`**  <br>Inserts all of the elements in the specified collection into this list, starting at the specified position                                           |
|             `void` | **`clear()`**  <br>Removes all of the elements from this list                                                                                                                                                 |
|           `Object` | **`clone()`**  <br>Returns a shallow copy of this `ArrayList` instance                                                                                                                                        |
|          `boolean` | **`contains(Object o)`**  <br>Returns `true` if this list contains the specified element                                                                                                                      |
|             `void` | **`ensureCapacity(int minCapacity)`**  <br>Increases the capacity of this `ArrayList` instance, if necessary, to ensure that it can hold at least the number of elements specified by the minimum             |
|                `E` | **`get(int index)`**  <br>Return the element at the specified position in this list                                                                                                                           |
|              `int` | **`indexOf(Object o)`**  <br>Returns the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element                                                 |
|          `boolean` | **`isEmpty()`**  <br>Returns `true` if this list contains no elements                                                                                                                                         |
|              `int` | **`lastIndexOf(Object o)`**  <br>Returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element                                              |
|                `E` | **`remove(int index)`**  <br>Removes the element at the specified position in this list                                                                                                                       |
|          `boolean` | **`remove(Object o)`**  <br>Removes the first occurrence of the specified element from this list, if it’s present                                                                                             |
|   `protected void` | **`removeRange(int fromIndex, int toIndex)`**  <br>Removes from this list all of the elements whose index is between `fromIndex` inclusive, and `toIndex` exclusive                                           |
|                `E` | **`set(int index, E element)`**  <br>Replaces the element at the specified position in this list with the specified element                                                                                   |
|              `int` | **`size()`**  <br>Returns the number of elements in this list                                                                                                                                                 |
|         `Object[]` | **`toArray()`**  <br>Returns an array containing all of the elements in this list in proper sequence (from first to last element)                                                                             |
|          `<T> T[]` | **`toArray(T[] a)`**  <br>Returns an array containing all of the elements in this list in proper sequence (from first to last element); the runtime type of the returned array is that of the specified array |
|             `void` | **`trimToSize()`**  <br>Trims the capacity of this `ArrayList` instance to be the list’s current size                                                                                                         |

## LinkedList
(quelli di ArrayList, e in più)

|Metodo|Descrizione|
|:--|:--|
|`void addFirst(E e)`|Aggiungere l’elemento in testa alla lista|
|`void addLast(E e)`|Aggiungere l’elemento in coda alla lista|
|`Iterator<E> descendingIterator()`|Restituire un iteratore che parte dall’ultimo elemento della lista e si sposta verso sinistra|
|`E getFirst()`|Restituisce il primo elemento della lista|
|`E getLast()`|Restituisce l’ultimo elemento della lista|
|`E removeFirst()`|Rimuove e restituisce il primo elemento|
|`E removeLast()`|Rimuove e restituisce l’ultimo elemento|
|`E pop()`|Elimina e restituisce l’elemento in cima alla lista vista come pila|
|`void push(E e)`|Inserisce un elemento in cima alla lista vista come pila|

## ListIterator
metodo per iterare bidirezionalmente:
- da sx a dx:
```java
// da sx a dx
ListIterator<Integer> i = l.listIterator();
while(i.hasNext()){
	System.out.println(i.next());
}
```
- da dx a sx - se si specifica un intero, si parte da quella posizione
```java
ListIterator<Integer> i = l.listIterator();
while(i.hasPrevious()){
	System.out.println(i.previous());
}
```


| metodo                  | descrizione                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| `void add(E, e)`        | inserisce l'elemento specificato nella lista                                                         |
| `boolean hasNext()`     | ritorna `true` se esiste un elemento successivo                                                      |
| `boolean hasPrevious()` | ritorna `true` se esiste un elemento precedente <br>(per quando si scorre la lista al contrario)<br> |
| `E next()`              | ritorna l'elemento successivo                                                                        |
| `int nextIndex()`       | ritorna l'indice dell'elemento successivo                                                            |
| `E previous()`          | ritorna l'elemento precedente                                                                        |
| `E previousIndex()`     | ritorna l'indice dell'elemento precedente                                                            |
| `void remove()`         | rimuove l'ultimo elemento ritornato da `next` o `previous`                                           |
| `void set(E, e)`        | sostituisce l'ultimo elemento ritornato  da `next` o `previous` con quello specificato               |

## Map

| return  | metodo | descrizione |
| ------- | ------ | ----------- |
| void    |        |             |
| boolean |        |             |
| Set<>   |        |             |
