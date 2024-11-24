## visione d'insieme
I **file** sono l'elemento principale per la maggior parte delle applicazione (fanno spesso da input e output). 
- "sopravvivono" ai processi (a differenza della RAM dei processi, che viene sovrascritta)

proprietà desiderabili dei file:
- esistenza a lungo termine
- condivisibilità con altri processi (tramite nomi simbolici)
- strutturabilità (directory gerarchiche)
### gestione dei file
i file sono gestiti dal **File Management System** - insieme di programmi e librerie di utilità che vengono eseguiti in *kernel mode*.
- le librerie, invece, vengono invocate come syscall (sempre in kernel mode)

Hanno a che fare con la memoria secondaria (dischi, USB...).
- in Linux, invece, selezionate porzioni di RAM possono essere trattate come file

Forniscono un'astrazione sotto forma di operazioni tipiche, e per ogni file vengono mantenuti degli attributi (*metadati*) - proprietario, data di creazione ecc.

> [!summary] operazioni su file
> Le operazioni tipiche su file sono:
> - creazione (e scelta del nome)
> - cancellazione
> - apertura
> - lettura (solo su file aperti)
> - scrittura (solo su file aperti)
> - chiusura (necessaria per la performance)

### terminologia
Si introduce della terminologia utile:

**campi**
- dati di base
- contengono valori singoli
- caratterizzati da lunghezza e tipo di dato
- es. carattere ASCII

**record**
- insieme di campi correlati, ognuno trattato come un'unità
- es. un impiegato ha i record nome, cognome, matricola ecc.

**file**
- hanno un nome
- sono insiemi di record correlati
	- nei Sistemi Operativi generici moderni, ogni record è un solo campo con un byte
- ognuno trattato come un'unità con nome proprio
- possono implementare meccanismi di controllo all'accesso

**database**
- collezione di dati correlati
- mantengono relazioni tra gli elementi memorizzati
- vengono realizzati con uno o più file
- i DBMS (database managing systems) sono tipicamente processi di un Sistema Operativo 

### file managing systems
I sistemi per la gestione di file forniscono servizi agli utenti e alle applicazioni per l'uso di file, e definiscono il modo in cui i file sono usati.
#### obiettivi
- rispondere alla *necessità* degli utenti riguardo la gestione dei dati
- garantire he i dati nei file siano *validi*
- ottimizzare le *prestazioni* (sia dal punto di vista del Sistema Operativo - throughput - che dell'utente - tempo di risposta -)
- fornire supporto per diversi tipi di memoria secondaria
- *minimizzare la perdita* di dati
- fornire un insieme di *interfacce standard* per i processi utente
- fornire supporto per l'I/O effettuato da *più utenti in contemporanea*

#### requisiti
1) ogni utente deve essere in grado di creare, cancellare, leggere, scrivere e modificare un file
2) ogni utente deve poter accedere, in modo controllato, ai file di un altro utente
3) ogni utente deve poter leggere e modificare i permessi di accesso ai propri file
4) ogni utente deve poter ristrutturare i propri file in modo attinente al problema affrontato
5) ogni utente deve poter muovere dati da un file a un altro
6) ogni utente deve poter mantenere una copia di backup dei propri file (in caso di danno)
7) ogni utente deve poter accedere ai propri file tramite nomi simbolici

#### organizzazione del codice
[[4 - gestione della memoria#elementi centrali per il progetto di un sistema operativo]]

- **Directory Management** - tutte le operazioni utente che hanno a che fare con i file
- **File System** - struttura logica ed operazioni fisiche
- **Organizzazione Fisica** - da identificatori di file a indirizzi fisici su disco (allocazione/deallocazione)
- **Scheduling & Control** - qui ci sono i vari SCAN ecc.

## le directory