---
created: 2025-06-21T10:11
updated: 2025-06-22T17:53
---
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
- la flag `-a | --all` permette di vedere anche i file nascosti (che iniziano con `.`)
- la flag `-A | --almost-all` mostra anche i file nascosti ma non quelli impliciti
- `--author`, usata con `-l`, mostra l'autore di ogni file
- `-c`, 
	- usata con `-lt`, ordina per (e mostra) il  ctime (momento dell'ultimo cambiamento)
	- usata con `-l`, mostra il ctime e ordina per nome
	- altrimenti, ordina per ctime più recente per primo
- `-d | --directory` mostra le directory e non i loro contenuti
-  `-R | --recursive` permette di visualizzare ricorsivamente il contenuto delle sottodirectory

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

