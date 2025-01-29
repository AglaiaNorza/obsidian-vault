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
 
![[ist-legali1.png|center|450]]
dato uno schema di relazione R e un insieme F di dipendenze funzionali su R, ci sono delle dipendenze funzionali che non sono in F, ma sono soddisfatte da ogni istanza legale di R.

per esempio:

$$\text{Matricola} \rightarrow \text{CodiceFiscale} \rightarrow \text{DataNascita} $$

sarà sempre vero per ogni istanza legale - quindi, sarà soddisfatta anche `Matricola -> DataNascita`
### chiusura di un insieme di dipendenze fuzionali

>[!info] definizione
>dato uno schema di relazione R e un insieme F di dipendenze funzionali su R,
>la **chiusura di F** è l'*insieme di dipendenze funzionali che sono soddisfatte da ogni istanza legale di R*.
> 
>si denota con:
>$$F^+$$
>
>e si ha che:  $F \subseteq F^+$

### chiave
>[!info] definizione
>dati uno schema di relazione R e un insieme F di dipendenze funzionali, un sottoinsieme K di uno schema di relazione R è **una chiave** di R se:
>1) $$ K \rightarrow R \in F^+$$
>(in qualche modo, in questo insieme di dipendenze è presente la dipendenza `K -> R` - questa condizione la rende *superchiave* -perché sia chiave serve: )
>2) non esiste un sottoinsieme proprio `K'` di `K` tale che:
>	$$K'\rightarrow R \in F^+$$

per esempio, per uno schema Studente = Matricola, Cognome, Nome, Data: 
- il numero di matricola viene assegnato allo studente per identificarlo  
- poiché non ci possono essere due studenti con lo stesso numero di matricola, non ci possono essere due tuple con la stessa Matricola. 
- quindi `Matricola -> Matricola, Cognome, Nome, Data` deve essere soddisfatta da ogni istanza legale - matricola è chiave per studente.

>[!tip] chiave primaria
>dato uno schema di relazione R e un insieme F di dipendenze funzionali, possono esistere *più chiavi di R*
>- in SQL, una chiave sarà scelta come **chiave primaria**, e questa non potrà assumere valore nullo


### dipendenze funzionali banali
Sono dipendenze che non vale la pena specificare.
Sono date da:
$$ \text{Sottoinsiemi non vuoti X, Y di R tali che } Y \subseteq sub=X$$

perciò, ogni istanza di r soddisfa necessariamente la dipendenza funzionale $X\to Y$
(es. Nome, Cognome -> Nome)

Pertanto, se $Y\subseteq X,\,X\to Y\in F^+$ è detta **dipendenza banale**.

Dati uno schema di relazione R e un insieme di dipendenze funzionali F, si ha:
$$X\rightarrow Y \in F^+ \iff \forall A \in Y\; (X\rightarrow A \in F^+)$$

## domande orale
>[!question] possibili domande orale
>- cos'è una dipendenza funzionale? quando è soddisfatta?
>- cos'è una chiave?
>- cos'è un'istanza legale?
>- cos'è la chiusura di un insieme di dipendenze F?
>- cos'è una dipendenza banale?