### 1. Linguaggi Regolari (Automi)
* **Correttezza della Funzione di Transizione Estesa ($\delta^*$):** Dimostrazione per induzione sulla lunghezza della stringa $|w|$ che conferma che l'ultimo passo della computazione preserva il significato semantico.
* **Equivalenza NFA $\equiv$ DFA:** Dimostrazione che $L(NFA) \subseteq L(DFA)$ tramite la "Subset Construction" (costruzione dei sottoinsiemi). Si definisce ogni stato del DFA come un insieme di stati dell'NFA ($Q_{DFA} = P(Q_{NFA})$), gestendo le $\epsilon$-transizioni.
* **Conversione GNFA $\to$ Regex:** Algoritmo di conversione da Automa a Stati Finiti Generalizzato a Espressione Regolare. La dimostrazione procede per induzione sul numero di stati $k$, rimuovendo uno stato alla volta e aggiornando le etichette (regex) sugli archi rimanenti.
* **Pumping Lemma per Linguaggi Regolari:** Dimostrazione basata sul *Pigeonhole Principle* (Principio dei Cassetti). Se un DFA ha $P$ stati e legge una stringa $w$ con $|w| \ge P$, deve visitare $P+1$ stati, visitando necessariamente uno stato due volte ($q_p = q_s$), permettendo di ciclare la sottostringa $y$.

### 2. Linguaggi Context-Free (CFL)
* **Equivalenza CFG $\to$ PDA:** Costruzione di un PDA che simula le derivazioni di una Grammatica Context-Free (CFG) utilizzando la pila per le variabili e l'input per i terminali.
* **Equivalenza PDA $\to$ CFG:** Dimostrazione complessa per induzione sul numero di passi. Si costruiscono variabili grammaticali $A_{pq}$ che generano tutte le stringhe che portano il PDA dallo stato $p$ allo stato $q$ con pila vuota. Si distinguono due casi induttivi: la pila non si svuota mai internamente oppure si svuota in un punto intermedio.
* **Pumping Lemma per CFL:** Dimostrazione basata sugli alberi di derivazione (parse trees) di una grammatica in Forma Normale di Chomsky. Se l'albero è sufficientemente alto ($\ge |V|+1$), esiste un cammino con una variabile ripetuta, permettendo la scomposizione della stringa in $uv^ixy^iz$.

### 3. Calcolabilità e Indecidibilità
* **Non numerabilità dei Linguaggi:** Dimostrazione che l'insieme delle Macchine di Turing è numerabile, mentre l'insieme di tutti i linguaggi su un alfabeto (insieme delle parti di $\Sigma^*$) non lo è (uso della diagonalizzazione e delle sequenze caratteristiche).
* **Indecidibilità di $A_{TM}$ (Problema dell'Accettazione):** Dimostrazione per assurdo tramite diagonalizzazione. Si ipotizza un decisore $H$ e si costruisce una macchina $D$ che, data $<M>$, esegue l'opposto di $H(<M, <M>>)$. L'esecuzione $D(<D>)$ porta a una contraddizione.
* **Teorema $L \in DEC \iff L \in REC \cap CoREC$:** Dimostrazione che un linguaggio è decidibile se e solo se lui e il suo complemento sono riconoscibili. La prova costruttiva esegue due TM in parallelo.
* **Indecidibilità di $HALT_{TM}$:** Riduzione da $A_{TM}$. Se potessimo decidere se una macchina termina, potremmo decidere se accetta.
* **Teoremi di Incompletezza di Gödel:**
    * **1° Teorema:** In un sistema di prova $\Pi$ sufficientemente potente, esiste una proposizione vera ma non dimostrabile. La dimostrazione costruisce una frase autoreferenziale ("Non sono dimostrabile").
    * **2° Teorema:** Se un sistema $\Pi$ è consistente, non può dimostrare la propria consistenza ($Cons(\Pi)$).

### 4. Complessità Computazionale
* **2SAT $\in P$:** Dimostrazione che la soddisfacibilità di formule con 2 letterali per clausola è risolvibile in tempo polinomiale, riducendo il problema alla ricerca di componenti fortemente connesse in un grafo di implicazioni (insoddisfacibile sse $x \to \neg x$ e $\neg x \to x$).
* **Equivalenza Definizione NP:** Dimostrazione che la definizione di NP tramite *Verificatore Polinomiale* è equivalente a quella tramite *Macchina di Turing Non Deterministica (NTM)* polinomiale.
* **Teorema di Cook-Levin (SAT è NP-Completo):** Dimostrazione che ogni linguaggio in NP è riducibile a SAT ($L \le_m^p SAT$). Si costruisce una formula booleana che descrive un "Tableau" valido di computazione di una NTM (configurazioni legali, transizioni, stato iniziale/finale).
* **Teorema di Savitch ($PSPACE = NSPACE$):** Dimostrazione che $NSPACE(f(n)) \subseteq SPACE(f^2(n))$. Si usa un algoritmo ricorsivo (tipo "divide et impera") per verificare la raggiungibilità tra due configurazioni cercando un punto intermedio, riutilizzando lo spazio.
* **Gerarchie di Tempo e Spazio (Hierarchy Theorems):**
    * **Time Hierarchy Theorem:** Dimostrazione tramite diagonalizzazione che, dato più tempo ($t_2(n) \gg t_1(n)$), si possono decidere più linguaggi.
    * **Space Hierarchy Theorem:** Analogo per lo spazio. Si costruisce una macchina che simula tutte le altre entro un limite di spazio e ne inverte l'output.

---

## PARTE 2: LISTA ARGOMENTI DI TEORIA

### Automi e Linguaggi Regolari
* **DFA (Automa a Stati Finiti Deterministico):** Definizione formale $(Q, \Sigma, \delta, q_0, F)$.
* **NFA (Non Deterministico):** Differenze con DFA, $\epsilon$-transizioni.
* **Regex (Espressioni Regolari):** Sintassi e semantica.
* **Proprietà di Chiusura:** Unione, Concatenazione, Star (*), Intersezione, Complemento.
* **Dimostrare la Non-Regolarità:** Uso del Pumping Lemma e proprietà di chiusura (es. intersecare con una regex per ottenere un linguaggio noto non regolare come $0^n1^n$).

### Linguaggi Context-Free (CFL)
* **CFG (Grammatiche):** Variabili, Terminali, Regole di produzione, Derivazioni ($u \Rightarrow^* w$).
* **Forma Normale di Chomsky (CNF):** Struttura delle regole ($A \to BC$ o $A \to a$). Algoritmo di semplificazione (rimozione $\epsilon$-produzioni, regole unitarie).
* **PDA (Automi a Pila):** Definizione, utilizzo dello stack, accettazione per stato finale vs pila vuota.
* **Relazioni:** Grammatiche lineari (destre/sinistre) e loro equivalenza con gli Automi Finiti.

### Calcolabilità (Macchine di Turing)
* **Macchina di Turing (TM):** Definizione, configurazione, nastro infinito, testina.
* **Varianti della TM:** Multinastro, Non Deterministica (NTM). Equivalenza tra le varianti.
* **Riconoscibilità vs Decidibilità:** Differenza tra fermarsi sempre (decisore) e fermarsi solo se accetta (riconoscitore).
* **Problemi Decidibili:** $A_{DFA}, A_{NFA}, E_{DFA}, EQ_{DFA}, A_{CFG}, E_{CFG}$.
* **Problemi Indecidibili:** $A_{TM}, HALT_{TM}, E_{TM}, REG_{TM}$.
* **Mapping Reductions ($A \le_m B$):** Definizione e utilizzo per dimostrare indecidibilità (se $A$ è indecidibile e $A \le_m B$, allora $B$ è indecidibile).

### Complessità Computazionale
* **Classi di Tempo:**
    * **P:** Tempo polinomiale deterministico ($\bigcup DTIME(n^k)$).
    * **EXP:** Tempo esponenziale ($DTIME(2^{n^k})$).
    * **NP:** Tempo polinomiale non deterministico / Verificabile in tempo polinomiale.
* **NP-Completezza:**
    * Definizione di NP-Hard vs NP-Complete.
    * Riduzioni polinomiali ($A \le_m^p B$).
    * Esempi di riduzioni: $SAT, 3SAT, CLIQUE, 3COL, 4COL$.
    * Relazione tra classi: $P \subseteq NP \subseteq PSPACE \subseteq EXP$.
* **CoNP:** Definizione (complemento di NP) e problema $UNSAT$.
* **Classi di Spazio:**
    * $SPACE(f(n))$ vs $NSPACE(f(n))$.
    * **PSPACE:** Spazio polinomiale. Equivalenza $PSPACE = NSPACE$ (Savitch).
    * **L (Log-Space) e NL (Nondeterministic Log-Space):** Definizioni, riduzioni logaritmiche ($\le_m^L$).
    * **PATH:** Problema NL-Completo (raggiungibilità nei grafi diretti).
* **Relazioni Spazio-Tempo:**
    * $TIME(f(n)) \subseteq SPACE(f(n))$.
    * $SPACE(f(n)) \subseteq TIME(2^{O(f(n))})$.