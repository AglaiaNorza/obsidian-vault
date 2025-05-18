---
created: 2025-05-18T11:51
updated: 2025-05-18T13:01
---
## raffinamento dei requisiti
1) Utenti
	1) nome
	2) data di iscrizione
2) Video
	1) titolo
	2) durata
	3) descrizione
	4) path (univoco)
	5) può essere una risposta
	6) numero di visioni (calcolabile)
	7) categoria [v.3] unica
	8) tag [v.4] almeno uno
	9) valutazioni [v.6]
	10) commenti [v.7]
	11) Video Censurato (nessuna NUOVA interazione)
		1) motivo
		2) istante censura
3) Categoria
	1) nome
4) Tag
	1) nome
5) Visione
	1) data e ora
6) valutazione da 0 a 5 (una x utente)
	1) istante di valutazione
7) Commento (più commenti x video)
	1) istante
	2) testo
8) Playlist
	1) nome
	2) istante creazione
	3) ordine
	4) pubbliche o private

## UML

![[TuTubi2.png]]

### specifica dei tipi di dato
- DurataVideo: (minuti: Intero >= 0, secondi: Intero [0..59])

### specifica della classe Video
Ogni istanza di questa classe rappresenta un video pubblicato sulla piattaforma

`V.Video.no_risposte_autoreferenziali`

$$
\forall v_{1},\,v_{2},\,u_{1},\,u_{2}\ (\text{videorisp}(v_{1},v_{2}) \land \text{pubbl}(v_{1},\,u_{1})\land\text{pubbl}(v_{2},\,u_{2})\implies u_{1}\neq u_{2})
$$

oppure:

$$
\forall v_{1},v_{2}(v_{1}=v_{2} \implies \neg\text{videorisp}(v_{1},v_{2}))
$$

`V.Video.censura_no_commenti`

$$
\begin{flalign}&
\forall v,\,c,\,\,ice,\,ico \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,ice)  \\&
\land \;\text{commento\_vid}(c,\,v)\land \text{istante\_comm}(c,ico)\\&
\implies ico < ice\\&
)
\end{flalign}
$$

`V.Video.censura_no_rating`

$$
\begin{flalign}&
\forall v,\,u,\,\,ice,\,iva \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,iv)  \\&
\land \;\text{valutazione}(u,\,v)\land \text{istante\_val}(u,\,v,\,iva)\\&
\implies iva < ice\\&
)
\end{flalign}
$$

`V.Video.censura_no_visione`
$$
\begin{flalign}&
\forall v,\,vis,\,\,ice,\,ivi \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,ice)  \\&
\land \;\text{visione\_vid}(vis,\,v)\land \text{istante\_vis}(vis,ivi)\\&
\implies ivi < ice\\&
)
\end{flalign}
$$


alternativamente:

`V.Video.censura_no_interazioni`


