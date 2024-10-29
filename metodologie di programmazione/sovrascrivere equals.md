- Il metodo `equals` viene invocato per confrontare il contenuto di due oggetti.
- Per default, se i due sono "uguali", il metodo restituisce `true`.

Tuttavia, la classe Object non conosce il contenuto delle sottoclassi, quindi è necessario sovrascrivere il metodo.
```java
public class Punto{ 
	private int x, y, z;

	public boolean equals(Object o){
	if (o == null) return false;
	//chiedo se l'oggetto è stato costruito
	//con lo stesso costruttore
	if (getClass() != o.getClass()) return false;
	
	Punto p = (Punto)o;
	return x == p.x && y == p.y && z == p.z;
	}
}
```