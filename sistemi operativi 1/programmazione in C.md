---
created: 2025-04-05T19:49
updated: 2025-04-05T21:22
---
# introduzione

## ambiente di sviluppo ed esecuzione
Le fasi di *sviluppo* di un programma C sono quattro (ognuna svolta da un programma diverso):
1) il programmatore scrive un programma in un *editor di testo* e lo salva su disco
2) il **pre-processore** processa il codice
3) il **compilatore** compila il codice producendo un **file oggetto**, e lo salva su disco
4) il **linker** collega il file oggetto alle librerie, e crea un file eseguibile

>[!tip] Il programma **gcc** (Gnu Compiler Collection) è in grado di svolgere tutte le fasi necessarie alla creazione di un file eseguibile.

Le fasi di *esecuzione* sono invece:
5) il **loader** preleva il programma dal disco e lo carica in memoria principale
6) la **CPU** prende ogni istruzione e la esegue, salvando in memoria,se necessario, nuovi dati durante l'esecuzione 

>[!question]- C vs Java
>La compilazione di un programma in java non produce codice eseguibile, ma codice interpretabile dalla JVM contenuto nel `.class` - il vero processo in esecuzione è la JVM che esegue il `.class` interpretandolo
>
>Invece, la compilazione di un programma tramite gcc produce un file la cui esecuzione crea un processo indipendente da gcc (e quindi eseguibile su altri sistemi senza bisogno di ri-compilarlo)

## il linguaggio C
- è un linguaggio di *alto livello*: un programma è un insieme di istruzioni

### struttura di un programma C
In C è *obbligatoria* la presenza di una **main function**.
- main function e functions possono anche risiedere in diversi file `.c`

Ogni funzione è formata da un’**intestazione** (header), a sua volta composta da nome della funzione, tipo di valore ritornato e da una lista di parametri in input, e da un **basic block** (blocco di istruzioni) :

```C
<return-type> function-name (parameter-list){
	instruction 1;
	instruction 2;
	...
	return ...
}
```

- ogni statement è terminato da un `;`
- una funzione può avere un **valore di ritorno**, che viene impostato dalla keyword `return`, e viene ritornato al chiamante

> [!example] programma basilare
> ```C
> #include <stdio.h>
> 
> int main(){
> 	printf("scemo chi legge \n");
> 	return 0;
> }
> ```

>[!info] direttive al preprocessore: file header
> - con `#` si indicano le **direttive al preprocessore**
> - `stdio.h` è un **file header** (`.h`) che contiene costanti, funzioni per input, output e gestione dei file
> - `<>` indicano che il file header è un file standard del C in `/usr/include`
> - `""` indicano che il file header è dell'utente e si trova nella directory corrente o in un path specificato
> - `-I` permette di specificare le directory in cui cercare gli header file

### compilare ed eseguire

```
gcc -Wall prog-name.c
```
- in questo modo vengono stampati tutti i messaggi di warning (se presenti)

```
gcc -Wall prog-name.c -lm
```
- il flag `-lm` va specificato se si includono le librerie matematiche `<math.h>` (per usare funzioni come `sin`, `cos`, `log`, `ln`, ecc.)

Il risultato si troverà in un file eseguibile `a.out`

Per specificare il *nome* dell’output:
```
gcc -Wall prog-name.c -o executable-name.o
```

(il file si può eseguire con `./prog-name.o`)
#### precompilazione, compilazione, linking
Per eseguire solo la **precompilazione**:
```
cpp helloworld.c > precompilato.c
```
- esegue tutte le direttive del compilatore ed elimina i commenti

Per eseguire solo la **compilazione** (di un precompilato):
```
gcc -c precompilato.c -o file.o
```
- gcc controlla la sintassi
- per ogni chiamata a funzione, controlla che venga rispettato l'header
- crea del codice macchina solo per il contenuto delle funzioni 

Per eseguire solo **precompilazione + compilazione**:
```
gcc -c file.c -o file.o
```

Per eseguire solo **linking**:
```
gcc file.o
```
- risolve tutte le chiamate a funzione (per ogni funzione ci deve essere anche un'implementazione data dal programmatore o da librerie di sistema)
- l'inclusione delle librerie può essere automatica o specificata dall'utente

Linking di *più file*:
```
gcc file1.o file2.o file3.c
```
- si possono mischiare file `.c` e `.o`

Per fare **precompilazione, compilazione e linking**:
```
gcc file1.c ... filen.c
```

### variabili
>[!error]- identificatori validi
>1) Il primo carattere in un identificatore deve essere una lettera o underscore e può essere seguito solo da qualsiasi lettera, numero o underscore
>2) Non devono iniziare con una cifra
>3) Lettere maiuscole e minuscole sono distinte (case-sensitive).
>4) Virgole o spazi vuoti non sono consentiti all'interno di un identificatore
>5) Le parole chiave non possono essere utilizzate come identificatore
>6) Non devono avere una lunghezza superiore a 31 caratteri

Le variabili globali si dichiarano fuori dalle funzioni, i parametri nell'header e le variabili locali all'interno del blocco di codice di una funzione.

>[!question] variabili locali: a inizio funzione o vicino al primo uso?