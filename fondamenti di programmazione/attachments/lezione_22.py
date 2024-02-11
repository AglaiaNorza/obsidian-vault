# -*- coding: utf-8 -*-


# %% Introduzione agli Alberi di Gioco

## Gioco del Tris (filetto o tic-tac-toe) lo vediamo
## nella prossime lezioni

# Consideriamo questo gioco:
# dato lo stato della lista L
# calcolare tutti gli altri stati
# considerando come mossa la seguente proprieta':
    # Mossa: due elementi consecutivi
    # devono avere il solito resto se divisi per due
# prossimo stato:
    # quando la mossa **si verifica**
    # allora si crea un nuovo stato L'
    # che sostituisce agli elementi consecuitivi 
    # la somma dei due consecutivi (riduzione)
    
# Enumerare tutti i possibili stati
# e tornare tutte le foglie dell'albero di gioco
L = [99, 1, 3, 5, 20] #[d d d p]

class GameTree:
    def __init__(self, state):
        self.state = state
        self.state_viz = [ 'd' if s%2 == 1 else 'p'  for s in state] # per debug
        self.nexts = []
        self.next_states() # completa nexts
        
    def condition(self, pre, post):
        # se solito resto dai la somma
        if pre % 2 == post % 2:
            return pre + post
        
    def next_states(self):
        # andiamo di 2 in due quindi ci 
        # fermiamo ad uno prima della finme
        for i in range(len(self.state)-1):
            pre, post = self.state[i:i+2] # prende i e i+1
            somma = self.condition(pre, post)
            # se sono nella condizione
            # allora facciamo una mossa
            if somma: # if somma is not None
                # copio gli stati
                state = self.state[:]
                # quei 2 valori li sostituisci
                # con la somma
                state[i:i+2] = [somma]
                # enumero gli stati successivi
                self.nexts.append(GameTree(state))
                
    # def __repr__(self, livello=1):
    #     rez =  '\t'*livello + f"{self.state} {self.state_viz}"
    #     for node in self.nexts:
    #         rez += '\n'+ node.__repr__(livello+1)
    #     return rez
    
    def leaves(self):
        # se foglia non ho stati futuri
        if not self.nexts:
            return [ (self.state, self.state_viz)] # list of tuple of lists
        # assemblo le foglie di tutti i figli
        leaves = []
        for node in self.nexts:
            # mi faccio dare le foglie da
            # chi e' che mi sta sotto
            foglie_sotto = node.leaves() # lista
            leaves.extend(foglie_sotto)
        return leaves
    
    def leaves_external_list(self, L):
        if not self.nexts:
            # al contrario di prima combino  all'andata
            # semplicemente facendo append solo quando
            # sono nella foglia
            L.append((self.state, self.state_viz))
            
        # riapplico su tutti i figli
        for node in self.nexts:
            node.leaves_external_list(L)
            
            
    def leaves_list_default(self, L=None):
        
        start = False
        if L is None:
            L = []
            start = True
        
        if not self.nexts:
            # al contrario di prima combino  all'andata
            # semplicemente facendo append solo quando
            # sono nella foglia
            L.append((self.state, self.state_viz))
            
        # riapplico su tutti i figli
        for node in self.nexts:
            node.leaves_list_default(L)
        
        if start: return L
# %%
    
tree = GameTree(L)
#%%
#tree
W = tree.leaves()
# domanda chiesta a lezione
L = [] # questa verra' popolata in maniera distruttiva
       # senza creare ogni volta copie
       # viene fatto un append ogni volta che andiamo in una foglia
tree.leaves_external_list(L)
V = tree.leaves_list_default()
assert W == L == V, 'le due liste  devono essere uguali'

# %% Albero di gioco senza classe
state = [99, 1, 3, 5, 20] #[d d d p]

def game(state, L=None):
    # mi salvo se sono nella prima chiamata
    start = False
    if L is None:
        #lo sono...
        start = True
        # init lista vuota
        L = []
    # definisco booleano per foglia
    leaf = True
    # provo le mosse
    for i in range(len(state)-1):
        pre, post = state[i:i+2] # prende i e i+1
        # se la mossa e' verificata almeno una volta
        if pre % 2 == post % 2:
            #ricorsione, NON sonon in una foglia
            leaf = False
            somma = pre + post
            # nuovo stato tutti tranne i e i+1 ma metto la somma
            state_next = state[:i]+[somma]+state[i+2:]
            # ricorsione su next state
            game(state_next, L)
    # se dato uno stato, non entriamo mai in ricorsione
    # allora foglia
    if leaf:
        L.append((state,[ 'd' if s%2 == 1 else 'p'  for s in state]))
    # se era la prima chiamata torno L
    if start: return L
#%%
out = game(state)
print(out)
#assert out == W == V, 'le due liste  devono essere uguali'