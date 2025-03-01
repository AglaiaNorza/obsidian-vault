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

## switching
router e switch uniscono i colegamenti
Ci sono due tipi di reti basate su switch:
commutazione di circuito/di pacchetto

**circito** tra mittente e destinatario viene stabilito un collegamento dedicato - **circuito** - usato per l’intera comunicazione. Viene poi rilasciato il circuito e ne verrà stabilito uno nuovo per future comunicazioni.

Abbiamo bisogno di risorse fisiche (bande: capacità di trasmissione, altro …?)
Le informazioni riguardanti il circuito vengono mantenute dalla rete. 


Stabilita una rotta, riservate le risorse lungo la rotta - ogni dato spedito seguirà la rotta prefissata finché la comunicazione non finisce.

La commutazione ci garantisce che, una volta stabilito un circuito, una certa capacità sia garantita per un circuito.
1/4 garantito per tutta la comunicazione
Funziona bene quando il numero di dispositivi è ragionevole, ma non è flessibile.

esempi condivisione della risorsa
divisione frequenza: lo spettro delle frequenze viene diviso in sottointervalli (trasmissione consecutiva con capacità di banda limitata)
divisione tempo: tutto il canale per un piccolo lasso di tempo 

Secondo tipo di commutazione (oggi): commutazione di pacchetto, store and forward.
La rete è di tutti, si suddividono i dati in pacchetti (parti) che vengono trasmessi.
Il mittente spedisce i suoi pacchetti, il router riceve i pacchetti da tutti i mittenti, li mette in coda, e li spedisce in maniera seriale al prossimo router.
I pacchetti non sono tutti dello stesso nodo di origine (si mischiano, viaggiano indipendentemente).                 
Non viene riservata nessuna risorsa della comunicazione.
Store and forward: il router memorizza (store) e inoltra (forward) i pacchetti.
(il router ha code in ingresso e code in uscita)

Se mando una cartolina a mia nonna che abita nel palazzo di mia madre, potrebbe arrivare più tardi.

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