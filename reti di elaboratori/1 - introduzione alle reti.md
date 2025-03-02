Una **rete** è composta da dispositivi, chiamati **nodi** (collegati tra di loro da **link**), in grado di scambiarsi informazioni. I nodi possono essere sistemi terminali (end system), che utilizzano la rete per eseguire applicazioni e comunicare tra loro, oppure dispositivi di interconnessione, che si occupano di instradare e gestire il traffico dati all'interno della rete.

### dispositivi terminali
I **sistemi terminali** possono essere di due tipi:
1) **host** --> macchine generalmente di proprietà degli utenti, dedicate ad eseguire applicazioni (es. computer, cellulari)
2) **server** --> computer con elevate prestazioni che forniscono servizio a diverse applicazioni utente
### dispositivi di interconnessione
I **dispositivi di interconnessione** rigenerano e/o modificano il segnale che ricevono.
Si distinguono in:
- **router** --> collegano due o più reti
- **switch** --> collegano diversi sistemi terminali localmente
- **modem** --> trasformano la codifica dei dati (trasformano i dati digitali del computer in dati analogici della rete)
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
>In questo esempio, la linea può gestire contemporeaneamente quattro canali voce: quindi, se tutte le otto persone comunicano, la capacità della linea viene sfruttata completamente. Ma, se avviene una sola comunicazione tra due dispositivi, viene utilizzato solo 1/4 della capacità della rete (inefficiente).

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



(slide 37)Se solo un nodo sta spedendo, può spedire fino a raggiungere il massimo della velocità del canale - se sono in due, possono dividersi il canale
- molto più flessibile rispetto alla commutazione di circuito

internet (i minuscola) è a commutazione di pacchetto.

rappresentazione concettuale di internet

### accesso a internet

via rete telefonica [slide]
- con un modem non si possono inviare dati e parlare contemporaneamente
ehternet: 
- rate maggiore rispetto al wireless
wifi
- access point a cui ci colleghiamo, collegato in maniera cablata al router
- raggio di azione piccolo

rete cellulare 
- ci si collega ad una base station della compagnia telefonica