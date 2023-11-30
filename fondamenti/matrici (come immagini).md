2Le immagini si possono vedere come tensori di dimensione HWD3, o matrici di profondità 3.

```python
def create_matrix(rows, columns, value):
	matrix = []
	
	for each_r in range(rows):
		row = []
		
		for each_c in range(columns):
			row.append(value)
		matrix.append(row)
		
	return matrix
```

o, molto più semplicemente:
```python
def create_matrix(rows, columns, value):
	return [ [value] * columns for _ in range(rows) ]
```

> rows - y - height - matrix
> columns - x - width - matrix[0]
>canali - depth

stampare la matrice in maniera esteticamente piacevole:
```python
print(*mat, sep = "\n")
```

## Disegnare segmenti:

- dobbiamo avere **matrice** e **colore** (fa comodo avere un dizionario colormap con i colori e i loro codici)
- dobbiamo sapere come partire:

Un segmento orizzontale si rappresenta con:
- un ==punto di partenza== (x e y)
- o ==fino a dove== camminare (len of the segment) o un punto di arrivo (x)
(per un segmento verticale è la stessa cosa ma con la y)

```python
def mat_plotline_hor(mat, x, y, length, value):
	#mat è indicizzata [riga][colonna]
	mat[y][x+length] = [value]*length

```

```python
def mat_plotline_ver (mat, x, y, length, value):
	#mat è indicizzata [riga][colonna]
	for each_y in range(y, y+length):
		mat[each_y][x] = value

```

fare i quattro lati di un rettangolo:
```python
plot_line_h(mat, x, y, w, value) #1 
plot_line_h(mat, x, y+h-1, w, value) #2 
plot_line_v(mat, x, y, h, value) #3 
plot_line_v(mat, x+w-1, y, h, value) #4
```
(per la diagonale, ad ogni iterazione si aumentano sia x che y di 1)

## flippare and such

1) flip verticale:
```python
matrix[::-1]
#oppure
list(reversed(matrix))
```

2) flip orizzontale
```python
flipped_matrix = [row[::-1] for row in mat]

list(map(lambda r: r[::-1],mat))
```

3) girare orizzontalmente
(pensiero: quando scrivo la prima riga, devo prendere i valori dall’ultima colonna, perché sto scambiando le righe con le colonne)

```python
#H altezza della matrice: len(mat) 
#W larghezza della matrice: len(mat[0]) 

rotated=[[mat[r][c] for r in range(H)] for c in reversed(range(W))] #rotate left

#oppure 
list(reversed(list(map(list,zip(*mat)))))
```

4) trasporre
```python
return [ [ im[r][c] for r in range(H)] for c in range(W)  ] 
#oppure
list(map(list,zip(*im)))
```
###### crop
```python
def crop(im, x, y, w, h): #width, height 
	return [ [c for c in row[x:x+w]] for row in im [y:y+h] ]
```


## Operazioni:

- somma tra matrici: 
	 sommare ogni valore con il valore corrispondente
```
		     1 0 1        1 2 1       2 2 2
		     2 1 1   +    2 3 1   =   4 4 2
		     0 1 1        4 2 2       4 3 3
		     1 1 2        1 2 3       2 3 5
```

```python
#versione vagamente più complessa
new_mat = []
        for index in range(len(A)):
            new_list = []
            for jndex in range(len(A[0])):
                new_list.append(A[index][jndex] + B[index][jndex])
            new_mat.append(new_list)
```

```python
[ [el_A+el_B for el_A, el_B in zip(row_A, row_B)] for row_A, row_B in range(len(A))]
```

#### filtri

utile in generale: se cambi valori r,g,b:
```python
[ [(r,g,b) for (r,g,b) in row] for row in img]
#modifica r,g,b a piacimento
```

oppure, in funzione:
```python
def filter_func(pixel):
	return pixel #da modificare in base al filtro

def filter_im(im, filter_func):
    return [[ filter_func(pixel) for pixel in row] for row in im ] #matrice filtrata
```

##### luminosità
```python
def luminosita(pix,k):
    def clip(p):
        return max(min(int(round(p*k)),255),0) 
        #minimo e massimo così che non superi 255 e non vada sotto 0
    return tuple(clip(p) for p in pix)

def filter_im(im, filter_func, k):
    return [[ filter_func(c,k) for c in row] for row in im ]
```
##### grey-scale
```python
def gray(im):
    return [[ (sum(c)//3,)*3 for c in row] for row in im ]
```
##### blurring
```python
from tqdm import tqdm
def blur(im,x, y, H, W, k=5):
    # k=1;x=0 si fa -1, 0, +1 compreso
    somma = 0, 0, 0
    count = 0
    for xx in range(x-k,x+k+1):
        for yy in range(y-k,y+k+1):
            if 0 <= xx < W and 0 <= yy < H:
                pix = im[yy][xx]
                somma = tuple(map(lambda s,p: s+p, somma,pix))
                count += 1 
    return tuple(map(lambda s: min(max(s//count,0),255), somma))
    #s//count è per fare la media
    
    
def filter_im(im, filter_func):
    H, W = shape(im)
    return [[ filter_func(im,x,y, H, W) for x, c in enumerate(row)] 
            for y, row in tqdm(enumerate(im),desc='blurring',total=H) ]
images.visd(filter_im(im,blur))
```
	-tqdm - sorta di progress bar
cicliamo sulle righe con enumerate (abbiamo riga e numero di riga)
la filter function che blurra cicla sui pixel intorno al pixel scelto (con un raggio definito)

								 x x x
								 x O x
								 x x x

4 for annidati: due scorrono l'immagine e due lavorano sul pixel

la somma è un accumulatore di tipo tupla - fa la somma per tutti i componenti della tupla
```python
somma = tuple(map(lambda s,p: s+p, somma,pix))

#equivalente a:
	tuple(s+p for s, p in zip(somma, pix))
```

