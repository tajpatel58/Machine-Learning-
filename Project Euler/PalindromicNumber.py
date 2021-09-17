import math

def palindromicNumber():
    MAXPALINDROMIC =0
    for i in range(100,1000):
        for j in range(100,1000):
            d = i*j
            c = list(str(d))
            p = ['']*len(c)
            for k in range(0,len(c)):
                p[k]=c[len(c)-1-k]
            y = ''.join(c)
            z = ''.join(p)
            if int(y)-int(z)==0 and d >= MAXPALINDROMIC:
                MAXPALINDROMIC = d
    print(MAXPALINDROMIC)
palindromicNumber()
