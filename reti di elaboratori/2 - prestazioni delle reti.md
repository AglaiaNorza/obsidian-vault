Internet è una rete di reti, composta da reti di accesso e dal backbone internet.

## rete di accesso
Un **access network** è formato da tutti i dispositivi e collegamenti fisici che connettono un sistema al primo *edge router*, ovvero al primo router che si incontra, che fa da ponte tra il backbone e la rete di accesso.

Il **backbone** è la rete composta esclusivamente da router e collegamenti tra router. Può essere a commutazione di circuito, o a commutazione di pacchetto.

## struttura di Internet
Internet ha una struttura fondamentalmente gerarchica. Si divide in reti di livelli diversi:
- ISP di **primo livello**: danno una copertura più estesa (nazionale/internazionale), e comunicano tra loro "come pari".
	- un esempio sono le dorsali sottomarine, che collegano anche continenti diversi
- ISP di **secondo livello**: hanno copertura nazionale o distrettuale, e si possono connettere a ISP di livello 1, o ad altri ISP di livello 2
- ISP di **terzo livello** e ISP locali: "last hop network", sono le più vicine ai sistemi terminali

Un pacchetto passerà attraverso diverse reti di diversi livelli.
Uno dei problemi principali delle reti è quello del **routing**, ovvero trovare il percorso che un pacchetto deve seguire dalla sorgente alla destinazione.

![[routing.png|center|400]]
## capacità e prestazioni delle reti
La velocità di una rete misura *quanto velocemente riesce a trasmettere e ricevere i dati*.

Nel caso di una rete a commutazione di pacchetto, si parla di:
- ampiezza di banda e bit rate
- throughput
- latenza
- perdita di pacchetti
### bandwidth e bitrate
L'**ampiezza di banda** è una caratteristica del mezzo trasmissivo, che indica *quanto il canale è in grado di trasmettere*. Si misura in hertz, e rappresenta la larghezza dell'intevallo di frequenze utilizzato dal sistema trasmissivo. Maggiore è l'ampiezza di banda, maggiore è la quantità di informazione che può essere trasmessa.

Il **bit rate** è la velocità di trasmissione, ovvero la (massima) quantità di bit al secondo che un link può trasmettere.

Il bit rate è *proporzionale* alla banda in hertz (maggiore è la banda, maggiore sarà il bit rate).

> [!info] banda
> Quando si parla di **banda** di un tipo di rete si intende quindi il bit rate garantito dai suoi link.
>  
> (es: il rate di un link Fast Ethernet è 100Mbps, ovvero può inviare al massimo 100Mbps)

Il bit rate fornisce un'indicazione della **capacità** di una rete di trasferire dati.

### throughput
Il throughput indica quanto velocemente una rete possa *effettivamente* (mentre il rate nominalmente) trasmettere dati.

È il numero di bit al secondo che *passano attraverso un punto* della rete.
- è quindi misurato, come il rate, in numero di bit al secondo, ma è quasi $\leq$ del bit rate (che èuna misura della *potenziale* velocità di un link)

>[!example] esempio 
>Una strada è progettata per far transitare 1000 auto al minuto. Se c'è traffico, questo numero scende a 100.
>Il rate è 1000 auto al minuto, il throughput è 100 auto al minuto.

Se vogliamo misurare il throughput end-to-end (dalla partenza alla destinazione).

Il collegamento con il rate minore è quello che determina il valore massimo del throughput.

In generale, in un percorso con $n$ link in serie, si ha: $\text{Throughput}=min(T_{1},\,T_{2},\,\dots,\,T_{n})$.

[slide 23?]
## delay e loss
Il throughput può variare per numero di utenti connessi, oppure per delle latenze, o addirittura perdita di pacchetti.

Ci sono diversi fattori che determinano la latenza (tempo che un pacchetto impiega dal momento di partenza al momento di arrivo) di un pacchetto.

Nella commutazion di pacchetto, i pacchetti si accodano nei buffer dei router.
Se arrivano più pacchetti di quanti possano uscire, questi dovranno attendere.

Intanto, un pacchetto deve essere processato all'interno del nodo. Poi, ci può essere un tempo di accodamento, e poi il tempo che il router impiega a trasmettere un pacch

Ci sono qiundi 4 ritardi che concorrono al ritardo toale che il pacchetto subisce:
### ritardo di elaborazione
1) controllo sugli errori: il pacchetto è integro? se no, viene tipicamente scartato
2) determinazione del canale di uscita
3) tempo dalla ricezione dalla porta di input alla consegna alla porta di output (ci sono buffer sia nelle porte di ingresso che nelle porte di uscita)

### ritardo di accodamento
Il pacchetto viene messo in coda sul buffer di uscita, dove ci sono altri pacchetti
- attesa di trasmissione (possibile sia nella coda di input che nella coda di output): dipende dalla congestione del router
	- può variare da pacchetto a pacchetto (diverse code possono essere più o meno piene)

### ritardo di trasmissione
Dipende dal canale. 
è il tempo richiesto per trasmettere tutti i bit del pacchetto sul collegamento.
$t_{2}-t_{1}$

Questo ritardo si può stimare con una formula (perché dipende dal rate del collegamento e dalla lunghezza del pacchetto): $\text{ritardo di trasmissione}=\frac{L}{R} =\frac{\text{lunghezza del pacchetto in bit}}{\text{bit rate del collegamento}}$

### ritardo di propagazione
Quanto impiega un pacchetto immesso a propagarsi sul canale ("tempo di viaggio" lungo il canale).
Dipende dalla lunghezza del collegamento, e dalla velocità di propagazione del collegamento

velocità di propagazione != rate
vale per il singolo bit 
tipicamente corrisponde alla velocità della luce

$\text{Ritardo di propagazione}=\frac{d}{s}=\frac{\text{lunghezza collegamento}}{\text{velocita' di propagazione}}$

(la prima auto arriverà prima di 62 mins, ma l'ultima 62 quindi 62 totali)

la prima auto arriva prima che le altre vengano trasmesse.

[slide 32, 33]

Se le code sono piene, i pacchetti in arrivo vengono persi.

Esiste uno strumento che permette di misurare il ritardo ....

Il round trip time include i 4 ritardi.
Può succedere, se c'è congestione, che 