---
created: 2025-03-20T14:18
updated: 2025-04-19T16:51
---
I protocolli di trasporto forniscono la **comunicazione logica** tra processi applicativi di host differenti.
- gli host eseguono processi *come se fossero direttamente connessi* 

I protocolli di trasporto vengono eseguiti nei **sistemi terminali**:
- **lato invio** ⟶ incapsula i messaggi in segmenti e li passa a livello di rete
- **lato ricezione** ⟶ decapsula i segmenti in messaggi e li passa a livello di applicazione

>[!info] incapsulamento/decapsulamento
>
>![[incaps-decaps.png|center|450]]
>
> i pacchetti a livello di trasporto sono chiamati **segmenti** se viene usato il protocollo TCP, o **datagrammi utente** se viene usato il protocollo UDP

>[!tip] relazione tra livello di trasporto e livello di rete
>Il **livello di rete** si occupa della comunicazione tra host (e si basa sui servizi del livello di collegamento). Il **livello di trasporto** si occupa della comunicazione tra processi (si basa sui servizi di rete e li potenzia).
>
>![[rete-trasporto.png|center|500]]
>
>>[!example] analogia con la posta ordinaria
>>Si può fare un'analogia con la posta: una persona di un condominio invia una lettera ad una persona di un altro condominio attraverso un portiere.
>>
>>- processi = persone
>>- messaggi delle applicazioni = lettere 
>>- host = condomini
>>- protocollo di trasporto = portiere
>>- protocollo del servizio rete = servizio postale

## indirizzamento
La maggior parte dei sistemi operativi è multiutente e multiprocesso. È quindi necessario individuare:
- host locale e host remoto (indirizzi IP)
- processo locale e processo remoto (numeri di porta)

>[!info] indirizzo IP vs numero di porta
>
>![[IP-n-porta.png|center|350]]
>
>indirizzo IP e numero di porta formano il **socket address**.

## multiplexing/demultiplexing
Il multiplexing/demultiplexing fa sì che il servizio di trasporto da host a host a livello di rete possa diventare un servizio di trasporto da processo a  processo per le applicazioni in esecuzione sugli host.

Il **multiplexing** viene effettuato dall'host mittente, che raccoglie dati da varie socket e li incapsula con l'intestazione.

Il **demultiplexing** viene effettuato dall'host ricevente, che consegna i segmenti ricevuti alla socket appropriata.

>[!info] funzionamento del demultiplexing
>1) l'host riceve i datagrammi IP
>	- ogni datagramma ha un IP di origine e uno di destinazione
>	- ogni datagramma trasporta un segmento a livello di trasporto
>	- ogni segmento ha un numero di porta di origine e un numero di porta di destinazione
>1) l'host utilizza gli indirizzi IP e i numeri di porta per inviare il segmento al processo appropriato
>
>![[pacchettoTCPUDP.png|center|300]]
>

>[!example] analogia del portiere
>Nell'esempio precedente, i portieri effettuano un'operazione di multiplexing quando raccolgono le lettere dai condomini e le imbucano, e una di demultiplexing quando ricevono le lettere dal postino, leggono il nome del destinatario e gliele consegnano.

## API di comunicazione
La **socket** API (spiegata meglio [[11 - interfaccia socket|qui]]) è un'interfaccia di comunicazione che permette la comunicazione tra tra livello di applicazione e livello di trasporto.

![[socket.png|center|400]]

- appare come un terminale, ma non è un'entità fisica (una struttura dati creata ed utilizzata dal programma applicativo)
- la comunicazione tra un processo client e un processo server è la comunicazione tra due socket create nei due lati di comunicazione

![[socket-comms.png|center|450]]

### socket address

>[!info] un socket address è composto da **indirizzo IP** (32 bit) e **numero di porta** (16 bit)
>
>![[socket-address.png|center|500]]
> 
>- i numeri di porta (che vanno quindi da 0 a 65535) si dividono in *well-known ports*  (per server comuni e noti) e *assigned ports*
>	- `0` ⟶ non usato
>	- `1-255` ⟶ well-known processes
>	- `256-1023` ⟶ riservati per altri processi
>	- `1024-65535` ⟶ per user apps (quindi "utilizzabili")

L'interazione client-server è bidirezionale. È necessaria quindi una coppia di indirizzi socket: quello **locale** (mittente) e quello **remoto** (destinatario).

>[!question] individuare i socketi *lato client*
>- **socket address locale** ⟶ viene fornito dal sistema operativo, che:
>	- conosce l'indirizzo IP del computer su cui il client è in esecuzione
>	- assegna temporaneamente un numero di porta
>- **socket address remoto**:
>	- il numero di porta è noto in base all'applicazione
>	- l'indirizzo IP viene fornito dal DNS

>[!question] individuare i socket *lato server*
>- **socket address locale** ⟶ fornito dal sistema operativo
>	- conosce l'IP del computer su cui il server è in esecuzione
>	- il numero di porta è noto al server perché è assegnato dal progettista (well-known o scelto)
>- **socket address remoto** ⟶ è il socket address locale del client che si connette - si trova nel pacchetto di richiesta
>
>>[!warning] il socket address locale di un server *non cambia*, mentre il socket address remoto *varia ad ogni interazione* con client diversi o con lo stesso client su connessioni diverse
