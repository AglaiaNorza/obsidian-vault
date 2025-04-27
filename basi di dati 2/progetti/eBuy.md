---
created: 2025-04-27T14:49
updated: 2025-04-27T17:09
---
## raffinamento dei requisiti
1) post
	1) categoria [vedi 2]
	2) post con asta
		1) prezzo iniziale
		2) prezzo di rialzo
		3) scadenza
		4) concluso
			1) bid vincitore (se esiste)
				1) prezzo
	3) "compralo subito"
		1) prezzo
2) categoria
	1) sottocategorie (se esistono)
3) utenti
	1) nome
	2) data di registrazione
4) bid
	1) istante
	2) utente offerente [vedi 2]
	3) prezzo [calcolato]
5) oggetto
	1) nuovo
		1) durata della garanzia
	2) usato
		1) condizione (tra: ottimo, buono, discreto, da sistemare)
		2) durata della garanzia (opzionale)

### specifica dei tipi di dato

### specifica della classe Bid
Ogni istanza di questa classe rappresenta una "bid" (ossia un'offerta) piazzata da un Utente su un oggetto del tipo "Asta".

**prezzo(): Intero > 0** 

*pre-condizioni*:
- nessuna

*post-condizioni*:
- l'operazione non modifica il livello estensionale
- il valore del risultato "result" è definito così:
	- sia "A" l'oggetto di tipo Asta coinvolto nel link di tipo "bid_asta" con this
	- sia "Bids" l'insieme dei link del tipo bid_asta che coinvolgono A
		- sia "B" la cardinalità di Bids
	- sia "P" il valore dell'attributo "prezzo"
	- sia "R" il valore dell'attributo "prezzo_rialzo" di A
	- result = P + B $\times$ R

### specifica della classe AstaConclusa
Ogni istanza di questa classe rappresenta un'asta che si è conclusa.

**prezzo_finale(): Intero >= 0**:

*pre-condizioni*:
- l'oggetto this deve essere coinvolto in un link del tipo "bid_vincitrice" con un'istanza "B" della classe "Bid"

*post-condizioni*:
- l'operazione non modifica il livello estensionale
- il risultato "result" è definito così:
	- sia "B" l'istanza della classe "Bid" coinvolta con this in un link del tipo "bid_vincitrice"
	- result = B.prezzo()

