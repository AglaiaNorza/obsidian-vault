un programma java si salva in un file unicode, con il titolo dell'identificatore della dichiarazione della classe.

HelloWorld.java
```java
public class HelloWorld
{
	public static void main(String[] args)
	{
		System.out.print("Hello, World!");
		System.out.println();
	}
}
```
![[Screen Shot 2024-02-28 at 10.54.17.png]]
un programma deve quindi iniziare con una dichiarazione di una classe (il cui titolo sarà il nome del file), seguito da un metodo chiamato "public static void main" che riceve un array stringhe.

> [!example]- processo compilazione
>![[Screen Shot 2024-02-28 at 11.13.41.png]]
##### argomenti in entrata
Gli args possono essere passati come argomenti in entrata - Strings[] rappresenta l'array di stringhe fornite sulla command line dopo il nome del file.

![[Screen Shot 2024-02-28 at 11.47.51.png]]