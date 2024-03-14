---
sticker: lucide//chevrons-right
---
#### while
- le istruzioni sono eseguite fino a quando la condizione è vera
- la condizione viene controllata ad ogni ciclo
```java
while(<condizione booleana>){
	<istruzioni>;
}
```

##### do while:
- si comporta come il while, ma la condizione viene controllata alla fine di ogni ciclo e non all'inizio (prima fa, poi vede)

```java
do{
	<istruzioni>;
}
while(<condizione booleana>)
```

##### for:
sintassi:
- inizializzazione di una variabile
- espressione booleana
- incremento
- istruzioni
```java
//più istruzioni
for (<iniz.>; <espr. booleana>; <incremento>){

	<istruzioni>;
	
}
```
 
```java
//singola istruzione
for (<iniz.>; <espr. booleana>; <incremento>)
	<istruzione>;
```

>[!danger] "two for one"!
>Le istruzioni di inizializzazione e incremento possono riferirsi a più variabili (quasi come mettere due for in uno):
>```java
>for (int k = 0, i = 0; i<=10; i++, k+=5)
>```
>Le istruzioni di inizializzazione e incremento possono riferirsi a più variabili (quasi come mettere due for in uno):
>
> - è il punto e virgola che divide la fine di una "sezione" - due cose nella stessa sezione sono separate da virgola

##### uscire da un ciclo
- istruzione `break` - esce dal ciclo che lo contiene

per **uscire da cicli annidati**, si può dare un'**etichetta** prima da un ciclo e uscire da quel ciclo con `break <etichetta>`
```java
outer:
for (int i=0; i<h; i++){

	for (int j=0; j<w; j++){
	//codice

	if (j==i) break outer;
	}
}
//break outer ti porta qui
```

##### saltare all'iterazione successiva
- istruzione `continue` - salta l'iterazione corrente
```java
for (int i=0; i<h; i++){
	if (s.charAt(i) != "c") continue
}
```


