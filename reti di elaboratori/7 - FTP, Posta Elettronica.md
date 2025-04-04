---
created: 2025-03-21T15:06
updated: 2025-04-04T18:14
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
- il server FTP mantiene lo "stato", ovvero la directory corrente e l'autenticazione precedente.

