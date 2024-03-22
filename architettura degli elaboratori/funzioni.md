---
sticker: lucide//arrow-left-right
---
Una funzione è un frammento di codice che *riceve degli argomenti* e *calcola un risultato*.
- ha un indirizzo di partenza
- riceve uno o più argomenti(mettiamo dei valori nei registri)
- svolge un calcolo
- ritorna un risultato
- torna all'istruzione seguente a quella che l'ha chiamata
 
![[chiamata chiamante.png | 400]]

##### STRUTTURA DI UNA FUNZIONE
 - per **chiamare una funzione**: `jal <etichetta>` - registra nel registro `$ra` la posizione dell'istruzione successiva (`$ra <- PC+4`) e cambia il Program Counter per iniziare l'esecuzione del corpo della funzione (`PC <- etichetta`)
- per **uscire dalla funzione** e continuare l'esecuzione del chiamante: `jr $ra` salta all'indirizzo messo prima in `$ra` 
- per **passare valori alla funzione**: 
	- registri per passare alla funzione (fino a 4 valori a 32 bit o 2 a 64 bit) - `$a0, $a1, $a2, $a3`
	- per restituire dalla funzione (fino a 2 valori a 32 bit o 1 a 64 bit) - `$v0, $v1`

##### preservare il contenuto dei registri
Conviene preservare il contenuto dei registri usati dalla funzione e ripristinarlo:
- *meno vincoli* alla funzione chiamante
- utile nelle *funzioni che chiamano altre funzioni*, che rischiano di perdere valori (sicuramente quello di `$ra`)
- "elimina" il limite di spazio per i dati posto dai soli 4 registri `$a0-3`

Le informazioni da preservare hanno un ciclo di vita caratteristico, dovuto al nidificarsi delle chiamate delle funzioni:
- salvo stato prima di chiamata 1
 
	- salvo stato prima di chiamata 2
	- ...
	- ripristino stato prima di chiamata 2
 
- ripristino stato prima di chiamata 1
 
Questo è il comportamento di uno **stack**, in cui
aggiungere un elemento (**push**) e togliere l’ultimo inserito (**pop**).

Viene realizzata con un **vettore** di cui si tiene l’indirizzo dell’*ultimo elemento occupato nel registro $sp* (Stack Pointer).

>[!example] esempio chiamate nidificate:
>- main chiama foo che chiama bar
>- foo ha bisogno di `$s0, $s1, $s2`
>- bar ha bisogno di `$s0, $s1`
> 
>Visto che foo sa che ha bisogno dei 3 registri + il link di `$ra`, prima di chiamare bar, foo va a scrivere `$s0, $s1, $s2` e `$ra` sullo stack.
>- Salto a bar, salvo i valori di `$s0, $s1` prima di sporcarli, la funzione fa quello che deve fare, torna a `$ra` (ovvero foo), e ora il programma deve riscrivere nei registri tutto quello che ha salvato prima nello stack.

##### uso dello stack - push e pop
Lo stack si trova nella parte "alta" della memoria e cresce verso il basso.
Supponiamo di voler salvare e ripristinare il registro `$ra`.

** <font color="#b2a2c7">PUSH</font>**:
- si **decrementa** lo `$sp` della dimensione dell'elemento(in genere una word)
- si **memorizza** l'elemento nella posizione 0 `$sp`
 
** <font color="#b2a2c7">POP</font>**:
- si legge l'elemento dalla posizione 0 `$sp`
- si incrementa o

