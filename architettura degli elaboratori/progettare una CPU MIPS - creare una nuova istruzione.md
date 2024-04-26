 ### aggiungere una nuova istruzione
supponiamo di voler creare una nuova istruzione.
dobbiamo:
- definire la sua **codifica**
- definire **cosa faccia**
- individuare le **unità funzionali necessarie**
- individuare i **flussi di informazione** necessari
- individuare i **segnali di controllo** necessari
- calcolare il **tempo** necessario per la nuova istruzione (e se modifica il tempo totale)

#### aggiungere il jump (j)
supponiamo che la codifica sia:
 
![[codifica jump.png|400]]

il campo da 26 bit rappresenta l'**istruzione di destinazione** del salto ed
- è un indirizzo assoluto.

poiché sono 26 bit e non 32, bisogna svolgere una serie di operazioni:
1) si guadagnano due bit facendo lo **shift logico** a sinistra (moltiplicando quindi per 4) (gli zeri sono presi con la messa a terra)]
2) i 4 bit "mancanti" vanno presi dai MSB di PC+4 (bit che indicano il "blocco" in cui ci si trova, quindi prendendoli da PC+4 ci muoviamo nello stesso blocco di 256mb) - si fa con una sorta di `or` che è in realtà un collegamento di cavetti
 
	![[jump cambio bit.png|200]]

**cosa fa** il jump?
`PC <- left shift 2 bit istruzione[25-0] OR (PC+4)[31-28]`

**unità funzionali**: PC+4 (presente), shift left 2 bit con input a 26 bit (da aggiungere), OR con i bit di PC+4 (si ottiene dalle connessioni), MUX per selezionare il nuovo PC (da aggiungere)

**flusso dei dati**: `Istruzione[25-0] -> SL2 -> (OR) -> MUX -> PC`

**segnali di controllo**: `jump` per il MUX, `RegWrite` e `MemWrite` = 0

**tempo necessario**: fetch e, in parallelo il tempo dell'adder che calcola PC+4

![[jump mips arch.png|center|400]]

#### jump and link (jal)
si comporta come jump, ma salva PC+4 nel registro `$ra`

**cosa fa**: `PC <- left shift 2 bit istruzione[25-0] OR (PC+4)[31-28]` + `$ra <- PC+4`

**unità funzionali**: - quelle di jump -
\+ MUX per selezionare il valore di PC+4 come valore di destinazione, MUX per selezionare il registro `$ra` come destinazione

**flusso dei dati**: `Istruzione[25-0] -> SL2 -> (OR) -> MUX -> PC`
e, in più
`PC+4 -> MUX -> registri (dato da memorizzare)`
(31 = `$ra`) `31 -> MUX -> registri (registro destinazione)` 

 **segnali di controllo**: `jump` per il MUX, `RegWrite` e `MemWrite` = 0

**tempo necessario**: il WriteBack deve avvenire dopo che siano finiti sia il fetch che il calcolo di PC+4 (che va memorizzato in `$ra`), perciò il tempo sarà dato dal massimo tra fetch e add sommato al WB. 

![[jal arch mips.png|center|400]]

#### add immediate (addi)
**cosa fa**: somma la parte immediata al registro `rs` e pone il risultato in `rt`

**unità funzionali**: ALU per la somma (presente),
MUX che seleziona la parte immediata come secondo argomento (presente),
estensione del segno della parte immediata (presente)

**flusso dei dati**: `Registri[rs] -> ALU`
`Costante -> est. segno -> ALU`
`ALU -> Registri[rt]`

**segnali di controllo**: ALUsrc = 1, MemtoReg = 0, RegWrite = 1, MemWrite, Branch, Jump = 0;

**tempo necessario** quanto un'istruzione di tipo R

si comporta quasi come la `lw cost(rs)` ma invece di salvare si scrive sui registri.

![[addi arch mips.png|center|400]]

#### jump to register (jr)
**cosa fa**: trasferisce in `PC` il contenuto del registro `rs`

**unità funzionali**: MUX per selezionare il PC dall'uscita del blocco registri

**flusso dei dati**: `Registri[rs] -> PC

**segnali di controllo**: `JumpToReg`, che abilita il MUX per inserire in PC il valore del registro

**tempo necessario**: Fetch + Reg

![[circuito con jr.png|center|400]]

