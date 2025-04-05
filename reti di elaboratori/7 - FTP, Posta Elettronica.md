---
created: 2025-03-21T15:06
updated: 2025-04-05T09:29
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
2) tabilita la connessione, il client fornisce *nome utente* e *password*, che vengono inviate sulla connessione TCP come parte dei comandi
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
- la connessione viene chiusa (dal server) dopo il trasferimento dati --> si crea *una nuova connessione per ogni file trasferito* all'interno della sessione

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
