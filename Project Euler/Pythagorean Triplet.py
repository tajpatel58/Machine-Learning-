
import math
for a in range(1,1000):
    for b in range(1,1000):
        c = a**2+b**2
        d = math.sqrt(c)
        e= [0]*3
        if b>a and d==int(d) and a+b+d==1000:
            print(a)
            print(b)
            print(d)
            print(a*b*d)
            break
        else:
            continue
