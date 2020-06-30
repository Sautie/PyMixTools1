#Miguel Sautié-Castellanos,
#the main function for testing by backtracking if two matrices, mat1 and mat2, represent the same graph
#:MatIsom(v, t, f, mat2, mat1)
#OutIsomBacktracking(mat1,mat2): an output function

# MatIsom depends directly (and indirectly) on the following 8 functions: permatrix1, transpo,
#matmult, sdegrees, perma,ADja,ADsim, permuteMatrix

def permatrix1(y):   #function for generating a permutation matrix matper from the permutation y
    j=0
    matper=[]
    while (j<len(y)):            
        if ((y[j]<len(y))and(y[j]>1)):
            matper.append([0]*(y[j]-1)+[1]+[0]*(len(y)-y[j])) 
        elif (y[j]==len(y)):
            matper.append([0]*(y[j]-1)+[1])
        elif (y[j]==1):
            matper.append([1]+[0]*(len(y)-1))
        j+=1
    return matper

def transpo(matp):  # matrix transposition
    return list(map(list, zip(*matp)))    

def matmult(mat1, mat2):   # for matrix multiplication
    prod=[[0 for x in range(len(mat1))] for y in range(len(mat1))]
    i=j=k=0
    while (i<len(mat1)):
        j=0
        while (j<len(mat1)):
            k=0
            while (k<len(mat1)):
                prod[i][j]= prod[i][j]+(mat1[i][k]*mat2[k][j])
                k+=1
            j+=1
        i+=1
    return prod

def sdegres(mat1):   #for computing the degree sequence of the graph's vertices
    i=0
    sdegres=[0]*len(mat1)
    while (i < len(mat1)):
        j=0        
        while (j<len(mat1[0])):            
            sdegres[i]=sdegres[i]+mat1[i][j]
            j+=1
        i+=1
    return sdegres

def perma(mat1,mat2):      # for generating a list of consecutive numbers: represent the first permutation taken by MatIsom
    h=list(range(len(mat1)+1))     
    return h[1:len(mat1)+1]


def Adja(mat1, mat2, p): # function for testing if vertex p in mat1 and mat2 share the same neighbors 
    v1=mat1[p]
    v2=mat2[p]
    i=0 
    c=0
    while(i<len(mat1)):
        if (v2[i]==v1[i]):
            c+=1
        i+=1
    return c==len(mat1)

def ADsim(mat1, mat2): # function for testing if the vertices of mat1 and mat2 share the same neighbors 
    f=i=0
    while(f<len(mat1)):
        if (not(Adja(mat1, mat2, f))):
            return False
        f+=1
    return True

def permuteMatrix(mat1, y): #function for swapping rows and columns of the matrix mat1 with permutation matrices
    mp=permatrix1(y)
    tmp=transpo(mp)
    pro1=matmult(mp, mat1)
    pro2=matmult(pro1, tmp)
    return pro2
#################MatIsom: recursive function that determine by backtracking if two adjacency matrices
# mat1 and mat2 represent the same graph 
def MatIsom(v,t, f, mat2=None, mat1=None):  # permutation v, matrices mat1 and mat2, internal indexes t annd f for generating permutations
    if mat2 is None:
        mat2=[]  
    if mat1 is None:
        mat1=[]     
    if(t==f):
        pro=[]
        vs1=[]
        vs2=[]
        pro=permuteMatrix(mat1, v)
        vs2=sdegres(mat2)
        vs1=sdegres(pro)
        if (vs1==vs2):
            if (ADsim(pro, mat2)):              
                return True       
    else:
        i=t
        while (i<f+1):
            v[t],v[i] = v[i],v[t]
            if MatIsom(v, t+1, f, mat2, mat1)==True:
                return True
            v[t],v[i] = v[i],v[t]
            i+=1
        return False
######################### end of MatIsom ############    
def OutIsomBacktracking(mat1,mat2):  # output function for MatIsom
    if ((len(mat1)==len(mat2))and(len(mat1[0])==len(mat1))and(len(mat2[0])==len(mat2))):        
        v=perma(mat1,mat2)
        f=len(mat1)-1
        t=0
        if (mat1==mat2):
            print("You have introduced the same matrix")
        elif (MatIsom(v,t, f, mat2, mat1)):  #call of the function MatIsom for determining by backtracking whether both matrices represent the same graph or not
            print("A and B represent the same undirected graph")
        else:
            print("A and B do not represent the same undirected graph")
    else:
        print("Both matrices must be square and must have the same size")

 ###Main function##           
                
X = [[0,1,0,1],    #symmetric adjacency matrices for testing graph isomorphism, X and Y represent the same undirected graph
    [1,0,1,1],     # X,Y and Z do not represent the same undirected graph
    [0,1,0,0],
    [1,1,0,0]]

Y = [[0,0,1,1],
    [0,0,1,0],
    [1,1,0,1],
    [1,0,1,0]]

Z= [[0,1,0,1],
    [1,0,1,0],
    [0,1,0,0],
    [1,0,0,0]]




OutIsomBacktracking(X,Y)

