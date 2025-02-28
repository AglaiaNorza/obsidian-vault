Il primo router che incontriamo si chiama anche *edge router* (è il router a cui si collega la rete di accesso) (fa da ponte tra il backbone e la rete di accesso).
Una rete di accesso è composta da tutti i dispositivi (compresi i collegamenti) che ci danno la possibilità di raggiungere il primo router del backbone.

Il **backbone** è la rete composta esclusivamente da router e collegamenti tra router.

Queste reti funzionano con una commutazione a pacchetto.

Le reti di primo livello sono quelle che danno una copertura più estesa, e comunicano tra loro allo stesso livello.
Le reti di primo livello sono collegate tra di loro mediante cavi - se un oceano divide reti, vengono posati cavi sottomarini.

Gli ISP di livello due (nazionali) usufruiscono del servizio fornito dagli ISP di livello 1.
Gli ISP di livello 3 (locali) usufruiscono del servizio degli ISP di livello 2.

(*gerarchia*)

Un pacchetto (quindi un blocco di dati) passerà attraverso diverse reti di diversi livelli.
Uno dei problemi principali delle reti è quello di trovare il percorso che un pacchetto deve seguire dalla sorgente alla destinazione - **routing**.

## capacità e prestazioni
La velocità di una rete misura *quanto velocemente riesce a trasmettere e ricevere i dati*.

Nel caso di una rete a commutazione di pacchetto, si parla di:
- ampiezza di banda
- 


### bandwidth
L'**ampiezza di banda** è una caratteristica del mezzo trasmissivo, che indica *quanto il canale è in grado di trasmettere*. Si misura in hertz, e rappresenta la larghezza dell'intevallo di frequenze utilizzato dal sistema trasmissivo. Maggiore è l'ampiezza di banda, maggiore è la quantità di informazione che può essere trasmessa.

Il **bit rate** è la velocità di trasmissione, ovvero la (massima) quantità di bit al secondo che un link può trasmettere.

Il bit rate è *proporzionale* alla banda in hertz.

Per *banda* di un tipo di rete si intende quindi il bit rate garantito dai suoi link
(es: il rate di un link Fast Ethernet è 100Mbps, ovvero può inviare al massimo 100Mbps)

Il bit rate fornisce un'indicazione della **capacità** di una rete di trasferire dati.

### throughput
Il throughput indica quanto velocemente una rete possa *effettivamente* (mentre il rate nominalmente) trasmettere dati.

è misurato, come il rate, in numero di bit al secondo, ma è quasi sempre diverso dal rate.

Tipicamente, il thoughput è $\leq$ al bit rate (che è misura della *potenziale* velocità di un link, metre il thoughput è factual).

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