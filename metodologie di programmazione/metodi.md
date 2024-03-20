- il miglior modo di sviluppare e mantenere un programma grande è costruirlo a partire da pezzi più piccoli e semplici: **divide et impera**

vantaggi dei metodi:
- i metodi *modularizzano* un programma dividendolo in unità autocontenute
- le istruzioni di un metodo non sono visibili da un altro metodo - ma alcuni metodi non utilizzano lo stato dell'oggetto e si applicano all'intera classe -> **metodi statici**
***
##### metodi statici
un metodo statico si definisce specificando `static` nell'intestazione del metodo

**accesso**: 
- dall'interno della classe *chiamando il metodo*
- dall'esterno, con `NomeClasse.nomeMetodo()`
- si può chiamare un metodo statico anche da un oggetto, con la consapevolezza che il risultato ottenuto non dipenderà dai campi dell'oggetto stesso
>[!example]- esempio
>```java
>public static String getLinea(int k){
>  //bla bla bla
>}
>
>public static void main(String[] args){
>LineaDiTesto s = new LineaDiTesto("titolo", 5);
>
>//accesso da un oggetto
>s.getLinea(5);
>
>//accesso da un metodo statico
>getlinea(5);
>}
>
>```

***
##### metodi get e set
- l'accesso ad alcuni campi è garantito dai metodi `get()` e `set()`
- garantiscono la *consistenza dei dati*, senza dare l'accesso pubblico al campo
- fanno da filtro tra i dettagli implementativi e ciò che vede l'utente esterno
---
#### numero variabile di parametri 
Si possono dichiarare metodi con un numero variabile di parametri - sintassi `type...` 
- permette quindi di chiamare un metodo con un numero arbitrario di parametri del tipo specificato
- di fatto è un riferimento ad un array
- va specificato come **ultimo parametro**
 
```java
public double sum(double... values){}
```