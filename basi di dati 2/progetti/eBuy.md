---
created: 2025-04-27T14:49
updated: 2025-04-27T16:49
---
## raffinamento dei requisiti
1) post
	1) post con asta
		1) prezzo iniziale
		2) prezzo di rialzo
		3) scadenza
		4) concluso
			1) bid vincitore (se esiste)
				1) prezzo
	2) "compralo subito"
		1) prezzo
2) utenti
	1) nome
	2) data di registrazione
3) bid
	1) istante
	2) utente offerente [vedi 2]
	3) prezzo [calcolato]
4) oggetto
	1) nuovo
	2) usato
		1) condizione (tra: ottimo, buono, discreto, da sistemare)

### specifica dei tipi di dato

### specifica della classe Bid
Ogni istanza di questa classe rappresenta una "bid" (ossia un'offerta) piazzata da un Utente su un oggetto del tipo "Asta".

**prezzo(): Intero > 0** 

*pre-condizioni*:
- 


