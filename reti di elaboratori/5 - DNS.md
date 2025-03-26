## indirizzi ip
Gli host internet hanno **hostname**, nomi facili da ricordare ma che forniscono poche informazioni sulla collocazione degli host all'interno di Internet.

Per questo, esistono gli **indirizzi IP** per gli host: sequenze di 32 bit usate per indirizzare i datagrammi.

>[!info] indirizzo IP
>Un indirizzo IP consiste in una stringa di 4 byte, in cui ogni punto separa uno dei byte espressi con un numero decimale da 0 a 255.
>
>Ha una *struttura gerarchica*:
>- rete di appartenenza
>- indirizzo di nodo

## DNS: Domain Name System
Il Domain Name System ha il compito di associare un hostname al relativo  indirizzo IP.
- per la memorizzazione, usa un *database distribuito* implementato in una gerarchia di server DNS
- per l'accesso, si usa un *protocollo a livello applicazione* che consente agli host di interrogare il database distribuito per **risolvere** (tradurre) i nomi

>[!tip] il DNS viene utilizzato dagli altri protocolli a livello applicazione per tradurre hostname in indirizzi IP
>- utilizza il trasporto UDP e indirizza la porta `53`
>
>>[!question]- perché usa UDP?
>> L'utilizzo di UDP richiede meno overhead, in quanto (al contrario di TCP) il suo setup richiede poco tempo. In più, visto che vanno contattati diversi server per una risposta, mettere su una connessione (come richiesto da TCP) sarebbe uno spreco di tempo. Infine, i messaggi sono brevi e, se non hanno risposta entro un timeout, vengono semplicemente re-inviati.

>[!example] esempio di interazione con HTTP
>un bowser(ossia client HTTP) di un host utente richiede l’URL `www.someschool.edu`
>1. l’host esegue il lato client dell’applicazione DNS
>2. il browser estrae il nome dell’host, `www.someschool.edu` dall’URL e lo passa al lato client dell’applicazione DNS
>3. il cient DNS invia un query contenente l’hostname a un server DNS
>4. il client DNS riceve una risposta che include l’indirizzo IP corrispondente all’hostname
>5. ottenuto l’indirizzo IP dal DNS, il browser può dare inizio alla connessione TCP verso il server HTTP localizzato a quell’indirizzo IP
