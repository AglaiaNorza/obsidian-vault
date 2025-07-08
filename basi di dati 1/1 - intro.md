---
created: 2025-05-13T21:40
updated: 2025-07-08T09:48
---
- Un **database** è un insieme di file mutualmente connessi, organizzati in strutture di dati che ne facilitano la gestione.
- I **Database Management Systems** sono strumenti software per la gestione di grandi masse di dati.

Un'informazione in formato elettronico può essere registrata come:
- *dato strutturato* - gli oggetti sono rappresentati da brevi stringhe di simboli e da numeri
- *dato non strutturato* - testi scritti in un linguaggio naturale

>[!info] obiettivo di una base di dati
>facilitare l'elaborazione di dati sulla base delle loro **relazioni**

esistono due tipi principali di modelli:
- **modelli logici** - indipendenti dalle strutture fisiche ma disponibili nel software
- **modelli concettuali** - indipendenti dalle modalità di realizzazione, rappresentano le entità nel mondo reale e le loro relazioni nelle prime fasi della progettazione

Gli elementi di un modello relazionale sono:
- **oggetto** - un Record
- **campi** - informazioni di interesse

questi elementi sono intesi come tuple, e vengono raccolti in una tabella (**istanza**)

>[!info] i tre livelli di astrazione di un database
>![[astrazione-db.png|500]]
>- *schema esterno* - descrizione di una porzione della base di dati in un modello logico attraverso viste parziali, che riflettono esigenze e privilegi di particolari tipi di utenti
>- *schema logico* - descrizione del database nel modello logico principale del DBMS
>- *schema fisico* - rappresentazione dello schema logico per mezzo di strutture fisiche di memorizzazione (file)

>[!tip] indipendenza dei dati
>i dati sono indipendenti a livello: 
>- fisico: il livello logico e quello esterno sono indipendenti da quello fisico
>- logico:  il livello esterno è indipendente da quello logico (aggiunte o modifiche alle viste non richiedono modifiche al livello logico)

> in ogni base di dati, esistono:
> - lo **schema**, invariante nel tempo - ne descrive la scrittura (intestazione delle tabelle: lista di attributi e i loro tipi)
> - l'**istanza** - i valori attuali, che possono cambiare anche molto rapidamente
> (in una tabella, l'intestazione della tabella è lo schema e i dati sono l'istanza)

- i dati devono soddisfare dei "vincoli" che esistono nella realtà di interesse
- i dati devono essere protetti da accessi non autorizzati; il DBA deve considerare:
	- il valore corrente dell'informazione per l'organizzazione
	- il valore corrente dell'informazione per chi vuole violare la privatezza
	- chi può accedere a quei dati e in quale modo
	e decidere: regolamento di accesso ed effetti di una violazione 

>[!info] transazione
>Una **transazione** è una sequenza di operazioni che costituiscono un'unica operazione logica - deve essere eseguita completamente (*committed*) o non deve essere eseguita affatto (*rolled back*)

per ripristinare un valore corretto della base di dati si usano:
- transaction log (con dettagli delle operazioni, valori precedenti e seguenti alla modifica)
- dump (copia periodica del DB)