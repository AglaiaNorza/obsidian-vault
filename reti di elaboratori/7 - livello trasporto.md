---
created: 2025-03-20T14:18
updated: 2025-04-06T16:09
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
Il multiplexing/demultiplexing permette di far diventare il servizio di trasporto host ⟶ host a livello di rete un servizio di trasporto processo ⟶  processo per le applicazioni in esecuzione sugli host.

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


Come gestiamo i numeri di porta? C'è un API di comunicazione: socket API - interfaccia tra livello di comunicazione e livello di trasporto (ci permette di passare pacchetti al livello di trasporto).

Una socket appare come un terminale/file, ma è in realtà una struttura dati creata e utilizzata dal programma applicativo. 
Comunicare tra 