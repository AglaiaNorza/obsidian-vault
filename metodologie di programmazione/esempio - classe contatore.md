

```java
public class Counter
{
	// valore intero del contatore
	private int value;

	//costruttore del contatore
	public Counter()
	{
		value = 0;
	}
	
	//incrementa il contatore
	public void count()
	{
		 value++;
	}
	//ritorna il valore corrente 
	public int getValue() {return value;}
}
```

il costruttore inizializza il valore del campo value - quando si costruisce un counter essenzialmente si inizia a contare, quindi setta il valore a 0.
