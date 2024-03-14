- un gruppo di variabili (elementi) tutte **dello stesso tipo**
- sono **oggetti** (quindi le variabili di array contengono il riferimento all'array)
- gli elementi di un array possono essere tipi primitivi o riferimenti a oggetti (anche altri array)
- la lunghezza dell'array si specifica dentro le quadre

>[!tip] tip
>la lunghezza di un array può essere specificata con una variabile
>```java
> int numeroDiCifre = new Scanner(System.in).nextInt();
> int[] numeri = new int[numeroDiCifre];
>```

##### creazione array senza valori
```java
//dichiarazione
int[] a; //inizializza a a "null" (è un oggetto)

//creazione senza valori
a = new int[10]
```
- ogni elemento di un array creato senza valori sarà inizializzato al suo valore di default (es. int a 0)
- nella dichiarazione non si può specificare la dimensione - NO `int[10] a;`

##### creazione con valori
- se si inizializza un vettore con elementi,  non serve specificare la lunghezza
 
```java
a = new int[] {5, 2, 10, -4, 5, 0, 8}
```

- in questo caso, **non si può specificare la lunghezza**

##### accesso
- si accede a un elemento dell’array specificando il nome dell’array seguito dalla posizione (indice) dell’elemento tra parentesi quadre.
- l'indice è **sempre positivo**.
```java
System.out.println(a[5]);
```

>[!warning] lunghezza array
>per accedere alla lunghezza di un array, non servono le parentesi
>```java
>a.length //sì
>a.length() //no
>```
