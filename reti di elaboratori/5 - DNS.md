---
created: 2025-03-29T16:36
updated: 2025-04-14T12:37
---
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
>- utilizza il trasporto [[8 - UDP|UDP]] e indirizza la porta `53`
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

>[!tip] root e TLD server non contengono informazioni applicative (come indirizzi IP e mail server), ma svolgono una funzione di **supporto alla risoluzione** fornendo indicazioni su quali server DNS siano autorevoli per ciascun dominio
>- i server autorevoli **contengono i record effettivi** 

>[!example] esempio
>Il client vuole l’IP di `www.amazon.com`
>1. Il DNS interroga il server root per trovare il server DNS `com`
>2. Il client interroga il server DNS `com` per ottenere il server DNS `amazon.com`
>3. Il client interroga il server DNS `amazon.com` per ottenere l’indirizzo IP di `www.amazon.com`

### server DNS root
In Internet ci sono 13 server DNS radice, ognuno replicato per motivi di sicurezza e affidabilità (per un totale di 247 root server).

I root server vengono contattati dai server DNS locali, e:
- contattano server DNS TLD se non conoscono la mappatura
- ottengono la mappatura
- restituiscono la mappatura del server DNS locale

![[dns-root.png|center|500]]

### server TLD
I server Top-Level Domain si occupano dei domini `com`, `org`, `net`, `edu` ecc., e di tutti i domini locali di alto livello, quali `it`, `uk`, `fr`, `ca` e `jp`.

**etichette dei domini generici**:

| etichetta | descrizione                            |
| --------- | -------------------------------------- |
| `aero`    | companie aree e aziende aerospaziali   |
| `biz`     | aziende (simile a com)                 |
| `com`     | organizzazioni commerciali             |
| `coop`    | associazioni di cooperazione           |
| `edu`     | istituzioni educative                  |
| `gov`     | istituzioni governative                |
| `info`    | fornitori di servizi informatici       |
| `int`     | organizzazioni internazionali          |
| `mil`     | organizzazioni militari                |
| `museum`  | musei                                  |
| `name`    | nomi di persone                        |
| `net`     | organizzazioni che si occupano di reti |
| `org`     | organizzazioni senza scopo di lucro    |
| `pro`     | organizzazioni professionali           |
### authoritative servers
Un authoritative server viene interrogato per risolvere il nome di un host pubblicamente accessibile.
- ogni organizzazione dotata di host pubblicamente accessibili deve fornire i record DNS di pubblico dominio che mappano i nomi di tali host in indirizzi IP
- possono essere mantenuti dall'organizzazione o da un service provider
- in genere sono due server: primario e secondario

>[!example] esempio
> 
>![[authoritative-es.png|center|450]]

### server DNS locale
- non appartengono strettamente alla gerarchia dei server
- ciascun ISP ne ha uno (detto anche "default name server")

Quando un host effettua una richiesta DNS, la query viene inviata al suo server DNS locale, che opera da proxy e inoltra la query in una gerarchia di server DNS.

## query 
La restituzione dell'indirizzo IP può avvenire tramite query iterativa o query ricorsiva.
### query iterativa
Ogni volta che il DNS locale fa una query, esso stesso riceve risposta da uno dei livelli della gerarchia e si occupa di inviare un'altra richiesta al livello inferiore.
- (il server contattato risponde con il nome del prossimo server da contattare)

![[query-iterativa.png|center|400]]

### query ricorsiva
Il compito di tradurre il nome viene affidato al server DNS contattato (in maniera ricorsiva).

![[query-ricorsiva.png|center|400]]

## caching
Il DNS sfrutta il caching per migliorare le prestazioni e per ridurre il numero di messaggi DNS che "rimbalzano" in Internet.

Una volta che un server DNS impara la mappatura, la mette nella **cache**.
- tipicamente, un server DNS locale memorizza nella cache gli indirizzi IP dei server TLD o di competenza (quindi non si visitano molto spesso i server radice)
- le informazioni nella cache vengono invalidate dopo un certo periodo

## DNS record
Ogni mapping è mantenuto nei database sotto forma di **resource record**.

| tipo      | interpretazione del campo valore                                                        |
| --------- | --------------------------------------------------------------------------------------- |
| **A**     | indirizzo IPv4 a 32 bit                                                                 |
| **NS**    | identifica i server autoritativi di una zona                                            |
| **CNAME** | indica che un nome di dominio è un alias per il nome di un dominio ufficiale (canonico) |
| **SOA**   | specifica una serie di informazioni autoritative riguardo una zona                      |
| **MX**    | indica il server di posta del dominio                                                   |
| **AAAA**  | indirizzo IPv6                                                                          |
Il formato di un Resource Record è: `< Name, Value, Type, TTL >`

>[!info] type A
>$$
>\text{hostname} \Rightarrow \text{IP \textcolor{red}{a}ddress}
>$$
>- `name` è il nome dell’host
>- `value` è l’indirizzo IP
>```
> < relay.bar.foo.com, 45.37.93.126, A >

>[!info] type CNAME
>$$
>\text{alias} \Rightarrow \text{\textcolor{red}{c}anonical \textcolor{red}{name}}
>$$
>- `name` è il nome alias di qualche nome canonico
>- `value` è il nome canonico
>```
> < foo.com, relay1.bar.foo.com, CNAME >
>```

>[!info] type NS
>$$
>\text{domain name} \Rightarrow \text{\textcolor{red}{n}ame \textcolor{red}{s}erver}
>$$
>- `name` è il dominio (es: `foo.com`)
>- `value` è il nome dell’host del server di competenza di questo dominio
>```
>< foo.com, dns.foo.com, NS >
> ```

>[!info] type MX
>$$
>\text{alias} \Rightarrow \text{\textcolor{red}{m}ail server canonical name}
>$$
>- `value` è il nome canonico del server di posta associato a `name`
> ```
> < foo.com, mail.bar.foo.com, MX >
> ```


>[!example] esempio
>Un server di competenza conterrà un record di tipo `A` per l’hostname, mentre un server non di competenza conterrà un record di tipo `NS` per il dominio che include l’hostname, e un record di tipo `A` che fornisce l’indirizzo IP del server DNS di competenza nel campo `value` del record DNS.

## messaggi
Nel protocollo DNS, le query e i messaggi di risposta hanno lo stesso formato.

![[messaggi-dns.png|center|500]]

- **identificazione** ⟶ numero di 16 bit per la domanda - la risposta usa lo stesso numero
- **flag**:
	- *domanda o risposta*
	- *richiesta di ricorsione*
	- *ricorsione disponibile*
	- *risposta di competenza* (il server è competente per il nome richiesto)
- **numero** ⟶ numero di occorrenze delle quattro sezioni di tipo di dati che seguono (numero di domande/di RR di risposta ecc.)
- nel **corpo** del messaggio si hanno:
	- **domande** ⟶ campi per il nome richiesto e il tipo di domanda
	- **risposte** ⟶ RR nella risposta alla domanda (più RR nel caso di server replicato)
	- **competenze** ⟶ record per i server di competenza
	- **informazioni aggiuntive** che possono essere usate
		- nel caso di una risposta `MX`, il campo di risposta contiene il record MX con il nome canonico del server di posta, mentre la sezione aggiuntiva contiene un record di tipo `A` con l'indirizzo IP relativo all'hostname canonico del server di posta

> [!example] esempio
> Immaginiamo che un client voglia risolvere `www.example.com` in un indirizzo IP.
> 
> 1) Il client invia al server DNS una *richiesta* con:
>- `ID`: 1234
>- `Flags`: richiesta (`QR = 0`)
>- `Numero di domande`: 1 (`www.example.com`, tipo `A`)
>- Le altre sezioni sono vuote.
> 
>1) Il server DNS *risponde* con:
>- `ID`: 1234 (lo stesso della richiesta)
>- `Flags`: risposta (`QR = 1`)
>- `Numero di domande`: 1 (`www.example.com`)
>- `Numero di RR di risposta`: 1 (`A 93.184.216.34`)
>- `Numero di RR autorevoli`: 1 (`NS ns1.example.net`)
>- `Numero di RR addizionali`: 1 (`ns1.example.net A 203.0.113.10`)
> 
>La risposta dice che:
>- `www.example.com` ha l’IP `93.184.216.34` (sezione Risposte).
>- Il server DNS autoritativo è `ns1.example.net` (sezione Competenza).
>- L'IP di `ns1.example.net` è `203.0.113.10` (sezione Informazioni Aggiuntive).

## inserire record nel database DNS
Per aggiungere nuovi domini al DNS, si può contattare un **registrar** (aziende commerciali accreditate dall’ICANN), che, in cambio di un compenso, verifica l’unicità del dominio richiesto e lo inserisce nel database (TLD).
- dovremo poi aggiungere i relativi RR necessari nel nostro server di competenza (almeno un RR di tipo `A`)

>[!example] in che modo gli utenti otterranno l'IP di un nuovo sito web?
>
>![[dns-new-ex.png|center|400]]