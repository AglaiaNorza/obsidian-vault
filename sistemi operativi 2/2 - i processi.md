---
created: 2025-06-30T19:01
updated: 2025-07-01T10:38
---
In linux, le due entità fondamentali sono i file (che rappresentano le risorse) e i processi (che permettono di elaborare dati e usare le risorse).
- un file eseguibile in esecuzione è un processo

>[!example] esempio
>Alcuni esempi di processi sono quelli creati eseguendo i comandi come `dd`, `ls`, `cat`, `cp`... 
>- ma non tutti i comandi creano dei processi! per esempio, comandi come `echo` e `cd` vengono eseguiti all'interno del processo di *shell*.

Un file eseguibile eseguito più volte darà vita a un nuovo processo ogni volta. Linux è multi-processo, quindi non occorre aspettare il termine dell'esecuzione di un processo prima di lanciarlo nuovamente.

### ridirezione dell'output
I simboli `>` e `<` possono essere usati per redirigere l'output di un comando su un file.

>[!example] esempi
>- `ls > dirlist` ⟶ l'output di `ls` viene ridirezionato in `dirlist`
>- `2>&1 ls > dirlist` ⟶ l'output di stderr (`2`) viene ridirezionato dove sta andando (`&`) lo stdout (`1`), e lo stdout viene ridirezionato in `dirlist` (`ls > dirlist`) - MA ! bash elabora il comando da sinistra a destra: quando `2>&1` viene elaborato, lo `stdout` non era ancora stato ridirezionato, quindi lo `stderr` andrà sul terminale, e l'output di `ls` in `dirlist`.
>- `ls > dirlist 2>&1` ⟶ sia lo `stderr` che lo `stdout` vengono ridirezionati in `dirlist`
>- `2>/dev/null` ⟶ nasconde gli errori generati da un comando

## rappresentazione dei processi
[ già trattata [[2 - processi (e thread)|qui (sistemi operativi 1)]]]

I processi sono identificati da **Process Identifier** (PID) e **Process Control block** (PCB), e sei aree di memoria.

Il **PID** è univoco, e in ogni istante non ci possono essere due processi con lo stesso PID. Il PID di un processo terminato si può riutilizzare.

Il **PCB** è unico per processo e contiene:
- PID: Process Identifier
- PPID: Parent Process Identifier
- real UID: Real User Identifier
- real GID: Real Group ID
- effective UID: Effective User Identifier (UID assunto dal processo in esecuzione)
- effective GID: Effective Group ID (come sopra per GID)
- saved UID: Saved User Identifier (UID avuto prima dell’esecuzione del SetUID)
- saved GID: Saved Group Identifier (come sopra per GID)
- current Working Directory: directory di lavoro corrente
- umask: file mode creation mask
- nice: priorità statica del processo

>[!question] RUID vs EUID
>Quando si setta il `SetUID` di un file eseguibile:
>- il `RUID` è l'id di chi lo esegue
>- l'`EUID` è l'id del proprietario del file

Le **aree di memoria** sono:
- **text segment** ⟶ istruzioni da eseguire (in linguaggio macchina)
- **data segment** ⟶ dati statici inizializzati (variabili globali e locali static) e alcune costanti di ambiente
- **BSS** ⟶ (Block Started from Symbol) contiene dati statici non inizializzati; la distinzione dal data segment si fa per motivi di realizzazione hardware
- **heap** ⟶ dati dinamici
- **stack** ⟶ chiamate a funzioni con corrispondenti dati dinamici
- **memory mapping segment** ⟶ tutto ciò che riguarda librerie esterne dinamiche usate dal processo, nonché estensione dello heap in alcuni casi

>[!summary] aree di memoria
>
>![[memoria-processi.png|center|500]]

>[!tip] aree condivise
>Alcune aree di memoria però potrebbero essere condivise:
>- il text segment tra più istanze dello stesso processo
>- due processi potrebbero avere lo stesso BSS o Data segment o MMS
>- lo stack non è mai condiviso
### stato di un processo
Un processo si può trovare in uno di questi stati:
- **running (R)** ⟶ in esecuzione su un processore
- **runnable (R)** ⟶ pronto per essere eseguito; aspetta lo scheduler
- **(interruptible) sleep (S)** ⟶ in attesa di qualche evento; non può essere scelto dallo scheduler
- **zombie (Z)** ⟶ terminato, il suo PCB viene ancora mantenuto dal kernel perchè il processo padre non ha ancora richiesto il suo “exit status”
- **stopped (T)** ⟶ caso particolare di sleeping: ha ricevuto un segnale `STOP` ed è in attesa di un segnale `CONT`
- **traced (t)** ⟶ in esecuzione di debug, oppure in generale in attesa di un segnale
- **uninterruptible sleep (D)** ⟶ come sleep, ma tipicamente sta facendo operazioni di I/O su dischi lenti e non può essere interrotto né ucciso

### modalità di esecuzione di un processo
Un processo può essere eseguito in:
- **foreground**:
	- il comando può legger l'input da tastiera e scrivere a schermo
	- finché non termina, il prompt non viene restituito e non si possono sottomettere altri comandi alla shell
- **background**:
	- il comando non può leggere l'input da tastiera, ma può scrivere a schermo
	- il prompt viene immediatamente restituito
	- mentre il job viene eseguito in background, si possono dare altri comandi alla shell
	- per eseguire un programma in background, si usa `&`

>[!question] lista di job
>per vedere la lista di job in esecuzione, si usa il comando `jobs [-l] [-p]`

>[!summary] `bg` e `fg`
> - il comando `bg` permette di portare un processo in background
> - `fg%n` porta in foreground il processo `%n`
> - `bg%n` porta in background il processo `%n`
> 
> si possono identificare job anche con:
> - `%prefix` dove `prefix` è la parte iniziale del comando del job desiderato
> - `%+` oppure `%%` ⟶ l'ultimo job eseguito
> - `%-` ⟶ il penultimo job eseguito

## pipelining dei comandi
Per eseguire un job composto da più comandi, si usa:
```
comando 1 | comando 2 | ... comando n
```
- lo standard output di un comando `i` diventa l'input del comando `i+1`
- se si usa `|&`, invece, sarà lo *standard error* ad essere ridirezionato sullo standard input del comando successivo

## altri comandi
### `ps [opzioni] [pid...]`
Mostra le informazioni dei processi in esecuzione.
- per ogni processo, mostra `PID`, `TTY` (terminale), `TIME` (tempo totale di esecuzione), `CMD` (comando)
- legge le informazioni dai file virtuali in `/proc`
- senza argomenti, mostra i processi dell'utente attuale lanciati dalla shell corrente

Opzioni:
- `-e` ⟶ mostra tutti i processi di tutti gli utenti lanciati da tutte e shell o al boot (figli del processo `0`)
- `-u {utente, }` ⟶ tutti i processi degli utenti nella lista
- `-p {pid, }` ⟶ tutti i processi con PID nella lista
- `-o {field, }` ⟶ permette di scegliere i campi da visualizzare
- `-f` ⟶ restituisce colonne aggiuntive: `UID`, `PPID`, `C` (fattore di utilizzo della CPU), `STIME` (tempo di avvio)
- `-l` ⟶ altre colonne addizionali: `F` (flag), `PRI` (priorità (maggiore la priorità, minore il numero)), `NI` (nice value, influenza la priorità), `ADDR` (indirizzo di memoria del processo), `SZ` (dimensione dell'immagine del processo in pagine), `WCHAN` (waiting channel, indirizzo della funzione del kernel all'interno del quale, se è in sleep, si è fermato)
- `-c {cmds}` ⟶ solo i processi il cui nome eseguibile è in `{cmds}`

#### campi mostrati da `ps`
- `PPID` ⟶ parent pid
- `C` ⟶ parte intera della percentuale di uso della CPU
- `STIME` (o `START`) ⟶ ora (o data) in cui è stato fatto partire il comando
- `TIME` ⟶ tempo di CPU usato fino ad ora
- `CMD` ⟶ comando (con argomenti)
- `F` ⟶ flag associate al processo:
	- `1`: processo "forkato" ma ancora non eseguito
	- `4`: ha usato privilegi da superutente
	- `5`: entrambi i precedenti
	- `0` nessuno dei precedenti
	- `-y -l` elimina questo campo 
- `S` ⟶ stato del processo in una sola lettera
- `UID` ⟶ utente che ha lanciato il processo
- `PRI` ⟶ attuale priorità del processo (priorità alta = numero basso)
- `NI` ⟶ valore di nice da aggiungere alla priorità
- `ADDR` ⟶ indirizzo in memoria del processo (utile solo per backwards compatibility)
	- `-y -l` elimina questo campo e lo sostituisce con `RSS` (resident set size, dimensione del processo in memoria principale)
- `SZ` ⟶ dimensione totale attuale del processo in numero di pagine (sia in memoria che su disco)
- `WCHAN` ⟶ se il processo è in sleep, in `WCHAN` c'è la funzione del kernel all'interno della quale si è fermato

### `top [-b] [-n num] [-p {pid, }]`
