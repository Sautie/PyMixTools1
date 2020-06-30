
import numpy as np

def Merge(Tab_merged, Sub_Tab_merged1, Sub_Tab_merged2, Sub_Tab_merged3, Sub_Tab_merged4 ) :

    n_merged1 = len(Sub_Tab_merged1)
    n_merged2 = len(Sub_Tab_merged2)
    n_merged3 = len(Sub_Tab_merged3)
    n_merged4 = len(Sub_Tab_merged4)
    
    first_Tab_merged = list(range(n_merged1+n_merged2))
    seconde_Tab_merged= list(range(n_merged3+n_merged4))

    i=0
    j=0
    k=0

    while(i < n_merged1 and j < n_merged2):
        if( Sub_Tab_merged1[i] <= Sub_Tab_merged2[j]):
        
            first_Tab_merged[k] = Sub_Tab_merged1[i] 
            k = k+1
            i = i+1
            
        else:
            first_Tab_merged[k] = Sub_Tab_merged2[j]
            k = k+1
            j = j+1         
         
     while(i < n_merged1):
        first_Tab_merged[k] = Sub_Tab_merged1[i]
        k = k+1
        i = i+1
    
    while(j < n_merged2):
        first_Tab_merged[k] = Sub_Tab_merged2[j]
        k = k+1
        j = j+1
        
    i=0
    j=0
    k=0
###############################################################################3

    while(i < n_merged3 and j < n_merged4):
        if( Sub_Tab_merged3[i] <= Sub_Tab_merged4[j]):
            seconde_Tab_merged[k] = Sub_Tab_merged3[i] 
            i = i+1
            k = k+1
        else:
            seconde_Tab_merged[k] = Sub_Tab_merged4[j]
            j = j+1 
            k = k+1
         
    while(i < n_merged3):
        seconde_Tab_merged[k] = Sub_Tab_merged3[i]
        k = k+1
        i = i+1
    
    while(j < n_merged4):
        seconde_Tab_merged[k] = Sub_Tab_merged4[j]
        k = k+1
        j = j+1    
        
        
    i = 0
    j = 0
    k = 0
##############################################################################     

    while(i < len(first_Tab_merged) and j < len(seconde_Tab_merged)):
             
        if( first_Tab_merged[i] <= seconde_Tab_merged[j]):

            Tab_merged[k] = first_Tab_merged[i] 
            k = k+1
            i = i+1
        else:
            Tab_merged[k] = seconde_Tab_merged[j]
            k = k+1
            j = j+1
            

    while(i < len(first_Tab_merged)):
        Tab_merged[k] = first_Tab_merged[i]
        k = k+1
        i = i+1
    
    while(j < len(seconde_Tab_merged)):
        Tab_merged[k] = seconde_Tab_merged[j]
        k = k+1
        j = j+1  
    
def mergesort4(tab, n):
    x = []
    if(type(tab) != type(x)):
        tab = tab.tolist()
    
    if( n < 2 ): 
        return tab
        
        
    if( n == 2):
        if(tab[1]<tab[0]):
            tempo = tab[0]
            tab[0] = tab[1]
            tab[1] = tempo 
        return tab
            
    if( n == 3 ):
        if(tab[0] > tab[1]):     
            tempo = tab[0]       
            tab[0] = tab[1]      
            tab[1] = tempo          
        if(tab[1] > tab[2]):       
            tempo = tab[1]       
            tab[1] = tab[2]      
            tab[2] = tempo        
        
        if(tab[0] > tab[1]):       
            tempo = tab[0]
            tab[0] = tab[1]
            tab[1] = tempo 
        return tab

 
    #sinon on divise en 4 
    if( n > 3 ):
        mid =  n // 2           
        quart = n //4
        
        Sub_tab1 = tab[0:quart]
        Sub_tab2 = tab[quart:mid]
        Sub_tab3 = tab[mid:(quart+mid)]
        Sub_tab4 = tab[(quart+mid):n]

        mergesort4(Sub_tab1, len(Sub_tab1))
        mergesort4(Sub_tab2, len(Sub_tab2))
        mergesort4(Sub_tab3, len(Sub_tab3))
        mergesort4(Sub_tab4, len(Sub_tab4))
        Merge(tab, Sub_tab1, Sub_tab2, Sub_tab3, Sub_tab4 ) 
        return tab  

# playing with mergesort
if __name__=="__main__":

    A = [56, 4]
    print("Array : ", A)
    test1 = mergesort4(A, len(A)) == sorted(A)
    print("correctly sorted?", test1)

    B = np.random.randint(low = 0, high = 100, size = (20))
    print("Array : ", B)
    test2 = mergesort4(B, len(B)) == sorted(B)
    print("correctly sorted?", test2)

    print("Votre note serait =", np.mean([test1, test2])*100, "%" )
    
    
    
    
    
    
    
