In Java, l'operatore di assegnazione `=` non effettua una copia di un oggetto, ma solo del **riferimento** all'oggetto.
Per creare una copia di un oggetto, è necessario chiamare `clone()`.

- `clone()` non richiama il costruttore della classe, ma la sua implementazione nativa *copia l'oggetto campo per campo*, creando una **shallow copy**. 
	- questo crea problemi nel caso in cui i campi siano riferimenti
 
 
Per creare copia della propria classe, serve quindi sovrascrivere `clone()`.
- è necessario implementare l'interfaccia `Cloneable`, oppure `Object.clone()` emetterà l'eccezione `CloneNotSupportedException`.

Per evitare che si copino i riferimenti, è necessario il **deep cloning**:
- si usa `Object.clone()` per la clonazione dei tipi primitivi
- si richiama `.clone()` sui campi che sono riferimenti ad altri oggetti, impostando i nuovi riferimenti nell'oggetto clonato.

```java
public IntVector getCopy()
{
	try
	{
		IntVector v = (IntVector)clone();
		v.list = (ArrayList<Integer>)list.clone();
		return v;
	}
	catch(CloneNotSupportedException e){return null;}

}
```