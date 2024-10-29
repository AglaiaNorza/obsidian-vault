
> [!info]- index
> - [[#classe|classe]]
> - [[#oggetto|oggetto]]
> - [[#file sorgenti|file sorgenti]]
> - [[#campi|campi]]
> 	- [[#campi#inizializzazioni implicite|inizializzazioni implicite]]
> - [[#metodi|metodi]]
> 		- [[#inizializzazioni implicite#chiamate di metodi|chiamate di metodi]]
> - [[#costruttori|costruttori]]
> 	- [[#costruttori#creazione di un oggetto|creazione di un oggetto]]
> - [[#variabili locali vs campi|variabili locali vs campi]]
> - [[#classi e metodi final|classi e metodi final]]


possono:
- modellare oggetti nel mondo reale
- rappresentare oggetti grafici, entità software, concetti astratti, stati di un processo

#### classe
prototipo astratto per gli oggetti di un particolare tipo.
Ne definisce la struttura in termini di:
- campi - **stato** degli oggetti (variabili d'istanza) - tipicamente sono *privati*
- **metodi** - comportamenti dell'oggetto

#### oggetto
è un'**istanza** di una classe.
Un programma può creare e usare uno o più oggetti della stessa classe.

![[classe vs oggetto.png]]

| **classe**                                                             |     | **oggetto**                                                                        |
| ---------------------------------------------------------------------- | --- | ---------------------------------------------------------------------------------- |
| definita nel *codice sorgente*                                         |     | si trova all'interno di un programma<br>*in esecuzione*                            |
| scritta da chi programma                                               |     | creato nel runtime di un programma                                                 |
| specifica la *struttura* (numero e tipi)<br>dei campi dei suoi oggetti |     | contiene *specifici valori* dei campi, che<br>possono variare durante l'esecuzione |
| specifica il comportamento dei suoi<br>oggetti tramite i metodi        |     | si comporta nel modo descritto nella <br>classe quando il metodo viene *chiamato*  |


****
#### file sorgenti
- ogni classe è memorizzata in un **file separato**
- il **nome** del file deve essere lo **stesso della classe**, con estensione .java, iniziare con una maiuscola e seguire la CamelCase
- i nomi sono case-sensitive.
 
>[!info] struttura del codice di una classe
> 
![[anatomia classe.png]]

- [[esempio - classe contatore]]

*****
#### campi
o variabili d'istanza
- costituisce la memoria privata di un oggetto
- ha un tipo di dati e un nome 
 
>[!info] dichiarazione di un campo:
>```java
> private [static] [final] tipo_di_dato nome;
>```

- *static* - se specificato, indica che il campo è condiviso da tutti
- *final* - se specificato, indica che il campo è una costante (non è modificabile)

##### inizializzazioni implicite 
al momento della creazione di un oggetto, i campi di una classe sono inizializzati automaticamente:

| campo            |     | inizializzato a |
| ---------------- | --- | --------------- |
| int, long        |     | 0, 0L           |
| float, double    |     | 0.0f, 0.0       |
| char             |     | '\0'            |
| boolean          |     | False           |
| classe qualsiasi |     | null            |
questo succede per i campi di una classe, ma non per le variabili locali dei metodi

#### metodi
- tipicamente *pubblici* (visibili a tutti)
- nomi iniziano con la minuscola e seguono la camelCase
- possono (ma non devono) avere parametri d'ingresso e restituire valori 
 
>[!info] definizione di un metodo:
>```java
> public tipo_dati nomeMetodo(tipo_dati_in nomeParam...)
> {
> // istruzioni
> }
>```
- dopo public - valore restituito - `void` se nessun valore
- tra le parentesi - parametri in ingresso

>[!tip] this
>`this.var` risolve conflitti di omonomia se in un metodo (es. costruttore) si passano argomenti con lo stesso nome di variabili
>> [!example] esempio
>>```java
>>public Persona(String nome, String cognome){
>>	this.nome = nome;
>>	this.cognome = cognome;
>>} 
>>//qui, this.nome si riferisce al campo "nome" della classe Persona 
>>//(che sarà tra i campi)
>>```

>[!example]- esempi
>```java
>public void reset(int newValue)
>{
>	value = newValue;
>}
>```
>```java
>public int getValue()
>{
>	return value;
>}
>```

###### chiamate di metodi
- il numero e i tipi di parametri(argomenti) passati a un metodo deve coincidere con i parametri formali del metodo


#### costruttori
metodi per la **creazione di oggetti** di una classe.
- **stesso nome** della classe.
- inizializzano i campi dell'oggetto.
- prendono zero, uno o più parametri.
- **non hanno valori di uscita** ma non specificano void
- non è obbligatorio specificare un costruttore - se non viene specificato, il compilatore ne crea uno di default (pubblico e vuoto - non fa nulla)

>[!danger] overloading
>Java permette di sovraccaricare le segnature dei metodi.
> - Si possono specificare **metodi con lo stesso nome**, che abbiano numero e/o tipo di parametri diversi, e Java saprà quali chiamare.

>[!example] esempio:
>```java
>//costruttore classe
>public Counter()
>{
>	value = 0;
>}
>//costruttore classe con valore iniziale
>public Counter(int initialValue)
>{
>	value = initialValue;
>}
>```
>il primo costruttore si chiama senza parametri d'ingresso, il secondo passandogli un intero (Java sa quale stai chiamando in base a se passi un valore o no)

##### creazione di un oggetto
un oggetto viene creato con l'operatore `new`.
```java
static public void main(String[] args)
{
	Counter contatore1 = new Counter();
	Counter contatore2 = new Counter(42);

	System.out.println("Valore del contatore1: " + contatore1.getValue());
	System.out.println("Valore del contatore2: " + contatore2.getValue());
}
```
il main è statico - non serve creare l'istanza della classe che lo riconosce.
- Main e Counter possono ma non devono essere nella stessa classe (/file), basta che main sia in una classe che vede Counter.

****
#### variabili locali vs campi

| *campi*                                                                  |     | *variabili locali*                                                                           |
| ------------------------------------------------------------------------ | --- | -------------------------------------------------------------------------------------------- |
| variabili dell'**oggetto**                                               |     | variabili di un **metodo**                                                                   |
| visibili almeno all'interno di tutti gli oggetti della <br>stessa classe |     | esistono da quando sono definite fino al termine dell'esecuzione<br>della chiamata al metodo |
| esistono per tutta la vita di un oggetto                                 |     |                                                                                              |







#### classi e metodi final
Per quanto riguarda le classi e i metodi, la parola chiave `final` permette di impedire ad altri programmatori di:
- creare sottoclassi - se si tratta di una classe final
- sovrascrivere metodi - se si tratta di metodi final