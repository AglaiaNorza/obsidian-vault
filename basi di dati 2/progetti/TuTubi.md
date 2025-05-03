---
created: 2025-05-03T12:54
updated: 2025-05-03T13:20
---
(use case: registrazione utenti, pubbl video, visualizz video, esprimere valutazioni)


1) utenti
	1) nome
	2) data di iscrizione
	3) prendere le sue playlist
2) video
	1) titolo
	2) durata
	3) descrizione
	4) nome del file (univoco)
	5) categoria (unica) [vedi 3]
	6) tag (almeno uno) [vedi 4]
	7) può essere video risposta
	8) numero di volte che è stato visionato 
3) categoria
	1) nome
4) tag
	1) nome
5) visione video
	1) data e ora
6) valutazioni
	1) valore: da 0 a 5
	2) l'utente che ha pubblicato un video non può votarlo
	3) ogni utente può votare al più una volta
	4) impossibile votare un video non visionato
7) commenti testuali
	1) data e ora
	2) un utente può esprimere più commenti testuali
	3) impossibile commentare un video non visionato
8) playlist
	1) collezioni ordinate di video [vedi 2]
	2) nome
	3) data di creazione
	4) pubbliche o private
9) 





vincolo: video risposta non pubblicato da se stesso