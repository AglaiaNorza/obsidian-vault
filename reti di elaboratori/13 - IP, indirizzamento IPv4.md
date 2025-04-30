---
created: 2025-04-01
updated: 2025-04-30T14:12
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
>- **identificatore, flag, offset di frammentazione** ⟶ servono per gestire la frammentazione dei pacchetti [vedi [[13 - IP, indirizzamento IPv4#frammentazione|sotto]]] (IPv6 non prevede frammentazione)
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
>![[frammentazione-es2.png]]
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
>- ogni interfaccia di host e router internet ha un indirizzo IP *globalmente univoco*
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
>- otterrà indirizzi della forma `a.b.c.d/x`, dove `x` bit indicano la *sottorete* e `32-x` bit indicano 
>
>>[!tip] nota bene: i `32-x` bit possono presentare un'aggiuntiva struttura di sottorete
>
>L'ISP, a sua volta, si rivolge all'Internet Corporation for Assigned Names and Numbers (**ICANN**), che: 
>- gestisce i server radice DNS
>- alloca i blocchi di indirizzi
>- assegna e risolve dispute su nomi di dominio

Per assegnare un indirizzo IP ad un host, si può decidere tra assegnazione temporanea o permanente, e tra configurazione manuale o con [[14 - DHCP, NAT, forwarding, ICMP|DHCP]]