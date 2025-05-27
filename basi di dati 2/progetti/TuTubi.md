---
created: 2025-05-03T12:54
updated: 2025-05-27T18:44
---
(use case: registrazione utenti, pubbl video, visualizz video, esprimere valutazioni)

1) utenti
	1) nome
	2) data di iscrizione
	3) prendere le sue playlist pubbliche
2) video
	1) titolo
	2) durata
	3) descrizione
	4) nome del file (univoco)
	5) categoria (unica) [vedi 3]
	6) tag (almeno uno) [vedi 4]
	7) può essere **video risposta**
		1) non si può rispondere a un video pubblicato da se stessi
	8) può essere **video censurato**
		1) no visioni, no commenti, no voti, no playlist, no ricerca
		2) motivo
	9) numero di volte che è stato visionato
	10) ricerca video per tag e valutazione
	11) AGGIUNGO: data post? 
3) categoria
	1) nome
	2) ottieni video con maggiore numero di risposte
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

### specifica dei tipi di dato
- DurataVideo (minuti: Intero, secondi: Intero < 60)

### specifica della classe Video
Ogni istanza di questa classe rappresenta un video della piattaforma.

`V.Video.no_risposta_autoreferenziale`

Per ogni istanza `v1: Video`, `v2: Video`, `u1: Utente`, `u2: Utente`, se esistono i link
- `(u1, v1):pubblicazione`
- `(u2, v2):pubblicazione`
- `(v1:originale, v2:risposta):vid_risp`
allora `u1 != u2`
-----
`V.Video.censura`

Per ogni istanza `v:Video`, se `v:VideoCensurato`, allora per ogni `int` si ha:
- se `(v,int):comm_vid` o `(v,int):visione_video`, allora `int.istante < v.istante_censura`
- E
- se `(v, int):valutazione`, allora `(v, int):valutazione.istante < v.istante_censura`

--- 
`V.Video.valutazione_solo_se_visione`

Per ogni `v:Video`, `u:Utente`, `i_valut`, 
- se esiste `(u,v):valutazione` tale che `(u,v):valutazione.istante = i_valut`, allora esistono `vis:Visione`, `i_vis` tale che
	- `(u,vis):utente_visione` E `(vis,v):visione_video` E `(vis,v):visione_video.istante = i_vis` E `i_valut >= i_vis`

--- 
`V.Video.commento_solo_se_visione`
 
Per ogni `v:Video`, `u:Utente`, `c:Commento`, `i_comm`, 
- se esistono `(u,c):utente_comm` E `(c,v):comm_vid` E `c.istante = i_comm`, allora esistono `vis:Visione`, `i_vis` tale che
	- `(u,vis):utente_visione` E `(vis,v):visione_video` E `(vis,v):visione_video.istante = i_vis` E `i_comm >= i_vis`

### specifica delle classe Visione
Ogni istanza di questa classe rappresenta una visione di un video.

`V.Visione.solo_registrati`

Per ogni `v:Visione`, `u:Utente`, `i_vis`, `i_iscr`, si ha
- se `(u,v):utente_visione` e `(u,v):utente_visione.istante = i_vis` e `u.istante_iscrizione = i_iscr`
- allora, `i_vis > i_iscr`

### specifica della classe Playlist
Ogni istanza di questa classe rappresenta una playlist.

`V.Playlist.creazione.solo.registrati`



### vincoli
- entry della playlist in ordine