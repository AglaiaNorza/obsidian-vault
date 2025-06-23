---
created: 2025-05-14T10:21
updated: 2025-06-23T16:00
---
# DBMS
**chiave** ⟶ non esistono due ennuple della stessa tabella che coincidono sul valore di 1+ attributi
- ogni tabella ha una **chiave primaria** - non può essere NULL

**foreign key** ⟶ dati in tabelle diverse sono correlati attraverso valori comuni, in particolare, attraverso valori delle chiavi (di solito primarie)
- foreign key da un insieme di attributi A di T1 verso tutti gli attributi di una chiave K di T2: 
	- `T1(A) references T2(K)` significa che tutti i valori di T1(A) devono occorrere come valori della chiave K in una ennupla di T2
	- `foreign key: Modulo(aula) references Aula(codice)`

I DBMS seguono un'architettura a **3 livelli**:
- livello interno ⟶ strutture interne di memorizzazione
- livello logico ⟶ modello relazionale dei dati
- livello esterno ⟶ viste sui dati (viste diverse per utenti diversi)
# creazione database, schemi, tabelle
```sql
create database nome_database [opzioni]
```
- crea un database
```sql
create schema nome_schema [opzioni]
```
- crea uno schema (namespace) all'interno del database corrente

>[!info] schema
>uno schema di database definisce in che modo i dati vengono organizzati all'interno di un database relazionale; questo include vincoli logici quali nomi di tabelle, campi, tipi di dati e le relazioni tra queste entità.
> 
><small>(definizione di [IBM](https://www.ibm.com/it-it/topics/database-schema))</small>

```sql
create table nome_tabella (...)
```
- crea una nuova tabella all'interno di uno schema del database corrente

**sintassi**:
```sql
create table [nome schema.]nome_tabella (
	nome_attr dominio [vincoli dominio],
	nome_attr dominio [vincoli dominio],
	.....
	nome_attr dominio [vincoli dominio],
	[altri vincoli intra-relazionali]
	[altri vincoli inter-relazionali]
)
```

### domini SQL predefiniti
**domini numerici**:
- *interi*: `integer`, `smallint` e altri
- *approssimati*: `float(prec)`, `real`, `double precision`

**stringhe**:
- `character [varying] (lung_max)` o `char`/`varchar`
- `text`

**istanti temporali**:
- `date` (anno, mese, giorno)
- `time` (ora, min, sec)
- `timestamp` (anno, ..., sec)

**vari**:
- `interval`: intervalli temporali
- `Boolean`: booleani
- `CLOB`, `BLOB`: non strutturati, di grande dimensione

> [!example]
> ```sql
> create table Corso (
> 	codice integer not null,
> 	nome character varying (100) not null,
> 	aula varchar(10) not null,
> )
> ```
### valori di default
```sql
create table Impiegato (
	nome ...,
	cognome ...,
	stipendio integer default 0
)
```

### vincoli di dominio
```sql
create table Impiegato (
	nome varchar(100) not null,
	cognome varchar(100) not null,
	stipendio integer default 0
			check (stipendio >= 0)
)
```
- ogni ennupla deve soddisfare `stipendio >= 0`
- il vincolo viene controllato prima dell'inserimento o modifica di ennuple (in caso di errore, l'inserimento/modifica non ha luogo e viene generato un errore)
### vincoli deferrable
Un vincolo di integrità può essere dichiarato `deferrable` ⟶ è possibile per l'utente decidere se valutarlo solo al termine della transazione corrente.

### trigger: vincoli generici
Alcuni vincoli non sono traducibili con le tecniche viste fino ad ora (es. vincoli inter-tabelle). Si possono usare asserzioni (non usate) o trigger.

```sql
create [constraint] trigger <nome>
	{ before | after | instead of } {<operaz. intercettata> [ or ... ]}
	on <tabella>
	[ from referenced_table_name ]
	{ not deferrable | [deferrable] 
		{initially immediate | initially deferred }}
	[ for [each] { row | statement } ]
	[ when ( <condizione> ) ]
	execute procedure <nome funzione> ( <argomenti> )
```

- l'`operazione intercettata` può essere `insert`, `update`, `delete`
- l'istante dell'invocazione: prima, dopo o invece dell'operazione (instead vale solo per le viste)
- `deferrable` solo se di tipo `constraint` e `after`
- `when:` se falsa, la funzione non viene eseguita
- `for each row` ⟶ invocata una volta per ogni ennupla impattata dall'operazione
- `for statement` ⟶ invocata una volta per comando

### domini SQL definiti dagli utenti
esistono `create type` e `create domain`

Un **dominio specializzato** definisce un sottoinsieme di valori di un dominio esistente:
```sql
create domain nome_dominio as tipo_base
	[valore di default]
	[vincolo]
```

- si usano `check` e `value`

> [!example]
> ```sql
> create domain voto as integer
> 	default 0
> 	check (value >= 18 and value <= 30)
> ```

Un **dominio enumerativo** definisce un insieme finito, piccolo e stabile di valori, ognuno identificato da un'etichetta.

```sql
create type nome_dominio as 
	enum ("valore 1", ..., "valore N")
```

I valori di un **dominio di tipo record** sono record di valori, uno per ogni *campo* del record. Il valore di ogni campo del record è del rispettivo dominio.

```sql
create type nome_dominio as (
	campo1 dom1, ..., campoN domN
)
```

> [!example]
> ```sql
> create type indirizzo as (
> 	via varchar(200), città varchar(100)
> )
> ```

I domini creati dall'utente possono essere modificati o rimossi
- `alter domain`, `alter type`, `drop domain`, `drop type`

### vincoli di chiave
- `primary key` ⟶ chiave primaria
- `unique` ⟶ altre chiavi

```sql
create table Studente (
	matricola integer not null,
	nome varchar(100) not null,
	cognome varchar(100) not null,
	nascita date,
	cf character(16) not null
	
	primary key (matricola), //chiave primaria
	unique (cf), //altre chiavi
	unique (cognome, nome, nascita)
)
```

si può scrivere anche

```sql
create table Studente (
	matricola integer primary key,
)
```

### valori progressivi
A volte è necessario aggiungere un identificatore artificiale in un'entità (es. ristrutturazione classi che non hanno chiave primaria).

PostrgreSQL fornisce il costrutto delle **sequenze**:
```sql
create sequence Prenotazione_id_seq;

create table Prenotazione (
	id integer default nextval('Prenotazione_id_seq') not null
	istante timestamp not null,
	primary key (id)
);
```

Alternativamente, esiste una scorciatoia:

```sql
create table Prenotazione (
	id serial not null,
)
```

## modifica e cancellazione di tabelle/schemi/database
**modifica**:
- `alter table`

**cancellazione**:
- `drop table`
- `drop schema`
- `drop database`

# query

## select
### select
Istruzione di interrogazione: `select` ⟶ restituisce il risultato in forma di **tabella**

```sql
select tabella.attributo1, 
		...
		tabella.attributoN
from tabella
where condizine
```


> [!example] esempio
> 
> $$
> \pi_{\text{indirizzo}}(\sigma_{\text{nome='FixIt'}}(\text{Officina}))
> $$
> 
> ```sql
> select Officina.indirizzo
> from Officina
> where Officina.nome = 'FixIt'
> ```

- se non c'è ambiguità nel nome di un attributo, si può indicare senza nome della tabella

>[!example] stesso esempio
> ```sql
> select indirizzo
> from Officina
> where nome = 'FixIt'
> ```

- se non c'è una condizione (ovvero `where true`), `where` si può escludere
### select distinct
`select distinct` rimuove i duplicati dalla tabella di ritorno

```sql
select distinct cognome, nome
from Persona
where eta > 40
```

- se ci sono omonimi con più di 40 anni, restituisce il loro nome e cognome una volta sola

### select *
`select *` restituisce tutti i dati delle ennuple selezionate

![[selectstar.png|center|400]]

```sql
select *
from Persona
where eta > 40
```

## condizioni
### condizione like
`like` si usa per caratterizzare le stringhe

```sql
select campo
from tabella 
where campo like stringa
```

- `'%'` indica qualsiasi stringa
- `'_'` indica qualsiasi carattere

> [!example] esempio
> 
> - persone che hanno un cognome che inizia con 'R'
> 
> ```sql
> select *
> from Persona
> where cognome like 'R%'
> ```

### is null e is not null
- si usano per selezionare valori null o non null

```sql
select * 
from Persona 
where eta > 40 or eta is null
```

```sql
select * 
from Persona 
where eta is not null
```

## più tabelle
Per fare un join tra più tabelle:

![[joinsql.png|center|400]]


```sql
select Officina.indirizzo
from Officina, riparazione
where Officina.nome = Riparazione.officina
and Riparazione.veicolo = 'HK 243 BW'
```

### alias di tabelle
Si possono anche usare alias per i nomi delle tabelle (o per gli attributi)

```sql
select o.indirizzo
from Officina as o, Riparazione as r
where o.nome = r.officina
	and r.veicolo = 'HK 243 BW'
```

oppure:

```sql
select o.indirizzo
from Officina o, Riparazione r
where o.nome = r.officina
	and r.veicolo = 'HK 243 BW'
```

### occorrenze multiple di una tabella
esempio: veicoli che sono stati riparati in almeno due officine

```sql
select distinct r1.veicolo as targa
from Riparazione as r1, Riparazione as r2
where r1.veicolo = r2.veicolo
	and r1.officina <> r2.officina
```

## ordine
### order by
Il risultato di un'interrogazione SQL può essere ordinato

```sql
select * 
from Officina
where ...
order by clausola1 asc|desc, ..., clausolaN asc|desc
```

## funzioni aggregate nella target list

Le funzioni aggregate calcolano un singolo valore a partire da tutte le ennuple (il risultato è quindi una tabella con una sola ennupla)
### count
(conta)

- numero di riparazioni del veicolo
```sql
select count(*)
from Riparazione
where veicolo = 'HK 243 BW'
```

- numero di officine distinte che hanno riparato il veicolo

```sql
select count(distinct officine)
from Riparazione
where veicolo = 'HK 243 BW'
```

Quindi
- `count(*)` ⟶ numero di ennuple
- `count(attributo)` ⟶ numero di valori non `NULL` per l'attributo con duplicati
- `count(distinct attributo)` ⟶ numero di valori non `NULL` e distinti per l'attributo

### funzioni matematiche
- `sum(attributo)` (anche su tempo)
- `avg(attributo)` (anche su tempo)
- `min(attributo)` (su domini ordinati)
- `max(attributo)` (su domini ordinati)

>[!tip] i valori `NULL` sono ignorati

### group by
Le funzioni aggregate possono essere applicate a partizioni delle tuple.

- nomi delle persone con figli e stipendio >= 45 con i nomi dei figli
```sql
select g.id as gid, g.nome as genitore, f.nome as figlio
from Persona g, GenFiglio gf, Persona f
where g.id = gf.gen and gf.figlio = f.id and g.stipendio >= 45
```

- nomi delle persone con figli e stipendio >= 45 con il numero di figli

```sql
select g.id as gid, g.nome as genitore, count(f.nome) as nFigli
from Persona g, GenFiglio gf, Persona f
where g.id = gf.gen and gf.figlio = f.id and g.stipendio >= 45
group by g.id, g.nome
```

- mette nello stesso gruppo le ennuple che hanno lo stesso `g.id` e `g.nome`
- conta quante righe (quanti figli) ci sono in quel gruppo

- gli attributi nella target list devono comparire nella clausola `group by`

![[groupby.png|center|450]]

#### having
La condizione `having` esprime una condizione sui gruppi (e può contenere funzioni aggregate)
- si omettono le ennuple dei gruppi che non soddisfano la condizione `having`
- ! non si possono usare gli alias nella condizione having

restituire i nomi delle persone con stipendio >= 45 e almeno 2 figli insieme al numero di figli:
```sql
select g.id as gid, g.nome as genitore, count(f.nome) as nFigli
from Persona g, GenFiglio gf, Persona f
where g.id = gf.gen and gf.figlio = f.id and g.stipendio >= 45
group by g.id, g.nome
having count(f.nome) >= 2
```

## operatori insiemistici
### union
```sql
queryA
union [all |  distinct]
queryB
```

### differenza
```sql
queryA
except / minus
queryB
```

### intersezione
```sql
queryA
intersect
queryB
```

-  più efficiente con join

```sql
select distinct i.nome
from Impiegato i, Impiegato j
where i.nome = j.cognome
```

## query annidate

- persone che hanno almeno un figlio
```sql
select *
from Persona p
where exists (select *
		from Paternita 
		where padre = p.nome)
	or exists (select *
		from Maternita
		where madre = p.nome)
```

- le sotto-query non possono contenere operatori insiemistici
- non è possibile, in una query, fare riferimento a variabili definite in blocchi più interni

```sql
select *
from Persona
where reddito = (select max(reddito) from Persona)

select *
from Persona
where reddito >= all (select reddito from Persona)
```

```sql
select *
from Persona p
where (eta, reddito)
	not in (select eta, reddito
		from Persona
		where nome <> p.nome)
```

## join naturale

```sql
select mat.figlio as persona,
	mat.madre as madre, pat.padre as padre
from Maternita mat natural join Paternita pat
```


