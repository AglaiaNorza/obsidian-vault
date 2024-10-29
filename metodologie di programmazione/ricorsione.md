>[!Info] come funziona?
>- ogni volta che viene effettuata una chiamata a un metodo viene creato un **nuovo ambiente**, un "*record di attivazione*"
>- il record di attivazione contiene la zona di *memoria per le variabili locali* del metodo e l'*indirizzo di ritorno al metodo chiamante* - ad ogni chiamata, il record corrispondente viene aggiunto sullo stack
>- lo **stack** è la pila dei record di attivazione delle chiamate annidate effettuate

definizione ricorsiva di un fattoriale:
```java
public int fattorialeRicorsivo(int n){

	if(n == 0) return 1;
	return n*fattorialeRicorsivo(n-1);
}
```

> [!Example]+ riconoscere una stringa palindroma
> ```java
> public class Palindroma{
> 
> 	public boolean isPalindroma(String s){
> 		return isPalindroma(s, 0, s.length()-1);
> 	}
> 
> 	public boolean isPalindroma(String s, int a, int b){
> 	
> 		if(a>b) return true;
> 		
> 		return s.charAt(a) == s.charAt(b)
> 			&& isPalindroma(s, a+1, b-1)
> 			
> 	}
> }
> ```

- è buon uso (mia assumption) avere *due metodi* - uno pubblico che chiama la ricorsione, e uno privato che la svolge 

>[!Tip] mutua ricorsione
>- si verifica quando due metodi *si richiamano tra loro*.
>- è necessario fare attenzione ai casi base per evitare una ricorsione infinita
>>[!Example]- controlla numeri pari dispari
>>```java
>>public class PariDispari{
>>
>>	public boolean pariDispari(Arraylist< Integer> l){
>>		return pariDispari(l, 0);
>>	}
>> 		
>> 	 private boolean pariDispari(ArrayList< Integer> l, int k){
>> 		 if(k == l.size()) return true;
>> 		 return(l.get(k)% 2 == )
>> 	 }
>>	
>>	
>>	
>>	
>>
>>}
>>```

##### strutture dati ricorsive
anche le *strutture dati* possono essere ricorsive:
```java
public class Lista{

	private int k;
	private Lista succ; 
	
	//bla bla bla
}
```
- è ricorsiva perché, nella sua definizione, utilizza come campo una `Lista` stessa
