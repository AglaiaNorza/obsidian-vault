---
sticker: lucide//locate
tags:
  - tipi
---
I tipi generici sono un *modello di programmazione* che permette di definire, con una sola dichiarazione, un intero **insieme di metodi o classi**.

```java
public class Valore<T>{
	private final T val;
	
	public Valore(T val){this.val = val;}

	public T get(){return val;}
	
	public String getType(){return val.getClass().getName();}
}
```

- per definire un tipo generico della classe, si utilizza la sintassi a **parentesi angolari** dopo il nome della classe con il tipo generico da utilizzare `public class Valore<T>`
- da quel punto, si usa il tipo generico come una classe qualsiasi

>[!info]+ istanziare la classe generica
>```java
>Valore\<Integer> i = new Valore<>(42);
>Valore\<String> s = new Valore<>("ciao");
>Valore<Valore\<String>> v = new Valore<>(s);
>
>//i get type di questi saranno: 
>Integer, String, Valore
>```

>[!question] perché non usare Object?
>a questo punto, perché non dovrei usare sempre `Object` per generalizzare al massimo? 
>perché non ci dà informazioni sui tipi che si usano e costringe a *continui downcast*

> [!example]- esempi: tipi generici e diversi tra loro
> ```java
> public class Coppia\<T>{
> 	private T a,b;
> 	
> 	public Coppia(T a, T b){
> 		this.a = a;
> 		this.b = b;
> 	}
> }
> ```
>  
> ```java
> public class Coppia\<T, S>{
> 	private T a;
> 	private S b;
> 
> 	public Coppia(T a, s b){
> 		this.a = a;
> 		this.b = b;
> 	}
> }
> ```
> 

- i tipi generici funzionano **solo con tipi derivati** (non con i primitivi)

##### estendere un'interfaccia generica con vincolo di comparabilità sul tipo generico
```java
public interface MinMax<T extends Comparable<T>>{
	T min();
	T max();
}

public class MyClass<T extends Comparable<T>>
						implements MinMax<T>{
	
}

```

- si possono comparare con minimo e massimo due tipi generici solo se tra i due c'è un principio di ordinamento, quindi l'interfaccia prende in input solo tipi T o suoi sottotipi
- `<T extends Comparable<T>>` si specifica anche nella classe che implementa l'interfaccia perché il vincolo deve essere specificato a tutti i livelli

##### definire un metodo generico
- si può definire un metodo generico anche in una classe non generica
 
per definire un metodo generico con proprio tipo generico, è necessario **anteporre il tipo generico tra parentesi angolari al tipo di ritorno**

```java
static public <T> void esamina(ArrayList<T> lista){}
```

>[!Warning]+ tipi generici e sottotipi
>- un metodo non può normalmente prendere un sottotipo di un tipo generico, ma solo il tipo stesso 
>```java
>static public void esamina(ArrayList < Frutto> frutti){
>// non funziona se passo un ArrayList\<Arancia>
>}
>```
> 
>- ma posso vincolare meglio per fare in modo che funzioni
>```java
>static publc < T extends Frutto> void
>	esamina(ArrayList\<T> frutti)
>```
>per non creare problemi, non è quindi possibile fare l'upcasting (o, per esempio, si potrebbe aggiungere una pera a un insieme di mele)

>[!info]+ upcasting con array
>l'upcasting è però possibile **a tempo di compilazione** con gli array, ma a tempo di esecuzione si ottiene un'eccezione

#### il jolly "?"
nel caso in cui non sia necessario utilizzare il tipo generico `T` nel corpo della classe o del metodo, è possibile usare il **jolly** `?` 
```java
public static void mangia
	(Arraylist<? extends Mangiabile> frutta){}
```
che è equivalente a 

```java
public static void mangia
	(Arraylist<T extends Mangiabile> frutta){}
```
ma senza la notazione del tipo che si utilizza.

- <font color="#8db3e2">esempio</font>:
```java
public class Punto<T extends Number>{
	private T x;
	private T y;

	// bla bla bla

	public static void main(String[] args){
	Punto<?> p = new Punto<Integer>(10, 42);
	System.out.println(p);
	
	p = new Punto<Double>(11.0, 43.5);
	<System.out.println(p);
	}
}
```

##### dietro le quinte
dietro le quinte avviene la **cancellazione del tipo**.
quando il compilatore traduce il metodo o la classe in bytecode:
- **elimina la sezione del tipo parametrico** e lo sostituisce con quello reale
- per default il tipo generico viene **sostituito con** `Object`
- viene creata *solo una copia* del metodo/classe
 
![[cancellazione dei tipi java.png|center|400]]

>[!warning] ottenere informazioni sull'istanza di un generico
>per via della cancellazione del tipo, non possiamo 