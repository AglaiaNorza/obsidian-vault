---
sticker: lucide//file-warning
---
Le eccezioni in Java sono ben definite.

| eccezione                    | descrizione                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| `IndexOutOfBoundsException`  | accesso ad una posizione non valida di un array o una stringa             |
| `ClassCastException`         | cast illecito di un oggetto a una sottoclasse a cui non appartiene        |
| `ArithmeticException`        | condizione aritmetica non valida                                          |
| `CloneNotSupportedException` | metodo `clone()`  non implementato o errore durante la copia dell'oggetto |
| `ParseException`             | errore inaspettato durante il parsing                                     |
| `IOError` e `IOException`    | grave errore di input o output                                            |
| `IllegalArgumentException`   | parametro illegale come input di un metodo                                |
| `NumberFormatException`      | errore nel formato di un numero (estende `Illegal...`)                    |
|                              |                                                                           |

![[eccezioni java.png| 400]]

>[!question]- perché non restituire un valore di errore?
>- perché bisognerebbe restituire un valore "speciale" per ogni tipo di errore e prevedere una codifica dei valori di errore comuni a tutti i metodi
>- perché bisognerebbe gestire gli errori per ogni istruzione eseguita

>[!info]- vantaggi/svantaggi delle eccezioni
>- gli errori vengono propagati verso l'alto lungo lo stack di chiamate
>- **codice più robusto**: il polimorfismo controlla per noi il tipo di errore
><br/>
>- l'onere di gestire gli errori si sposta sulla **JVM** che **deve decidere** il modo più opportuno per gestire la situazione

##### <font color="#dbe5f1">cosa si può gestire con le eccezioni</font>

**<font color="#9bbb59">SI PUÒ GESTIRE</font>**
- **errori sincroni**, che si verificano dopo l'esecuzione di un'istruzione
	- **errori non critici**, che derivano da condizioni anomale (es. divisione per zero)
	- **errori critici** interni alla JVM:
		- conversione di tipo non consentita
		- accesso a una variabile null
		- mancanza i memoria
		- riferimento a una classe inesistente

** <font color="#c0504d">NON SI PUÒ GESTIRE</font>**
- **eventi asincroni** (click del mouse, ricezione messaggi su rete)
- eventi che avvengono **parallelamente** all'esecuzione, e quindi **indipendenti dal flusso di controllo**

#### blocco try-catch
il blocco try-catch consente di catturare le eccezioni

- **blocco try**
 
nel blocco try si inseriscono le istruzioni dalle quali vengono sollevate le eccezioni che vogliamo catturare
```java
//bla bla
try{
	armadietto.apriArmadietto(bolt);
}
catch ...//vedi dopo
```

- blocco **catch**
 
nel blocco catch si specifica il *tipo di eccezione* da catturare e cosa fare nel caso l'eccezione sia sollevata.
- è possibile specificare *molteplici blocchi catch* per diverse eccezioni
```java
try{
	//try
}
catch(NonToccareLaMiaRobaExc e){
	//cosa faccio se eccezione
}
catch(ArmadiettoGiApertoExc e1){
	//cosa faccio se aperto
}
```

>[!warning] l'ordine conta!
>è importante considerare l'ordine con cui si scrivono i diversi blocchi catch e catturare le eccezioni **da quella più specifica a quella più generale**, poiché la JVM sceglie il *primo catch compatibile*

da Java 7 in poi, è possibile specificare un'unica clausola catch con diversi tipi di eccezione utilizzando l'operatore `|`:
```java
try{//bla bla
	if(condizione) throw new Ecc1();
	else throw new Eccezione2();
}
catch(Ecc1 | Ecc1){//bla bla
}
```

#### flusso in presenza e assenza eccezioni
Se durante l’esecuzione **non vengono sollevate eccezioni**:
- ciascuna istruzione all’interno del blocco try viene eseguita normalmente
- terminato il blocco try, l’esecuzione riprende dalla *prima linea dopo il blocco try-catch*

Se viene sollevata un’eccezione:
- L’esecuzione del blocco try viene interrotta
- Il controllo passa al **primo blocco catch compatibile** (tale che il tipo dichiarato nella clausola catch sia dello stesso tipo dell’eccezione sollevata, o un suo super-tipo)
- L’esecuzione riprende dalla *prima linea dopo il blocco try-catch*

#### politica catch-or-declare
una volta sollevata un'eccezione, possiamo:
- **ignorare** l'eccezione e *propagarla* al metodo chiamante, ma aggiungendo all'intestazione del metodo la clausola `throws` seguita dalle eccezioni potenzialmente sollevate (*declare*)
- **catturare** l'eccezione, gestendo la situazione anomala in modo opportuno e prendendo provvedimenti (*catch*)

se il requisito catch-or-declare non viene soddisfatto, il compilatore dà un errore che indica che l'eccezione deve essere catturata o dichiarata.
##### ignorare le eccezioni
se intendiamo ignorare le eccezioni, siamo costretti a **dichiarare esplicitamente il suo sollevamento** con `throws`.

il costrutto dichiara che il metodo può sollevare eccezioni dello stesso tipo (o un sottotipo) di quelle elencate dopo `throws`.

se tutti i metodi all'interno dell'albero delle chiamate dell'esecuzione decidono di ignorare l'eccezione, l'esecuzione viene **interrotta**.
 
![[ignorare le eccezioni java.png|centre|400]]


#### il blocco finally
è un blocco speciale posto dopo tutti i blocchi try-catch, che viene eseguito **a prescindere dal sollevamento di eccezioni** - le istruzioni nel blocco `finally` vengono SEMPRE eseguite (anche se nel blocco try-catch c'è un return, un break, un continue)
- l'unico caso in cui non vengono eseguite è con l'utilizzo di `System.exit()`

Tipicamente, all'interno del blocco `finally`, vengono eseguite operazioni di clean-up (chiusura file aperti, rilascio risorse...)

#### la classe Throwable
la classe che implementa le eccezioni è `Throwable`, che estende direttamente Object.
(gli oggetti di tipo `Throwable` sono gli unici che è possibile utilizzare con il meccanismo delle eccezioni)

la classe `Throwable` ha come sottoclassi:
- `Exception` 
	- eccezioni interne alla JVM (classe `RuntimeException`)
	- eccezioni regolari (`IOException`, `ParseException` ecc)
- `Error` - cattura l'idea di condizione **irrecuperabile** (casi rari)

Le eccezioni possono essere di tipo **checked** e **unchecked**:
 
![[error exception java.png |centre|400]]

**checked**:
- è sempre necessario attenersi al paradigma *catch-or-declare*
- eccezioni comuni, che estendono `Exception`

**unchecked**:
- non si è obbligati a dichiarare le eccezioni sollevate o a catturarle, ma è possibile farlo
- eccezioni che estendono `Error` o `RuntimeException`

