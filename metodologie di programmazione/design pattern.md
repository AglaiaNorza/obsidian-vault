#### strategy pattern
- progettiamo un'**interfaccia funzionale** per ogni comportamento
- per ogni possibile tipo di comportamento *implementiamo l'interfaccia*

![[interfacce e comportamenti .png|center|500]]
![[esempio anatra comportamenti.png|center|500]]

#### observer observable

> [!Example] esempio
> un esempio valido è quello di un abbonamento:
> - ci si abbona a un determinato settimanale e, ogni volta che viene stampata una nuova edizione, questa viene consegnata.
> - si cancella l'abbonamento quando non si vogliono più ricevere copie, ma l'abbonamento rimane "disponibile"

![[observer observable.png|center|500]]

- è essenziale che le classi osservabili **non dipendano** da quelle che osservano


| metodo                            | cosa fa                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `void addObserver(Observer o)`    | aggiunge un observer alla lista di observer dell'oggetto                                                                         |
| `void deleteObserver(Observer o)` | elimina un dato observer dalla lista di observer dell'oggetto                                                                    |
| `void deleteObservers()`          | elimina tutti gli observers dalla lista                                                                                          |
| `void notifyObservers()`          | se l'observable è cambiato, notifica tutti gli osservatori e chiama il metodo `clearChanged` per indicare che non è più cambiato |
| `void clearChanged()`             | indica che il metodo non è più cambiato                                                                                          |
| `protected void setChanged()`     | segna questo oggetto come "cambiato" - ora `hasChanged` ritornerà `true`                                                         |
| `boolean hasChanged()`            | testa se l'oggetto è cambiato                                                                                                    |



#### builder 
- pattern per la **creazione di oggetti**
- utile quando si hanno *molti parametri*, tra cui alcuni opzionali - infatti creare troppi costruttori rende poco agevole la progettazione

##### passi per il pattern
1) crea una **nuova classe** - tipicamente `ClasseBuilder` con "Classe" = classe che si vuole costruire
	- `ClasseBuilder` può anche essere una classe statica annidata all'interno di `Classe` (in quel caso, si chiamerà solo builder - `Classe.Builder`)
	- il costruttore di `Classe` viene impostato come privato o si usa la visibilità di package se `ClasseBuilder` non è annidato
2) `ClasseBuilder` ha metodi per l'impostazione dei valori iniziali dei campi dell'oggetto da costruire
	- ciascuno dei metodi restituisce l'istanza del builder (`this`) così da poter effettuare chiamate in cascata
3) `ClasseBuilder` è dotata di un metodo `build`, che restituisce un'istanza di `Classe` o una sua sottoclasse secondo le impostazioni specificate
4) `ClasseBuilder` può essere dotata di un costruttore per obbligare l'impostazione iniziale di uno o più campi dell'oggetto da costruire

>[!info] vantaggi e svantaggi
>**vantaggi**:
>- permette di rendere *più flessibile* la costruzione di oggetti con più parametri
>- rende il codice di costruzione più leggibile
>- evita il passaggio di parametri poco chiari ed evita stati intermedi non validi dell'oggetto costruito
>
>**svantaggi**:
>- la costruzione richiede *più chiamate* a metodi


#### singleton
- serve a creare **classi con un'unica istanza**
1) privatizzare tutti i costruttori e, se non presenti, privatizzare quello di default
2) inizializzare un campo statico privato `instance`
	- il campo sarà il riferimento all'unica istanza della classe - ottenibile tramite il metodo `getInstance()`
	- l'implementazione di `getInstance()` è sempre la stessa

```java
public class Paperino{

	static private Paperino instance;

	static public Paperino getInstance(){
		if(instance==null){
		istanza = new Paperino();} 
		
		return istanza;
	}
	
	private Paperino(){
		//costruzione dell'unico oggetto
	}
}
```

>[!info] principio di design
>fa in modo che la classe *modelli la realtà* e non permetta cose concettualmente insensate
>

#### decorator
- serve ad aggiungere **nuove responsabilità** a un oggetto **senza che esso lo sappia**

il decorator:
- estende la classe astratta dell'oggetto
- è costruito con un'istanza concreta della classe astratta dell'oggetto
- inoltra le richieste di tutti i comportamenti all'oggetto (componente)
- effettua azioni aggiuntive

![[decorator pattern.png|center|500]]

>[!info] principio di design
>le classi dovrebbero essere **aperte all'estensione ma chiuse alla modifica** (Open-Closed Principle)

#### command/callback
- a volte è necessario effettuare richieste ad oggetti senza sapere nulla sull'operazione richiesta
- l'operazione va eseguita **in futuro**, quando necessario - è necessario rendere l'operazione modulare, in modo che possa essere associata a un oggetto (diverse associazioni possono essere fatte dinamicamente)

##### implementazione
1) si crea un'**interfaccia** che espone il metodo generale
	- ogni funzione concreta implementa l'interfaccia `Callback`
	- 