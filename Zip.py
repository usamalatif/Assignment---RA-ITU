def Zip(Array1,Array2):
    List = []
    if (len(Array1)>0 and len(Array2)>0):
        a=0
        if(len(Array2)>len(Array1) or len(Array2)==len(Array1)):
            
            
            while(a<len(Array1)):
                List.append((Array1[a], Array2[a]))
                a = a+1
        elif (len(Array2)<len(Array1)):
            
            while(a<len(Array2)):
                List.append((Array1[a],Array2[a]))
                a = a+1
    return List

a = Zip([1],[1,1,1,1])           
print a           
        
