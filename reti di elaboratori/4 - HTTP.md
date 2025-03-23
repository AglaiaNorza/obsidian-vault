## World Wide Web
Il World Wide Web (WWW) è un'applicazione internet nata dalla necessità di scambio e condivisione di ingormazioni tra ricercatori universitari di varie nazioni.

- opera su richiesta (on demand)
- è facile rendere disponibili le informazioni
- hyperlinks e motori di ricerca permettono di navigare su molti siti

Il World Wide Web è formato da:
- Web client (es. browser) --> interfaccia con l'utente
- Web server 
- HTML --> linguaggio per pagine web
- HTTP --> protocollo per la *comunicazione tra client e server web*

>[!example]- architettura generale di un browser
>
>![[browser.png|center|500]]

### URL
Per accedere a e visualizzare una pagina, si usa l'URL (Uniform Resource Locator).
Esso è composto da 3 parti:
1) il **protocollo**
2) il **nome della macchina** in cui è situata la pagina
3) il **percorso del file** (localmente alla macchina) 

(è possibile specificare una porta all'interno dell'URL)

```
protocol://host/path 
protocol://host:porta/path # con specifica porta
```

### documenti web
Esistono tre tipi di documenti web:
1) documenti **statici** --> contenuto predeterminato memorizzato sul server
2) documenti **dinamici** --> creati dal web server alla ricezione della richiesta
3) documenti **attivi** --> contiene script o programmi che verranno eseguiti nel browser (lato client)

## HTTP
HTTP (HyperText Transfer Protocol) è un **protocollo a livello applicazione** del Web.

### modello client/server
HTTP segue il modello **client/server**:
- *client* --> il *browser* richiede, riceve e visualizza gli oggetti del web
- *server* --> il server web invia oggetti in risposta ad una richiesta

>[!info] HTTP definisce in che modo i client web richiedono le pagine ai server web e come questi le traferiscono ai client

Dal **lato client**:
- il browser determina l'URL ed estrae *host* e *filename*
- esegue *connessione TCP* alla porta `80` dell'host indicato nell'URL
- invia una richiesta per il file
- ricve il file dal server
- chiude la connessione
- visualizza il file