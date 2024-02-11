- un asterisco - liste
- due asterischi - dizionari

```python
*full_name, = "aglaia", "stocazzo", "norza" 
#["aglaia", "stocazzo", "norza"]

*first_name, last name = "aglaia", "stocazzo", "norza"
#f_n ["aglaia", "stocazzo"]
#l_n ["norza"]
```

si possono usare anche per unire due dizionari (o liste):
```python
num_dict = {f:1, g:2} 
num_dict_2 = {j:4, l:m} 

print ({**num_dict, **num_dict_2}) 
#{f:1, g:2, j:4, l:m}
```
##### nelle funzioni
si utilizzano principalmente in due casistiche:

1) **definizioni** di funzione:
	PACKING - i valori dati come input vengono impacchettati
	(nei dizionari, la chiave è il nome della variabile e il valore è il suo valore)
```python
def foobar (kwargs**):
	#blablabla

print(foobar(ciao=True, nonna=False, hi=4))
#dizionario {ciao:True, nonna:False, hi:4}
```

2) **chiamate** di funzione:
	UNPACKING - spacchetta i valori dentro la funzione
```python
L = [1, 2, 3, 4]

print(*L)
#stampa tutto il contenuto di L sulla stessa riga 
#(se voglio righe diverse devo mettere "sep=\n")
```
