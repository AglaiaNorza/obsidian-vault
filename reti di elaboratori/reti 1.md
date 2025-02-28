**nodi** collegati da *link*.

Nodi su cui sono attive app: host
Nodi su cui non sono attive app: switch o router (con più funzioni)

**rete** : composta da dispositivi in grado di scambiarsi informazioni (end system) e dispostivi di interconnessione (fanno viaggiare le informazioni)

Sistemi terminali:
1) host -→ con cui l’utente interagisce (portatile, cellulare) - ospitano applicazioni
2) server -→ più potenti, eseguono programmi che forniscono servizio alle applicazioni utente
	- tipicamente gestiti dagli amministratori di sistema

### dispositivi di interconnessione
In alcuni casi rigenerano e in altri modificano il segnale
3 tipi:
- router - collegano una rete ad altre reti
- switch - colllegano più sistemi terminali a livello locale
- modem - trasformano la codifica dei dati 

I dispositivi di rete sono cablati (o guidati) da mezzi chiamati link.

I collegamenti possono essere fisici o wireless (onde elettromagnetiche o satellite).

### mezzi trasmissivi cablati
(un nodo non è solo trasmittente o ricevente, è entrambi allo stesso tempo).
Se il mezzo è cablato, il segnale si può propagare

coassiale we do not care

**cavo a fibra ottica**: 
- non subisce interferenze

### wireless
Il segnale si propaga nell’aria.
- possono subire molte più interferenze

pro:
-  si può usare ovunque

contro: 
- soffrono l’ambiente circostante
	- riflessione
	- ostruzione

+interessanti: LAN

## classificazione delle reti

LAN - ha una parte cablata (ethernet) e una wireless (wifi)
MAN - gran parte della rete è cablata
WAN - a livello nazionale 
Internet - livello planetario

### LAN
Solitamente è una rete privata, che collega i sistemi terminali in un singolo edificio.
Ogni sistema all’interno della LAN ha il suo indirizzo IP, che lo identifica univocamente.

- nasce con lo scopo di condividere risorse tra sistemi terminali - oggi si connette ad altre RETI ED ESTESA SU LARGA SCALA.

#### con cavo condiviso: 
non più utilizzata
- cavo a cui è possibile collegare ogni dispositivo
- rete broadcast: quando un nodo trasmette, tutti gli altri ricevono (solo uno alla volta può ricevere)

#### switch
ogni dispositivo è direttamente collegato allo switch - esso riconosce l’indirizzo di destinazione e invia il pacchetto al solo destinatario e non agli altri.
Consente a coppie di dispositivi che non hanno sorgente e destinazione in comune di comunicare contemporaneamente tra di loro.

(se 1 e 2 vogliono trasmettere a 5, lo switch serializzerà)

## WAN
può servire una città, una regione, una nazione…. 
- interconnette switch, router e modem (non host)
- è tipicamente gestita da un Internet Service Provider che fornisce servizio alle varie LAN

Wan punto punto: due reti in comunicazione tramite un collegamento
Wan a commutazione: più dispositivi collegati tra di loro

SLIDE punto-punto

Rete GARR - rete dedicata a università, centri di ricerca ecc (nazionale) che collega centri di “cultura”. - in fibra ottica

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