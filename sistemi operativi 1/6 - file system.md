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

### sistemi per la gestione di file
![[5 - gestione dell'IO#problemi nel progetto del sistema operativo#3 - file system]]