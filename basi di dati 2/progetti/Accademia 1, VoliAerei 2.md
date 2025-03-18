# Accademia1
Gestione delle tabelle orarie relative al ruolo di docente universitario.

1) Docenti
	1) nome
	2) cognome
	3) data di nascita
	4) matricola (univoca)
	5) posizione universitaria (tra: ricercatore, professore associato, professore ordinario)
	6) progetti a cui partecipa [ vedi 2 ]
2) Progetti di ricerca
	1) nome
	2) acronimo ??
	3) data di inizio
	4) data di fine
	5) docenti che partecipano [ vedi 1 ]
	6) Work Package di cui è composto
3) Work Package
	1) nome
	2) data di inizio
	3) data di fine
4) Impegni
	1) giorno 
	2) durata in ore (intero)
	3) tipologia
		1) motivazione

# VoliAerei2
1) Voli
	1) codice (da standard)
	2) durata (in minuti)
	3) compagnia aerea [ vedi 2 ]
	4) aeroporto di partenza
	5) aeroporto di arrivo
2) Aeroporti
	1) codice (da standard)
	2) nome (stringa)
	3) città [ vedi 3 ]
	4) nazione [ vedi 4 ]
3) Città
	1) nome
	2) numero abitanti
4) Nazioni
5) Compagnie
	1) nome
	2) anno di fondazione (intero > 0)
	3) città sede direzione [ vedi 3 ]
6) Voli charter
	1) tappe intermedie (con ordine)
	2) modello di velivolo