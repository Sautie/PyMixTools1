# using backtracking (depth-first search) to find the abacus of weigth (w) minimal size
# Miguel Sautie
import numpy as np
def abacus_weight(A):   
    la=A.shape    
    if (la[0]==2)and(A.ndim==2):
        w = [None] * (la[1]+1)        
        w[0]=1
        i=1
        for j in range(0, la[1]):
            if (A[0,j]<=j)and(A[1,j]<=j):
                w[i]=w[A[0,j]]+w[A[1,j]]
                i=i+1
            else:
                return -1
    return w[la[1]]

def minimal_size_abacus(w):
    # Input : integer w>=1
    # Output : abaque of minimal size
    def mini_S_abacus(T, m, poids, w):
        if (w==2)or(w==poids):
            return T
        while (poids<w):
            y = np.array([[m], [m]])
            T=np.append(T, y, axis=1)
            m=T.shape[1]-1
            poids=abacus_weight(T)
            #depth-first search for generating abacus of different sizes and weights
            if poids<=w:
                return mini_S_abacus(T, m+1, poids, w) 
            u=T.shape[1]-1            
            Mi=999
            b=0
            Ta=np.array([[0], [0]])
            while (u>=0):
                uu=u
                while (uu>=0):
                    T[1,u]=uu
                    poids=abacus_weight(T)
                    po=w-poids
                    if(po>0)and(po<Mi):
                        Ta=np.copy(T)                       
                        Mi=po                       
                    if (poids==w):
                        return T
                    uu=uu-1                
                u=u-1
            if (b!=1):
                T=np.copy(Ta)
            m=m+1
            poids=abacus_weight(T)  
    A = np.array([[0], [0]])    
    return mini_S_abacus(A, 1, 0, w).tolist()


if __name__=="__main__":
    A1 = np.array([[0, 1, 2, 3, 4], [0, 1, 0, 2, 2]])
    A2 = np.array([[0, 0, 0, 0, 3], [0, 1, 2, 3, 4]])
    A3 = np.array([[0, 2, 2, 2], [0, 1, 2, 3]])
    A4 = np.array([[10], [0]])
   
    # Answers should be
    # 13, 9, -1, -1

    print("---------- 3 a) ---------------")
    print("A1", int( abacus_weight(A1) )==13)
    print("A2", int( abacus_weight(A2) )== 9)
    print("A3", int(abacus_weight(A3)) == -1)
    print("A4", int(abacus_weight(A4)) == -1)


    w1 = 4
    result1 = list([[0,1],[0,1]])
    
    w2=3
    result2_a = list([[0,0],[0,1]])
    result2_b = list([[0,1],[0,0]])

    print(list(minimal_size_abacus(w1))==result1)
    print(list(minimal_size_abacus(w2))==result2_a or list(minimal_size_abacus(w2))==result2_b)





