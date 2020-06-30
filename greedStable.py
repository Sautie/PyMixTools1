import graphM
#Miguel Sautie Castellanos
#algorithme vorace pour resoudre le probleme du Stable (trouver le stable de taille maximale)
def IsEdge(Mat,i,j):
    return Mat[i][j] == 1

def Degree(Mat,i):
    d=0;
    for j in range(len(Mat[i])):
        d=d+Mat[i][j]
    return d

def DegreesR(Mat):
    rows = len(Mat)
    degrees = []
    for i in range(rows):
        degrees.append(Degree(Mat,i))
    pos = []
    pos=sorted(range(len(degrees)), key=lambda k: degrees[k])
    degrees.sort()
    return pos,degrees

def delRows(matrix, i):
    del(matrix[i])
    return matrix

def delCols(matrix, j):
    del(matrix[0][j])
    return matrix   
            
def neighbours(matrix, p):
    c=0
    Nindex=[]    
    for j in range(len(matrix[p])):
        if (matrix[p][j]==1):
            c=c+1;
            Nindex.append(j)
    return Nindex,c

def proNeigh(matrix, i, j):
    j+=1
    if (len(matrix)>i):
        while (j<len(matrix[i])):
            if (matrix[i][j]==1):            
                return j
            j+=1
    j=-2
    return j

##################

def delSommet(matrix,degrees,pos,names,k=0):
    a=-1
    b=-1
    sommet=-1
    u=pos[k]
    if (len(matrix)>u):
        matrix=delRows(matrix, pos[k])       
        matrix=delCols(matrix, pos[k])
    y=0            
    while(y<len(pos)):
        if (pos[y]>pos[k]):
            pos[y]-=1
        y+=1
    sommet=names.pop(k)   
    a=pos.pop(k)
    b=degrees.pop(k)        
    return a,b,sommet,matrix,degrees,pos,names

def delNeigb(matrix,degrees,pos,names,i=0):   ## dans le tableau 2d Matrix, elimine les voisins du sommet i ## better with a heap
    p=0
    p=proNeigh(matrix,pos[i],p)
    lm=len(matrix)    
    while ((p>=0)and(p<len(matrix))):
        matrix=delRows(matrix, p)  
        kk=0
        #print(p)
        while ((kk<len(pos))and(pos[kk]!=p)):
            kk+=1
        if ((kk<len(pos))and (pos[kk]==p)):
            del(degrees[kk])
            del(names[kk])            
            y=0            
            while(y<len(pos)):
                if (pos[y]>pos[kk]):
                    pos[y]=pos[y]-1                
                y+=1
            del(pos[kk])
            print(len(pos))
            print(kk)
        if(p>=0):
            matrix=delCols(matrix, p)
        lm=len(matrix)
##        print(pos[i])        
        p=proNeigh(matrix,pos[i],p)       
    return matrix,degrees,pos,names



############## main program
u=0
matrix=graphM.M
(pos,degrees)=DegreesR(matrix)
names=pos
(Nindex,c)=neighbours(matrix,pos[0])
uu=0
Lp=len(pos)
stable=[]
r=0
a=1
while (len(pos)>0):    
    (matrix,degrees,pos, names)=delNeigb(matrix,degrees,pos,names,uu)
    if (len(pos)>0):   
        (a,b,sommet,matrix,degrees,pos, names)=delSommet(matrix,degrees,pos,names,uu)
        if (a>0):
            stable.append(sommet)
       # stable.append(b)
    r+=1     
    print(len(pos))

print(stable)




