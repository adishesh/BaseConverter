mapping = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#mapping = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#mapping = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

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

base2_symbols = ['0','1']
base10_symbols = ['0','1','2','3','4','5','6','7','8','9']

print(baseXtoY('1111011',sourceSymbols = base2_symbols, destSymbols = base10_symbols))
