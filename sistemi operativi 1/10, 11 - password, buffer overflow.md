---
created: 2025-04-26T23:09
updated: 2025-05-31T22:15
---
# password
## password in Linux
Linux utilizza due file per gestire gli utenti e le relative password: `/etc/passwd` e `/etc/shadow`.
> Originariamente, esisteva solo il file `passwd`, che conteneva la password dell'utente in plaintext.

Per ogni riga (che corrisponde ad un utente) in `passwd`, ne esiste una in `shadow` che indica la sua password.

### /etc/passwd
È un file plaintext, contenente l'intera lista di account presenti del sistema. Include anche utenti di sistema e speciali.

Ciascuna riga indica informazioni fondamentali su un utente del sistema, e ha il formato:

![[etc-passwd.png|center|450]]

1) **username**: stringa alfanumerica, il nome utente usato per il login
2) **password**: (inutilizzato) "x" indica che l'hash delle password è nel file shadow
3) **uid**: user id numerico dell'utente (alcuni hanno significati speciali: per esempio, `0` indica il root)
4) **gid**: id del gruppo - ogni utente, una volta creato, è assegnato ad un *primary group*, descritto nel file `/etc/group`
5) **GECOS**: contiene informazioni generali sull'utente
6) **home directory**: path assoluto alla home directory dell'utente
7) **shell**: path assoluto alla shell usata dall'utente

### /etc/shadow
File plaintext contenente l'hash delle password di ogni utente ed altre informazioni aggiuntive.
- ha permessi molto restrittivi, perché sottrarrlo e decifrarlo è uno degli obiettivi principali di un attacco

Ciascuna riga contiene informazioni sulla password del rispettivo utente:

![[etc-shadow.png|center|450]]

1) **username**: nome dell'utente, definito in `passwd`
2) **password**: password salvata usando il Modular Crypt Format
3) **last changed**: data dell'ultimo cambiamento della password (in numero di giorni trascorsi dallo Unix Epoch, 1 gennaio 1970)
4) **min age**: minimo numero di giorni dall'ultimo cambio prima che possa essere nuovamente cambiata
5) **max age**: massimo giorni dopo i quali è necessario cambiare la password
6) **warn**: quanti giorni prima della scadenza della password va avvisato l'utente

### Modular Crypt Format
È il formato usato nello shadow file per salvare gli hash delle password:

$$\text{\$ID\$salt\$hash}$$

- **ID**: algoritmo di hashing usato per la password (MD5, blowfish...)
- **salt**: salt usato nel processo di hashing (vedi [[10, 11 - password, buffer overflow#salt (salvati dal sale)|salt (salvati dal sale)]])
- **hash**: hash della password, calcolato con l'algoritmo e il salt

### funzione hash
Una funzione hash trasforma un input di lunghezza variabile in output di lunghezza fissa in *maniera deterministica*.

>[!info] funzione hash crittografica
>Una funziona hash è detta **crittografica** se:
>- È computazionalmente difficile calcolare l’*inverso* della funzione hash
>- È computazionalmente difficile, dato un input $x$ ed il suo hash $d$, trovare *un altro input* $y$ che abbia lo *stesso hash* $d$
>- È computazionalmente difficile trovere *due input* diversi di lunghezza arbitraria $x$ e $y$ che abbiano lo *stesso hash* $d$

>[!question]- perché non cifrare direttamente la password?
> - se si usa cifratura ed un attaccante ottiene la chiave, potrebbe decifrare ed ottenere tutte le password in plaintext
> - le funzioni hash sono one-way
> - se un attaccante ottiene l’hash, sarà più difficile scoprire la password che l’ha generato
> - è comunque semplice verificare se una password corrisponde a quella salvata in formato hash: basta fare l’hash della password e verificarne l’equivalenza (hashing  ́e deterministico)

## attacchi a password
Gli hashing delle password restano comunque attaccabili.
Gli attacchi più comuni sono di due tipi:
- **attacco dizionario**
- **rainbow table**

### attacco dizionario
Sfrutta la pigrizia degli utenti nello scegliere password *brevi* e *semplici*, e nel *riutilizzare* molte volte la stessa password per servizi diversi.

Si compila una lista di password comunemente utilizzate e si effettua un attacco bruteforce:
- per ogni password nella lista, si calcola l'hash finché esso non corrisponde

>[!summary] pros and cons
>**vantaggi**:
>- molto semplice da effettuare (richiede solo una lista di password)
>- versatile: fuziona per qualsiasi funzione hash
>- ci sono molti tool che aiutano ad automatizzare il tutto
>
>**svantaggi**:
>- può essere molto lento (richiede la computazione in real time dell'hash)
>- la password può non essere presente nel dizionario

### attacco rainbow table
Sfrutta il fatto che le funzioni hash sono deterministiche.

Si pre-computano tutti gli hash e si crea un dizionario (rainbow table) di coppie hash-plaintext password.
- il dizionario viene creato offline e riutilizzato per diversi attacchi

> in realtà, utilizza un sistema più complesso di funzioni di riduzione per mantenere trattabili le dimensioni della tabella, noi semplifichiamo

>[!summary] pros and cons
>**vantaggi**:
>- molto semplice da effettuare (la rainbow table è precompilata)
>- molto più veloce del dizionario
>
>**svantaggi**:
>- rigidità: funziona solo per la funzione hash per la quale è stata creata la rainbow table (bisogna creare più rainbow table per più funzioni)
>- fermato dal salt !

### salt (salvati dal sale)
Il **salt** è un valore randomico, generato quando un utente sceglie la password, che viene aggiunto alla computazione dell'hash.
Il salt viene poi salvato in chiaro insieme all'hash calcolato.

Il salt rende impossibile l'uso delle rainbow tables: se per ogni utente c'è un salt randomico diverso, non posso precomputare gli hash.
In più, fa sì che due utenti diversi con la stessa password abbiano due hash diversi (molto probabilmente i loro salt saranno diversi).

# buffer overflow
L'area di memoria di un processo caricato in memoria è divisa in:

![[mem-proc-so.png|center|200]]

Lo stack è costituito da *stack frames*. 
Ciascuno stack frame contiene: parametri passati alla funzione, variabili locali, indirizzo di ritorno e instruction pointer.

in particolare, una chiamata di funzione prosegue in questo modo:
- se ci sono parametri passati alla funzione, sono aggiunti allo stack
- l’indirizzo di ritorno (return address) è aggiunto allo stack
- il puntatore allo stack frame viene salvato sullo stack
- viene allocato spazio ulteriore sullo stack per le variabili locali della funzione chiamata

>[!example]- esempio stack di funzioni
>Per esempio, se G è chiamata da F, lo stack sarà:
>
>![[stack-funz.png|center|400]]

## il problema: stack smashing

```C
void foo(char *s) {
	char buf[10];
	strcpy(buf, s);
	printf("buf is %s\n", s);
}

foo("stringatroppolungaperbuf");
```

In questo esempio, stiamo inserendo troppi dati rispetto alla dimensione del buffer, ma il computer (che non sa effettivamente quando il buffer finisca), continua a sovrascrivere tutti gli indirizzi di memoria che trova fino al completamento dell'operazione.

Quindi, dopo questa operazione, lo stack si troverebbe circa in questa situazione:

![[stack-dopo.png|center|350]]

Questo tipo di overflow porta generalmente alla terminazione di un programma per segmentation fault. Ma, se i dati inseriti nell'overflow sono preparati in modo accurato, è possibile per esempio *modificare l'indirizzo di ritorno arbitrariamente*, ed **eseguire codice arbitrario**.

Ci sono quattro modi principali per farlo:
1) **shellcode**
2) **return-to-libc**
3) stack frame replacement (solo nominato)
4) return-oriented programming (solo nominato)

### shellcode
Lo shellcode è un piccolo (deve rientrare nelle dimensioni del buffer) pezzo di codice che viene eseguito quando si sfrutta una vulnerabilità per attaccare un sistema. Tipicamente, avvia una **command shell** da cui l'attaccante può prendere il controllo della macchina.
- l'idea alla base è quindi inserire *codice eseguibile* nel buffer, e cambiare il *return address* con l'indirizzo del buffer.


> [!example] esempio
> Se per esempio `buf` ha indirizzo `0x00005555555551da`, un attacco potrebbe essere:
>  
> ```C
> void foo(char *s) {
> 	char buf[10];
> 	strcpy(buf, s);
> 	printf("buf is %s\n", s);
> }
> 
> foo("<\shellcode>\xda\x51\x55\x55\x55\x55\x00\x00");
> ```
> Una volta completata la chiamata a `foo()`, il processore salterà all'indirizzo `0x00005555555551da` ed eseguirà lo shellcode
> 
> ![[shellcode.png|center|350]]

### return-to-libc
Non è sempre possibile inserire shellcode arbitrario nel buffer, ma esiste codice utile ad attacchi sempre presente in RAM e raggiungibile dai processi: le librerie dinamiche e di sistema.
- invece di usare shellcode, si può inserire come indirizzo di ritorno una **funzione di sistema** utile per l'attacco

> [!example] esempio
> Per esempio, assumendo di conoscere l'indirizzo di `system()`, un attacco potrebbe essere:
> 
> ```C
> void foo(char *s) {
> 	char buf[10];
> 	strcpy(buf, s);
> 	printf("buf is %s\n", s);
> }
> 
> foo("AAAAAAAAAAAAAAAA<\indirizzo di system>AAAA'bin/sh'");
> ```
> 
> Dopo la chiamata a `foo`, il processore salterà quindi a `system()` e ne seguirà i codice usando come parametro `bin/sh` 

## contromisure
Le contromisure che si possono prendere si dividono in quelle attuabili a *tempo di compilazione*, e quelle attuabili a *tempo di esecuzione*.

### a tempo di compilazione
1) utilizzo di linguaggi di programmazione e di funzioni *sicuri* (l'overflow è possibile solo perché C utilizza funzioni che spostano dati senza limiti di dimensione).
2) **stack smashing protection**:
	- il compilatore inserisce del codice per generare un valore casuale (chiamato *canary*) a runtime, che viene inserito tra il frame pointer e l'indirizzo di ritorno.
	- se il canary viene modificato prima che la funzione ritorni, vuol dire che è stato sovrascritto da un possibile attacco e l'esecuzione viene interrotta.

### a tempo di esecuzione
1) **executable space protection**
	- il Sistema Operativo marca pagine/segmenti dello stack e heap come non eseguibili
	- se un attaccante cerca di eseguire codice nello stack, il sistema termina il processo con un errore
	- (return-to-libc funziona comunque)
2) **address space layout randomization**
	- ad ogni esecuzione si randomizzano gli indirizzi dove sono caricati i diversi segmenti di un programma (stack, heap ecc)
	- è molto più difficile indovinare l'indirizzo del buffer contenente lo shellcode e anche quello delle librerie se non si sa dove inizia lo stack