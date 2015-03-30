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


# default symbols sequence 
# listing symbols by extending hex symbols sequence, base 1 to base 36
default_symbols_seq = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = [ x for x in default_symbols_seq ]

def convertBase(inputNum, frm, to):
    return baseXtoY(inputNum, d[:frm], d[:to])

print( convertBase("2310",frm = 10, to =16))
"""
# Examples

base10 = ['0','1','2','3','4','5','6','7','8','9']

base26 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print( baseXtoY( '12314123',
                 inputBaseSymbols = base10 ,
                 outputBaseSymbols = base26) )

"""
