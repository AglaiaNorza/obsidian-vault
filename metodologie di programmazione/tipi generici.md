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