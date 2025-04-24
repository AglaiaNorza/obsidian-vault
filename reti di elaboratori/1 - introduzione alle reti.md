---
created: 2025-03-03T13:49
updated: 2025-04-24T21:06
---
Una **rete** è composta da dispositivi, chiamati **nodi** (collegati tra di loro da **link**), in grado di scambiarsi informazioni. I nodi possono essere sistemi terminali (end system), che utilizzano la rete per eseguire applicazioni e comunicare tra loro, oppure dispositivi di interconnessione, che si occupano di instradare e gestire il traffico dati all'interno della rete.

### dispositivi terminali
I **sistemi terminali** possono essere di due tipi:
1) **host** ⟶ macchine generalmente di proprietà degli utenti, dedicate ad eseguire applicazioni (es. computer, cellulari)
2) **server** ⟶ computer con elevate prestazioni che forniscono servizio a diverse applicazioni utente
### dispositivi di interconnessione
I **dispositivi di interconnessione** rigenerano e/o modificano il segnale che ricevono.
Si distinguono in:
- **router** ⟶ collegano due o più reti
- **switch** ⟶ collegano diversi sistemi terminali localmente
- **modem** ⟶ trasformano la codifica dei dati (trasformano i dati digitali del computer in dati analogici della rete)
### collegamenti
I dispositivi di rete sono collegati tramite mezzi chiamati **link**. 
Questi possono essere *cablati* (es. rame, fibra ottica) o *wireless* (es. onde elettromagnetiche, satellite).
#### mezzi trasmissivi cablati
I dati viaggiano da un sistema terminale ad un altro passando per una serie di coppie trasmettente-ricevente, attraverso mezzi *fisici*.

Alcuni esempi sono il cavo coassiale o, più interessante, la fibra ottica, che non subisce interferenze.
#### mezzi trasmissivi wireless
Il segnale si propaga nell’*atmosfera* e nello spazio eterno.
- non richiedono l'installazione di cavi
- si possono usare ovunque
- ma: possono subire molte più interferenze (es. riflessione, ostruzione)

L'esempio più noto è quello della LAN.
## classificazione delle reti
Le reti si possono classificare in base al loro range:

| scala    | tipo                      | esempio        |
| -------- | ------------------------- | -------------- |
| Dintorni | Personal Area Network     | bluetooth      |
| Edificio | Local Area Network        | WiFi, ethernet |
| Città    | Metropolitan Area Network | DSL            |
| Paese    | Wide Area Network         | grandi ISP     |
| Pianeta  | The Internet              | Internet       |

### LAN: Local Area Network
Solitamente è una rete *privata*, che collega i sistemi terminali in un singolo edificio.
Ogni sistema all’interno della LAN ha il suo indirizzo **IP**, che lo identifica univocamente.

- nasce con lo scopo di condividere risorse tra sistemi terminali - oggi si connette ad altre reti per consentire comunicazioni su larga scala.

#### con cavo condiviso: 
(non più utilizzata)

![[cavo-condiviso.png|center|400]]

- cavo a cui è possibile collegare ogni dispositivo
- è una rete **broadcast**: quando un nodo trasmette, tutti gli altri ricevono (quindi solo un nodo alla volta può trasmettere)

#### con switch di interconnessione:
![[LAN-switch.png|center|380]]

Ogni dispositivo è direttamente collegato allo switch - esso riconosce l’indirizzo di destinazione e invia il pacchetto al solo destinatario e non agli altri.
- consente a coppie di dispositivi che non hanno sorgente e destinazione in comune di comunicare contemporaneamente tra di loro

(se due dispositivi vogliono trasmettere allo stesso destinatario, lo switch serializzerà le loro trasmissioni)
### WAN: Wide Area Network
Può servire una città, una regione, una nazione…. 
- interconnette switch, router e modem (non host)
- è tipicamente gestita da un *Internet Service Provider* che fornisce servizio alle varie LAN

Si divide in:
- WAN **punto punto**: due reti in comunicazione tramite un collegamento (cablato o wireless)
- WAN **a commutazione**: più di due punti di terminazione - usata nelle dorsali di internet

>[!example] esempio: la rete GARR
>Un esempio di WAN è la rete GARR (in fibra ottica), che collega centri di cultura (università, biblioteche, musei...).

È difficile trovare LAN o WAN isolate: sono di solito *connesse tra di loro* per formare un internet (internetwork).

>[!example] esempio 
>Per esempio, due edifici in due città diverse con due LAN possono essere messi in comunicazione tramite una WAN punto-punto:
>
>![[WAN-LAN.png|center|450]]
>
>(i router instradano i pacchetti da una LAN all'altra)

## switching (commutazione)
I sistemi terminali comunicano tra loro attraverso dispositivi come switch e router, che si trovano nella rotta tra i sistemi sorgente e destinazione.

Ci sono due tipi di reti basate su switch: reti a commutazione di circuito e a commutazione di pacchetto.

### rete a commutazione di circuito
Tra mittente e destinatario viene stabilito un collegamento dedicato - **circuito** - usato per l'intera comunicazione. Dopo la comunicazione, il circuito viene rilasciato (per ogni comunicazione viene stabilito un nuovo circuito).

Le risorse necessarie al circuito (banda ecc) sono riservate per tutta la comunicazione, e le informazioni sul circuito vengono mantenute dalla rete.

![[comm-circuito.png|center|450]]

Anche se ci sono più percorsi, solo uno di questi verrà usato per l'intera comunicazione.

>[!tip] La commutazione ci garantisce che, una volta stabilito un circuito, la sua capacità sia garantita (e usata completamente).

>[!bug] Funziona bene quando il numero di dispositivi è ragionevole, ma non è flessibile 

>[!example] esempio
> 
>![[es-comm-circ.png|center|400]]
>
>In questo esempio, la linea può gestire contemporeaneamente quattro canali voce: quindi, se tutte le otto persone comunicano, la capacità della linea viene sfruttata completamente. Ma, se avviene una comunicazione tra solo due dispositivi, viene utilizzato solo 1/4 della capacità della rete (inefficiente).

>[!example]- esercizio
>Si vuole inviare un file di $\text{160000bits}$ dall'host $A$ all'host $B$ su una rete a commutazione di circuito. 
>- I link hanno rate pari a $\text{536kbps}$ e usano il TDM con $\text{48 slot/sec}$. 
>- Il tempo per stabilire il circuito tra $A$ e $B$ è $\text{500ms}$. 
> 
>Quanto impiega l'host A a trasmettere il file?
>
>1) il link ha $1536\text{kbps}$, divisi in $48$ slots/sec. Quindi, ogni slot ha $\frac{1536}{48}=32\text{kbps}$.
>2) il file è di $\frac{160000\text{bit}}{32 \cdot 10^3\text{bps}}=5\text{s}$
>3) il tempo totale è quindi: $\text{500ms+5ms}=5,5\text{s}$
#### suddivisione della rete
Con la commutazione di circuito le risorse della rete vengono quindi suddivise in pezzi, che saranno poi allocati ai vari collegamenti.
Se non utilizzate, le risorse rimangono inattive.

Ci sono due modi per dividere la banda della rete: 

>[!info] Frequency Division Multiplexing (FDM)
>
>![[FDM.png|center|500]]

>[!info] Time Division Multiplexing (TDM)
>
>![[TDM.png|center|500]]

### rete a commutazione di pacchetto
Anche detta "*store and forward*".
In questo caso si suddividono invece i dati in **pacchetti**, che vengono trasmessi sulla rete. La comunicazione non è quindi continua.

![[comm-pacchetto.png|center|500]]

Il mittente spedisce i suoi pacchetti, il router riceve i pacchetti da tutti i mittenti, li mette in coda (*store*), e li spedisce in maniera seriale al prossimo router (*forward*).
I pacchetti non sono tutti dello stesso nodo di origine (si mischiano, **viaggiano indipendentemente**). Per questo, blocchi di dati (anche dello stesso file) possono prendere percorsi diversi e arrivare in momenti diversi.

![[comm-pacch-2.png|center|400]]

- non viene riservata *nessuna risorsa* per la comunicazione.

È più flessibile: la banda viene sempre utilizzata al massimo (anche se non tutti gli host stanno comunicando).

- se più dispositivi cominicano tra loro e la linea di comunicazione non ha la capacità necessaria per inviarli tutti, i pacchetti vanno memorizzati in una coda e possono incorrere in ritardi
## Internet
Una internet (con la 'i' minuscola) è costituita da due o più reti interconnesse. L'internet più famosa è "Internet" (con la 'I' maiuscola), composta da migliaia di reti interconnesse.
- Internet è a commutazione di pacchetto

>[!summary] rappresentazione concettuale di Internet
> 
>![[Internet.png|center|400]]
### accesso a internet
Qualsiasi utente può connettersi a Internet, tramite un ISP a cui deve essere fisicamente collegato. Il collegamento che connette l'utente al primo router di Internet è detto **rete di accesso**.

Si può accedere a internet in tre modi diversi:
- via *rete telefonica*
- tramite *reti wireless*
- con *collegamento diretto*

#### via rete telefonica
È possibile collegarsi a internet modificando la linea telefonica tra la sede del dispositivo e la centrale telefonica con una WAN punto-punto.
##### servizio dial-up
Si inserisce sulla lina telefonica un modem (modulatore-demodulatore) che converte i dati digitali in analogici (per la linea telefonica) e viceversa.

![[dial-up.png|center|450]]

- è un metodo lento, che impedisce di parlare e navigare contemporaneamente

##### Digital Subscriber Line (DSL)
Supporta la comunicazione digitale ad alta velocità sulla linea telefonica.
Si divide il collegamento tra l'abitazione e l'ISP in tre bande di frequenza non sovrapposte.

![[DSL.png|center|450]]

- è veloce e permette di usare contemporaneamente voce e dati

#### tramite ethernet
Lo switch (Ethernet) della LAN è generalmente collegato ad un router istituzionale connesso ai router della dorsale

#### wireless
Può essere:
- **WiFi** ⟶ tramite un Access Point locale connesso alla Ethernet cablata
	- ha un raggio di azione limitato a qualche decina di metri
- **Cellulare** ⟶ utilizza la rete cellulare, tramite gli Access Point della compagnia telefonica
	- ha un raggio di decine di chilometri