## raffinamento dei requisiti
1) Docenti
	1) nome
	2) cognome
	3) luogo di nascita [ vedi 2 ]
	4) data di nascita
	5) matricola (stringa da standard) (univoco)
	6) posizione universitaria
2) Città
	1) Nazione
3) Progetti di ricerca
	2) nome
	3) acronimo
	4) data di inizio
	5) data di fine
	6) docenti che partecipano [ vedi 1 ]
	7) Work Package (molti) [ vedi 4 ]
4) Work Package 
	1) nome
	2) data di inizio
	3) data di fine
5) Impegni
	1) giorno
	2) durata 
	3) tipologia
		1) motivazione

## diagramma delle classi

![[Accademia2.png]]

### specifica dei tipi
- Periodo: {inizio: Data, fine: Data > inizio}