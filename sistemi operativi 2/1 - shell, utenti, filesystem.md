# shell
La shell è un'interprete di comandi, ovvero un programma che esegue altri comandi.
- la shell scrive un prompt e attende che l'utente scriva un comando
- il prompt tipico è di questo tipo: `utente@nomemacchina:~path`

Ogni comando ha questa struttura:
```
comando [opzioni] argomentiobbligatori
```

Le opzioni hanno due segnature:
- `--parola` (es. `-interactive`)
- `-carattere` (es. `-i`)

Esse possono anche avere un **argomento** (anch'esso con segnature diverse)
- `-k1` o `-k 1`
- `--key=1`

Le opzioni *senza argomenti* sono raggruppabili:
- `-b -r -c` $\iff$ `-brc`

Esistono anche le opzioni BSD-style, senza dash (es. `tar xfz nomefile.tgz`).

## utenti
Durante l'installazione di Linux, è necessario specificare almeno un utente (utente principale).
- non tutti gli utenti possono fare login 
	- `root` non può fare il login, ma un utente può acquisire i diritti di `root` attraverso `su` e `sudo`
- ogni utente appartiene almeno ad un **gruppo** (ne viene automaticamente creato uno con lo stesso nome dell'utente principale)
	- per scoprire i gruppi a cui appartiene un utente, si usa `groups [nomeutente]`

>[!summary] creazione di utenti
>Si possono creare nuovi utenti tramite il comando `adduser nuovoutente` (di default, `nuovoutente` non apparterrà ai sudoers).
>- per aggiungere un utente a un gruppo, si usa `adduser nuovoutente gruppo`

Per cambiare utente, si usa `su [- | -l | --login] nomeutente`
- si usa tipicamente per diventare root (`su - | su - root | su -l root`)
## sudo
L'utente principale è un **sudoer**, ovvero appartiene al gruppo predefinito `sudo`
-  gli utenti del gruppo `sudo` possono eseguire comandi da super utente (`root`) usando `sudo comando`
- `sudo` è quindi un comando che prende in input un altro comando

# filesystem
Il filesystem contiene file e directory, e presenta una struttura gerarchica ad albero, in cui solo le directory possono avere figli.
- esistono (oltre ai file regolari) *file speciali*, che modellano unità di I/O

Linux ha un solo filesystem che ha come radice `/` (root), che contiene, direttamente o indirettamente, tutti i file e le directory.

>[!warning] divieti
>In una stessa directory è vietato creare:
>- due file con lo stesso nome
>- due directory con lo stesso nome
>- un file e una directory con lo stesso nome

- i nomi dei ffile e delle directory sono **case-sensitive**

## directory
Ogni file o directory è raggiungibile da `/` mediante un path assoluto.

>[!tip] `~` equivale a `/home/currentuser`

Per conoscere la **current working directory**, si usa `pwd`. Per cambiare directory, si usa `cd [path]` (`path` può essere assoluto o relativo).
- `cd` senza path ritorna alla home
- `..` indica la parent directory, mentre `.` la cwd

Per **creare una directory**, si usa il comando `mkdir nomedir`.
- la flag `-p` crea anche le parent directory se non esistono (es. `mkdir dir1/dir2` crea anche `dir1` se essa non esiste)

Per **creare un file**, si usa il comando `touch nomefile`.

Per conoscere il **contenuto di una directory**, si usa il comando `ls [directory]`.
- informazioni sulle flag ([[1 - shell, utenti, filesystem#inode|sotto]])

Per visualizzare l'**albero delle directory**, si  usa il comando `tree [-a] [-L maxdepth] [-d] [-x] [nomedir]`
- `-d` mostra solo le directory
- `-x` si usa per rimanere nel filesystem corrente (se incontra un mount point di un altro filesystem, non lo esplora)

## mounting
Il filesystem root `/` contiene elementi eterogenei (disco interno, filesystem su disco esterno, filesystem di rete...) grazie al meccanismo di **mounting**.
- `mount` e `cat /etc/mtab` visualizzano i filesystem montati
- `cat /etc/fstab` visualizza i filesystem montati al boot

| directory | spiegazione                                           | montata           |
| --------- | ----------------------------------------------------- | ----------------- |
| `/boot`   | kernel e file di boot                                 | no                |
| `/bin`    | binari (eseguibili) di base                           | no                |
| `/dev`    | periferiche hardware e virtuali (devices)             | boot              |
| `/etc`    | file di configurazione di sistema                     | no                |
| `/proc`   | dati e statistiche di processi e parametri del kernel | boot              |
| `/sys`    | informazioni e statistiche di device di sistema       | boot              |
| `/media`  | mountpoint per device di I/O                          | quando necessario |
| `/mnt`    | come `/media`                                         | quando necessario |
| `/sbin`   | binari di sistema                                     | no                |
| `/var`    | file variabili (log, code di stampa, mail...)         | no                |
| `/tmp`    | file temporanei                                       | no                |
| `/lib`    | librerie                                              | no                |

>[!summary] esempi di opzioni di mounting comuni
>
> | opzione    | significato                                                            |
> | ---------- | ---------------------------------------------------------------------- |
> | `ro`       | read-only                                                              |
> | `rw`       | read-write                                                             |
> | `noexec`   | non permette l'esecuzione di file binari                               |
> | `nosuid`   | disabilita i bit SUID e SGID (vedi [[1 - shell, utenti, filesystem#permessi di accesso\|sotto]])                               |
> | `nodev`    | non permette dispositivi a livello di file                             |
> | `relatime` | aggiorna il tempo di accesso solo se più vecchio del tempo di modifica |
> | `noatime`  | non aggiorna il tempo di accesso                                       |
> | `sync`     | tutte le scritture avvengono in modalità sincrona                      |
> | `user`     | permette agli utenti normali di montare il filesystem                  |
> | `uid=1000` | imposta l'utente proprietario                                          |
> 

Una qualsiasi directory `D` può diventare un punto di mount per un altro filesystem `F` se e solo se la directory root di `F` diventa accessibile da `D`. Se `D` è vuota, dopo il mount conterrà `F`; se non è vuota, i dati che conteneva precedentemente saranno di nuovo accessibili dopo l'unmount.

>[!summary] partizioni
>Un disco può essere diviso in 2+ partizioni (per esempio una contenente il sistema operativo e una contenente i dati dell'utente)

## tipi di filesystem

Esistono diversi tipi di filesystem:

| Nome     | Journal | Partiz (TB) | File (TB) | Nome file (bytes) |
| -------- | ------- | ----------- | --------- | ----------------- |
| ext2     | No      | 32          | 2         | 255               |
| ext3     | Si      | 32          | 2         | 255               |
| ext4     | Si      | 1000        | 16        | 255               |
| reiserFS | Si      | 16          | 8         | 4032              |

Dal punto di vista del programmatore, il tipo di filesystem definisce la codifica dei dati, mentre dal punto di vista dell'utente, la dimensione massima di partizioni e file, la lunghezza massima dei nomi dei file e la presenza o assenza di journaling.
## `passwd` e `group`

I due file `/etc/passwd` e `/etc/group` sono organizzati per righe (sequenze di caratteri terminate con line feed (`0x0A`)).

Il file `passwd` contiene tutti gli **utenti**, ed è strutturato in questo modo:
- `username:password:uid:gid:gecos:homedir:shell`
	- (al posto di `password` si trova una `x` - le password si trovano in `/etc/shadow` (vedi [[10, 11 - password, buffer overflow|password (SO1)]]))
	- `gecos` contiene informazioni sull'utente

l file  contiene tutti i **gruppi**, ed è strutturato in questo modo:
- `groupname:password:groupID:lista utenti`
	- anche qui la password è assente
- gli utenti della lista sono separati da `,`
## inode
(come già visto in [[6 - file system#gestione file in UNIX|file system (SO1)]]) Ogni file del filesystem è rappresentato da una struttura dati chiamata **inode**, univocamente identificata da un *inode number*.
- la cancellazione di un inode libera l'inode number, che potrà quindi essere riutilizzato

I principali attributi degli inode sono:
- **type** ⟶ tipo di file (regular, block...)
- **user ID** ⟶ ID del proprietario del file
- **group ID** ⟶ ID del gruppo a cui appartiene il proprietario
- **mode** ⟶ permessi (read, write, exec) di accesso per proprietario, gruppo e tutti gli altri
- **size** ⟶ dimensione in byte del file
- **timestamps**
	- *ctime* ⟶ cambiamento di un attributo
	- *mtime* ⟶ modifica (solo scrittura)
	- *atime* ⟶ access time (solo lettura)
- **link count** ⟶ numero di hard links
- **data pointers** ⟶ puntatore alla lista dei blocchi che compongono il file (se si tratta di una directory, il contenuto su disco è costituito da due colonne: nome del file/directory e relativo inode number)
### `ls`
Per visualizzare le informazioni contenute nell'inode di un file, si usa il comando `ls`.

![[ls-output.png|center|500]]

- `total` (`totale` in italiano) indica la dimensione della directory (non compreso il sottoalbero) in blocchi su disco (un blocco ha dimensione tra 1 e 4kB)

>[!summary] flag
>- la flag `-a | --all` permette di vedere anche i file nascosti (che iniziano con `.`)
> - `-l` elenca i contenuti in formato esteso: una tabella che contiene (per ogni entry)
> 	- permessi 
> 	- numero di directory all'interno della entry, comprese . e .. (per i file sarà 1)
> 	- proprietario
> 	- proprietario del gruppo
> 	- dimensione in byte
> 	- ultima modifica
> 	- nome
> - `-i | --inode` mostra l'inode number di ogni file
> - `-n` consente di visualizzare ID utente e ID gruppo invece del nome esteso
> - `-t | --time=WORD` ordina per timestamp (`WORD` indica per quale timestamp; default: modified time)
> -  `-R | --recursive` permette di visualizzare ricorsivamente il contenuto delle sottodirectory
> - `-r | --reverse` ordine inverso
> - `-s | --size` mostra la dimensione, in blocchi, di ogni file
> - `--author`, usata con `-l`, mostra l'autore di ogni file
> - per visualizzare i timestamp, con l'opzione `-l`, si usano:
> 	- `-c` per ctime
> 	- `-u` per atime
> 	- (mtime è il default)
> - `-d | --directory` mostra le informazioni sulla directory stessa e non sui suoi contenuti
> - `--hide=PATTERN` non mostra le entry che corrispondono al pattern

### `stat`
Il comando `stat filename` restituisce varie informazioni su un file.

![[stat-output.png|center|500]]

- `stat -c %B filename` restituisce la dimensione dei blocco su disco su cui si trova il file (non la dimensione del file stesso)

## permessi di accesso
Il proprietario di un file definisce i permessi di accesso (chi può leggere, scrivere, eseguire un file). Sono visualizzabili con `ls` o `stat`.

![[permessi-segnatura.png|center|500]]

![[permessi-file.png|center|450]]

>[!summary] più informazioni sui significati dei permessi
>
>![[permessi-significati.png|center|550]]

### permessi speciali
I permessi speciali sono `setuid`, `setgid` e `sticky bit`.

Nella notazione ottale, sono specificati nel primo numero, in questo modo:
- `4` = setuid
- `2` = setgid
- `1` = sticky bit

(il bit assumerà come valore la somma tra i permessi speciali attivi).

Nella notazione a stringa, invece, il carattere che indica il permesso speciale assume la posizione del permesso di esecuzione. Se il file ha anche il permesso di esecuzione, la lettera che rappresenta il permesso speciale sarà minuscola altrimenti, sarà maiuscola).
- `s` nella prima terna di permessi ⟶ setuid
- `s` nella seconda terna di permessi ⟶ setgid
- `t` (nell'ultima terna di permessi) ⟶ sticky bit

>[!example] esempio
> ```
> 6760/rws rwS ---
> ```
> - setuid e setgid sono attivi 
> - il primo numero è `6` (= `4` + `2`)
> - l'utente ha il permesso di esecuzione, quindi la `s` è minuscola
> - il gruppo non ha il permesso di esecuzone, quindi la `S` è maiuscola
#### sticky bit (t)
Se applicato sulle directory, corregge il comportamento di `w+x` (che permette la cancellazione di file in una directory su cui si hanno i permessi `w+x` senza avere permessi di scrittura sui file stessi) permettendo la cancellazione dei file solo **se si hanno permessi di scrittura** su di essi.
- inutile se applicato su file

>[!example] esempio
>
>Se un utente `U` vuole quindi cancellare un file `f` in una directory `D`:
>- senza sticky bit, gli sarà sufficiente avere i diritti di scrittura su `D` 
>- con lo sticky bit, gli sono necessari anche i permessi di scrittura su `f`

#### setuid bit (s)
Si usa sui file eseguibili. Quando vengono eseguiti, i privilegi con cui opera il corrispondente processo non sono quelli dell'utente che esegue il file ma quelli dell'utente **proprietario** del file.
- per esempio, il comando `passwd` ha il `setuid` (infatti permette ad un utente di modificare la propria password)

#### setgid bit (s)
Analogo di `setuid`, ma con i gruppi (i privilegi sono quelli del gruppo che è proprietario del file eseguibile).
- può essere applicato ad una directory, e in quel caso ogni file creato al suo interno ha il gruppo della directory anziché quello primario di chi crea i file

### settare permessi
Per settare permessi, si usa il comando `chmod mode [, mode...] filename`. Il comando segue un formato ottale:
- si usano 4 numeri tra 0 e 7, come dalle tabelle sopra
- il primo numero indica `setuid`, `setgid` e `sticky`
- gli altri sono per utente, gruppo e altri
- si possono fornire solo 3 numeri se si assumono `setuid`, `setgid` e `sticky` settati a `0`

![[chmod-numeri.png|center|450]]

`chmod` ha anche una modalità simbolica che utilizza le lettere per settare i permessi:
- il formato è: `[ugoa][+-=][perms...]`, dove:
- `u` = user, `g` = group, `o` = other, `a` = all
- `perms` è:
	- `zero`
	- una o più lettere nell’insieme `{rxwXst}`
		- `X` = permesso di esecuzione condizionato (si aggiunge `x` solo se l'elemento è una directory, o almeno uno degli altri utenti (u/g/o) ha già il permesso di esecuzione)
	- una lettera nell’insieme `{ugo}` ⟶ aggiunge i permessi dell'insieme corrispondente (dell'utente/del gruppo/di others)
### cambiare il proprietario
Per cambiare il proprietario di un file, si usa `chown [-R] proprietario {file}` <small>(è possibile specificare anche un gruppo)</small>, mentre per cambiare la proprietà di gruppo di un file, si usa `chgrp [-R] gruppo {file}`.
- se il file è una directory, con la flag `-R` si applica il comando anche a tutte le sottodirectory
## altri comandi

### `umask [mode]`
Setta la maschera dei file, ovvero i diritti di accesso al file o alle directory nel momento della loro creazione, a `mode`.

La maschera può essere:
- un **numero ottale** da uno a quattro cifre (secondo la rappresentazione ottale dei permessi) che indica i permessi che si desidera **negare** (quindi, per esempio `1` negherà il permesso di esecuzione)
	- i permessi saranno quindi dati da `0777 - umask` per i file, e `0666 - umask` per le directory (in realtà sarebbe un `& !(umask)`) 
- una **stringa** secondo la rappresentazione simbolica dei permessi che indica l'insieme dei permessi che possono essere **concessi**

### `cp [-r] [-i] [-a] [-u] {filesorgenti} filedestinazione`
Permette di copiare file.
- `-r` ⟶ recursive (per directory)
- `-i` ⟶ interactive: avvisa in caso di sovrascrizione
- `-u` ⟶ la sovrascrittura avviene solo se l'mtime della sorgente è più recente di quello della destinazione
- `-a` ⟶ archive: i file copiati mantengono i loro permessi, proprietari, timestamp e altri attributi
- `-b` ⟶ fa un backup dei file già esistenti nella destinazione (così che non vengano sovrascritti)
- `-l` ⟶ invece di copiare, crea hard link
- `-s` ⟶ invece di copiare, crea symlink
- `--preserve=ATTR_LIST` ⟶ permette di preservare gli attributi specificati

### `mv [-i] [-u] [-f] {filesorgenti} filedestinazione`
Sposta (o rinomina!) file.
- `-i` e `-u` come in `cp`
- `-f` (force) è di default (non chiede prima di sovrascrivere)

### `rm [-f] [-i] [-r] {file}`
Rimuove file (non c'è un cestino)
- `-f` forza la cancellazione 

### `ln [-s] src [dest]`
Crea symlink e hardlink.
- `-s` per symlink (hardlink è il default)

>[!tip] eliminare la sorgente
>se il file sorgente viene rimosso, un symlink smette di funzionare, mentre un hardlink continua a funzionare (poiché è un riferimento diretto al contenuto del file e non al suo nome)

### `touch [-a] [-m] [-t timestamp] {file}`
Serve per creare file o modificare il loro timestamp.
- funziona anche con directory
- `-a` cambia solo l'access time
- `-m` cambia solo il modified time
- `-t` setta il timestamp desiderato

### `du [-c] [-s] [-a] [-h] [--exclude=PATTERN] [files...]`
Calcola la dimensione dei file e/o directories dati in input.
- `-c` (o `--total`) ⟶ mostra anche la somma totale delle dimensioni
- `-s` (`--summarize`) ⟶ (invece di mostrare la dimensione di ogni file in una directory fornita) mostra solo la dimensione totale per ogni argomento
- `-a` (`-all`) ⟶ mostra tutti i file (normalmente mostra solo il peso di tutte le directory)
- `-h` (`--human-readable`) ⟶ mostra le dimensioni in formati leggibili (e.g. M, G)

### `df [-h] [-l] [-i] [file]`
Mostra la dimensione e l'attuale uso dei filesystem.
- `-h` (`--human-readable`) ⟶ mostra le dimensioni in formati leggibili (e.g. M, G)
- `-l` (`--local`) ⟶ mostra solo i filesystem locali
- `-i` (`--inodes`) ⟶ mostra le informazioni sugli inode invece che sui blocchi
- `file` ⟶ mostra le informazioni relative al filesystem che contiene il file fornito in input

## `dd [opzioni]`
Serve per creare file in modo elaborato, (es. copiare file che non possono essere copiati con `cp`, preparare un file ad essere formattato, copiare parte di un file). `[opzioni]` è una sequenza `variabile=valore`.
- `bs=BYTES` ⟶ legge e scrive fino a `BYTES` byte alla volta (il default è 512)
- `count=N` ⟶ copia solo `N` blocchi dell'input
- `conv=CONVS` ⟶ converte i file secondo la lista di simboli `CONS` fornita in input (con separatore `,`)
- `if=FILE` ⟶ file di input (se non dato, legge da tastiera)
- `of` ⟶ file di output (se non dato, scrive a schermo)
- `skip=N`, `seek=N` ⟶ saltano i primi `N` blocchi (rispettivamente di input e output)

### `mkfs [-t type fsoptions] device`
Crea un filesystem su un device (è un front-end per i vari builder di filesystem usati da Linux).
- `-t type` ⟶ specifica il tipo di filesystem da creare (tra [[1 - shell, utenti, filesystem#tipi di filesystem|questi]])
- `fsoptions` ⟶ `ro` (read-only) oppure `rw` (read-write)
- `device` ⟶ nome del dispositivo (in `/dev`) o anche file regolare