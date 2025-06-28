---
created: 2025-04-30T17:16
updated: 2025-06-28T20:25
---
Il protocollo IP (Internet Protocol) è responsabile della **suddivisione in pacchetti**, del **forwarding** e della **consegna** dei datagrammi a livello rete (host to host).
- è un protocollo *inaffidabile* e *connectionless*
- offre un servizio di consegna best effort

>[!summary] formato dei datagrammi
> 
>![[darifare.png|center|500]]
>
>- **numero di versione** ⟶ consente la corretta interpretazione del datagramma (può essere 4 per IPv4 o 6 per IPv6)
>- **lunghezza dell'intestazione** ⟶ indica dove inizia il campo dati (un datagramma IP può contenere un numero variabile di opzioni) (la lunghezza di un'intestazione senza opzioni è di 20 byte)
>- **tipo di servizio** ⟶ permette di distinguere diversi datagrammi con requisiti di qualità del servizio diverse (per esempio alcuni pacchetti potrebbero richiedere una consegna rapida, mentre altri potrebbero essere meno sensibili al ritardo)
>- **lunghezza del datagramma** ⟶ rappresenta la lunghezza totale del datagramma in byte (inclusa l'intestazione) - serve per capire se il pacchetto è arrivato per intero
>- **identificatore, flag, offset di frammentazione** ⟶ servono per gestire la frammentazione dei pacchetti [vedi [[13 - IP, indirizzamento IPv4, DHCP, NAT#frammentazione|sotto]]] (IPv6 non prevede frammentazione)
>- **tempo di vita** (Time To Live) ⟶ incluso per assicurare che i datagrammi non resitno in circolazione per sempre nella rete; viene decrementaton ad oni hop e il datagramma viene eliminato se TTL=0
>- **protocollo** ⟶ indica il protocollo a livello di trasporto a cui va passato il datagramma (es: `6: TCP`, `17: UDP`)
>	- utilizzato solo quando il datagramma raggiunge la destinazione finale
>- **checksum dell'intestazione** ⟶ consente ai router di rilevare errori sui datagrammi ricevuti (al contrario di TCP/UDP, viene fatta solo sull'intestazione)
>	- viene ricalcolata nei router intermedi
>- **indirizzi IP di origine e destinazione** ⟶ sono inseriti dall'host che crea il datagramma
>- **opzioni** ⟶ consentono di estendere l'intestazione IP (per test o debug della rete)
>- **dati** ⟶ contiene il segmento di trasporto da consegnare alla destinazione

## frammentazione
Un datagramma IP può dover viaggiare attraverso reti con caratteristiche diverse - ogni router estrarrrà il datagramma, lo elaborerà e lo incapsulerà in un nuovo frame.

>[!info] Maximum Transfer Unit
>La **Maximum Transfer Unit** è la massima quantità di dati che un frame a livello di collegamento può trasportare.
>- la MTU varia in base alla tecnologia

Diverse reti hanno diversi MTU, quindi i datagrammi IP troppo grandi vengono suddivisi in datagrammi più piccoli (frammentazione). I frammenti saranno riassemblati solo una volta raggiunta la destinazione, prima di raggiungere il livello di trasporto.

### bit dell'intestazione
Alcuni bit dell'intestazione sono usati per identificare e riordinare i frammenti. Quando un host di destinazione ricefve una serie di datagrammi dalla stessa origine deve individuare i frammenti, determinare quando ha ricevuto l'ultimo e stabilire come debbano essere riassemblati.

Per farlo, usa:
- **identificazione** (16 bit) ⟶ identificativo associato a ciascun datagramma al momento della creazione (tutti i frammenti di uno stesso datagramma avranno la stessa identificazione)
	- IP + identificazione identificano in modo unico un datagramma
- **flag** (3 bit):
	- riservato
	- do not fragment: `1` se il datagramma non va frammentato
	- more fragments: `1` se il frammento è intermedio, `0` se è l'ultimo
- **offset** ⟶ secifica l'ordine del frammento all'interno del datagramma originario


>[!example] esempio di frammentazione
> 
>![[frammentazione-es.png|center|400]]
>
>![[frammentazione-es2.png|center|500]]
>
>- Il primo frammento ha un valore del campo offset pari a 0
>- l'offset del secondo si ottiene dividendo per 8 la lunghezza del primo frammento (esclusa l'intestazione)
>- l'offset del terzo si ottiene dividendo per 8 la somma della lunghezza del primo e del secondo (esclusa l'intestazione)
>- ...
>- l'ultimo frammento ha il bit `M` impostato a 0

# indirizzamento IPv4
Un indirizzo IP è formato da 32 bit (4 byte) in notazione decimale puntata.

>[!info] interfaccia
>l'**interfaccia** è il confine tra host e collegamento fisico
>- ogni interfaccia di host e router internet ha un indirizzo IP *globalmente univoco* (circa, in realtà se si usano NAT o indirizzi privati non è così)
>- i router devono necessariamente essere connessi ad almeno due collegamenti
>- un host, in genere, ha una sola interfaccia

- gli indirizzi IPv4 sono in totale $2^{32}$ (più di 4 miliardi), e possono essere scritti in notazione binaria, decimale puntata, o esadecimale

## gerarchia nell'indirizzamento
Un indirizzo IPv4 si divide in **prefisso** e **suffisso**.
- il prefisso individua la rete
	- può avere lunghezza fissa (nel caso di indirizzamento con classi) o variabile (indirizzamento senza classi)
- il suffisso individua il collegamento al nodo

### indirizzamento con classi
L'indirizzamento con classi nasce dalla necessità di supportare sia reti piccole che grandi. Ci sono tre lunghezze di prefisso: 8, 16 e 24 bit.

>[!info] prefissi e classi
> 
> ![[classi-ip.png|center|450]]
> 
>- negli indirizzi di classe A, il primo bit del primo ottetto è sempre 0
>- negli indirizzi di classe b, i primi 2 bit del primo ottetto sono sempre 10
>- negli indirizzi di classe C, i primi 3 bit del primo ottetto sono sempre 110

>[!question] pros and cons
>*pros*:
>- il principale *vantaggio* è dato dal fatto che, una volta individuato un indirizzo, si può facilmente risalire alla classe e alla lunghezza del prefisso
>- il principale *svantaggio* è invece il problema dell'esaurimento degli indirizzi:
>	- la classe A può essere assegnata solo a 128 organizzazioni nel mondo, ognuna con 16.777.216 nodi: la maggior parte degli indirizzi verrebbe sprecata, e poche organizzazioni potrebbero usufruire di indirizzi di classe A
>	- la classe B ha lo stesso problema
>	- per la classe C, sono disponibili solo 256 host per ogni rete

### indirizzamento senza classi
L'indirizzamento senza classi nasce dalla necessità di avere maggiore flessibilità nell'assegnamento degli indirizzi. Vengono usati blocchi di *lunghezza variabile* che non appartengono a nessuna classe.
- un indirizzo non è quindi da solo in grado di definire la rete (o blocco) a cui appartiene

La lunghezza del prefisso è **variabile** (da 0 a 32 bit) e viene aggiunta all'indirizzo separata da uno slash.
#### notazione CIDR
La **Classless InterDomain Routing** è la strategia di assegnazione degli indirizzi.

> [!summary] struttura dell'indirizzo
> L'indirizzo IP viene diviso in due parti e mantiene la forma decimale puntata `a.b.c.d/n`, dove `n` indica il numero di bit nel prefisso.
> 
>>[!example] esempio
>> ![[ind-cidr.png|center|400]]

In questo modo, se $n$ è la lunghezza del prefisso:
- il numero di indirizzi nel blocco è dato da $N=2^{32-n}$
- per trovare il *primo indirizzo*, si impostano a $0$ tutti i bit del suffisso ($32-n$ bit)
- per trovare l'*ultimo indirizzo*, si impostano a $1$ tutti i bit del suffisso

>[!info] struttura
> 
>![[struttura-ind-blocchi.png]]

La **maschera dell'indirizzo** è un numero composto da 32bit in cui i primi $n$ bit a sinistra sono impostati a 1 e il resto a 0.
- viene usata per ottenere l'*indirizzo* di rete usato nell'instradamento dei datagrammi verso la destinazione

Essa può essere usata da un programma per calcolare in modo efficiente le informazioni di un blocco, usando solo tre operatori sui bit:
- il **numero degli indirizzi del blocco** è $n=\neg(\text{maschera})+1$
- il **primo indirizzo del blocco** è $\text{qualsiasi ind. del blocco}\land \text{maschera}$
- l'**ultimo indirizzo del blocco** è $\text{qualsiasi ind. del blocco}\lor \neg\text{maschera}$ 

>[!info] indirizzi IP speciali
>
>![[indirizzi-speciali.png|center|450]]
>- `0.0.0.0` è utilizzato dagli host al momento del **boot**
>- gli indirizzi IP che hanno `0` come numero di rete si riferiscono alla **rete corrente**
>- `255.255.255.255` permette la trasmissione **broadcast** sulla rete locale
>- gli indirizzi con tutti `1` nel campo host permettono l'invio di pacchetti **broadcast a LAN distanti** (se il numero di rete è opportuno)
>- gli indirizzi `127.xx.yy.zz` sono riservati al **loopback** (i pacchetti non vengono immessi nel cavo, ma elaborati localmente e trattati come pacchetti in arrivo)

>[!question] come si ottiene un blocco di indirizzi?
>Per ottenere un blocco di indirizzi IP da usare in una sottorete, un amministratore di rete deve contattare il proprio ISP e ottenere un blocco di indirizzi contigui con un prefisso comune
>- otterrà indirizzi della forma `a.b.c.d/x`, dove `x` bit indicano la *sottorete* e `32-x` bit indicano i singoli dispositivi nell'organizzazione
>
>>[!tip] nota bene: i `32-x` bit possono presentare un'aggiuntiva struttura di sottorete
>
> [per più info sulle sottoreti, vedi [[13 - IP, indirizzamento IPv4, DHCP, NAT#sottoreti|sotto]]]
>
>L'ISP, a sua volta, si rivolge all'Internet Corporation for Assigned Names and Numbers (**ICANN**), che: 
>- gestisce i server radice DNS
>- alloca i blocchi di indirizzi
>- assegna e risolve dispute su nomi di dominio

Per assegnare un indirizzo IP ad un host, si può decidere tra assegnazione temporanea o permanente, e tra configurazione manuale o con DHCP.
# DHCP
L'obiettivo del **Dynamic Host Configuration Protocol** (DHCP) è consentire all'host di ottenere dinamicamente il suo indirizzo IP dal server di rete.
- è possibile *rinnovare la proprietà* dell'indirizzo in uso
- è possibile il *riuso* degli indirizzi
- supporta anche gli utenti mobili che si vogliono unire alla rete
- è utilizzato nelle reti in cui gli host si aggiungono e rimuovono dalla rete con estrema frequenza

L'assegnazione degli indirizzi ai singoli host o router è **automatizzata**.

>[!tip] nonostante sia un protocollo del livello di rete, DHCP è implementato come un programma **client/server** di livello **applicazione**
>in particolare:
>- il *client* è un host appena connesso che desidera ottenere informazioni sulla configurazione della rete (non solo un indirizzo IP)
>- il *server* è ogni sottorete che dispone di un server DHCP, o altrimenti un router che fa da agente di appoggio DHCP

Quando un host vuole entrare a far parte di una rete, necessita di indirizzo IP, maschera di rete, indirizzo del router e indirizzo DNS.

>[!info] panoramica DHCP
>- l'host invia un messaggio broadcast alla rete, cercando i server DHCP al suo interno - `DHCP discover`
>- un server DHCP risponde (sempre con un messaggio broadcast) offrendo un possibile indirizzo IP - `DHCP offer`
>- l'host risponde accetta l'indirizzo IP con `DHCP request`
>- il server DHCP invia l'indirizzo con `DHCP ack`

>[!tip] DHCP usa UDP
### messaggi DHCP

>[!summary] formato dei messaggi
>
>![[dhcp-format.png|center|350]]
>
>- `Opcode` ⟶ codice operazione: richiesta (`1`) o risposta (`2`)
>- `Htype` ⟶ tipologia dell'hardware
>- `Hlen` ⟶ lunghezza dell'indirizzo hardware
>- `Hcount` ⟶ numero massimo di hop che il pacchetto può compiere
>- `Transaction ID` ⟶ numero intero impostato dal client e ripetuto dal server
>- `Time elapsed` ⟶ numero di secondi da quando il client ha inviato il primo messaggio di richiesta
>- `Flags` ⟶ il primo bit definisce l'unicast (`1`) o il multicast (`0`), gli altri 15 non vengono utilizzati
>- `Client IP address` ⟶ IP del client, impostato a `0` se il client non lo conosce
>- `Your IP address` ⟶ IP del client, inviato dal server
>- `Server IP address` ⟶ IP del server, impostato a un IP di broadcast se il client non lo conosce
>- `Gateway IP address` ⟶ indirizzo del router di default
>- `Server name` ⟶ nome di dominio del server (64 byte)
>- `Boot file name` ⟶ nome di file usato per informazioni aggiuntive
>- `Options` ⟶ nel pacchetto non è previsto un campo per il tipo di messaggio, quindi qui viene indicato un **magic cookie** pari a `99.130.83.99` segna l’inizio della parte del pacchetto che contiene le opzioni specifiche del protocollo DHCP, di questo tipo:
>
> ![[DHCP-magiccookie.png|center|300]]

>[!example] esempio di completamento richiesta DHCP
>
>![[DHCP-es.png|center|400]]
>
>- vengono usate porte *well-known* (`68` dal client e `67` dal server), perché la risposta del server è broadcast (due client DHCP diversi su due host diversi potrebbero aver scelto la stessa porta effimera e due client diversi potrebbero pensare che la risposta sia per loro)
>- in `DHCPDISCOVER`, il client usa come IP mittente `0.0.0.0`, e come IP destinatario `255.255.255.255` (broadcast on local network)
>- in `DHCPOFFER`, il messaggio viene mandato in broadcast, ma l'host sa che è riferito a lui grazie al transaction ID
>- anche `DHCPREQUEST` e `DHCPACK` vengono mandati in broadcast, pur sapendo IP mittente e destinatario
>- ulteriori informazioni oltre all'IP (maschera, server DNS, router) sono fornite dal server al client attraverso il `DHCPACK`: il server inserisce il pathname di un file che contiene le info mancanti, e il client usa FTP per ottenerlo

# sottoreti, NAT
## sottoreti

> [!info] sottorete
> È detta **sottorete** una rete isolata i cui punti terminali sono collegati all'interfaccia di un host o di un router.

>[!example] esempio
>
>![[sottoreti-es.png|center|300]]
>- la maschera di sottorete `\24` indica che i 24 bit più a sinistra definiscono l'indirizzo della sottorete; ogni host connesso alla sottorete `223.1.1.0/24` deve avere un indirizzo della forma `223.1.1.xxx`

Dato un indirizzo IP e la sua maschera di rete, per sapere a quale blocco appartiene (se il prefisso ha lunghezza variabile):
- se il prefisso è multiplo di 8 bit ⟶ gli indirizzi vanno da `a.b.c.0` a `a.b.c.255`
- se il prefisso non è multiplo di 8 bit ⟶ bisogna vedere la *rappresentazione binaria* di `d`:  per esempio, se si ha `a.b.c.d/26` con `d = 10xxxxxx`, gli indirizzi andranno da `10000000` a `10111111`.


Con la proliferazione di sottoreti *SOHO* (small office, home office), ogni volta che si vuole installare una rete locale per connettere più macchine, l’ISP deve allocare un intervallo di indirizzi per coprire la sottorete, e spesso ciò risulta impossibile per la mancanza di indirizzi aggiuntivi nella sottorete - in questo caso si usano gli **indirizzi privati**, con la traduzione degli indirizzi di rete (NAT).

## NAT
Il **Network Address Translation** (NAT) è una tecnica tramite la quale i router possono nascondere i dettagli della propria rete domestica al mondo esterno.
- un **unico indirizzo IP** è sufficiente per tutte le macchine di una rete locale
- è possibile cambiare gli indirizzi delle macchine di una rete privata senza doverlo comunicare all'Internet globale
- è possibile cambiare ISP senza modificare gli indirizzi delle macchine della rete privata
- i dispositivi interni alla rete non sono esplicitamente indirizzabili e visibili dal mondo esterno (il che garantisce maggiore sicurezza)

>[!info] NAT
>
>![[NAT.png|center]]
>- i router abilitati al NAT non appaiono al mondo esterno come router ma come un unico dispositivo con un unico indirizzo IP, e tutto il traffico verso Internet deve riportare lo stesso indirizzo
>
>**implementazione**:
>
>- quando un router NAT riceve il datagramma, genera per esso un **nuovo numero di porta d'origine**, **sostituisce l'indirizzo IP** origine con il proprio indirizzo IP sul lato WAN e **sostituisce il numero di porta** iniziale con il nuovo numero
>
>![[NAT-trad.png|center|500]]
>
>il campo `numero di porta` è lungo 16 bit: NAT può supportare più di 60.000 connessioni simultanee con un solo indirizzo IP lato WAN

>[!error] NAT è contestato perché:
>- i router dovrebbero elaborare pacchetti *solo fino al livello di rete* (mentre, per NAT, un router deve spesso guardare anche il livello di trasporto)
>- il numero di porta viene usato per *identificare host e non processi*
>- viola l'*argomento punto-punto*: gli host dovrebbero comunicare tra di loro direttamente, senza intromissione di nodi né modifica di indirizzi IP e numeri di porta
>- causa interferenza con le applicazioni P2P in cui ogni peer dovrebbe essere in grado di avviare una connessione TCP con qualsiasi altro peer (a meno che il NAT non sia specificamente configurato per quella applicazione P2P)

# forwarding di datagrammi IP
>[!info] forwarding
>Inoltrare significa **collocare il datagramma sul giusto percorso** (*porta di uscita del router*) che lo farà avanzare verso la destinazione.
>- ovvero, inviare il datagramma al *prossimo hop*

In particolare, quando un host ha un datagramma da inviare, lo invia al router della rete locale; quando un router riceve un datagramma da inoltrare, accede alla tabella di routing per trovare il successivo hop a cui inviarlo.
- l'inoltro richiede una riga nella tabella per ogni blocco di rete

>[!example] esempio 
>
>![[forw-es.png|center|450]]
>
>>[!summary] altra rappresentazione della tabella di inoltro
>>
>>![[tabella-inoltro.png|center|500]]
>>- la prima colonna contiene i bit che identificano il blocco di indirizzi (lunghezza inferiore a 32 bit)
>>- un datagramma contiene però l'indirizzo IP dell'host di destinazione (lungo 32 bit) e non indica la lunghezza del prefisso di rete ⟶ per l'**instradamento**, si lavora così:
>>	- si controllano le corrispondenze con le diverse righe della tabella in ordine: la prima corrispondenza sarà quella corretta (sono ordinate per lunghezza, quindi se i primi x bit combaciano con la prima riga, quella corretta sarà quella, altrimenti si confronta un numero $\leq$ di bit con la seconda riga, e così via)
>>
>>>[!example] esempio
>>>
>>>![[tabella-inoltro.png|center|450]]
>>>
>>>Per esempio, il processo di inoltro di un datagramma con indirizzo di destinazione `180.70.65.140` (`10110100 01000110 01000001 10001100`) è questo:
>>>- la prima maschera (`/26`), ovvero `10110100 01000110 01000001 11` è applicata all'indirizzo di destinazione
>>>
>>>![[mask-es.png|center|450]]
>>>
>>>- il risultato è `180.70.65.128`, che non combacia con l'indirizzo di rete corrispondente
>>>- la seconda maschera `/25` è applicata all'indirizzo di destinazione; il risultato è `180.70.65.128`, che combacia ⟶ l'indirizzo del salto successivo e il numero di interfaccia `m0` vengono estratti dalla tabella e riusati per inoltrare il datagramma

## aggregazione degli indirizzi
Inserire nella tabella una riga per ogni bloco può portare alla creazione di tabelle molto lunghe (in cui la ricerca impiega molto tempo). Una possibile soluzione è l'**aggregazione degli indirizzi**: si combinano più reti specifiche in una rete più generale quando queste hanno lo stesso next hop, senza perdere le informazioni di routing.

>[!example] esempio
> 
>![[aggreg-indirizzi.png|center|500]]
> - in questo caso, gli indirizzi delle società 1, 2 e 3 (tutti indirizzi del tipo `140.24.7.xx/26`) vengono aggregati da $\text{R2}$ in una sola rete più ampia (`140.24.7.0/24`)

# ICMP
>[!summary]- overview del livello di rete
>
>![[rete-overview.png|center|450]]

**Internet Control Message Protocol** è il protocollo che si occupa della **notifica degli errori**. Infatti, ci sono errori che IP non gestisce, come:
- caso in cui un router deve scartare un datagramma perché non riesce a trovare un percorso per la destinazione finale
- caso in cui un datagramma ha il campo `TTL == 0`
- caso in cui un host di destinazione non ha ricevuto tutti i frammenti di un datagramma entro un limite di tempo

ICMP viene quindi usato da host e router per *scambiarsi informazioni a livello di rete*.

>[!tip] ICMP viene considerato parte di IP anche se usa IP per inviare i suoi messaggi

>[!example] esempio
>
>![[ICMP.png|center|450]]
>
> Un tipico use-case di ICMP è fornire un meccanismo di **feedback per i messaggi IP** inviati. 
> 
> In questo esempio, $A$ sta cercando di mandare un datagramma IP a $B$. Tuttavia, quando arriva al router $\text{R3}$, viene rilevato un problema di qualche tipo e il datagramma viene scartato. Allora $\text{R3}$ invia un messaggio ICMP ad $A$ per avvisarlo, se possibile con abbastanza informazioni da permettergli di correggere il problema. 
> - $\text{R3}$ può inviare il messaggio ICMP solo ad $A$ (non a $\text{R2}$ o $\text{R1}$)


> [!summary] messaggi ICMP
> I messaggi ICMP hanno un campo `tipo` e un campo `codice` e contengono l'intestazione e i primi 8 byte del datagramma IP che ha provocato la generazione del messaggio.
> 
> | tipo | codice | descrizione                             |
> | ---- | ------ | --------------------------------------- |
> | 0    | 0      | risposta eco (a ping)                   |
> | 3    | 0      | rete destinatario irraggiungibile       |
> | 3    | 1      | host destinatario irraggiungibile       |
> | 3    | 2      | protocollo destinatario irraggiungibile |
> | 3    | 3      | porta destinatario irraggiungibile      |
> | 3    | 6      | rete destinatario sconosciuta           |
> | 3    | 7      | host destinatario sconosciuto           |
> | 4    | 0      | riduzione (controllo di congestione)    |
> | 8    | 0      | richiesta eco                           |
> | 9    | 0      | annuncio del router                     |
> | 10   | 0      | scoperta del router                     |
> | 11   | 0      | TTL scaduto                             |
> | 12   | 0      | errata intestazione IP                  |
> |      |        |                                         |

- `ping` si basa sui messaggi di richiesta e risposta `echo` di ICMP

>[!tip] traceroute e ICMP
>Traceroute invia una serie di datagrammi IP alla destinazione, ciascuno contenente un segmento UDP con un numero di porta inutilizzata (il primo con `TTL=1`, il secondo con `TTL=2`, ecc.) e avvia un timer per ogni datagramma.
>
>Quando l’$n$-esimo datagramma arriva all’$n$-esimo router:
>- il router scarta il datagramma
> - invia all’origine un messaggio di allerta ICMP con il nome del router e l’indirizzo IP
> - quando il messaggio ICMP arriva, l’origine può calcolare l'RTT
> - (traceroute lo fa per 3 volte)