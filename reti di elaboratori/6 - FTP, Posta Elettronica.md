---
created: 2025-03-21T15:06
updated: 2025-04-16T17:12
---
## FTP
L'FTP (File Transfer Protocol) è un programma di trasferimento di file da/a un host remoto.

> [!summary] utilizzo
> Il comando per accedere ed essere autorizzato a scambiare informazioni con l’host remoto è:
> ```bash
> ftp NomeHost
> # vengono richiesti nome utente e password
> ```
> 
> - trasferimento di un file <u>da</u> un host remoto:
> ```bash
> ftp> get file1.txt
> ```
> 
> - trasferimento di un file <u>a</u> un host remoto:
> ```bash
> ftp> put file3.txt
> ```

L'FTP segue il modello **client/server**:
- il lato **client** è quello che inizia il trasferimento
- il lato **server** è l'host remoto

![[FTP.png|center|450]]

La comunicazione avviene così:
1) quando l'utente fornisce il nome dell'host remoto (con `ftp NomeHost`), il processo client FTP stabilisce una connessione TCP sulla **porta 21** con il processo server FTP
2) stabilita la connessione, il client fornisce *nome utente* e *password*, che vengono inviate sulla connessione TCP come parte dei comandi
3) una volta ottenuta l'*autorizzazione* del server, il client può inviare uno o più file memorizzati nel file system locale verso quello remoto (o viceversa)

### connessioni
Durante la comunicazione FTP, avvengono due connessioni:
#### connessione di controllo
La connessione di controllo si occupa delle informazioni di **controllo del trasferimento** e usa regole molto semplici, così da ridurre lo scambio di informazioni allo scambio di *una riga di comando* per ogni interazione.
- avviene sulla **porta 21**
- viene aperta al comando `ftp NomeHost`
- tutti i comandi dell'utente sono trasferiti sulla connessione di controllo
- è detta una connessione *out of band* (fuori banda), perché utilizza un canale separato rispetto alla connessione dati per gestire comandi e risposte tra client e server
- il server FTP è stateful, ovvero mantiene la directory corrente e l'autenticazione precedente.

>[!tip] è una connessione **persistente**

#### connessione dati
Si occupa del trasferimento dei file.
- aperta dal server quando riceve un comando per trasferire file (es. `get`, `put`) sulla **porta 20**
- la connessione viene chiusa (dal server) dopo il trasferimento dati ⟶ si crea *una nuova connessione per ogni file trasferito* all'interno della sessione

>[!error] è una connessione **non persistente**

### comandi e risposte
Esiste una corrispondenza 1:1 tra il comando immesso dall'utente e quello FTP inviato sulla connessione di controllo. Ciascun comando è seguito da un *codice di ritorno*: risposta spedita dal server al client.

**esempi di comandi**:

| comando | argomenti              | descrizione                                     |
| ------- | ---------------------- | ----------------------------------------------- |
| `ABOR`  |                        | interruzione del comando precedente             |
| `CDUP`  |                        | sale di un livello nell’albero delle dir        |
| `CWD`   | nome della dir         | cambia la dir corrente                          |
| `DELE`  | nome del file          | cancella il file                                |
| `LIST`  | nome della dir         | elenca il contenuto della dir                   |
| `MKD`   | nome della dir         | crea una nuova dir                              |
| `PASS`  | password utente        | password                                        |
| `PASV`  |                        | il server sceglie la porta                      |
| `PORT`  | numero di porta        | il client sceglie la porta                      |
| `PWD`   |                        | mostra il nome della directory corrente         |
| `QUIT`  |                        | uscita dal sistema                              |
| `RETR`  | nome di uno o più file | trasferisce uno o più file dal server al client |
| `RMD`   | nome della dir         | cancella la dir                                 |
| `RNTO`  | nome (del nuovo) file  | cambia il nome del file                         |
| `STOR`  | nome di uno o più file | trasferisce uno o più file dal client al server |
| `USER`  | identificativo         | identificazione dell’utente                     |

**esempi di risposte**:

| codice | descrizione                                        |
| ------ | -------------------------------------------------- |
| 125    | connessione dati aperta                            |
| 150    | stato del file OK                                  |
| 200    | comando OK                                         |
| 220    | servizio pronto                                    |
| 221    | servizio in chiusura                               |
| 225    | connessione dati aperta (?)                        |
| 226    | connesione dati in chiusura                        |
| 230    | login dell’utente OK                               |
| 250    | azione sul file OK                                 |
| 331    | nome dell’utente OK: in attesa della password      |
| 425    | non è possibile aprire la connesione dati          |
| 450    | azione sul file non eseguita; file non disponibile |
| 452    | azione interrotta; spazio insufficiente            |
| 500    | errore di sintassi; comando non riconosciuto       |
| 501    | errore di sintassi nei parametri o negli argomenti |
| 530    | login dell’utente fallito                          |
Le risposte sono composte da un numero di 3 cifre (codice della risposta) e un testo (parametri necessari o informazioni supplementari).

>[!example] esempio richiesta e risposta
>![[FTP-es.png|center|500]]

## posta elettronica
La posta elettronica ha tre componenti principali:
1) **User Agent** ("mail reader") ⟶ usato per scrivere e inviare un messaggio, o per leggerlo
	- viene attivato dall'utente o da un timer, e informa l'utente se c'è una nuova mail
	- si occupa anche di composizione, editing, lettura dei messaggi
	- (esempi: Outlook, Thunderbird..)
2) **Message Transfer Agent** ⟶ (lato server) usato per trasferire il messaggio attraverso Internet
	- composto da una **mailbox** con i messaggi in arrivo e da una **coda dei messaggi** da trasmettere (eseguirà tentativi ogni x minuti per alcuni giorni)

>[!tip] comunicazione tra MTA
>Per la comunicazione tra *server di posta*, i Mail Transfer Agent usano il **SMTP** (Simple Mail Transfer Protocol)
>
>![[SMTP-MTA.png|center|300]]

3) **Message Access Agent** ⟶ usato per leggere le mail in arrivo

>[!example] posta elettronica: scenario classico
> 
>![[SMTP-es.png|center|450]]

## protocollo SMTP
Il protocollo SMTP (Simple Mail Transfer Protocol) usa TCP per trasferire in modo *affidabile* i messaggi di posta elettronica dal client al server, utilizzando la **porta 25**.
- il trasferimento è *diretto*: dal server trasmittente al server ricevente

Ci sono 3 fasi di trasferimento
1) **handshaking**
2) **trasferimento di messaggi**
3) **chiusura**

I comandi sono composti da testo ASCII, mentre le risposte da un codice di stato ed un'espressione.

- SMTP usa **connessioni persistenti**, e più oggetti vengono trasmessi in un unico messaggio
- il messaggio (intestazione e corpo) deve essere nel formato ASCII a 7 bit

>[!question]- differenze tra HTTP ed STMP
>una delle differenze sostanziali tra HTTP ed STMP (entrambi protocolli utilizzati per trasferire file da un host all’altro) è:
>- HTTP è un protocollo di **pull**: gli utenti iniziano le connessioni TCP e scaricano i file da loro richiesti
>- SMTP è un protocollo di **push**: il server di posta inizia la connessione TCP e spedisce il file
>
>In più, in HTTP, ogni oggetto è incapsulato nel suo messaggio di risposta (mentre appunto SMTP permette di trasmettere più oggetti in un unico messaggio)

>[!example] esempio (scenario)
>1. alice usa il suo user agent per comporre il messaggio da inviare a `rob@someschool.edu`
>2. lo user agent di alice invia un messaggio al server di posta di alice: il messagio è posto nella coda di messaggi
>3. il lato client di SMTP del mail server di alice apre una connessione TCP con il server di posta di roberto
>4. il client SMTP invia il messaggio di alice sulla connessione TCP tramite il message transfer agent
>5. il server di posta di roberto riceve il messaggio e lo pone nella casella di posta di roberto
>6. roberto invoca il suo user agent per leggere il messagio (lo user agent di roberto preleverà il messaggio tramite il message access agent del suo mail server)
>
>![[mail-es.png|center|400]]
>


### scambio di messaggi al livello di protollo
![[smtp-es2.png|center|500]]

1) il client SMTP (che gira sull'host server di posta in invio) fa stabilire una *connessione sulla porta 25* verso il server SMTP (sull'host server di posta in ricezione)
	1) se il server è inattivo, il client riprova più tardi
	2) se il server è attivo, viene stabilita la connessione
2) il server e il client effettuano una forma di *handshaking*: il client indica indirizzo email di mittente e destinatario
3) il client invia il messaggio
4) il messaggio arriva al server destinatario (TCP è affidabile)
	1) (la connessione è persistente) se ci sono altri messaggi, si usa la stessa conessione, altrimenti il client invia richiesta di *chiusura connessione*

>[!example] esempio di interazione SMTP
>
>![[SMP-interaction.png|center|450]]

### formato dei messaggi di posta elettronica
Un messaggio di posta elettronica è composto da:
- righe di intestazione 
	- per esempio: to, from, subject
- corpo (in caratteri ASCII)

| header  | descrizione                                                                      |
| ------- | -------------------------------------------------------------------------------- |
| to      | indirizzo di uno o più destinatari                                               |
| from    | indirizzo del mittente                                                           |
| cc      | indirizzo di uno o più destinatari a cui si invia per conoscenza (crack cocaina) |
| bcc     | blind cc: gli altri destinatari non sanno che anche lui riceve il messaggio      |
| subject | argomento del messaggio                                                          |
| sender  | chi materialmente effettua l’invio (es: nome della segretaria)                   |

>[!example] esempio delle fasi di trasferimento
>
>![[trasferimento-es.png|center|300]]

#### protocollo MIME
Per permettere di inviare messaggi in formati diversi dall'ASCII, è stato definito il protocollo MIME (Multipurpose Internet Mail Extension).
- ci sono alcune righe aggiuntive nell'intestazione dei messaggi per dichiarare il tipo di contenuto MIME:

![[MIME.png|center|500]]

- alcune righe di intestazione vengono inserite anche dal server di ricezione SMTP

![[MIME2.png|center|450]]

## protocolli di accesso alla posta
SMTP è un protocollo di *push*: si occupa della consegna del messaggio sul server del destinatario - non può quindi essere usato per operazioni di pull.

Per queste ultime, si possono usare:
- POP3 (Post Office Protocol - version 3)
- IMAP (Internet Mail Access Protocol) - ha funzioni più complesse e permette la manipolazione di messaggi memorizzati sul server
- HTTP - gmail, hotmail ecc.

### POP3
Il protocollo **POP3** permette al client ricevente di aprire una connessione TCP verso il server di posta sulla **porta 110**.

- è un protocollo *stateless* tra le varie sessioni.
- non fornisce all'utente procedure per creare cartelle remote ed assegnare loro messaggi: l'utente può crearle solo localmente

Una volta stabilita la connessione, si procede in 3 fasi:
1) **autorizzazione**: lo user agent invia nome utente e password per essere identificato
2) **transazione**: l'agente utente recupera i messaggi
3) **aggiornamento**: dopo che il client ha inviato il `QUIT` (e la connessione si è quindi conclusa), vengono cancellati i messaggi marcati per la rimozione

>[!summary] comandi POP3
>
>![[comandi-POP3.png|center|500]]
>
> - questo esempio usa la modalità "scarica e cancella": roberto non può rileggere le mail se cambia client (saranno eliminate sul server e salvate solo sul client da cui le ha lette e scaricate)
> - si può usare anche la modalità "scarica e mantieni", che mantiene i messaggi sul server dopo che sono stati scaricati dal client

### IMAP
> Con POP3, se si accede alla mail da computer diversi, le cartelle create localmente dal proprio programma di posta non sono mantenute - questo problema è risolto da IMAP.

Il protocollo **IMAP** mantiene tutti i messaggi in un *unico luogo*: il server
- consente all'utente di organizzare i messaggi in cartelle

Inoltre, IMAP è **stateful**: conserva lo stato dell'utente tra le varie sessioni (nomi delle cartelle, associazioni tra identificatori dei messaggi e nomi delle cartelle)

### HTTP
Alcuni mail server forniscono accesso alla mail via web (attraverso il protocollo HTTP).
- lo user agent è il web browser
- l'utente comunica con il suo mailbox mediante http, ma il protocollo di comunicazione tra mail server rimane SMTP

>[!example] webmail
>
>![[webmail.png|center|500]]