---
sticker: lucide//package
---
- le classi sono categorizzate in **packages** (fisicamente, cartelle).
- ogni package racchiude classi e le loro funzionalità.
- quando si utilizza una classe è necessario **specificare il package**
- una classe può essere inserita all'interno di un package:
	- specificandolo all'inizio del package (con `package`)
	- posizionando il file nella sottocartella
- il package java.lang (che contiene String) non va importato.
<br/>
- la naming convention è **tutto minuscolo**
<br/>
- per evitare di specificare il package di una classe ogni volta che viene usata, si importa la classe
>[!example]- esempio
>```java
>import java.util.Scanner
>//bla bla bla codice
>Scanner input = new Scanner(System.in);
>//invece di java.util.Scanner input...
>```

- quando si importa un package locale, si può o importare ogni classe (`import l_2_9.Punto`) oppure usare l'asterisco per importare tutto (`import l_2_9.*`)

