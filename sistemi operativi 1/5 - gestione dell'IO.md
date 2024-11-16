[ rilettura utile: [[1 - sistemi operativi#gestione I/O|gestione I/O generale]]]
## dispositivi di I/O

ci sono tre macrocategorie di IO:
- leggibili dall'utente
- leggibili dalla macchina - comunicazione con materiale elettronico (es. dischi, USB)
- di comunicazione (input: tastiera, mouse, output: scheda di rete)

Queste macrocategorie sono molto diverse tra di loro, il che causa problemi al sistema: bisogna gestirli tutti e pensare a come tener conto delle diversità.
### funzionamento

Un dispositivo di *input* prevede di **essere interrogato sul valore** di una certa grandezza fisica al suo interno (es. codice Unicode di un tasto premuto) - un processo effettua una syscall `read` su un dispositivo per leggere un dato.
- al processo non interessa che tipo di macchina sia, ma solo il valore da leggere

Un dispositivo di *output* prevede di poter cambiare il valore di una certa grandezza fisica al suo interno (es. monitor - valore rgb dei pixel) - un processo effettua una syscall `write` per cambiare qualcosa.
- spesso l'effetto è direttamente visibile, alcune volte serve usare una funzionalità di lettura

Esistono quindi, al minimo, due syscall: `read` e `write` (che prendono in input, tra le varie cose, un identificativo del dispositivo). Al momento di una syscall, il Kernel si interpone tra processo utente e dispositivo fisico: comanda l'inizializzazione del trasferimento di informazioni, mette il processo in blocked e passa ad altro.

A trasferimento completato arriva l'interrupt (si termina l'operazione e il processo ritorna ready)
- ci possono essere dei problemi: es. un disco si è smagnetizzato
- potrebbe essere necessario fare anche altri trasferimenti, per esempio dalla RAM dedicata al DMA a quella del processo (se c'è il DMA di mezzo si complica - è il DMA a prendere i dati dalla zona utente e portarli nella zona I/O)

> [!info] driver
> La parte di Kernel che gestisce un particolare dispositivo I/O si chiama **driver** (è formata da una serie di moduli di sistema che implementano funzionalità specifiche in base al dispositivo).

### differenze tra dispositivi I/O
i dispositivi I/O possono differire sotto molti aspetti:
- *data rate* (quanto velocemente si legge/scrive)
- *applicazione*
	- ogni dispositivo I/O ha una diversa applicazione ed uso: i dischi sono usati per memorizzare file (e richiedono software per quello), ma anche per la memoria virtuale (per cui servono altri software e hardware)
- *difficoltà nel controllo*
	- una tastiera o un mouse sono più banali, mentre una stampante è più articolata (per esempio a causa dei dischi magnetici), e un disco è tra le cose più complicate
	- fortunatamente, molte cose sono controllate da hardware dedicato - la *divisione dei compiti* è (in ordine) tra: 
		- processo utente
		- syscall del Sistema Operativo 
		- driver
		- hardware (controller dei dispositivi)
- *unità di trasferimento dati* 
	- in stream di byte o caratteri (usati da memoria non secondaria, es. stampanti, schede audio...)
	- in blocchi di byte di lunghezza fissa (usati per esempio dai dischi)
- *rappresentazione dei dati*
	- i dati sono rappresentati secondo codifiche diverse su dispositivi diversi (es. ASCII vs UNICODE)
- *condizioni di errore*
	- (la natura degli errori varia molto da dispositivo a dispositivo)
	- es. diverse conseguenze: fatali (come leggere da un blocco rotto) o ignorabili (come scrivere su un blocco rotto - si scrive direttamente sul successivo)
## organizzazione della funzione di I/O
>[!summary]- ripasso diverse gestioni I/O
>I/O *programmato*:
>- l'azione su I/O viene eseguita dal modulo I/O e non dal processore, quindi il processore deve controllare costantemente lo stato dell'I/O fino a quando l'operazione non è completa (rimanendo bloccato)
> 
>I/O *da interruzioni*:
>- il processore viene interrotto quando il modulo I/O è pronto a scambiare dati (il processore, una volta ricevuto un write, manda un comando al modulo dell'I/O e continua a svolgere le operazioni fino a quando l'interrupt handler non lo notifica del fatto che l'operazione è terminata)
> 
>I/O con *Direct Access Memory*
> - (le istruzioni richiedono di trasferire informazioni tra dispositivo e memoria) - la DMA trasferisce un blocco di dati dalla memoria, e un'interruzione viene mandata quando il trasferimento è completo

Ci sono sostanzialmente quattro modi di gestire l'I/O:


|                         | senza interruzioni | con interruzioni               |
| ----------------------- | ------------------ | ------------------------------ |
| passando per la CPU     | I/O programmato    | I/O guidato dalle interruzioni |
| direttamente in memoria |                    | DMA                            |
### approfondimento: DMA

- il processore **delega le operazioni di I/O al modulo DMA**, che trasferisce i dati direttamente da o verso la memoria principale (evitando perdite di tempo)

![[DMA.jpg|center|450]]