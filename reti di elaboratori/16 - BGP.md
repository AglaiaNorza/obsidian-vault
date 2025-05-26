---
created: 2025-04-01
updated: 2025-05-26T15:23
---
## struttura di Internet

> [!summary] recap
> Internet è composta da:
> - dorsali, gestite da società private ⟶ forniscono la connettività globale
> - network provider ⟶ usati dalle dorsali per avere connettività globale, forniscono connettività ai clienti Internet
> - customer network ⟶ usano i servizi dei network provider

Fino ad ora, abbiamo seguito una visione omogenea della rete, vista come una collezione di router interconnessi (in cui ciascun router era indistinguibile dagli altri).

Nella pratica, però, ci sono 200 milioni di destinazioni, e archiviare le informazioni d’instradamento su ciascun host richiederebbe un’enorme quantità di memoria. In più, il traffico generato dagli aggiornamenti link state non lascerebbe banda per i pacchetti di dati, e il distance vector non convergerebbe mai.

Per questi motivi è necessaria **autonomia amministrativa**: ciascuno dovrebbe essere in grado di amministrare la propria rete, pur mantenendo la possibilità di connetterla alle reti esterne.
- in particolare, ogni ISP è un’autorità amministrativa autonoma: usa le sottoreti che vuole e impone politiche specifiche sul traffico

### instradamento gerarchico
Ogni ISP è un **sistema autonomo** (Autonomous System) e può eseguire un protocollo di routing che soddisfa le sue esigenze.

Tutti i router di uno stesso autonomous system eseguono lo stesso algoritmo di routing, chiamato protocollo di routing interno al sistema autonomo o intradominio (*intra-AS*), o Interior Gateway Protocol (*IGP*).

Deve invece esserci un unico protocollo inter-dominio che gestisce il routing tra i vari sistemi autonomi, chiamato inter-dominio (*inter-AS*) o Exterior Gateway Protocol (*EGP*).

I protocolli inter-dominio sono eseguiti su **router gateway**, che connettono i sistemi autonomi e inoltrano pacchetti a destinazioni esterne.

>[!question]- perché i protocolli d’instradamento inter-AS sono diversi da quelli intra-AS?
>politiche:
>- **inter-AS** ⟶ il controllo amministrativo desidera avere il controllo su come il traffico viene instradato e su chi instrada attraverso le sue reti
>- **intra-AS** ⟶ c'è un unico controllo amministrativo, le questioni politiche hanno un ruolo molto meno importante nello scegliere le rotte interne al sistema
>
>prestazioni:
>- **inter-AS** ⟶ le politiche possono prevalere sulle prestazioni
>- **intra-AS** ⟶ orientato alle prestazioni
### sistemi autonomi
Ad ogni sistema autonomo viene assegnato un **numero identificativo univoco** di 16bit dall'ICANN.

Gli Autonomous Systems possono avere diverse dimensioni, e sono classificati in base al modo in cui sono connessi ad altri AS, in:
- **AS stub** ⟶ ha un solo collegamento verso un altro AS. Il traffico è generato o destinato allo stub ma non transita attraverso di esso (esempio: grande azienda)
- **AS multihomed** ⟶ ha più di una connessione con altri AS, ma non consente transito di traffico (esempio: azienda che usa servizi di più  network provider, ma non fornisce connettività agli altri AS)
- **AS di transito** ⟶ è collegato a più AS e consente il traffico (esempi: network provider e dorsali)

>[!example] esempio
>
>![[sist-trasporto.png|center|400]]
>
> Ogni router all'interno degli AS sa come raggiungere tutte le reti che si trovano nel suo AS, ma non come raggiungere una rete che si trova in un altro AS.
>
>Per il routing **intra-dominio**, si usano i protocolli **RIP** e **OSPF**. Per il routing **inter-dominio**, si usa **BGP**.

## Border Gateway Protocol
BGP è un protocollo **path-vector** (come distance-vector, ma al posto delle distanze si mantengono i percorsi). Viene usato per determinare percorsi per le coppie origine-destinazione che interessano più AS.

Esso mette a disposizione di ciascun AS un modo per:
- ottenere informazioni sulla **raggiungibilità delle sottoreti** da parte di AS confinanti
- propagare le informazioni di raggiungibilità a tutti i roter interni di un AS
- **determinare percorsi buoni** * verso le sottoreti sulla base delle informazioni di raggiungibilità e delle politiche dell'AS
	- \* un percorso "buono" non è necessariamente quello più breve: le ragioni dietro la sccelta di percorsi sono principalmente politico-economiche

BGP consente a ciascuna sottorete di comunicare la propria esistenza al resto di Internet.

### path-vector routing
Il path-vector routing consente alla sorgente di controllare il percorso scelto in base a criteri "personalizzati" (minimizzare il numero di hop, evitare alcuni nodi...).

Vengono inviati, invece che solo destinazioni,  *percorsi*. Ogni nodo riceve quindi un path vector da un vicino e aggiorna il proprio path vector applicando la propria politica.

>[!example] esempio 
>
>![[pathvector-es1.png|center|400]]
>
>se $C$ riceve una copia del vettore di $B$:
>
>![[pathvector-es2.png|center|400]]

**algoritmo**:
```
Path_Vector_Routing() {
	// Inizializzazione
	for (y=1 to N) {
		if (y è me_stesso)
			Path[y] = me_stesso
		else if (y è un vicino)
			Path[y] = me_stesso+il_nodo_vicino
		else
			Path[y] = vuoto
	}
	Spedisci il vettore {Path[1], Path[2], ..., Path[y]} a tutti i vicini
	
	// Aggiornamento
	repeat (sempre) {
		wait (un vettore Path_w da un vicino w)
		for (y=1 to N) {
			if (Path_w comprende me_stesso)
				scarta il percorso
			else
				Path[y] = il_migliore_tra{Path[y], (me_stesso+Path_w[y])}
		}
		if (c'è un cambiamento nel vettore)
			Spedicsci il vettore {Path[1], Path[2], ..., Path[y]} a tutti i vicini
	}
}
```

qundi, ogni nodo:
- inizializza i percorsi verso ogni nodo
- spedisce il vettore a tutti i vicini
- aspetta di ricevere un vettore da un vicino, e:
	- se il vettore comprende se stesso, lo scarta (per evitare cicli)
	- altrimenti, modifica il suo vettore in base al criterio scelto
- se c'è stato un cambiamento nel vettore, lo invia a tutti i vicini

### eBGP e iBGP
Tutti i router devono usare una variante di BGP chiamata **BGP interno** (iBGP).

In più, per permettere ad ogni router di instradare correttamente i pacchetti, è necessario installare su tutti i router di confine dell'AS il **BGP esterno** (eBGP).

>[!tip] quindi, i **router di confine** devono eseguire tre protocolli di routing (intra-dominio, eBGP, iBGP), mentre **tutti gli altri** ne eseguono due (intra-dominio e iBGP)

BGP permette a coppie di router di scambiarsi informazioni di instradamento su connessioni **TCP** usando la porta `179`.
- i router ai capi di una connessione TCP sono chiamati **peer BGP**, e la connessione TCP con tutti i messaggi BGP che vi vengono inviati è detta **sessione BGP**

>[!warning] le linee di sessione BGP non corrispondono sempre a collegamenti fisici

>[!info] eBGP
> Nel protocollo eBGP, due router di confine che si trovano in due diversi AS formano una coppia di peer BGP e si scambiano messaggi.
> 
> ![[eBGP.png|center|400]]
>
>Da solo, eBGP non basta per fornire tutte le informazioni su come instradare pacchetti: infatti, i router di confine sanno come instradare pacchetti *solo ad AS vicini*, e nessuno dei *router non di confine* sa come instradare un pacchetto destinato alle reti che si trovano in altri AS.
>
>Per questo, è necessario usare anche iBGP.

>[!info] iBGP
> iBGP crea una sessione tra **ogni possibile coppia di router all'interno di un AS**.
> - non tutti i nodi hanno messaggi da ricevere, ma tutti ricevono
> 
> ![[iBGP.png|center|400]]
> 
> - il processo di aggiornamento non termina dopo il primo scambio di messaggi, ma quando non ci sono più aggiornamenti

Le informazioni ottenute da eBGP e iBGP vengono combinate per creare le tabelle dei percorsi.

### tabelle di routing
Le tabelle di percorso ottenute da BGP non vengono usate di per sé per l'instradamento dei pacchetti, ma vengono inserite nelle **tabelle di routing intra-dominio**, generate da RIP o OSPF.

- nel caso di **stub**, l'unico router di confine dell'area aggiunge una regola di default alla fine della sua tabella di routing e definisce come prossimo router quello che si trova dall'altro lato della connessione eBGP

>[!example]- stub
>
>![[tabella-stub.png|center|400]]

- nel caso di **AS di transito**, il contenuto dellla tabella di percorso deve essere inserito nella tabella di routing, ma bisogna impostare il costo (si imposta costo pari a quello per raggiungere il primo AS nel percorso)

>[!example]- di transito
>
>![[tabella-astransito.png|center|400]]

### attributi del percorso e rotte BGP
Quando un router annuncia una rotta per una sessione BGP, include anche un certo numero di **attributi BGP**.
- prefisso + attributi = rotta

Due attributi molto importanti sono:
- `AS-PATH`, che serve per **selezionare i percorsi** 
	- elenca i sistemi autonomi attraverso cui è passato l'annuncio del prefisso (ogni sistea autonomo ha un identificativo univoco), permettendo di evitare cicli
- `NEXT-HOP`: l'**IP dell'interfaccia** su cui viene inviato il pacchetto

Quando un router gateway riceve un annuncio di rotta, utilizza le *proprie politiche di importazione* per decidere se accettare o filtrare la rotta.

### selezione dei percorsi BGP
Un router può ricavare più di una rotta verso una destinazione, e deve quindi sceglierne una.

Le regole di eliminazione sono:
1) alle rotte viene assegnato come attributo un valore di **preferenza locale**, e si selezionano lle rotte con i valori più alti
2) si seleziona la rotta con il valore `AS-PATH` più breve
3) si seleziona la rotta il cui `NEXT-HOP` ha costo minore (*hot-potato routing*)
4) se rimane ancora più di una rotta, il router si basa sugli identificatori BGP


>[!example] advertising ristretto
>Gli ISP vogliono instradare solo il traffico delle loro customer network, e non quello di altre reti.
>
>![[adv-ristretto.png]]
> 
>- $A$ annuncia il percorso $Aw$ a $B$ e a $C$
>- $B$ sceglie di non annunciare $BAw$ a $C$
>	- $B$ non ha vantaggio a instradare $CBAw$, poiché nessuno tra $C$, $A$, $w$ è cliente di $B$
>	- $C$ non scopre il percorso $CBAw$
>- $C$ instraderà solo $CAw$ (senza usare $B$) per raggiungere $w$

### messaggi BGP
I messaggi BGP vengono scambiati attraverso **TCP**, e sono:
- `OPEN` ⟶ **apre** la connessione TCP e **autentica** il mittente
- `UPDATE` ⟶ annuncia il **nuovo percorso** (o cancella quello vecchio)
- `KEEPALIVE` ⟶ **mantiene la connessione attiva** in mancanza di `UPDATE`
- `NOTIFICATION` ⟶ **riporta gli errori** del precedente messaggio; usato anche per chiudere il collegamento