---
created: 2025-05-18T11:51
updated: 2025-05-18T15:38
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

---

`V.Video.censura_no_commenti`

$$
\begin{align*}&
\forall v,\,c,\,\,ice,\,ico \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,ice)  \\&
\land \;\text{commento\_vid}(c,\,v)\land \text{istante\_comm}(c,ico)\\&
\implies ico < ice\\&
)
\end{align*}
$$

`V.Video.censura_no_rating`

$$
\begin{align*}&
\forall v,\,u,\,\,ice,\,iva \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,iv)  \\&
\land \;\text{valutazione}(u,\,v)\land \text{istante\_val}(u,\,v,\,iva)\\&
\implies iva < ice\\&
)
\end{align*}
$$

`V.Video.censura_no_visione`
$$
\begin{align}&
\forall v,\,vis,\,\,ice,\,ivi \ \\&
( \\&
\text{VideoCensurato}(v)\land\text{ist\_cens}(v,\,ice)  \\&
\land \;\text{visione\_vid}(vis,\,v)\land \text{istante\_vis}(vis,ivi)\\&
\implies ivi < ice\\&
)
\end{align}
$$


alternativamente:

`V.Video.censura_no_interazioni`

$$\begin{align}&
\forall v,\,ice \\& 
( \\&
 \text{VideoCensurato}(v) \land \text{ist\_cens}(v,\,ice) \implies\\&
 (\\&
(\forall vis,\,ivi \ (\text{visione\_vid}(v,\,vis)\land\text{istante\_vis}(vis,\,ivi)\implies ivi< ice) )\ \land \\&
(\forall com,\,ico\ (\text{commento\_vid}(v,\,com)\land\text{istante\_comm}(com,\,ico)\implies ico< ice))\  \land\\&
(\forall ute,\,iva \ (\text{valutazione\_vid}(v,\,ute)\land\text{istante\_val}(v,\,ute,\,iva)\implies iva < ice)\\&
)) \\&
)
\end{align}
$$

### specifica della classe Visione
Ogni istanza di questa classe rappresenta una visione di un video effettuata da un utente.

`V.Visione.visione_dopo_iscrizione`

$$
\forall u,\,v,\,iscr,\,ivi(\text{utente\_visione}(u,v)\land\text{ist\_iscr}(u,iscr)\land\text{istante\_vis}(v,ivi)\implies iscr < ivi)
$$

### specifica della classe Commento
Ogni istanza di questa classe rappresenta un commento lasciato da un utente ad un video.

`V.Commento.commento_dopo_visione`

$$\begin{align*}&
\forall ut,\,com,\,icom,\,vid(\text{utente\_commento} (ut,\,com)\land\text{commento\_vid}(com,vid)\land\text{istante\_comm}(com,\,icom) \\&
\implies \exists vis,\,ivi (\text{utente\_visione}(ut,vis)\land \text{visione\_vid}(vis,\,vid) \land\text{istante\_vis}(vis,\,ivi) \land ivi<icom)\\&
)
\end{align*}
$$

### specifica della classe Utente
Ogni istanza di questa classe rappresenta un utente della piattaforma.

`V.Utente.valutazione_dopo_visione`

$$
\begin{align*}&
\forall ut,\,vid,\,ival(\text{valutazione}(ut,\,vid) \land\text{istante\_val}(ut,\,vid,\,ival) \implies \\&
\exists vis,\,ivis(\text{utente\_visione}(ut,\,vis)\land\text{visione\_vid}(vis,\,vid)\land\text{istante\_vis}(ut,\,vid,\,ivis)\land ivis < ival)\\&
) \\&

\end{align*}
$$

`V.Utente.no_valutazione_autoreferenziale`

$$
\forall ut,\,vid \ (\text{pubbl\_video}(ut,\,vid)\implies \neg(\text{valutazione}(ut,\,vid)))
$$