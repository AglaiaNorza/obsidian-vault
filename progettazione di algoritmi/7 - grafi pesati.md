>[!example]- analogia dei contenitori d'acqua
>Abbiamo tre contenitori d'acqua con capienza 4, 7 e 10 litri. Inizialmente, i contenitori da 4 e 7 litri sono pieni, mentre quello da 10 è vuoto. Possiamo fare un solo tipo di operazione: versare acqua da un contenitore ad un altro, fermandoci quando il contenitore sorgente è vuoto o quello destinazione pieno.
>
>Vogliamo sapere se esiste una sequenza di operazioni di versamento che termina lasciando esattamente 2L di acqua nel contenitore da 4 o nel contenitore da 7.
>
>Il problema si può modellare con un grafo $G$:
>- i *nodi* di $G$ rappresentano i possibili stati di riempimento dei contenitori (tramite una configurazione $(a,b,c)$ dove le tre lettere rappresentano il numero di litri nei tre contenitori)
>- c'è un *arco* tra un nodo $(a,b,c)$ a un nodo $(a',b',c')$ se dallo stato $(a,b,c)$ è possibile passare allo stato $(a',b',c')$ con un versamento lecito
>
>![[grafo-acqua.png|center|300]]
>
> Per risolvere il problema, basta chiedersi se nel grafo diretto $G$ almeno uno dei nodi $(2,*,*)$ o $(*,2,*)$ è raggiungibile a partire dal nodo $(4,7,0)$.
> - per facilitare la ricerca, possiamo aggiungere un nodo pozzo $(-1,-1,-1)$ con archi entranti solo dai nodi $(2,*,*)$ e $(*,2,*)$, e chiederci se questo sia raggiungibile da $(4,7,0)$ 