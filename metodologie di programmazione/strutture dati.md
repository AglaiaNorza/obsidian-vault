### collection
Strutture dati già pronte all'uso con interfacce e algoritmi per manipolarle.
- contengono e "strutturano" riferimenti ad altri oggetti, tipicamente dello stesso tipo.

alcune interfacce:

| interfaccia | descrizione                                                                              |
| ----------- | ---------------------------------------------------------------------------------------- |
| Collection  | interfaccia alla radice                                                                  |
| Set         | collezione **senza duplicati**                                                           |
| List        | collezione **ordinata** che può contenere **duplicati**                                  |
| Map         | associa coppie **(chiave, valore)**, *senza chiavi duplicate* (vedi dizionari in python) |
| Queue       | collezione **first-in, first-out** (fifo)                                                |
>[!info]- gerarchia delle interfacce
>![[collection gerarchia.png | 500]]

##### iterazione esterna su una collezione
1) mediante gli **iterator**:
```java
Iterator<Integer> i = collezione.iterator()
while(i.hasNext()){
	int k = i.next();
	System.out.println(k);
}
```
2) mediante il costrutto **for each**:
```java
for(Integer k: collezione)
	System.out.println(k);
```
4) (solo su liste) mediante **indici** 
```java
for(int j=0; j<collezione.size(); j++){
	int k = collezione.get(j)
	System.out.println(k)
}
```
##### iterazione interna su una collezione
- il metodo `Iterable.forEach` permette l'iterazione su *qualsiasi collezione* senza specificare come effettuare l'iterazione
	- utilizza il **polimorfismo** (chiamerà il `forEach` della classe specifica)
- `forEach` prende in input un **Consumer**, un'*interfaccia funzionale*


in my dream house, i have:
- (c-words: cats and cups)
- electric boiler
- printer 
- fortnite in the AM (videogames)
- decent wifi
- list comprehensions
- muji
- arnica

