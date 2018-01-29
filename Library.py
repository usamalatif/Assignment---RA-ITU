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

def Reducer(function,Array):
    result = 1
    for i in Array:
        result = function(result,i)
    return result
def Filter(function,Array):
    result = []
    for i in Array:
        result.append(function(i))
    

    return [i for i in result if i is not None] #To Control None Values
def ForEach(Function,Array):
    for i in Array:
        Function(i)
    return True
def Map(function,Array):
    result = []
    for i in Array:
        result.append(function(i))
    return result
