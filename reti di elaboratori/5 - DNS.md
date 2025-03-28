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
>un browser (ossia client HTTP) di un host utente richiede l’URL `www.someschool.edu`
>1. l’host esegue il lato client dell’applicazione DNS
>2. il browser estrae il nome dell’host, `www.someschool.edu` dall’URL e lo passa al lato client dell’applicazione DNS
>3. il cient DNS invia una query contenente l’hostname a un server DNS
>4. il client DNS riceve una risposta che include l’indirizzo IP corrispondente all’hostname
>5. ottenuto l’indirizzo IP dal DNS, il browser può dare inizio alla connessione TCP verso il server HTTP localizzato a quell’indirizzo IP

>[!question]- il DNS può essere centralizzato?
>Non si può memorizzare il database DNS in un singolo server perché:
>- singolo punto di fallimento (se crashasse, crasherebbe Internet)
>- volume di traffico troppo elevato 
>- distanza dal database centralizzato: un singolo server non può essere fisicamente vicino a tutti i client
>- manutenzione: dovrebbe essere aggiornato continuamente per includere nuovi nomi di host
### aliasing
Il DNS offre il servizio di **aliasing**, che permette di associare a un nome complesso un nome semplice da ricordare.
- un host può avere uno o più alias 
>[!example] esempio
> `relay1.west-coast.enterprise.com` potrebbe avere `enterprise.com` e `www.enterprise.com`
> - `relay1.west-coast.enterprise.com` è un hostname canonico
>- `enterprise.com` e `www.enterprise.com` sono alias

- il DNS può essere invocato da un'applicazione anche per avere il nome canonico di un alias

### distribuzione del carico
DNS viene utilizzato per distribuire il carico tra server replicati: i siti con molto traffico vengono replicati su più server, e ciascuno di questi gira su un sistema terminale diverso con un diverso indirizzo IP.

L'hostname canonico è associato quindi ad un *insieme di indirizzi IP* contenuti nel DNS. Quando un client effettua una richiesta DNS, il server ritorna l'insieme di indirizzi, ma variando l'ordinamento ad ogni risposta, così da distribuire il traffico.

## gerarchia dei server DNS
Nessun server DNS mantiene il mapping per tutti gli host in internet: questo è distribuito su svariati server DNS.

Le informazioni sono organizzate in base al **dominio**, e ci sono tre classi di server DNS organizzatti in una gerarchia:
- **Root**
- **Top-Level Domain** (TLD)
- **Authoritative**
- (ci sono poi i server DNS *locali*, con cui interagiscono direttamente le applicazioni)

![[gerarchia-database.png|center|550]]

>[!example] esempio
>Il client vuole l’IP di `www.amazon.com`
>1. Il DNS interroga il server root per trovare il server DNS `com`
>2. Il client interroga il server DNS `com` per ottenere il server DNS `amazon.com`
>3. Il client interroga il server DNS `amazon.com` per ottenere l’indirizzo IP di `www.amazon.com`

### server DNS root
In Internet ci sono 13 server DNS radice, ognuno replicato per motivi di sicurezza e affidabilità (per un totale di 247 root server).

I root server vengono contattati dai server DNS locali, e:
- contattano server DNS TLD se non conoscono la m