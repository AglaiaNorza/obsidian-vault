Supponiamo di voler creare una base di dati contenente i seguenti dati di studenti universitari:
- dati anagrafico-identificativi (nome, cognome, data, comune, provincia, matricola, CF)
- dati curricolari (per ogni esame: voto, data, codice, titolo e docente)
##### ipotesi 1
la base di dati consiste di una sola relazione con schema:
- Curriculum (Matr, CF, Cogn, Nome, DataN, Com, Prov, C#, Tit, Doc, DataE, Voto)
 
questa ipotesi non funziona bene a causa della sua ridondanza: 
>[!warning] ridondanza in una base di dati 
> 
> La ridondanza dà luogo a:
> - spreco di spazio in memoria
> - anomalie di aggiornamento - se cambia il docente del corso, il dato deve essere modificato *per ogni esame*
> - di inserimento - non posso inserire i dati anagrafici di uno studente *finché non ha sostenuto un esame*
> - di cancellazione - eliminando i dati anagrafici di uno studente potrebbero essere *eliminati i dati di un corso*

##### ipotesi 2
tre schemi di relazione:
- Studente (Matr, CF, Cogn, Nome, Data, Com, Prov)
- Corso (C#, Tit, Doc)
- Esame (Matr, C#, Data, Voto)

>[!warning] problemi ipotesi 2
>![[es-bdr.png|400]]

##### ipotesi 3
quattro schemi di relazione:
- Studente (Matr, CF, Cogn, Nome, Data, Com)
-  Corso (C#, Tit, Doc)
- Esame (Matr, C#, Data, Voto)
- Comune (Com, Prov)

>[!done] quando uno schema è "buono"?
>quando non presenta:
>- ridondanze
>- anomalie di aggiornamento, inserimento e cancellazione
### vincoli
condizioni su quello che stiamo progettando.
(molti si impongono direttamente sulle tabelle)
- un **vincolo** è una rappresentazione nello schema di una condizione valida nella realtà di interesse
- un'istanza della base di dati è **legale** se soddisfa ~~tutti i vincoli~~ tutte le dipendenze funzionali (dei vincoli che non sono dipendenze funzionali non ci interessa)

### DBMS
un DBMS permette di:
- definire insieme allo schema della base di dati i vincoli
- verificare che un'istanza della base di dati sia legale
- in base a specifici vincoli predefiniti, impedire l'inserimento di tuple che violerebbero tali vincoli.

un DBMS è dotato di procedure per la verifica di vincoli che ricorrono più frequentemente:
- vincoli di dominio (es. 18<= voto <= 30)
- chiavi
- contenimento di domini (es. il numero di matricola in un verbale deve essere il numero di matricola di uno studente)

(le dipendenze funzionali definite su uno schema di relazione esprimono particolari vincoli di dipendenza tra sottoinsiemi di attributi dello schema stesso, che devono essere soddisfatti da ogni istanza dello schema)