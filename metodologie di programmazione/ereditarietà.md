---
sticker: lucide//corner-right-down
---
l'ereditarietà è una forma di **riuso del software** in cui una classe è creata:
- assorbendo i membri di una classe esistente
- aggiungendo nuove caratteristiche (o migliorando quelle esistenti)
 
l'ereditarietà aumenta le probabilità che il sistema sia implementato e mantenuto efficientemente.

> la parola chiave che ci permette di ereditare è `extends`

la sintassi è:
```java
public class SottoClasse extends SuperClasse{}
```

>[!warning] attenzione 
>in Java una classe può estendere **solo una superclasse** (non può "derivare" da più classi)

Una sottoclasse:
- estende una superclasse
- eredita i **membri** della superclasse
- eredita **campi e metodi d'istanza** secondo il livello di accesso specificato
- può aggiungere **nuovi metodi e campi**
- può **ridefinire i metodi che eredita** ma NON i campi

In realtà, tutte le classi di Java estendono una classe object (che contiene cose come `equals()`, `toString()` ecc.)

##### chiamata al super-costruttore
quando si crea una classe derivata, il suo costruttore potrà (dovrà?) chiamare il costruttore della classe superiore.
***
##### esempio: classe forma
per esempio, si potrebbe progettare una classe Forma, che rappresenta una forma generica, e poi specializzarla estendendo la classe
```java
public class Forma{
	public void disegna() {}
}

public class Triangolo extends Forma{
	private double base;
	private double altezza;

	//metodi ecc
}

public class Cerchio extends Forma{
	private double raggio;

	//metodi ecc
}
```
 ---
#### classi astratte
una classe astratta viene definita attraverso la parola chiave `abstract`  e **non può essere istanziata** (non possono esistere oggetti per quella classe).

##### metodi astratti
Anche i **metodi** possono essere astratti (solo all'interno di classi astratte).
In questo caso, non hanno corpo nelle classi astratte ma *devono essere implementati* nelle classi non astratte

```java
 public abstract class PersonaggiDisney{
	abstract void faPasticci();
 }

public class Paperoga extends PersonaggiDisney{
	public void faPasticci(){
		System.out.println("bla bla bla");
	}
}
```

#### visibilità
- visibilità **protetta** - `protected` - rende visibile il campo o il metodo a tutte le sottoclassi, ma anche a tutte le classi del package.