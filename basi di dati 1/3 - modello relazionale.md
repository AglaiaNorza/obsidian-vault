- il modello relazionale è un modello basato sulla nozilone matematica di **relazione**.
- le relazioni si traducono in maniera naturale in **tabelle** (quindi i termini tabella e relazione sono interscambiabili)
- dati e relazioni (riferimenti) tra dati di tabelle diverse sono rappresentati come **valori**

### relazioni

>[!warning] tre interpretazioni di "relazione"
>- relazione matematica (teoria degli insiemi)
>- relazione secondo il modello relazionale dei dati
>- relazione (relationship) o associazione, che rappresenta una classe di fatti nel modello concettuale Entity-Relationship - un tipo di collegamento concettuale tra entità diverse

una **relazione matematica** è un qualsiasi sottoinsieme del prodotto cartesiano di 1+ domini. una relazione sottoinsieme del prodotto cartesiano di k domini si dice di grado k. gli elementi di una relazione si dicono *tuple* o *ennuple*. ogni tupla di una relazione di grado k ha k componenti ordinate, ma non c'è ordinamento tra le tuple.
	`{(nero, 0), (nero, 2), (bianco, 0)} è una relazione di grado 2, cardinalità 3`.
- si usano quasi sempre domini predifiniti, comuni ai linguaggi di programmazione (es. stringhe, interi)

ma come interpretare i dati delle tabelle? assegnando nomi alla tabella e alla colonna.

- un **attributo** è definito da un *nome* A e dal *dominio* dell'attributo A, `dom(A)`
- dato un insieme di attributi R, un'*ennupla* (tuple) su R è una **funzione definita su R che associa ad ogni attributo A in R un elemento di dom(A)**
- se t è un'ennupla su R e A è un attributo in R, allora indichiamo con t(a) il **valore assunto dalla funzione** t in corrispondenza dell'attributo A

![[relazioni1.png|300]]   ![[relazioni2.png|300]]

Ogni relazione può essere implementata come una tabella in cui **ogni riga è una tupla** della relazione (differente da ogni altra) e *ogni colonna è una componente* (valori omogenei, provenienti dallo stesso dominio).
Le colonne corrispondono ai domini D1, D2, ..., Dk e hanno associati i *nomi degli attributi*, nomi univici che descrivono il loro ruolo.
La coppia nome di attributo-dominio è chiamata *attributo*. L'insieme di attributi di una relazione è detto *schema*. Uno schema è invariante nel tempo e descrive la struttura di una relazione (mentre un'istanza è volatile).

- se t è una tupla, t[nome] indica il valore dell'attributo con nome nome.

>[!warning] valori null
>i valori null rappresentano mancanza di informazione o impossibilità di applicare un'informazione 
>
>- tutti i valori null sono considerati diversi tra di loro, quindi non è ammesso avere valori null come chiavi
>- null è un valore polimorfo - non appartiene a nessun dominio, ma può sostituire valori in qualsiasi dominio
>- (null non è zero)

>[!tip] errori nelle basi di dati
>gli errori nelle basi di dati possono essere evitati con vincoli sui domini (es. limite inferiore per gli anni)
>
>![[erroridb.png|300]]
>
un **vincolo di integrità** è quindi una proprietà che deve essere soddisfatta da *ogni istanza* della base di dati perché essa sia corretta.
> 
> - i vincoli possono essere **intrarelazionali** (definiti su valori della stessa relazione) o **interrelazionali** (tra più relazioni)

#### chiavi
> le *chiavi* sono attributi o insiemi di attributi che identificano univocamente una tupla.

un insieme X di attributi di una relazione R è una chiave se soddisfa le condizioni:
1) *per ogni istanza di R* non esistono due tuple distinte t1 e t2 che hanno gli stessi valori (per tutti gli attributi in X)
2) *nessun sottoinsieme proprio di X* soddisfa la condizione 1.

Una **superchiave** è un insieme che contiene una chiave (una superchiave non è una chiave, ma una chiave è anche una superchiave).

Una relazione può avere più chiavi alternative: in questo caso, si sceglie quella più usata o composta da un numero minore di attributi, la cosiddetta **chiave primaria**.
- una chiave primaria non ammette valori nulli

il vincolo interrelazionale **foreign key**, o vincolo di integrità referenziale fa sì che porzioni di informazione in relazioni diverse siano correlate attraverso valori di chiave
 
![[foreignkey.png|350]]
 
Le dipendenze relazionali vengono definite prima di cominciare a inserire dati - definite **sullo schema** - e si può inserire un valore solo se soddisfa tutti i vincoli.

### dipendenze funzionali
Una **dipendenza funzionale** stabilisce un particolare legame semantico tra due insiemi non vuoti di attributi X e Y appartententi a uno schema R.
> `X -> Y` "X determina Y"

>[!info] uso delle lettere
>Le prime lettere dell'alfabeto (A,B,C) si riferiscono a singoli attributi 
>Le ultime lettere dell'alfabeto (X,Y,Z) si riferiscono a insiemi di attributi.

>[!example] esempio
>supponiamo di avere uno schema di relazione:
>- VOLI (CodiceVolo, Giorno, Pilota, Ora)
>
>i vincoli "informali" sono:
>- un volo con un determinato codice parte sempre alla stessa ora
>- esiste solo un volo con un dato pilota in un dato giorno ad una data ora
>- c'è un solo pilota di un dato volo in un dato giorno
>  
>  i vincoli corrispondono alle dipendenze funzionali:
>  - `CodiceVolo -> Ora`
>  - `{Giorno, Pilota, Ora} -> CodiceVolo`
>  - `{CodiceVolo, Giorno} -> Pilota`
>  
>  in questo caso, la chiave sarebbe `CodiceVolo, Giorno` 

(domanda di esame:)
>[!question] quando sono soddisfatte le dipendenze funzionali?
>Diremo che una relazione r con schema R soddisfa la dipendenza funzionale `X -> Y` se:
>1) la dipendenza funzionale `X -> Y` è applicabile ad R, ovvero sia X che Y sono sottoinsiemi di R.
>2) le ennuple r che concordano su X, concordano anche su Y (se le tuple sono uguali su X, devono essere uguali anche su Y)
>   `t1[X] = t2[Y]` --> `t1[Y] = t2[X]` (--> implica)
> 
> es. un'istanza con una sola tupla soddisfa `X->Y`, e la premessa della seconda condizione è verificata, quindi soddisfa la dipendenza funzionale, ma senza implicazioni su Y

## domande esame
>[!question] possibili domande esame 
>- cos'è una relazione/attributo/schema/istanza?
>- cos'è una chiave? (risposta da integrare con [[5 - dipendenze funzionali#chiave]])
>- cos'è una dipendenza funzionale e quando si dice soddisfatta? (integrare con [[5 - dipendenze funzionali]])