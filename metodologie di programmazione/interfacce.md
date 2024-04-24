---
sticker: lucide//monitor
tags:
  - interfacce
  - classi
---
parola chiave `interface`.
Le interfacce permettono di modellare **comportamenti comuni** a classi (anche se non sono in relazione gerarchica -> in Java non è consentito estendere più di una classe, ma una classe può implementare tutte le interfacce desiderate).

- definiscono e standardizzano l'interazione fra oggetti tramite un insieme di operazioni limitato.
- specificano solo il **comportamento** che un oggetto deve presentare all'esterno (quello che l'oggetto può fare) - l'*implementazione* di tale operazioni *non viene definita*.
<br/>
- sono classi astratte se non definiamo metodi di default.
##### metodi e interfacce
- è possibile specificare delle implementazioni di *default* di metodi non statici mediante la parola `default`.
- è anche possibile implementare *metodi statici* (che non godono di polimorfismo).
- da java 9 in poi, è possibile definire *metodi privati* all'interno di un'interfaccia (che possono essere chiamati solo dai metodi dell'interfaccia stessa).
---
Un'interfaccia è quindi una classe che può contenere soltanto:
- <font color="#e5b9b7">costanti</font>
- <font color="#e5b9b7">metodi astratti</font>
- (java 8): implementazione di default di <font color="#e5b9b7">metodi </font>e metodi statici
- (java 9): <font color="#e5b9b7">metodi privati </font>tipicamente da invocare in metodi di default
--- 
>[!info] visibilità di default
>- tutti i **metodi** dichiarati in un'interfaccia sono implicitamente public abstract.
>- tutti i **campi** dichiarati in un’interfaccia sono implicitamente public static final.

>[!warning] attenzione
>Tranne nel caso dei metodi di default o statici, non è possibile specificare alcun dettaglio implementativo dei metodi.
 
---
##### dichiarazione di un'interfaccia

![[interfaccia es.png | 480]]

--- 
### implementazione
Per realizzare un'interfaccia, è necessario che una classe la **implementi** tramite la parola chiave `implements`.
- una classe che implementa un'interfaccia espone pubblicamente il comportamento descritto dall'interfaccia.
- è obbligatorio che ogni metodo abbia la *stessa intestazione* che presenta nell'interfaccia.

Per una classe che implementa un'interfaccia, ci sono 3 possibilità:
1) fornire un'**implementazione concreta di tutti i metodi**
2) fornire un'implementazione concreta di **parte dei metodi**
3) **non fornire implementazioni concrete**
>[!warning] attenzione
>negli ultimi due casi, la classe andrà dichiarata `abstract`

--- 
#### relazione interfacce-classi
Quando una classe C implementa un'interfaccia I, tra queste due classi c'è una relazione di tipo **is-a** (la classe C è di tipo I).

- anche per le interfacce valgono le regole del polimorfismo:
	- si possono usare oggetti di sottoclassi come fossero del tipo dell'interfaccia: `Interfaccia oggetto = new Sottoclasse()`

>[!question] doppia implementazione e metodi di default
>Quando ho una classe che sta implementando due classi con già definiti due metodi di default, quando chiamo questo metodo sulla classe che sto definendo quale metodo viene chiamato? Chiamo quello giusto con la sintassi `Interfaccia.super.metodo();`

---
##### interfacce ed ereditarietà
Le interfacce possono ereditare più interfacce, rendendo quindi possibile l'**ereditarietà multipla** in Java.
Quando un'interfaccia eredita più interfacce, fa una specie di "merge" tra di esse.

---
### interfacce funzionali (o SAM)
a partire da Java8, è disponibile la nuova annotazione `@FunctionalInterface`, che **garantisce che l'interfaccia sia dotata di un solo metodo astratto** (può avere vari metodi di altri tipi)

- le interfacce funzionali si chiamano anche *Single Abstract Method*

le interfacce funzionali implementano spesso [[lambda functions]].

#### interfacce funzionali built-in

- `Predicate<T>` - funzione a valori booleani a un solo argomento generico T
```java
Predicate<String> predicate = s-> s.length() > 0;

Predicate<String> predicate2 = s-> s.startsWith("f")
```

esiste anche `BiPredicate`, con due valori in input.
```java
BiPredicate<String, Integer> bp2_4_3 = (s, i) -> s.length() == i;
```

- `Function<T, R>` - argomenti T d'ingresso e R di ritorno entrambi generici
```java
Function<String, Integer> toInteger = Integer::valueOf;
```

- `Supplier<T>` - funzione senza argomenti in input

```java
Supplier<String> stringSupplier = () -> "ciao";

Supplier<Person> personSupplier = Person::new;
personSupplier.get(); // new Person();
```

- `Consumer<T>` - argomento di tipo generico T e nessun tipo di ritorno
```java
Consumer<Person> greeter1 = p-> System.out.println("hello"+p);
```