---
sticker: lucide//repeat
---
- una variabile di un certo tipo può contenere un riferimento a un oggetto dello stesso tipo o di qualsiasi sua sottoclasse.
```java
// a è un riferimento a un
// animale, ma chiama il costruttore 
// di un suo sottotipo 
Animale a = new Gatto();

a = new Chihuahua();
// a può "polimorfare" a un altro sottotipo 
// di animale, e diventare un chihuahua
```

>[!warning] metodi delle sottoclassi
Quando faccio questa cosa, non posso chiamare un metodo specifico della sottoclasse che non esista nella superclasse - i vari overriding avranno però comunque effetto.

- la selezione del metodo da chiamare avviene in base all'effettivo tipo dell'oggetto riferito dalla variabile.
 

>[!info] binding
  -Associazione del proprio tipo ad ogni variabile.-
>- I linguaggi compilati fanno **binding statico** - il compilatore inizialmente osserva staticamente il codice senza eseguirlo e crea una tabella dei binding per associare variabili e tipo.
> - Il **binding dinamico** esiste anche in Java quando si parla di *polimorfismo* (ed è svolto dalla JVM) - l'associazione tra una variabile riferimento e un metodo da chiamare viene definita a tempo di esecuzione (si determina quale metodo dovrà essere invocato in una gerarchia di classi in cui è presente l'overriding).


