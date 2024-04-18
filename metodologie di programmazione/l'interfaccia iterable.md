Molte classi diverse che rappresentano sequenze hanno in comune il fatto di poter iterare sui loro elementi.
Le classi iterabili hanno tipicamente in comune i metodi `hasNext` (che controlla se c'è un elemento successivo al corrente), `next()` (che passa all'elemento successivo), e `reset()` (che resetta l'iterazione).
```java
public interface Iterabile{
	boolean hasNext();
	Object next();
	void reset();
}
```

Però ogni classe implementerà i metodi a modo suo.

> [!example]-
> per esempio, per un array di Integer si potrebbe implementare così
> ```java
> public class MyIntegerArray implements Iterabile{
> 	private Integer[] array;
> 	private int k = 0; //"indice"
> 
> 	public MyIntegerArray(Integer[] array){
> 		this.array = array;
> 	}
> 
> 	@Override
> 	public boolean hasNext(){
> 		return k < array.length;
> 	}
> 	
> 	@Override
> 	public Integer next(){
> 		return array[k++];
> 	}
> 	
> 	@Override
> 	public void reset() {k = 0;}
> }
> ```
> mentre, per esempio, il metodo `next()` sarebbe diverso per un array di chars (ritornerebbe un char)


le interfacce `Iterable` e `Iterator` permettono di iterare comodamente sugli oggetti, e disaccoppiano l'oggetto su cui iterare dall'oggetto che tiene la posizione dell'iterazione