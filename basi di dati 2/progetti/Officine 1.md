---
created: 2025-04-05T18:10
updated: 2025-04-07T13:21
---
## raffinamento dei requisiti
1) Officine
	1) nome
	2) indirizzo
	3) numero di dipendenti ( vedi 2 ) (calcolabile)
	4) dipendenti ( vedi 2 )
		1) anni di servizio
	5) direttore ( vedi 3 )
2) Dipendenti
	1) nome
	2) codice fiscale
	3) indirizzo
	4) numero di telefono
3) Direttori
	1) [caratteristiche dei dipendenti]
	2) data di nascita
4) Riparazioni
	1) codice
	2) veicoli ( vedi 5 )
	3) data e ora di accettazione
	4) data e ora di consegna (se terminate)
5) VeicoliStringa
	1) modello
	2) tipo
	3) targa
	4) anno di immatricolazione
	5) proprietario
6) Proprietari
	1) (caratteristiche dei dipendenti)

## UML

![[Officine1.png|center]]

### specifica dei tipi di dato
- Indirizzo : (via : Stringa, Civico : Intero > 0, CAP : Intero > 0)
- CF: come da standard
- NumeroTelefono: come da standard
- Targa: come da standard
- CodiceRiparazione: come da standard
### specifica della classe Officina
Ogni istanza di questa classe rappresenta un'officina.

**numero_dipendenti(): Intero >= 0**:

*pre-condizioni*:
- nessuna

*post-condizioni*:
- l'operazione non modifica il livello estensionale
- il valore del risultato "result" è definito come segue:
	- sia D l'insieme dei link di associazione "officina_dipendente" che coinvolgono "this"
	- sia N la cardinalità di D
	- result = N

### specifica della classe Dipendente
Ogni istanza di questa classe rappresenta un dipendente.

**anni_servizio(o: Officina): Intero >= 0**:

*pre_condizioni*:
- l'oggetto di invocazione "this" è coinvolto in un link dell'associazione "dip_officina" con l'istanza "o" di Officina fornita in input

*post-condizioni*:
- l'operazione non modifica il livello estensionale
- il valore del risultato "result" è definito così:
	- sia D il valore dell'attributo "anno_assunzione" del link "dip_officina" che coinvolge "this" e "o"
	- sia A l'anno di "adesso"
	- "result" = A - D
