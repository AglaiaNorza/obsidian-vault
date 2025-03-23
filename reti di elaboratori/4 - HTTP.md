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

Il **server**:
- accetta una connessione TCP da un client
- riceve il nome del file richiesto
- recupera il file dal disco
- invia il file al client
- rilascia la connessione
### Tempo di risposta
>[!info] Round Trip Time
>Il *Round Trip Time* è il tempo impiegato da un piccolo pacchetto per andare dal client al server e ritornare al client. 
>- include ritardi di propagazione, di accodamento e di elaborazione

Il **tempo di risposta** è formato da:
- un RTT per *inizializzare la connessione TCP*
- un RTT per la *richiesta HTTP* e i primi byte della risposta HTTP
- tempo di trasmissione del file

ovvero da 2 RTT + tempo di trasmissione.
### connessioni HTTP
Esistono due tipi di connessioni HTTP: 

**connessioni non persistenti**:
- un solo oggetto viene trasmesso su una connessione TCP
- ciascuna coppia richiesta/risposta viene inviata su una connessione TCP separata
- prima di inviare una richiesta al server è necessario stabilire una connessione

**connessioni persistenti** (modalità di default): 
- più oggetti possono essere trasmessi su una singola connessione TCP tra client e server
- la connessione viene chiusa quando rimane inattiva per un lasso di tempo configurabile (timeout)

>[!tip] connessioni persistenti vs non persistenti
>Le connessioni non persistenti non sono vantaggiose perché:
>- richiedono 2 RTT per oggetto
>- hanno un overhead per il sistema operativo per ogni connessione TCP
>- i browser aprono spesso connessioni TCP parallele per caricare gli oggetti
>
>Le connessioni persistenti invece richiedono un solo RTT di connessione per tutti gli oggetti (+ un RTT per ogni oggetto ricevuto dal server)

> [!example] esempio: connessioni non persistenti
> Supponiamo che l’utente immette l’URL `www.someSchool.edu/someDepartment/home.index`, che contiene testo e riferimenti a 10 immagini jpeg
> 
> 1. il processo *client* HTTP inizializza una connessione TCP con il processo server HTTP a `www.someSchool.edu` sulla porta `80`
> 2. il *server* HTTP all’host `www.someSchool.edu` in attesa di una connessione TCP alla porta 80 “accetta” la connessione e avvisa il client
> 3. il *client* HTTP trasmette un messaggio di richiesta (con l’URL) nella socket della connessione TCP. Il messaggio indica che il client vuole l’oggetto `someDepartment/home.index`
> 4. il *server* HTTP riceve il messaggio di richiesta, crea il messaggio di risposta che contiene l’oggetto richiesto e invia il messaggio nella sua socket
> 5. il *server* HTTP chiude la connessione TCP
> 6. il *client* HTTP riceve il messaggio di risposta che contiene il file html e visualizza il documento html. Esamina il file html, trova i riferimenti a 10 oggetti jpeg
> 7. i passi 1-5 sono ripetuti per ciascuno dei 10 oggetti jpeg

### formato dei messaggi
#### richiesta HTTP

> [!info] formato
> 
> ![[formato-HTTP.png|center|550]]
>
>esempio di richiesta HTTP:
> 
> ```JS
> GET /somedir/page.html HTTP/1.1     // request line
> Host: www.someschool.edu   // header lines v
> Connection: close      
> User-agent: Mozilla/4.0     
> Accept-Language:fr    
> (carriage return e line feed extra)   // blank line
> ```

**metodi**:

| metodo di richiesta | descrizione                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`               | usato quando il client vuole **scaricare** il documento specificato dall'URL da un server. Il server risponde con il documento richiesto nel corpo del messaggio di risposta                              |
| `HEAD`              | usato quando il client non vuole scaricare il documento, ma solo alcune **informazioni sul documento** (es: data dell’ultima modifica). Nella risposta, il server inserisce solo degli header informativi |
| `POST`              | usato per **fornire input** al server (es: contenuto dei campi di un form). l’input viene inserito nel corpo dell’entità                                                                                  |
| `PUT`               | utilizzato per **memorizzare un documento nel server**. il documento viene fornito nel corpo del messaggo, e la posizione di memorizzazione nell’URL                                                      |

>[!tip] è posibile inviare info al server (oltre che con POST) anche attraverso una richiesta GET
>utilizzando `&` negli URL
>```js
> www.somesite.com/animalsearch?monkeys&banana
>```

**intestazioni**:

| intestazione        | descrizione                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `User-Agent`        | indica il programma client utilizzato                                 |
| `Accept`            | indica il formato dei contenuti che il client è in grado di accettare |
| `Accept-charset`    | famiglia di caratteri che il client è in grado di gestire             |
| `Accept-encoding`   | schema di codifica supportato dal client                              |
| `Accept-language`   | linguaggio preferito dal client                                       |
| `Authorization`     | indica le credenziali possedute dal client                            |
| `Host`              | host e numero di porta del client                                     |
| `Date`              | data e ora del messaggio                                              |
| `Upgrade`           | specifica il protocollo di comunicazione preferito                    |
| `Cookie`            | comunica il cookie al server                                          |
| `If-Modified-Since` | invia il documento solo se è più recente della data specificata       |
