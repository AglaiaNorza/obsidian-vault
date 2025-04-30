---
created: 2025-04-05T19:49
updated: 2025-04-30T17:16
---
# ambiente di sviluppo ed esecuzione
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

# il linguaggio C
- è un linguaggio di *alto livello*: un programma è un insieme di istruzioni
## struttura di un programma C
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

## compilare ed eseguire
### precompilazione, compilazione, linking
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

>[!tip] `-o file.o` serve a specificare il *nome* dell'output

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

### flag
```
gcc -Wall prog-name.c
```
- il flag `-Wall` fa sì che vengano stampati tutti i messaggi di warning (se presenti)

```
gcc -Wall prog-name.c -lm
```
- il flag `-lm` va specificato se si includono le librerie matematiche `<math.h>` (per usare funzioni come `sin`, `cos`, `log`, `ln`, ecc.)
## variabili
>[!error]- identificatori validi
>1) Il primo carattere in un identificatore deve essere una lettera o underscore e può essere seguito solo da qualsiasi lettera, numero o underscore
>2) Non devono iniziare con una cifra
>3) Lettere maiuscole e minuscole sono distinte (case-sensitive).
>4) Virgole o spazi vuoti non sono consentiti all'interno di un identificatore
>5) Le parole chiave non possono essere utilizzate come identificatore
>6) Non devono avere una lunghezza superiore a 31 caratteri

- in C è necessario **dichiarare nome e tipo** di una variabile prima di poterla utilizzare 

>[!info] dichiarazione di variabili e costanti
>Per dichiarare una variabile (o una serie di variabili) si usa la seguente sintassi:
>
>```C
>optional_modifier data_type name_list;
>```
>- `optional_modifier` indica dei modificatori applicati al tipo di dato (come `signed`, `unsigned`, `const`)
>- `data_type` indica il tipo di valore
>- `name_list` è una lista di nomi delle variabili che si vogliono dichiarare

Le variabili globali si dichiarano fuori dalle funzioni, i parametri nell'header e le variabili locali all'interno del blocco di codice di una funzione.

>[!question]- dichiarazione di variabili locali: a inizio funzione o vicino al primo uso?
>##### a inizio funzione
>**vantaggi**:
>- historical context (era una convenzione)
>- memory allocation ⟶ il compilatore alloca la memoria per tutte le variabili una sola volta (più efficiente)
>- scope visibility ⟶ lo scope delle variabili è più chiaro e prevedibile
>- error prevention ⟶ si evitano errori legati all'uso di variabili prima della loro dichiarazione
>- code clarity ⟶ il codice è più leggibile
>
>**svantaggi**:
>- è meno chiaro quando le variabili vengano utilizzate per la prima volta
>- promuove il riuso di variabili per scopi differenti
>
>##### il più vicino possibile al punto di primo uso
>**vantaggi**:
>- riduce il lifespan delle variabili al minimo necessario
>- non promuove il riuso
>
>**svantaggi**:
>- meno ordinato

L'assegnazione di un valore ad una variabile può essere fatta:
- in fase di dichiarazione: `int x = 3;`
- in un momento successivo del codice
	- è possibile fare assegnazioni del tipo `a = b = 0;`
- leggendo un valore in input, per esempio con `scanf`
### numeri
>[!info] tipi di dato per i numeri
> 
>![[numeri-C.png|center|400]]

**intervalli di valori**:

| Type             | Storage size | Value range                                        |
| ---------------- | ------------ | -------------------------------------------------- |
| `char`           | 1 byte       | -128 a 127 o 0 a 255                               |
| `unsigned char`  | 1 byte       | 0 a 255                                            |
| `signed char`    | 1 byte       | -128 a 127                                         |
| `int`            | 2 o 4 bytes  | -32.768 to 32.767 o -2.147.483.648 a 2.147.483.647 |
| `unsigned int`   | 2 o 4 bytes  | 0 a 65.535 o 0 a 4.294.967.295                     |
| `short`          | 2 bytes      | -32.768 a 32.767                                   |
| `unsigned short` | 2 bytes      | 0 a 65.535                                         |
| `long`           | 8 bytes      | -9223372036854775808 a<br>9223372036854775807      |
| `unsigned long`  | 8 bytes      | 0 a 18446744073709551615                           |

| Type          | Storage size | Value range               | Precision             |
| ------------- | ------------ | ------------------------- | --------------------- |
| `float`       | 4 bytes      | 1.2E-38 a<br>3.4E+38      | 6 posizioni decimali  |
| `double`      | 8 bytes      | 2.3E-308 to<br>1.7E+308   | 15 posizioni decimali |
| `long double` | 10 bytes     | 3.4E-4932 to<br>1.1E+4932 | 19 posizioni decimali |

- la dimensione di un tipo di dato può essere ottenuta anche con `sizeof(datatype)`
- l tipo `char` può essere assegnato un carattere [ASCII](https://www.ascii-code.com/) attraverso le single quote: al posto di`char c = 97;`, si può scrivere `char c = 'a';`
### booleani
Esistono due tipi di dati per rappresentare valori booleani:
- `_Bool` ⟶ può memorizzare solo `0` e `1`
	- qualsiasi valore diverso da `0` verrà memorizzato come `1`
- `bool` ⟶ memorizza `true` e `false`
	- richiede l'uso di `<stdbool.h>`

In ogni espressione logica, `0` significa `false` e `1` o <u>diverso da zero</u> significa `true`.

## input e output
Quando un programma viene eseguito, l'ambiente run-time del C apre due file: `stdin` e `stdout`.
- (tutte le funzioni principali per l'I/O sono nel file `stdio.h`)

### output
Con `printf`, possiamo scrivere su `stdout` il valore di una variabile
```C
printf("format_string", value-list);
```
- `format_string` deve contenere dei *placeholder*; ogni placeholder inizia con `%` e serve a specificare il tipo di dato della variabile che si troverà al suo posto
- `value_list` può contenere sequenze di caratteri, variabili, costanti ed espressioni logico-matematiche
- `printf` riceve valori, ma C permette di manipolare anche indirizzi di memoria e passarli come input a funzioni (anche se, per stampare il contenuto di una locazione di memoria, si usa `scanf`)
- `printf` restituisce il *numero di caratteri stampati*

> [!summary] placeholder comuni
> - `%d` o `%i` per integer, `%l` per long
> - `%o` per integers in ottale, `%x` per integers in esadecimale
> - `%f`, `%e`, `%g` per float (f - formato standard, e - notazione scientifica, g - sceglie automaticamente il formato migliore tra f ed e)
> - `%lf` per double

>[!tip] formato completo di un placeholder: `%[parameter][flags][width][.precision][length]type` ([per saperne di più](https://en.wikipedia.org/wiki/Printf_format_string))

Possiamo controllare la spaziatura orizzontale e verticale della `printf` usando sequenze di escape `\`

| Escape Sequence | Name               | Description                                                                            |
| --------------- | ------------------ | -------------------------------------------------------------------------------------- |
| `\a`            | Alarm or Beep      | It is used to generate a bell sound in the C program.                                  |
| `\b`            | Backspace          | It is used to move the cursor one place backward.                                      |
| `\f`            | Form Feed          | It is used to move the cursor to the start of the next logical page.                   |
| `\n`            | New Line           | It moves the cursor to the start of the next line.                                     |
| `\r`            | Carriage Return    | It moves the cursor to the start of the current line.                                  |
| `\t`            | Horizontal Tab     | It inserts some whitespace to the left of the cursor and moves the cursor accordingly. |
| `\v`            | Vertical Tab       | It is used to insert vertical space.                                                   |
| `\\`            | Backlash           | Use to insert backslash character.                                                     |
| `\’`            | Single Quote       | It is used to display a single quotation mark.                                         |
| `\”`            | Double Quote       | It is used to display double quotation marks.                                          |
| `\?`            | Question Mark      | It is used to display a question mark.                                                 |
| `\ooo`          | Octal Number       | It is used to represent an octal number.                                               |
| `\xhh`          | Hexadecimal Number | It represents the hexadecimal number.                                                  |
| `\0`            | NULL               | It represents the NULL character.                                                      |
### input
Per prendere input da terminale, si usa la funzione `scanf`. La sua sintassi è:
```C
scanf(format-string, address-list)
```
- `format-string` contiene placeholder che comunicano a `scanf` il tipo di dato in cui la stringa in input viene convertita
- `address-list` contiene gli indirizzi di memoria in cui devono essere memorizzati i valori in input

>[!example] esempio 
>```C
> scanf("%d", &peso);
>```
>- `peso` è una variabile intera - `&` estrae il suo indirizzo di memoria e lo passa a `scanf`

`scanf` restituisce il *numero di valori letti in input*.
## operatori
- aritmetici: `+, -, *, /, %`
- relazionali: `==, !=, <, <=, >, >=`
- logici: `!, &&, ||`
- bitwise: `&, |, ~, ^`
- shift: `<<, >>`

La precedenza degli operatori segue il PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Substraction).

- C permette di abbreviare gli assegnamenti: `d = d-4` è equivalente a `d -= 4`
- esistono anche:
	- il *post-incremento*: `x++` (usa prima il valore di `x` e poi lo incrementa) 
	- il *pre-incremento*: `++x` (incrementa il valore di `x` prima di usarlo)

## loop
in C, ci sono tre tipi di costrutti iterativi:
- `while` loop: non ha costrizioni
- `do-while` loop: la condizione è testata *dopo* l'esecuzione del corpo del loop
- `for` loop: il numero di iterazioni è noto a priori
	- sintassi: `for (int i = 1; i<5; i++)`

C implementa gli statement `break` (per uscire da cicli e da `switch`) e `continute` (per saltare un'iterazione).

## stringhe
Le stringhe sono **array di caratteri** con ultimo elemento `\0` (detto NULL), il carattere di fine stringa.

Ci sono due modi di inizializzare una stringa:
```C
char r[10] = "L9 4apr"
// qui, i valori da r[8] in poi sono indeterminati

char r[] = "L9 4apr" // viene allocata una stringa di dimensione 8
```
- in questo caso, il carattere `\0` viene aggiunto automaticamente
```C
char r[10] = { 'L', '9', ' ', '4', 'a', 'p', 'r', '\0' }
```

> [!warning] attenzione
> Se invece una stringa venisse inizializzata così:
> ```C
> char r[10] = { 'L', '9', ' ', '4', 'a', 'p', 'r' }
> ```
> 
>  non sarebbe una stringa, in quanto `\0` non viene inserito automaticamente.

### funzioni
Molte funzioni per la gestione delle stringhe sono contenute in `string.h`.

Calcolare la **lunghezza** di una stringa:
```C
size_t strlen(const char *s);
```

**Copia** di una stringa:
```C
char *strcpy(char *dest, const char *src);

char *strncpy(char *dest, const char *src, size_t n);
```
- `strncpy` funziona come `strcpy`, ma al più `n` byte vengono copiati
- si può utilizzare `strcpy` anche per assegnare un valore ad una variabile (previa inizializzazione): `strcpy(s, "Lezione 9");`

**Confronto** di due stringhe:
```C
int strcmp(const char *s1, const char *s2);

// confronta i primi n byte di s1 e s2:
int strncmp(const char *s1, const char *s2, size_t n);
```

Le due funzioni restituiscono un valore che indica la relazione tra le due stringhe, in questo modo:

| valore | significato |
| ------ | ----------- |
| $<0$   | `s1<s2`     |
| $0$    | `s1==s2`    |
| $>0$   | `s1>s2`     |
**Concatenazione** di due stringhe:
```C
char *strcat(char *dest, const char *src);

// concatenati al più i primi n byte:
char *strncat(char *dest, const char *src, size_t n);
```
- concatena il contenuto della stringa `src` con quello di `dest`, e memorizza la nuova stringa in `dest`

Per l'**output** su `stdout`, esistono alternative a `printf`:
- `int putchar(int c)` ⟶ stampa a schermo un carattere (restituisce il carattere scritto, oppure un errore)
- `int puts(const char *s)` ⟶ scrive la stringa fornita su `stdout`, e aggiunge una newline (non stampa `\0`)
- `int fputs(const char *s, FILE *stream)` ⟶ copia la stringa fornita nello stream indicato (non copia `\0`)

Anche per l'**input** esistono alternative a `scanf`:
- `char *gets(char *s)` (deprecato) → legge una linea da `stdin` e la memorizza in `s`
- `char *fgets(char *s, int size, FILE *stream)` → legge i caratteri dal flusso indicato posizionandosi fino al primo carattere di nuova riga incluso e ne salva il contenuto in `s`
- `int getchar(void)` → legge un carattere da `stdin` e lo restituisce in output

## allocazione dinamica della memoria
I **puntatori** sono variabili che contengono l'indirizzo di una locazione di memoria.
```C
<type> *var_name;
 
// o anche 
<type>* var_name
```

Un puntatore ha *due valori* ad esso associati:
- il **valore diretto**: indirizzo di una cella di memoria a cui si accede mediante il nome della variabile
- il **valore indiretto**: il valore contenuto dalle celle di memoria a cui punta il valore diretto

### operatori `&` e `*`
L'operatore `*` è noto come **operatore di deferenziazione** (dereferencing), e permette di accedere al valore contenuto nell'indirizzo di memoria puntato.

L'operatore `&` è noto come **operatore di referenziazione** (referencing), che permette di ottenere l'indirizzo di memoria di una variabile.

> [!example] esempio
> ```C
> int num = 5;
> int *numPtr;
> 
> numPtr = &num; // assegna a numPtr l'indirizzo di num
> 
> *numPtr = 10; // assegna alla locazione puntata da numPtr il valore 10
> 
> *numPtr = *numPtr+1 // assegna alla locazione di numPtr il valore numPtr+1
> ```

