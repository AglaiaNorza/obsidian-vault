Dato uno schema di relazione $R$ e un insieme di dipendenze funzionali $F$ su $R$, *esiste sempre* una decomposizione $\rho=\{ R_{1},\,R_{2},\,\,\dots,\,R_{k} \}$ tale che:
- $\forall i,\,i=1,\dots,k,\,\,\,R_{i}$ è in 3NF
- $\rho$ preserva $F$
- $\rho$ ha un join senza perdita

e tale decomposizione può essere calcolata in tempo polinomiale.

