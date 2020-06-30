# -*- coding: utf-8 -*-
import time
from exemplaires import*

##Miguel Sautié-Castellanos
###########################################################################
##La méthode permuta2(k, p, p1, p2) est l'implementation d'un algorithme naïf pour 
##determiner l'appartennance de la permutation p au groupe de permutations généré par p1 et p2
##(et l'operation de multiplication) avec le nombre maximal de multiplications pre-fixé (k).
##Cette méthode utilise dedans les 3 méthodes suivantes: validPerm(p), product(p, q),
##permProducts(alpha, size). 3 sorties: Erreur, True and False,

##exemple :
##entrée:
##  print(permuta2(k1, p1, p11, p21))
##  print(permuta2(k2, p2, p12, p22))
##  print(permuta2(k3, p3, p13, p23))
##  print(permuta2(k4, p4, p14, p24))
##sortie
##  False
##  True
##  Erreur: une donnée n'est pas une permutation
##  True
##pour permuta2(k5, p5, p15, p25),permuta2(k5, p5, p15, p25))
##permuta2(k5, p5, p15, p25):on obtient erreur de memoire

###########################################################################

def product(p, q):  
    return tuple([q[p[i]-1] for i in range(len(p))])

## Méthode auxiliare booléen pour determiner si une liste de nombres est une permutation ou pas
## critère: la présence d'au moins deux éléments répétés
def validPerm(p):
    lp=len(p)
    for x in range(0, lp):
        for y in range(x+1,lp):
            if (p[x]==p[y]):
                return False
    return True

##Méthode auxiliare pour générer une liste de tous les mots possibles de taille (size) à partir
##de l'alphabet(alpha),chaque mot sera utilisé par la méthode permuta2 comme guide 
##pour calculer les produits entre les permutations,
##par exemple [1,1,2,2],indique l'ordre suivant des multiplications entre p1 et p2: p1*p1*p2*p2

def permProducts(alpha, size):
    pfin = [[L] for L in alpha[:]]
    if size == 1:
        return pfin
    for l in range(1, size):
        pfin = [[p]+pp for p in alpha for pp in pfin]
    return pfin

##La méthode booléen permuta2 a 3 sorties: Erreur, True and False; 
def permuta2(k, p, p1, p2):    
    f=0
    comp2=1
    if (not(validPerm(p)))or(not(validPerm(p1)))or(not(validPerm(p2))):         
        return "Erreur : une donnee n'est pas une permutation"  
    while (comp2<k):
        comp1=0
        Lperms=permProducts([1,2],comp2)##Lperms: contient tous les produits de comp2 permutations        
        while (comp1<len(Lperms)):      ##exemple:[[1,1,2],..:p1*p1*p2,.. pour comp2=3
            pi=list(range(1,len(p)+1)) 
            comp=0
            while (comp<comp2):
                if (Lperms[comp1][comp]==1):
                    pi=product(pi,p1) 
                else:
                    pi=product(pi,p2)
                if (pi==p):
                    return True                    
                comp=comp+1 ## variable compteur pour parcourir toutes les permutations p1 et p2
            comp1=comp1+1   ##variable compteur pour parcourir tous les produits de permutations,   
        comp2=comp2+1       ## nombre de permutations à multiplier (1...k)
    return False

   
################### main function #############################

##print(permuta2(k1, p1, p11, p21))
##print(permuta2(k2, p2, p12, p22))
##print(permuta2(k3, p3, p13, p23))
##print(permuta2(k4, p4, p14, p24))

##print(permuta2(k5, p5, p15, p25))
##print(permuta2(k6, p6, p16, p26))
##print(permuta2(k7, p7, p17, p27))
pi=tuple(range(1,len(p1)+1))
pp=product(pi, p11)
print(p11) 
print(pp)
print(pi)

p = tuple([3,2, 4, 5, 1])
pp=tuple([2,1,4,3,5])
ppp=tuple([2,3,4,5,1])
print(permuta2(18, p, pp, ppp))




###############################################################

##permuta2a: autre Méthode pour determiner
##l'appartennance de la permutation p au groupe de permutations généré par p1 et p2
##(et l'operation de multiplication) avec le nombre maximal de multiplications pre-fixé (k)
##trace d'exécution:

##entrée:
##  permuta2a(k1, p1, p11, p21)
##  permuta2a(k2, p2, p12, p22)
##  permuta2a(k3, p3, p13, p23)
##  permuta2a(k4, p4, p14, p24)
##Sortie:
##  False
##  True
##  Erreur: une donnée n'est pas une permutation
##  True

##def puis2(l):  
##    i=0
##    p=1
##    while (i<l):
##        p=p*2
##        i=i+1
##    return p
##
##def permuta2a(k, p, p1, p2):    
##    q=ll=f=0
##    if (not(validPerm(p)))or(not(validPerm(p1)))or(not(validPerm(p2))):
##        print("Erreur: une donnée n'est pas une permutation")
##        return
##    l=0    
##    ls=list()
##    while (l<k):    ##l=1 
##        ll=puis2(l+1)
##        f=0
##        if (ll==2):
##            if (p==p1)or(p==p2):
##                print(True)
##                return 
##            ls.append(p1)
##            ls.append(p2)
##            lla=ll
##        else:
##            lsAux=[]            
##            while (f<lla):
##                p11=product(ls[f],p1)            
##                p22=product(ls[f],p2)               
##                if (p==p11)or(p==p22):
##                    print(True)
##                    return                   
##                lsAux.append(p11)
##                lsAux.append(p22)                
##                f=f+1
##        if (ll>2):
##            ls=[]
##            ls=lsAux
##            lsAux=[]
##        lla=ll
##        l=l+1
##    print(False)
##    return


##start_time = time.time()
##permuta2a(k1, p1, p11, p21)
##permuta2a(k2, p2, p12, p22)
##permuta2a(k3, p3, p13, p23)
##permuta2a(k4, p4, p14, p24)
##print("--- %s seconds ---" % (time.time() - start_time))
