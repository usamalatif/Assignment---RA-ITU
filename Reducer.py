def ProductOfList(previousValue,newValue):
    return previousValue*newValue

def Reducer(function,Array):
    result = 1
    for i in Array:
        result = function(result,i)
    return result


Array = [1,2,3,4,5]


prod = Reducer(ProductOfList,Array)
print (prod)        
