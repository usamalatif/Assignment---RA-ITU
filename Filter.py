def CheckingPositiveValues(x):
    if(x>0):
        return x
    


def Filter(function,Array):
    result = []
    for i in Array:
        result.append(function(i))
    

    return [i for i in result if i is not None] #To Control None Values

Array = [-1,1,2,3,-3,-5,-10,10,11]

a = Filter(CheckingPositiveValues,Array)
print a
