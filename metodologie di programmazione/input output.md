#### output
- l'output su console viene generato usando la classe `System.out` 
- è un campo *statico*, *pubblico*, *final* di `System` di tipo `java.io.PrintStream` (che estende `java.io.OutputStream`)

#### input
- l'input da tastiera si ottiene utilizzando la classe `java.util.Scanner`, costruita con lo *standard input stream* (oggetto riferito da `System.in`)
- `System.in` è un campo *statico*, *pubblico*, *final* di `System` di tipo `java.io.InputStream`
- (uno scanner è come una scatola nera che riceve dati da un input stream, e permette di vedere questi dati come sequenze su cui si può iterare e fare conversioni di tipo)

```java
Scanner s = new Scanner(System.in);
int k = s.nextInt();
System.out.println("hai digitato " +k);

String string = s.next();
System.out.println("hai digitato " +string);
```

per più informazioni sullo [[java.util.Scanner|scanner]]