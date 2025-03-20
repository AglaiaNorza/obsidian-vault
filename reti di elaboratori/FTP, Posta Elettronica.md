out of band - usa due connessioni diverse per dati e controllo (i dati viaggiano sulla connessione dati e il controllo sulla connessione controllo??)

### comandi e risposte
sono comandi ASCII

anche FTP ritorna dei codice (comunicano come è andata la richiesta) 

## posta elettronica
3 componenti principali:
1) **user agent** - scrivere/leggere
2) - (lo manda al mail server)

### user agent

I Message Transfer Agent comunicano attraverso l'SMTP - Simple Mail Transfer Protocol (si usa tra server ma anche tra user agent che spedisce la mail e il suo mail server).
- trasferimento affidabile (TCP), su porta 25
- trasferimento diretto da server mittente a server destinatario

per mandare dati non in formato ASCII  