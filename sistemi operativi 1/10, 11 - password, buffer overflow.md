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
- **salt**: salt usato nel processo di hashing
- **hash**: hash della password, calcolato con l'algoritmo e il salt

### funzione hash
Una funzione hash trasforma un input di lunghezza variabile in output di lunghezza fissa in *maniera deterministica*.

>[!info] funzione hash 