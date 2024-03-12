la lettura dell'input si effettua con la classe `java.util.Scanner`
```java
public class ChatBotNonCosiInterattivo{

	public static void main(String[] args){

	//creazione Scanner per ottenere input
	java.util.Scanner input = new java.util.Scanner(System.in);

	System.out.println("Come ti chiami?");

	//legge i caratteri fino al newline(invio)
	//blocca il codice fino a quando 
	//non si dà l'input
	String nome = input.nextLine();

	System.out.println("Ciao " +nome+"!");
	
	}

}

```

se importo la classe all'inizio del codice, non devo specificare il package
```java
import java.util.Scanner;
//bla bla bla codice
Scanner input = new Scanner(System.in)
```


altre funzioni di Scanner

| **method**      |     | *use*                 |
| --------------- | --- | --------------------- |
| `nextBoolean()` |     | reads a boolean value |
| `nextByte()`    |     | reads a byte value    |
| `nextDouble()`  |     | reads a double value  |
| `nextFloat()`   |     | reads a float value   |
| `nextInt()`     |     | reads an int value    |
| `nextLine()`    |     | reads a String value  |
| `nextLong()`    |     | reads a long value    |
| `nextShort()`   |     | reads a short value   |
