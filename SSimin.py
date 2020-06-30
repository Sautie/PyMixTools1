# Algorithme vorace pour trouver l'ensemble S de cardinalité minimum
# tel que pour tout i, l'intersection de S avec Si n'est pas égale
# à l'ensemble vide
# Miguel Sautié-Castellanos

import numpy as np
import random


def random_graph(n,m):
    # Input : size n, m
    # Output : matrice representant A[i][j] = 1 ssi S_i contient l'element j
    A=np.array([[random.randint(0,1) for i in range(m)] for j in range(n)])   
    return A

def intersection(A):
         
    sz=np.shape(A)
    n_sets=A.sum(axis=0)    
    M_desc_order=n_sets.argsort()[::-1]    
    i=0    
    sf=set()
    S=set()
    while (i<len(M_desc_order)):    
        c=A[:,M_desc_order[i]]
        one_index = np.nonzero(c)[0]
        one_index=one_index+1        
        if (i==0):        
            sf.update(one_index)
            S.add(M_desc_order[i]+1)
        else:
            ind=set(one_index)
            dif=ind.difference(sf)
            if (len(dif)>0):
                sf.update(dif)
                S.add(M_desc_order[i]+1)
        if (len(sf)==sz[0]):
            return S
        i=i+1
    # If there is at least one empty set Si
    # then the intersection between S and Si will
    # not be different from the empty set for all i.    
    # (an empty set Si is a zeros row in
    # the random boolean matrix, it is highly probable, 
    # mainly when there are a lot of small sets Si,that is, 
    # smaller values of m and higher values of n)
    Si=A.sum(axis=1)  
    u=np.where(Si == 0)
    if len(u)>0:
        y=u[0]+1
        print("Warning: The intersection of the set S with at least one Si (set:",y[0],") is empty")            
    return S
                
    
def experiment(n, m, nb_experiments):   
    size_of_S = []
    for exp in range(nb_experiments):
        A = random_graph(n, m)
        S = intersection(A)
        size_of_S.append(len(S))
    return size_of_S   


if __name__=="__main__": 
    n = 20
    m = 100
    k = 50
 
    size_of_S = experiment(n, m, k)    
    print("mean", np.mean(size_of_S), "std", np.std(size_of_S))


