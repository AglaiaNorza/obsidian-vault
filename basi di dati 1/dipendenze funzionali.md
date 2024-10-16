>[!info] definizione di dipendenza funzionale
>una **dipendenza funzionale** su R è una coppia ordinata di sottoinsiemi non vuoti X ed Y di R
>$$X \to Y$$
>si legge "X determina (funzionalmente) Y"
>- X si dice **determinante**
>- Y si dice **dipendente**
>  
>  dati uno shcema R e una dipendenza funzionale `X->Y` su R, un'istanza **soddisfa** la dipendenza funzionale `X->Y` se:
>  
>$$ \forall t_{1}, t_{2} \in r \space (t_{1}[X]=t_{2}[X]]\implies t_{1}[Y]=t_{2}[Y])$$
>(implicazione logica)
>- essenzialmente, le dipendenze funzionali esprimono dei **vincoli** sui dati (es. se il codice fiscale di due persone è uguale, lo deve essere anche la data di nascita)

>[!example] esempio
>- in una relazione che rappresenta esami, non c'è dipendenza funzionale `Voto -> Lode` perché si può prendere 30 senza prendere la lode, e neanche `Lode->Voto`, perché non prendere la lode non determina il voto, che può essere tra il 18 e il 30

un'istanza si dice **legale** se rispetta *tutte le dipendenze* in F

---
 
![[ist-legali1.png|450]]
dato uno schema di relazione R e un insieme F di dipendenze funzionali su R, ci sono delle dipendenze funzionali che non sono in F, ma sono soddisfatte da ogni istanza legale di R.

![[ist-legali2.png|450]]

---

### chiusura di un insieme di dipendenze fuzionali

>[!info] definizione
>dato uno schema di relazione R e un insieme F di dipendenze funzionali su R,
>la **chiusura di F** è l'*insieme di dipendenze funzionali che sono soddisfatte da ogni istanza legale di R*.
> 
>si denota con:
>$$F^+$$
>
>e si ha che $$ F \subseteq F$$

### chiave
>[!info] definizione
>dati uno schema di relazione R e un insieme F di dipendenze funzionali,
>un sottoinsieme K di uno schema di relazione R è una **chiave** di R se:
>1) $$ K \implies R \in F^+$$
>2) non esiste un sottoinsieme proprio `K'` di `K` tale che:
>	$$K'\implies R \in F^+$$