
| dim                        | tip                                                                                                                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NFA $\equiv$ DFA           | delta = E (insieme degli stati raggiunti da ogni stato nel set)                                                                                                                    |
| chiusure REG               | unione nuovo stato con $\epsilon$, intersezione prod cartesiano, concat quando arrivo a fine L1 $\epsilon$ per $q_{02}$, star quando ho finito $\epsilon$ arco verso l'inizio      |
| reg $\equiv$ L(re) / regex | primo verso x induzione su casi regex, 2o verso NFA generalizzato + CONVERT(G')                                                                                                    |
| pumping lemma REG          | ricordati s <= p+1                                                                                                                                                                 |
| DFA to CFG                 | Vq + Vq -> aVp, $\phi$ biiettiva x  dimostrazione                                                                                                                                  |
| Chomsky                    | ricorda S0 -> S (poi $\epsilon$ regole poi regole unitarie poi k>=3 poi xX)                                                                                                        |
| CFL $\iff$ PDA             | lato CFL: costruiamo PDA x grammatica G con qstart, qloop, qacc + 4 delta<br>lato PDA: CFG con 3 regole claim Apq genera x iff porta P da p a q senza cambiare stack (x induzione) |
| pumping lemma CFL          | cammino + lungo i genera stringhe max $2^{i-1}$; p = $2^m$; cammino$\geq m+1$; prendo ripetizione DAL BASSO x questo sottoalbero altezza massima m+1                               |


| dim                        | tip                                                                                                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NTM to TM                  | nastro 3 in ordine lunghezza + lessicogragico                                                                                                                                       |
| Adfa, Anfa, Arex           | Adfa simula, Anfa e Arex trasformano in DFA e NFA                                                                                                                                   |
| Edfa, Ecfg                 | marca stati con archi entranti da marcati / marca var se ogni a dx marcata                                                                                                          |
| Eqdfa                      | differenza simmetrica + Edfa                                                                                                                                                        |
| Acfg                       | max 2n-1 passi                                                                                                                                                                      |
| linguaggi non rec          | TM numerabili, stringhe infinite non numerabili, ogni linguaggio e' una stringa infinita OR ! DEC = rec ^ coREC quindi non DEC -> o L o $\bar{L}$ non rec<br>(es. $\overline{ATM}$) |
| Atm non decidibile         | costruisco D che fa M< M> e diagonalizza - che succede se faccio D< D> ?                                                                                                            |
| DEC = REC ^ coREC          | (1) se L DEC anche !L DEC (2) eseguo M1 e M2 in parallelo                                                                                                                           |
| A < B dec e B dec -> A dec | decisore per A calcola f(w) e poi decide B                                                                                                                                          |
| HALTtm non dec             | x assurdo se HALTtm dec posso sapere se termina, ovvero decidere Atm (se termina simulo senno' rifiuto)                                                                             |
|                            |                                                                                                                                                                                     |
| REGtm non dec              |                                                                                                                                                                                     |
