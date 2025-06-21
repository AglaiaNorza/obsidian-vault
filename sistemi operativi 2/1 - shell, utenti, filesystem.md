---
created: 2025-06-21T10:11
updated: 2025-06-21T10:40
---
## shell
La shell è un'interprete di comandi, ovvero un programma che esegue altri comandi.
- la shell scrive un prompt e attende che l'utente scriva un comando
- il prompt tipico è di questo tipo: `utente@nomemacchina:~path`

Ogni comando ha questa struttura:
```
comando [opzioni] argomentiobbligatori
```

Le opzioni hanno due segnature:
- `--parola` (es. `-interactive`)
- `-carattere` (es. `-i`)

Esse possono anche avere un **argomento** (anch'esso con segnature diverse)
- `-k1` o `-k 1`
- `--key=1`

Le opzioni *senza argomenti* sono raggruppabili:
- `-b -r -c` $\iff$ `-brc`

Esistono anche le opzioni BSD-style, senza dash (es. `tar xfz nomefile.tgz`).

## utenti
Durante l'installazione di Linux, è necessario specificare almeno un utente (utente principale).
- non tutti gli utenti possono fare login 
	- `root` non può fare il login, ma un utente può acquisire i diritti di `root` attraverso `su` e `sudo`
- ogni utente appartiene almeno ad un **gruppo** (ne viene automaticamente creato uno con lo stesso nome dell')