## Miguel Sautie-Castellanos
##  2 fonctions:  1) CombPanorama et 2) pannix
## 1)CombPanorama, fonction qui combine un panL et un panR en un pan respectant les blocs de L
## et les blocs de R. 
## 2) pannix: à partir de l'ensemble E de n blocs construit le pan, c'est-a-dire la silhouette
## de surface minimale. Fonction qu'utilise dedans la Méthode combPanorama,
##et l'approche "diviser pour régner". Etapes, 1) décompose recursivement
## une séquence de blocs non-juxtaposés en instances plus petites (jusqu'aux blocs isolés),
## 2) fusionne d'abord les blocs isoles et après, des pans de plus en plus longues
## pannix ( complexite en temps de l'ordre de N Log(N))
## entrée: ensemble de blocs [[8, 3, 16],[2, 3, 6],[8, 5, 11],[25, 2, 125],[14, 3, 18],[7, 6, 10],[14, 1, 30]]
## sortie: pan [[2, 3, 6], [6, 0, 7], [7, 6, 10], [10, 5, 11], [11, 3, 18], [18, 1, 25], [25, 2, 125]]

def CombPanorama(panL, panR):
 ##fonction lineaire pour combiner deux pans (panL, panRa) en un pan. 
    
 ## entree:panR=[[2, 3, 6]],panL=[[8, 5, 11]]
 ## sortie: pan,[[2, 3, 6], [6, 0, 8], [8, 5, 11]]
    
 ## entree:panR=[[4, 70, 6]],panL=[[3, 5, 11]]
 ## sortie:pan, [[3, 5, 4], [4, 70, 6], [6, 5, 11]]

 ##panR=[[14, 3, 18], [18, 0, 25], [25, 2, 125]]
 ##panL= [[7, 6, 10], [10, 0, 14], [14, 1, 30]]
 ## sortie:pan, [[7, 6, 10], [10, 0, 14], [14, 3, 18], [18, 1, 25], [25, 2, 125]]    
    pan=[] 
    i=j=p=f=0
    ########## boucle 1 pour combiner  panL et panR
    while ((i < len(panL))and(j<len(panR))):
        triple=[]        
        if(panL[i][2]<=panR[j][0]):
            if (panL[i][2]!=panR[j][0]):  #
                pan.append(panL[i])
                p+=1
                triple.append(panL[i][2]),triple.append(0),triple.append(panR[j][0])
                pan.append(triple)
                p+=1
            i+=1
        elif(panL[i][0]>=panR[j][2]):                            
            if (panL[i][0]!=panR[j][2]):
                pan.append(panR[j])
                p+=1
                triple.append(panR[j][2]),triple.append(0),triple.append(panL[i][0])
                pan.append(triple)
                p+=1               
            j+=1
        elif (panL[i][2]<panR[j][2])and (panL[i][2]>panR[j][0])and(panL[i][0]<panR[j][0]): 
            if (panL[i][1]<panR[j][1]):                
                if (p==0):
                    print(i)
                    triple.append(panL[i][0]),triple.append(panL[i][1]),triple.append(panR[j][0])
                    pan.append(triple)
                    p+=1
                    triple=[]
                    triple.append(panR[j][0]),triple.append(panR[j][1]),triple.append(panL[i][2])
                    pan.append(triple)
                    p+=1
                else:
                    triple.append(panR[j][0]),triple.append(panR[j][1]),triple.append(panL[i][2])
                    pan.append(triple)
                    p+=1                
            else:
                if (p>0):
                    if(pan[p-1][1]==panL[i][1]):
                        pan[p-1][2]=panL[i][2]
                    else:
                        triple.append(panR[j][0]),triple.append(panL[i][1]),triple.append(panL[i][2])                        
                        pan.append(triple)
                        p+=1 
                else:
                    pan.append(panL[i])
                    p+=1
            i+=1 
        elif (panL[i][2]<=panR[j][2])and (panL[i][0]>=panR[j][0]):            
            if (panL[i][1]<=panR[j][1]):
                if (p==0):
                    triple.append(panR[j][0]),triple.append(panR[j][1]),triple.append(panL[i][2]) 
                    pan.append(triple)                    
                    p+=1 
                else:
                    if(pan[p-1][1]==panR[j][1]):
                        pan[p-1][2]=panL[i][2]
                    else:
                        triple.append(panL[i][0]),triple.append(panR[j][1]),triple.append(panL[i][2]) 
                        pan.append(triple)                        
                        p+=1
            else:
                if (p==0)and(panL[i][0]!=panR[j][0]):
                    triple.append(panR[j][0]),triple.append(panR[j][1]),triple.append(panL[i][0]) 
                    pan.append(triple)
                    p+=1
                if(p>0)and(pan[p-1][1]==panL[i][1]):
                    pan[p-1][2]=panL[i][2]
                else:
                    pan.append(panL[i])
                    p+=1          
            if (panL[i][2]==panR[j][2]):
                i+=1
                j+=1            
            else:
                i+=1
        elif (panL[i][2]>panR[j][2])and (panL[i][0]<panR[j][2])and(panL[i][0]>panR[j][0]):
            if (panL[i][1]<panR[j][1]):
                if (p==0):
                    pan.append(panR[j])
                    p+=1 
                elif (p>0):
                    if(pan[p-1][1]==panR[j][1]):
                        pan[p-1][2]=panR[j][2]
                    else:
                        triple.append(panL[i][0]),triple.append(panR[j][1]),triple.append(panR[j][2]) 
                        pan.append(triple)
                        p+=1
            else:
                if (p==0):
                    triple.append(panR[j][0]),triple.append(panR[j][1]),triple.append(panL[i][0]) 
                    pan.append(triple)
                    p+=1
                    triple=[] 
                    triple.append(panL[i][0]),triple.append(panL[i][1]),triple.append(panR[j][2]) 
                    pan.append(triple)
                    p+=1                    
                else:
                    triple.append(panL[i][0]),triple.append(panL[i][1]),triple.append(panR[j][2])
                    pan.append(triple)
                    p+=1
            j+=1
        elif (panL[i][2]>=panR[j][2])and (panL[i][0]<=panR[j][0]):
            if (panL[i][1]<=panR[j][1]):
                if (p==0)and(panL[i][0]!=panR[j][0]):
                    triple.append(panL[i][0]),triple.append(panL[i][1]),triple.append(panR[j][0]) 
                    pan.append(triple)
                    p+=1
                if(p>0)and(pan[p-1][1]==panR[j][1]):
                    pan[p-1][2]=panR[j][2]
                else:
                    pan.append(panR[j])
                    p+=1
            else:
                if (p==0):
                    triple.append(panL[i][0]),triple.append(panL[i][1]),triple.append(panR[j][2]) 
                    pan.append(triple)
                    p+=1
                else:
                    if(pan[p-1][1]==panL[i][1]):
                        pan[p-1][2]=panR[j][2]
                    else:
                        triple.append(panR[j][0]),triple.append(panL[i][1]), triple.append(panR[j][2])
                        pan.append(triple)
                        p+=1
            if (panL[i][2]==panR[j][2]):
                i+=1
                j+=1            
            else:
                j+=1              
 ########## boucle 2  pour rajouter les blocs restants du panR                  
    while (j<len(panR)):
        triple=[]  
        if(pan[p-1][2]==panR[j][0]):
            pan.append(panR[j])
            p+=1            
        elif (panL[i-1][2]<panR[j][2])and(f==0):
            if(panL[i-1][1]<=panR[j][1]):
                pan[p-1][2]=panR[j][2]
            else:
                triple.append(panL[i-1][2]),triple.append(panR[j][1]),triple.append(panR[j][2]) 
                pan.append(triple)
                p+=1            
            f=1
        j+=1            
   ######### boucle 3   pour rajouter les blocs restants du panL  
    while (i<len(panL)):
        triple=[]  
        if(pan[p-1][2]==panL[i][0]):
            pan.append(panL[i])
            p+=1
        elif (panR[j-1][2]<panL[i][2])and(f==0):
            if(panR[j-1][1]<=panL[i][1]):
                pan[p-1][2]=panL[i][2]
            else:
                triple.append(panR[j-1][2]),triple.append(panL[i][1]),triple.append(panL[i][2]) 
                pan.append(triple)
                p+=1 
            f=1
        i+=1
    
        
    return pan

###############  fonction pannix ################
##Fonction qu'utilise dedans la Méthode combPanorama,
##et l'approche "diviser pour régner". Etapes, 1) décompose recursivement
## une séquence de blocs non-juxtaposés en instances plus petites (jusqu'aux blocs isolés),
## 2) fusionne d'abord les blocs isolés et après, des pans de plus en plus longues
## pannix ( complexite en temps de l'ordre de N Log(N))
## entrée: ensemble de blocs [[8, 3, 16],[2, 3, 6],[8, 5, 11],[25, 2, 125],[14, 3, 18],[7, 6, 10],[14, 1, 30]]
## sortie: pan [[2, 3, 6], [6, 0, 7], [7, 6, 10], [10, 5, 11], [11, 3, 18], [18, 1, 25], [25, 2, 125]]

def pannix(pan):
    if pan is None:
        return None
    if len(pan) < 2: return pan 
    panL=pan[ : (len(pan) // 2)]
    panR=pan[(len(pan) // 2) :]    
    return CombPanorama(pannix(panL), pannix(panR))

###############  fonction main ################

pan=[[8, 3, 16],[2, 3, 6],[8, 5, 11],[25, 2, 125],[14, 3, 18],[7, 6, 10],[14, 1, 30]]     
print(pannix(pan))

##panR=[[2, 3, 6]]
##panL=[[8, 5, 11]]
##print(CombPanorama(panL, panR))

##panR=[[4, 70, 6]]
##panL=[[3, 5, 11]]
##print(CombPanorama(panL, panR))

##panR=[[14, 3, 18], [18, 0, 25], [25, 2, 125]]
##panL= [[7, 6, 10], [10, 0, 14], [14,▲ 1, 30]]
##print(CombPanorama(panL, panR))

 
##panR=[[5, 8, 56],[56, 8, 100],[100, 89, 167]] 
##panL= [[2, 3, 6], [6, 0, 8], [8, 5, 11], [11, 3, 16]]
##panR= [[7, 6, 10], [10, 0, 14], [14, 3, 18], [18, 1, 25], [25, 2, 125]]

 
