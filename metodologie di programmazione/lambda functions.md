Da Java 8 è possibile specificare funzioni utilizzando le **espressioni lambda**
```java
() -> {System.out.println("hello, lambda!");}
```

Tali espressioni permettono di creare **oggetti anonimi** assegnabili a riferimenti a [[interfacce#interfacce funzionali (o SAM) |interfacce funzionali]] compatibili con l'intestazione della funzione creata (perché le interfacce funzionali hanno solo un metodo astratto)
```java
@FunctionalInterface
public interface Runnable{
	void run();
}

Runnable r = ()->{System.out.println("hello");}

r.run(); //stampa "hello"
```

- sono da utilizzare principalmente quando il codice si scrive su una sola riga
##### sintassi:
```java
(tipo_param nome_param) -> {codice}
```
- il **tipo** dei parametri è **opzionale** perché viene desunto dall'interfaccia funzionale a cui si fa riferimento.
- le **parentesi tonde** sono opzionali se c'è solo un parametro in input.
- le **parentesi graffe** intorno al codice sono opzionali se il codice è di una riga sola
- non è necessaria `return` se il codice è formato solo dall'espressione di **return**.

>[!example]+ esempio
>espressioni tra loro *equivalenti*:
>```java
>(int a, int b) -> {return a+b;}
>(a, b) -> {return a+b;}
>(a, b) -> return a+b;
>(a, b) -> a+b;
>```

###### esempio: conversione da un tipo F a un tipo T
```java
@FunctionalInterface
public interface Converter <F, t>{
	T convert(F from);
}

Converter<String, Integer> converter = from -> Integer.valueOf(from); 
//converte da String a interi

Integer converted = converter.convert("123")

Converter<String, MyString> stringConverter = a -> new MyString(a);
//converte da String a Mystring
```

#### classi anonime ed espressioni lambda
>[!info] differenze
>la parola chiave `this`:
>- nelle **classi anonime** si riferisce all'oggetto anonimo
>- nelle **espressioni lambda** si riferisce all'oggetto della classe che le racchiude
> 
>la compilazione:
>- **classi anonime** - compilate come classi interne
>- **espressioni lambda** - compilate come metodi privati invocati dinamicamente

#### visibilità dalle espressioni lambda
- l'accesso alla variabili esterne da un'espressione lambda è simile a quello di una classe anonima
- si può accedere a:
	- **campi d'istanza** e **variabili statiche**
	- variabili **final** del metodo che definisce la lambda