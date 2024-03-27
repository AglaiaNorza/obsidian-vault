---
sticker: lucide//grip
---
- spesso è utile definire dei tipi detti **enumerazioni**, i cui valori possono essere scelti tra un insieme predefinito di identificatori univoci:
	- ogni identificatore corrisponde a una **costante**

- le **costanti enumerative** sono implicitamente **static**
- non è possibile creare un oggetto del tipo `enum` - quindi un'enumerazione ha tante istanze quante sono le costanti enumerative al suo interno
--- 
- le classi enumerative estendono la classe Enum, da cui ereditano i metodi `toString()` (restituisce il nome della costante) e `clone()` (restituisce l'oggetto enumerativo stesso senza farne copie, il che è impossibile)
- Enum a sua volta estende Object, quindi `equals()` restituisce `true` solo se le costanti enumerative sono identiche

--- 
un tipo enumerato viene dichiarato con la sintassi:
```java
public enum NomeEnumerazione{
	COSTANTE1, COSTANTE2,..., COSTANTEN;
}
//in realtà il punto e virgola è opzionale
```

>[!example]- esempio
>esempio: seme e valore di una carta
>```java
>public enum SemeCarta{
>CUORI, QUADRI, FIORI, PICCHE;
>}
>```

Come tutte le classi, la dichiarazione di un'enumerazione può contenere altre componenti tradizionali:
- costruttori
- campi
- metodi
--- 
#### costruzione istanze costanti
Non si possono creare nuove istanze, ma possono essere costruite le istanze "costanti":
- Si definisce un costruttore (NON pubblico, ma con *visibilità di default*)
- Si costruisce ciascuna costante (un oggetto separato per ognuna)
- Si possono definire altri metodi di accesso o modifica dei campi
--- 


###### esempio - classe mese: 
```java
//senza enumerazione
public class Mese{

	private int mese;

	//costruttore
	public Mese(int mese) {this.mese = mese;}

	public int toInt() {return mese;}

	public String toString(){
		switch(mese)
		{
		case 1: return "GEN";
		case 2: return "FEB";
		//eccetera
		default: return null;
		}
	}
}

//con enumerazione
public enum Mese{

	GEN(1), FEB(2), MAR(3), APR(4), 
	MAG(5), GIU(6), LUG(7), AGO(8),
	SET(9), OTT(10), NOV(11), DIC(12);

	private int mese;

	//costruttore delle costanti enumerative
	Mese(int mese){this.mese = mese}

	public int toInt() {return mese;}

}

```

#### metodi statici value:
- per ogni enumerazione, il compilatore genera il metodo statico `values()` che restituisce un **array delle costanti enumerative**
- viene generato anche `valueOf()`, che restituisce la **costante enumerativa associata alla stringa** fornita in input
	- se il valore non esiste, viene emessa un'eccezione

#### enumerazioni e switch:
le enumerazioni possono essere utilizzate all'interno di un costrutto switch:
```java
SemeCarta seme = null;

switch(seme){

	case CUORI: System.out.println("comeE"); break;
	
}
```

