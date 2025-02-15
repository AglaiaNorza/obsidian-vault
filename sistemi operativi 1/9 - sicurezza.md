> Secondo il NIST (National Institute of Standards and Technology), la definizione di "sicurezza informatica" è "la protezione offerta da un sistema informativo automatico al fine di conservare integrità, disponibilità e confidenzialità delle risorse del sistema stesso"

## obiettivi
Al centro della sicurezza, ci sono tre obiettivi:
- **integrità** --> i dati non devono essere modificati senza le dovute autorizzazioni
- **disponibilità** --> i servizi devono essere disponibili senza interruzioni
- **confidenzialità** --> i dati non devono essere letti senza le appropriate autorizzazioni

![[sec-triade.png|center|200]]

In più, si aggiungono due obiettivi:
- *autenticità*
- *tracciabilità* (accountability)

## minacce
Le principali minacce informatiche sono:
- **unauthorized disclosure** (accesso non autorizzato)
- **deception** (imbroglio)
- **disruption** (interruzione)
- **usurpation** (usurpazione)

### accesso non autorizzato
Avviene quando un'entità ottiene accesso a **dati per i quali non ha l'autorizzazione**. 
Minaccia la **confidenzialità**.

Gli attacchi che riescono ad ottenere un accesso non autorizzato sono:
- esposizione
- intercettazione
- inferenza
- intrusione

### imbroglio
Avviene quando un'entità autorizzata riceve **dati falsi** e pensa siano veri.
Minaccia l'**integrità**.

Gli attacchi sono:
- mascheramento (si ottengono le credenziale di un utente autorizzato; trojan)
- falsificazione
- ripudio

### interruzione
È un impedimento al corretto funzionamento dei servizi.
Minaccia l'**integrità** o la **disponibilità**.

Gli attacchi sono:
- incapacitazione
- ostruzione (DoS)
- corruzione

### usurpazione
Avviene se il sistema viene controllato direttamente da chi non ne ha l'autorizzazione.
Minaccia l'**integrità** del sistema.

Gli attacchi sono:
- appropriazione indebita (diventare amministratore di una macchina non propria)
- uso non appropriato (es. virus che cancella dati)

## asset
Sono le **risorse** da proteggere. 

Rispetto alla triade della sicurezza, gli asset sono:
 
![[asset-triade.png|center|400]]

## autenticazione
L'autenticazione è alla base della maggior parte dei controlli di accesso e traciabilità. Serve a determinare se un utente è abilitato ad accedere al sistema, e determina i privilegi dell'utente abilitato (*discretionary control access*: un utente può decidere a quali utenti concedere determinati permessi).

Si divide in due passi:
- identificazione
- verifica

### mezzi per l'autenticazione
Tradizionalmente, si dividono in tre fattori. Almeno uno deve essere presente (ma meglio usarne due contemporaneamente: 2FA).

- qualcosa che *sai*
- qualcosa che *hai*
- qualcosa che *sei*

>[!tip] ultimi sviluppi
>Recentemente, la biometrica è stata espansa in:
>
>- qualcosa che *sei* (biometrica statica): 
>	- caratteristiche facciali, impronte digitali, geometria della mano, retina, iride
>	- basata su riconoscimento di pattern (complesso e costoso)
>- qualcosa che *fai* (biometrica dinamica): 
>	- firma, voce, ritmo di battitura
>	- i pattern possono cambiare

I tipi di autenticazione principali sono:
- con **password** (la più usata)
- con **token**: oggetti fisici posseduti da un utente per l'autenticazione (es. smart card)

### memory card e smartcard
Le **memory card** possono memorizzare dati, ma senza elabolarli (es. scheda SD).
Sono spesso usate insieme a password o PIN. Il principale svantaggio si presenta nel caso in cui si perda il token.

Le **smart card** hanno invece un microprocessore, memoria e porte I/O.
Ne esistono diversi tipi, con diverse caratteristiche fisiche, interfacce (es. lettore/tastierino) e protocolli di autenticazione (es. generatore di password statico o dinamico).

## controllo di accesso
Determina quali tipi di acccesso sono ammessi, sotto quali circostanze e da chi.
Può essere:
- **discrezionale** - un utente può concedere i suoi stessi privilegi ad altri utenti
- **obbligatorio** - un utente non può concedere i suoi stessi privilegi ad altri utenti
- **basato su ruoli**
	- implementazione del principio di minimo privilegio: ciascun ruolo deve contenere il minimo insieme di diritti d’accesso per il ruolo stesso
	- un utente viene assegnato ad un ruolo, che lo abilita ad effettuare le operazioni richieste per quel ruolo
	- si utilizzano due tabelle per la gestione dei ruoli e dei permessi: una gestisce a quali utenti sono assegnati quali ruoli e una i permessi di ciascun ruolo

>[!example]- tabelle dei ruoli
> controllo d'accesso (utente-ruolo):
>![[controllo-accesso.png|center|200]]
>
>ruolo-oggetto:
>![[ruoli-oggetti.png|center|300]]

Le tre modalità possono essere presenti contemporaneamente su diverse classi di risorse.

## UNIX: meccanismi di protezione
in UNIX, la sicurezza è tipicamente basata sull’autenticazione dell’utente (*User-Oriented Access Control*), mentre il modello di controllo degli accessi mette al centro i dati stessi per decidere chi può fare cosa (*Data-Oriented Access Control*).

> Ci possono però anche essere altri meccanismi, come NIS, LDAP e Kerberos.

Per ogni utente ci sono uno **username** alfanumerico e un **uid** numerico (usato quando occorre dare un proprietario ad una risorsa).
Ogni utente appartiene ad un **gruppo**, identificato a sua volta da un gid.
Per tenerne traccia, esistono appositi file di sistema: `/etc/group` e `/etc/passwd` (approfondito meglio in [[10, 11 - password, buffer overflow#password in Linux|password]]).

> [!info] login
> Il login può essere fatti da terminale (`getty`) o tramite rete (`telnet`, `ssh`), e richiede una coppia username+password.
> Se la coppia corrisponde ad una entry di `/etc/passwd`, viene eseguita la shell lì indicata.
> Per uscire dalla shell si usa il comando `exit`.

### accesso ai file
Per ogni file ci sono tre terne di permessi: lettura, scrittura, esecuzione.
La prima terna è per il *proprietario*, la seconda per il *gruppo* del proprietario, la terza per *tutti* gli altri utenti.
(Il proprietario è chi ha creato il file, ma può essere cambiato con il comando `chown`, mentre i diritti si possono cambiare con `chmod`).

> [!example] esempio (federico, del gruppo `em`, è proprietario):
> ```
> -rwxr-xr-x 1 federico em 5120 Nov 7 11:03 a.out
> -rw-r--r-- 1 federico em 233 Nov 7 11:03 test.c
> ```

Le terne di diritti sono usate ogni volta che un processo richiede l’accesso ad un file. Si controllano in ordine le tre terne, e si prende l'elemento corrispondente all'accesso richiesto.

#### SETUID e SETGID
Può capitare che un utente si trovi nelle condizioni di dover eseguire comandi o modificare file a cui, in generale, *non ha permesso*.

Per questo motivo, alcuni comandi (come `passwd`) hanno nella terna l'elemento `s` (permesso speciale `SETUID` e/o `SETGID`). 
Tale permesso può essere accordato solo da un utente amministratore con `chmod u+s nomefile` e/o `chmod g+s nomefile`.

- vuol dire che l’`uid` o il `gid` del processo non sono quelli dell’utente che lo ha lanciato, ma del proprietario del file eseguibile.
- è però un meccanismo da usare con cautela, perché facilita gli attacchi rootkit.