tipi di dati di base built-in.

![[Screen Shot 2024-02-28 at 08.58.12.png]]
- Le stringhe non sono in realtà tipi primitivi.
 
>[!warning] attenzione ai char
> I char sono interpretati come veri e propri numeri unicode, quindi somma e sottrazione danno un risultato int.

#### variabili
Una variabile è creata tramite una **dichiarazione**, nella quale deve essere specificato il tipo:
```java
int contatore;
```
il punto e virgola è necessario alla fine di ogni istruzione.

il valore viene assegnato attraverso un'**assegnazione**:
```java
int contatore = 0;
```

le due cose possono essere fatte insieme:
```java
int contatore = 0;
```

> [!info] static typing
> Il tipo di una variabile (se primitivo) è **statico** - non può cambiare.

Il nome assegnato a una variabile è il suo **identificatore** (come in python, la prima lettera non può essere un numero) - gli identificatori sono case-sensitive.

>[!tip] notazione
Si utilizza la **notazione Camel case**:
> - quando si dichiara una variabile composta da più parole, la prima inizia con una minuscola e le successive con maiuscole (es. "contatoreTreniEsplosi")
> - le **classi** devono per forza iniziare con una maiuscola (poi si continua con la camel case)

#### finals:
le variabili **final** non possono cambiare valore all'interno di un programma (non si possono riassegnare) .
#### letterali (o costanti)
rappresentazioni a livello di codice sorgente del valore di un tipo di dato.
(es: 27 è un letterale per gli interi)
##### costanti intere e in virgola mobile
- Le costanti int sono semplici numeri.
- Le costanti long vengono specificate con il suffisso L.
- Le costanti double sono numeri con la virgola (che è un *punto*).
- Le costanti float hanno il suffisso f o F.
- Il prefisso *0b* indica una rappresentazione binaria (es. 0b101 è 5)
- Si può usare un trattino basso per separare le cifre (10_000 == 10000)
#### array:
```java
String[] a = {"a", "b", "c", "d"}
```
#### precedenza operatori aritmetici
![[Screen Shot 2024-02-28 at 09.39.14.png]]
come in matematica.
#### caratteri e stringhe
I char seguono la **codifica unicode** (basata su interi a 16 bit), e sono racchiusi da apici (singoli) - 'a'.
>[!info]- caratteri di escape
>- `'\t'` - tab
>- `'\n'` - a capo
>- `'\\'` - backslash
>- `' \' '` - apice
>- `'\"'` - virgolette

