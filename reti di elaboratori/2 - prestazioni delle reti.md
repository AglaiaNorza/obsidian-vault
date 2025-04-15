---
created: 2025-03-26T18:31
updated: 2025-04-14T22:54
---
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
- è quindi misurato, come il rate, in numero di bit al secondo, ma è quasi $\leq$ del bit rate (che è una misura della *potenziale* velocità di un link)

>[!example] esempio 
>Una strada è progettata per far transitare 1000 auto al minuto. Se c'è traffico, questo numero scende a 100.
>Il rate è 1000 auto al minuto, il throughput è 100 auto al minuto.

In un percorso da una sorgente a una destinazione, un pacchetto passerà attraverso diversi link con throughput diversi: come si misura il throughput medio "end-to-end"?
 
> [!tip] throughput medio
> In generale, in un percorso con $n$ link in serie, si ha: $$\text{Throughput}=min(T_{1},\,T_{2},\,\dots,\,T_{n})$$
> 
> - un collegamento che vincola un throughput end-to-end (il collegamento con minore throuhgput nel percorso) si chiama **collo di bottiglia**

>[!example]- esempio 
> 
>![[throughput.png|center|400]]
>
>qui, il throughput medio sarà quindi 100kbps

>[!bug] throughput nei link condivisi
>Il link tra due router raccoglie spesso il flusso da varie sorgenti e/o lo distribuisce a varie destinazioni. Il rate del link tra due router è quindi *condiviso* tra i flussi di dati.
>
>>[!example] esempio
>>![[through-cond.png|center|350]]
>>
>>In questo caso, quindi, il throughput end-to-end sarà 200kbps.
## delay
Il throughput può variare per una serie di motivi: numero di utenti connessi, latenze, o addirittura perdita di pacchetti.

Tra i fattori che incidono sul tempo di trasmissione ci sono l'accodamento dei pacchetti nei buffer dei router (necessario quando il traffico in ingresso supera la capacità di uscita), il tempo di elaborazione del pacchetto all'interno del nodo e il tempo di trasmissione effettivo del pacchetto da parte del router.

Ci sono qiundi 4 ritardi che concorrono al ritardo totale che il pacchetto subisce:
- ritardo di **elaborazione**
- di **accodamento**
- di **trasmissione**
- di **propagazione**
### ritardo di elaborazione
L'elaborazione prevede:
1) controllo sugli errori: il pacchetto è integro? se no, viene tipicamente scartato
2) determinazione del canale di uscita
3) tempo dalla ricezione dalla porta di input alla consegna alla porta di output (ci sono buffer sia nelle porte di ingresso che nelle porte di uscita)
### ritardo di accodamento
Il pacchetto viene messo in coda sul buffer di uscita, dove ci sono altri pacchetti. 
- si genera un'attesa di trasmissione (possibile sia nella coda di input che nella coda di output): dipende dalla congestione del router
	- può variare da pacchetto a pacchetto (diverse code possono essere più o meno piene)
- dipende dal *tasso di arrivo*, dal *rate* e dalla *lunghezza dei pacchetti*

Dati:
- $R=\text{rate di trasmissione (bps)}$
- $L=\text{lunghezza del pacchetto (bit)}$
- $a = \text{tasso medio di arrivo dei pacchetti (pkt/s)}$

abbiamo:

$$\frac{La}{R}=\text{intensità di traffico}$$

Se: 
- $La/R \sim 0$ ⟶ poco ritardo
- $La/R \rightarrow 1$ ⟶ ritardo consistente
- $La/R>1$ ⟶ più lavoro in arrivo di quanto possa essere effettivamente svolto 
### ritardo di trasmissione
È il tempo richiesto per trasmettere tutti i bit del pacchetto sul collegamento (dipende quindi dal canale).
Se il primo bit viene trasmesso al tempo $t_{1}$ e l'ultimo al tempo $t_{2}$, il ritardo di trasmissione è $t_{2}-t_{1}$.

Questo ritardo dipende quindi unicamente dal rate del collegamento e dalla lunghezza del pacchetto, quindi si può stimare con una formula:

$$\text{ritardo di trasmissione}=\frac{L}{R} =\frac{\text{lunghezza del pacchetto in bit}}{\text{bit rate del collegamento}}$$

### ritardo di propagazione
È dato dal tempo che un bit impiega a propagarsi sul canale ("tempo di viaggio" lungo il canale).
Dipende dalla lunghezza del collegamento, e dalla velocità di propagazione del collegamento.

$$\text{Ritardo di propagazione}=\frac{d}{s}=\frac{\text{lunghezza collegamento}}{\text{velocità di propagazione}}$$

>[!example] analogia del casello autostradale
>- Le automobili viaggiano a 100km/h. 
>- Il casello serve un'auto ogni 12 secondi (ovvero ha un rate di 5 auto/min).
>
>Quanto tempo occorre perché 10 auto passino il secondo casello?
>
>- tempo richiesto al casello per trasmettere l'intera colonna sull'autostrada: $\frac{10\text{ auto}}{5\text{ auto/min}}=2\text{ min}$
>- tempo richiesto a un'auto per viaggiare dall'uscita di un casello fino al casello successivo: $\frac{100\text{km}}{100\text{km/h}}=1\text{h}$
>
>Il tempo che intercorre da quando l'intera colonna di vetture si trova di fronte al primo casello di partenza a quando tutte le auto hanno passato il secondo casello è dato dalla somma del ritardo di trasmissione e del ritardo di propagazione, ovvero $62\text{ min}$ (la prima auto arriverà prima di 62 minuti, ma l'ultima passerà esattamente al 62-esimo).

### ritardo di nodo
il ritardo di nodo $d_{nodal}$ è dato dalla somma di:
- ritardo di **trasmissione**
- ritardo di **propagazione**
- ritardo di **elaborazione**
- ritardo di **accodamento**

$$d_{nodal}=d_{trans}+d_{prop}+d_{proc}+d_{queue}$$
## packet loss
Se una coda o un buffer hanno capacità limitata, quando il pacchetto trova la coda piena, verrà **scartato** (e sarà quindi perso).

Un pacchetto perso può essere ritrasmesso dal nodo precedente, dal sistema terminale che lo ha generato, o non essere ritrasmesso.

## ritardi e percorsi in internet
Cosa significano effettivamente packet delay e loss per Internet?

Esiste un programma diagnostico, `traceroute`, che fornisce una misura del ritardo dalla sorgente a tutti i router lungo il percorso Internet punto-punto verso la destinazione.

Il mittente invia dei pacchetti e ogni router risponderà al mittente, che calcolerà l’intervallo di tempo tra invio e risposta.

L’output del comando è composto da 6 colonne:

1. Numero del router nel percorso
2. Nome del router
3. Indirizzo del router
4. Tempo andata e ritorno 1° pacchetto
5. Tempo andata e ritorno 2° pacchetto
6. Tempo andata e ritorno 3° pacchetto

- il tempo di andata e ritorno (Round Trip Time) include i 4 ritardi visti precedentemente.
- se non riceviamo risposte o se il router nasconde le sue informazioni, vengono mostrati degli * . 
- inoltre, dato che il ritardo di accodamento varia in base alla congestione della rete, può accadere che per un router abbiamo un ritardo $T$ e per il router successivo un ritardo $T_{1}>T$.

>[!example] esempio di `traceroute` da `gaia.cs.umass.edu` a `www.eurecom.fr`
>![[traceroute.png|center|400]]

### prodotto rate * ritardo
Il prodotto $\text{rate} \cdot\text{ritardo}$ rappresenta il **massimo numero di bit che possono riempire un collegamento**.

>[!example] esempio
>Supponiamo di avere un link con un rate di $1\text{bps}$ e un ritardo di $5\text{sec}$.
>
>![[ratexritardo.png|center|350]]
>
>Non ci possono essere quindi più di $5\text{bit}$ contemporaneamente sul link.

Possiamo pensare al link tra due punti come a un tubo. La sezione trasversale del tubo rappresenta il rate e la lunghezza il ritardo. Possiamo dire che il volume definisce il prodotto rate-ritardo.

![[tubo.png|center|350]]


