---
sticker: lucide//file-clock
---
Il compito fondamentale di un sistema operativo è la **gestione dei processi** - computazioni di tipi diversi.
Deve quindi: 
- permettere l'esecuzione alternata di processi multipli (interleaving)
- assegnare le risorse ai processi (es. stampante, monitor ecc), e proteggere le risorse assegnate
- permettere ai processi di scambiarsi informazioni
- permettere la *sincronizzazione dei processi*

>[!info] definizioni di processo
>- un **programma in esecuzione** (o un'istanza di un programma in esecuzione, ogni esecuzione anche dello stesso programma è un processo diverso).
>- l'entità che può essere assegnata a un processore per l'esecuzione
>- un'unità di attività caratterizzata dall'esecuzione di una **sequenza di istruzioni**, da uno **stato**, e da un insieme associato di **risorse**
>- è composto da:
>	- *codice*: le istruzioni da eseguire
>	- un insieme di *dati*
>	- attributi che descrivono lo *stato* del processo

un "processo in esecuzione" vuol dire solo che "un utente ha richiesto l'esecuzione di un programma che non è ancora terminato" (quindi non vuol dire che sia necessariamente in esecuzione su un processore).
Dietro ogni processo c'è un *programma* (tipicamente memorizzato su archiviazione di massa - tranne per alcuni processi creati dal sistema operativo stesso), che, quando viene eseguito, genera almeno un processo.

>[!summary] macrofasi di un processo
>un processo ha 3 macrofasi: **creazione**, **esecuzione**, **terminazione**.
>- la terminazione può essere *prevista* (es. quando ha finito di eseguire le istruzioni, o quando un utente lo chiude) o *non prevista* (es. interrupt, eccezioni, accessi non consentiti)

#### elementi di un processo
Finché il processo è in esecuzione, ad esso è associato un insieme di informazioni, tra cui: 
- un identificatore (il sistema operativo deve poter identificare i processi)
- uno stato
- una priorità
- hardware context - valore corrente dei registri della CPU
- puntatori alla memoria
- informazioni sullo stato dell'I/O
- informazioni di accounting - quale utente lo segue

#### process control block
per ogni processo ancora in esecuzione, esiste un **process control block**, che racchiude le informazioni sul processo e si trova nella zona di memoria riservata al kernel.
- è creato e gestito dal sistema operativo, e gli permette di gestire più processi contemporaneamente
- la sua funzione principale è di avere abbastanza informazioni per poter fermare un programma in esecuzione e farlo riprendere dallo stesso punto in cui si trovava.

### traccia ed esecuzione di un processo
La traccia di un processo (**trace**) è la *sequenza di istruzioni che vengono eseguite*.
- il *dispatcher* è un piccolo programma che sospende un processo per farne andare in esecuzione un altro.

>[!example] esecuzione di un processo
>![[es-processo.png|100]]
>![[es-processo2.png|400]]
