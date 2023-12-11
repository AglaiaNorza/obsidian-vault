utili per aggiungere spice alle funzioni o alle classi, o per fare memoization nelle ricorsive.

in python, le funzioni sono first-class objects - possono essere passati come argomenti ad altre funzioni.

Un decoratore  è formato da:
- una **<font color="#b2a2c7">funzione esterna</font>**:
	- riceve come input una funzione (che sarà quella da decorare), e ritorna la funzione innestata
	- può comunque fare cose
<br>
- una **<font color="#4bacc6">funzione innestata</font>**:
	- riceve come input gli argomenti della funzione da decorare (segnati di solito come (* args, ** kwargs )), e  fa quello che deve fare:
		- come lo fa?
			- può usare gli argomenti passati alla funzione - "args" o "kwargs" ([[decoratori#^f52bed |più info]])
			- può chiamare la funzione e salvare il risultato in una variabile (o non salvarlo) - func(* args)
<br>
Per usare il decoratore su una funzione, basta scrivere, nella riga prima del def, @nomedeldecoratore.
Essenzialmente, è come chiamare una funzione composta:
decoratore(funzione).
Quindi l'ordine di esecuzione è:
1) @decoratore chiama il decoratore con la funzione
2) quindi si esegue prima la funzione esterna del decoratore, che fa le sue cose
3) funzione interna del decoratore - realisticamente chiama la funzione da decorare
4) funzione da decorare (che ritorna al decoratore)]
5) parte succesiva del decoratore
6) fine

*esempio di un decoratore che fa memoizing (mio codice per HW8):*
memoizing crea un dizionario in cui salva i risultati di actual check - se una stringa passata actual check è già nel dizionario, ritorna direttamente il valore associato, altrimenti aggiunge il valore chiamando la funzione e salvando l'output.
```python
def memoizing(func):
    subs = {}
    
    def dic_check(*args, **kwargs):
        if args in subs:
            return subs[args]

        else:
            new = func(*args)
            subs[args] = new
            return new

    return dic_check

@memoizing

def actual_check(longer, shorter):  

    dic_more, dic_less = {}, {}

    for i in shorter:
        dic_less[i] = dic_less.get(i, 0) +1

    for k in longer:
        dic_more[k] = dic_more.get(k, 0) +1


    for char, count in dic_less.items():
        if char not in dic_more or dic_more[char] < count:
            return False
            
    return True

```

note:
[[pack e unpack operators]]
(args è una tupla con tutti gli argomenti "non-keyword" - cioè che non hanno una coppia chiave-valore, come per esempio i dizionari. kwargs prende invece quei valori e li salva come dizionario - per esempio, se viene passato a = "lettera", lo metterà dentro il dizionario kwargs come a : "lettera")  ^f52bed