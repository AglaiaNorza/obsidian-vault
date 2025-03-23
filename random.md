
Sì. Infatti:
supponiamo per assurdo che esista un grafo $S\neq T$ (con peso inferiore di $T$) MST di $G'$ ma non di $G$.
Si avrebbe che 
$$\text{peso\_S}=\sum_{f\in E(S)}\;w'(f) <\sum_{e\in E(T)}w'(e)=\text{peso\_T}$$
con $w':G'\to R^+$.

Ma, poiché la costante $c$ è stata sommata al peso di ciascun arco, abbiamo che $w'(x)=w(x)+c$, con $w:G\to R^+$.

Avremmo quindi
$$\sum_{f\in E(S)}\;w(f)+c <\sum_{e\in E(T)}w(e)+c$$
che, semplificando le costanti, implicherebbe:
$$\sum_{f\in E(S)}\;w(f)<\sum_{e\in E(T)}w(e)$$
Questo è impossibile, in quanto implicherebbe che $S$ sia un MST per $G$ (falso per ipotesi), e quindi che $T$ non lo sia.
$T$ è quindi MST anche di $G'$.

2)

è garantito che si incontri almeno
