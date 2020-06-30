import exemplaires2
## Miguel, Sautié Castellanos
## méthode pour determiner si la fonction f appartient à l'ensemble de fonctions générées par s

def product(p, q):
    return tuple(q[p[i] - 1] for i in range(len(p)))

def composition2(s, f):    
   
    ## Ensemble initial si:  {(3, 1, 3, 4), (3, 4, 2, 1)}
    ## Fonction:  (1, 1, 1, 2)
    ## fonction composition2
    ## 0
    ## 1
    ## 2
    ## 3
    ## 4
    ## 5
    ## 6
    ## 7
    ## 8
    ## Réponse: TRUE; La fonction (1, 1, 1, 2) représent la composition des fonctions de l'ensemble s
    
    ls=list(s)
    c=0
    i=0
    w=0
    ww=0
    while (i<len(ls)): 
        ## boucle principale pour parcourir et ajouter les tuples
        if (ww<w):   ## if pour obtenir les derniers tuples ajoutés 
            i=0
            j=ww-1            
        else:
            j=i            
        ww=len(ls)
        while(j<len(ls)): 
           ## boucle interieur pour calculer la composition  
           ## entre les tuples et les ajouter à la ls/s
            pq=product(ls[i],ls[j])
            if (pq==f):    ## determine si f est généré    
                return (True, ls[:(i+j)])           
            else:                
                if(ls[i]!=ls[j]):  
                   ## commute les opérandes quand les tuples sont differents       
                    pq1=product(ls[j],ls[i])  ## composition des tuples
                    if (pq1==f):
                        return (True, ls[:(i+j)])
                    else:
                        s=set(ls)  ## conversion de set à list pour eviter tuples répétés 
                        ## ajoute le nouveau tuple obtenu par composition des opérands commutés
                        s.add(pq1)  
                s=set(ls)               
                s.add(pq)    ## ajoute le nouveau tuple obtenu par la composition des opérands         
                ls=list(s)
            j+=1  
        w=len(ls)        
        print(c)                       
        c+=1        ## variable compteur boucle principale
        i+=1
    return (False, ls[:(i+j)])

def pro(s1,f):         ## pro: fonction de sortie 
    print('\n',"Output: fonction composition2, compositionMiguelSautie.py, Miguel Sautié-Castellanos, devoir 1, ift 2125")
    print("Ensemble initial si: ", s1)
    print("Fonction: ", f)   
    (bo,s)=composition2(s1,f)    ## appel de la fonction composition2
    if (bo):        
        print("Réponse: TRUE; La fonction", f,"représent la composition des fonctions de l'ensemble s")      
    else:        
        print("Réponse: FALSE; La fonction", f,"ne représent pas la composition des fonctions de l'ensemble s")       
    return
 ## appels de la fonction de sortie pro (dedans se trouve la fonction composition2)

##pro(exemplaires.s1, exemplaires.f1)
##pro(exemplaires.s2, exemplaires.f2)
##pro(exemplaires.s3, exemplaires.f3)
##pro(exemplaires.s4, exemplaires.f4)
##pro(exemplaires.s5, exemplaires.f5)
pro(exemplaires.s6, exemplaires.f6)




## autres fonctions naïves de composition

##import random
##import datetime

##def sd(p, q):
##    
##    s = 0
##    lp=len(p)
##    for i, j in zip(p, q):
##        if i == j:
##            s += 1
##    return (s/lp)*100
##
##def search(auxr,pqr,pr,qr,j,ls,s,ds1,f):
##    boo=False
##    s=set(ls)
##    cc=0
##    while ((j+cc)<len(ls)):
##        if(auxr<ds1):
##            auxr=ds1
##            pr=pqr
##            pqr=product(qr,pr)
##            ds1=sd(pqr, f)           
##        else:
##            if ((j+cc)<len(ls)):
##                qr=ls[j+cc]
##            cc+=1
##        if (pqr==f):
##            boo=True
##            return (boo, s, cc)
##        else:                                
##            s.add(pqr)
##    return (boo, s, cc)

##def composition3v(s, f):
##    print('\n')
##    print("fonction composition3v")
##    ls=list(s)
##    c=0
##    aux=20.0  ## s1: 20.0  pour s1 s2 s3
##    p1=0.0
##    i=0
##    w=0
##    ww=0
##    while (i<len(ls)):
##        if (ww<w):
##            i=0
##            j=ww-1            
##        else:
##            j=i            
##        ww=len(ls)
##        while(j<len(ls)):
##            pq=product(ls[i],ls[j])
##            if (pq==f):
##                return (True, ls[:(i+j)])            
##            else:                
##                if(ls[i]!=ls[j]):
##                    pq1=product(ls[j],ls[i])
##                    ds1=sd(pq1, f)
##                    if (pq1==f):
##                        return (True, ls[:(i+j)])
##                    elif ((aux-ds1)<=p1):
##                        s=set(ls)
##                        (boo,s,cc)=search(aux,pq1,ls[i],ls[j],j,ls,s,ds1,f)
##                        if (boo):
##                            return (True,(ls[:(i+j+cc)]))                       
##                                                                       
##                ds=sd(pq, f)
##                if ((aux-ds)<=p1):
##                    s=set(ls)
##                    (boo,s,cc)=search(aux,pq,ls[i],ls[j],j,ls,s,ds,f)
##                    if (boo==True):
##                        return (True,(ls[:(i+j+cc)]))                 
##                ls=list(s)                
##            j+=1
##        w=len(ls) 
##        print(c)
##        c+=1
##        i+=1
##    return (False, ls[:(i+j)])
##
##def composition3R(s, f):
##    print('\n')
##    print("fonction composition3R")
##    ls=list(s)
##    c=0
##    aux=0.0  ## s1: 20.0  pour s1 s2 s3
##    p1=0.0
##    prob=0.70
##    i=0
##    w=0
##    ww=0
##    while (i<len(ls)):
##        if (ww<w):
##            i=0
##            j=ww-1            
##        else:
##            j=i            
##        ww=len(ls)
##        while(j<len(ls)):
##            pq=product(ls[i],ls[j])
##            random.seed(datetime.datetime.now())
##            r=random.random()           
##            if (pq==f):
##                return (True, ls[:(i+j)])            
##            else:                
##                if(ls[i]!=ls[j]):
##                    pq1=product(ls[j],ls[i])
##                    ds1=sd(pq1, f)
##                    if (pq1==f):
##                        return (True, ls[:(i+j)])
##                    elif ((r<prob)and (r>0.0)):
##                        if((aux-ds1)<p1):
##                            s=set(ls)
##                            (boo,s,cc)=search(aux,pq1,ls[i],ls[j],j,ls,s,ds1,f)
##                            if (boo):
##                                return (True,(ls[:(i+j+cc)])) 
##                    else:                    
##                        s=set(ls)
##                        s.add(pq1)
##                ds=sd(pq, f)
##                if ((r<prob)and (r>0.0)):                   
##                    if ((aux-ds)<p1):                        
##                        s=set(ls)
##                        (boo,s,cc)=search(aux,pq,ls[i],ls[j],j,ls,s,ds,f)
##                        if (boo):
##                            return (True,(ls[:(i+j+cc)])) 
##                else:
##                    s=set(ls)
##                    s.add(pq)
##                ls=list(s)                
##            j+=1
##        w=len(ls) 
##        print(c)
##        c+=1
##        i+=1
##    return (False, ls[:(i+j)])
##
