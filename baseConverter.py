def baseSystemToN(decimal,destSymbols):    
    base = len(destSymbols)
    num = []
    while True:
        q = decimal//base
        r = decimal % base
        num.append(r)
        decimal = q
        if q < base:
            num.append(q)
            break
    return ''.join([destSymbols[x] for x in num[::-1]])

def toSystemBase(s,sourceSymbols):
    base = len(sourceSymbols)   
    result = 0
    for i,j in enumerate(s[::-1]):
        result += sourceSymbols.index(j)*pow(base,i)
    return result

def baseXtoY(source,sourceSymbols,destSymbols):
    return baseSystemToN(
             toSystemBase(source,sourceSymbols),
             destSymbols )
