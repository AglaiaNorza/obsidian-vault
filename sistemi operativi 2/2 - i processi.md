---
created: 2025-06-30T19:01
updated: 2025-06-30T19:20
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
>- 