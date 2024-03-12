- le classi sono categorizzate in **packages**.
- ogni package racchiude classi e le loro funzionalità.
- quando si utilizza una classe è necessario **specificare il package**
- il package java.lang (che contiene String) non va importato.

- per evitare di specificare il package di una classe ogni volta che viene usata, si importa la classe
>[!example]- esempio
>```java
>import java.util.Scanner
>//bla bla bla codice
>Scanner input = new Scanner(System.in);
>//invece di java.util.Scanner input...
>```