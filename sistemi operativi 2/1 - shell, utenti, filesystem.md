---
created: 2025-06-21T10:11
updated: 2025-06-21T19:39
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

## path
Ogni file o directory è raggiungibile da `/` mediante un path assoluto.

>[!tip] `~` equivale a `/home/currentuser`

Per conoscere la current working directory, si usa `pwd`