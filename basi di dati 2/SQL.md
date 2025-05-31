---
created: 2025-05-14T10:21
updated: 2025-05-31T22:29
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
