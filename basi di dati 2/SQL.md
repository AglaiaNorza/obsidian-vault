---
created: 2025-05-14T10:21
updated: 2025-06-01T09:30
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
create type nome_dominnio as 
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
- `al`
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

## modifica e cancellazione di tabelle/schemi/database
**modifica**:
- `alter table`

**cancellazione**:
- `drop table`
- `drop schema`
- `drop database`


