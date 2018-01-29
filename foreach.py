def Sqr (x):
    return x*x

def ForEach(Function,Array):
    for i in Array:
        Function(i)
    return True



ForEach(Sqr,[1,2,3])
