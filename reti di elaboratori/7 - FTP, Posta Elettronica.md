---
created: 2025-03-21T15:06
updated: 2025-04-04T17:26
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

L'FTP segue il modello **client/server**