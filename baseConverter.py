def baseSystemTobaseN(n,outputBaseSymbols):    
    base = len(outputBaseSymbols)
    num = []
    while True:
        q = n//base
        r = n % base
        num.append(r)
        n = q
        if q < base:
            num.append(q)
            break
    return ''.join([outputBaseSymbols[x] for x in num[::-1]])

def toSystemBase(s,inputBaseSymbols):
    base = len(inputBaseSymbols)   
    result = 0
    for i,j in enumerate(s[::-1]):
        result += inputBaseSymbols.index(j)*pow(base,i)
    return result

def baseXtoY(source,inputBaseSymbols,outputBaseSymbols):
    return baseSystemTobaseN(
             toSystemBase(source,inputBaseSymbols),
             outputBaseSymbols )

