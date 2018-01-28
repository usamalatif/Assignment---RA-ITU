def Sqr (x):
    return x*x

def Map(function,Array):
    result = []
    for i in Array:
        result.append(function(i))
    return result


Array = [1,2,3,4,5,6,7]

a = Map(Sqr,Array)
print (a)
