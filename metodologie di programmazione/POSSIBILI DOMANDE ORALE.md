## slide 2/4 (oggetti)

>[!Question]- incapsulamento: cos'è e perché farlo
>- l'**incapsulamento** è il processo che nasconde i dettagli realizzativi (campi e implementazione), rendendo pubblica un’interfaccia (metodi pubblici).
>- aiuta a *modularizzare* lo sviluppo, creando un funzionamento "a scatola nera"
>- non è sempre necessario sapere tutto
>- facilita la maintenance

>[!Question]- parola chiave "static" (contributo slide più avanti: classi statiche)
>campi
>- un campo statico è relativo all'**intera classe** e non a un'istanza.
>- esiste in una sola locazione di memoria (nel MetaSpace)
> 
>metodi
>- si può accedere a un metodo statico da dentro una classe con la sua segnatura, o da fuori con la segnatura `Classe.metodo()`
>
>classi
>- una classe interna static non richiede l'esistenza di un oggetto della classe che la contiene e non ha riferimento implicito ad essa
>- non ha accesso allo stato degli oggetti della classe che la contiene

>[!Question]- enumerazioni
>- sono dei tipi i cui valori possono essere scelti tra un **insieme predefinito** di identificatori univoci.
>- le costanti enumerative sono implicitamente static
>- non è possibile creare un oggetto di tipo enum
>- il compilatore genera un metodo statico `values` che restituisce un array delle enum

>[!Question]- classi wrapper
>- permettono di convertire i valori dei primitivi in oggetti
>- sfruttano i meccanismi di **auto-boxing** (conversione automatica di un primitivo al suo wrapper) e **auto-unboxing** (l'inverso)

## slide 5/6 (ereditarietà e polimorfismo)

>[!Question]- classi e metodi astratti
>- una classe astratta non può essere istanziata, ma verrà estesa da classi che possono essere istanziate
>- un metodo astratto (definibile esclusivamente in una classe astratta) non viene implementato (ma solo definito con la sintassi `abstract tipo nome();`) - **tutte le classi non astratte che estendono una classe astratta devono implementare i suoi metodi astratti**

>[!Question]- this e super nei costruttori
>entrambi vanno collocati obbligatoriamente nella prima riga del costruttore.
>- `this` permette di chiamare un altro costruttore della stessa classe
>- `super` permette di chiamare il costruttore della superclasse
>se la superclasse non fornisce un costruttore senza argomenti, la sottoclasse deve esplicitamente definire un costruttore (infatti una sottoclasse deve necessariamente chiamare il costruttore della sua superclasse)

>[!Question]- differenza tra overriding e overloading
>- l'overriding è una ridefinizione (reimplementazione) di un metodo c**on la stessa segnatura** di una sopraclasse
>	- gli argomenti devono essere gli stessi
>	- il tipo di ritorno deve essere compatibile (lo stesso o una sua sottoclasse)
>	- non si può ridurre la visibilità
>- l'overloading è la creazione di un metodo con lo stesso nome ma con una **segnatura alternativa**
>	- i tipi di ritorno possono essere diversi (ma questo non può essere l'unico cambiamento)
>	- si può variare la visibilità a piacimento

>[!Question]- tipi di visibilità
>- **private** - visibile solo all'interno della classe
>- **public** - visibile a tutti
>- **default/package** - visibile all'interno del pacchetto
>- **protected** - visibile all'interno del pacchetto e alle sottoclassi

>[!Question]- is-a vs has-a
>- is-a rappresenta l'**ereditarietà**
>- has-a rappresenta la **composizione** - un oggetto contiene come membri riferimenti ad altri oggetti

>[!Question]- cos'è il polimorfismo?
>- il polimorfismo permette a una variabile di un certo tipo di contenere un riferimento a un oggetto di qualsiasi sua sottoclasse.
>- vengono chiamati i metodi in base al tipo effettivo dell'oggetto
>- il polimorfismo sfrutta il **binding dinamico** - l'associazione tra una variabile e un metodo viene stabilita a runtime

>[!Question]- come funzionano le conversioni con il polimorfismo?
>- si può creare un oggetto di una sottoclasse e assegnarlo a una variabile della superclasse
>- per fare `downcasting`, invece, serve casting esplicito
>- quando si fa `upcasting`, si possono chiamare solo i metodi e vedere solo i campi della superclasse

>[!Question]- classi e metodi final
>- la parola chiave final impedisce di creare sottoclassi o di reimplementare metodi

## slide 7 (interfacce)

>[!Question]- cos'è un'interfaccia?
>- un'interfaccia specifica il **comportamento** che un oggetto deve presentare all'esterno - l'implementazione delle operazioni non viene definita
>- un'interfaccia è una classe astratta al 100%

>[!Question]- caratteristiche (componenti) delle interfacce
>- è possibile definire implementazione di metodi statici o di default all'interno di un'interfaccia (i metodi statici non godono di polimorfismo vs google : Default methods allow you to add methods to existing interfaces without breaking existing implementations.)
>- tutti i metodi di un'interfaccia sono implicitamente `public abstract`
>- tutti i campi di un'interfaccia sono implicitamente `public static final`
>- in Java è permessa l'implementazione di molteplici interfacce, mentre non è permessa l'ereditarietà multipla

>[!Question]- iterable e iterator
>- iterator è un'interfaccia che permette di iterare su collezioni. espone i metodi `hasNext()`, `next()` e `remove()`
>- iterator è in relazione con l'interfaccia `Iterable` - chi implementa `Iterable` restituisce un `Iterator`

>[!Question]- classi nested e inner
>- le classi presenti all'interno di altre classi si chiamano **nested classes**. queste si definiscono **inner** se non sono statiche.
>- per istanziare una classe inner, è necessario prima istanziare la classe esterna che la contiene. (ogni classe interna ha un riferimento implicito alla classe che la contiene). dalla classe interna si può accedere a tutte le variabili e a tutti i metodi della classe esterna.
>- una classe annidata statica non richiede l'esistenza di un oggetto della classe esterna, e non ha riferimenti impliciti ad essa.