
def ifPandigital(a):
    c = list(str(a))
    for j in range(1,10):
        e = str(j)
        if e in c:
            c.remove(e)
        else:
            break
    if len(c)==0:
        return 1 # 1 Implies we have a pandigital number
    else:
        return 0

MAX=0
NUM=0
for k in range(1,10000):
    t=1
    y=0
    b = list(str(k))
    while(y!=1):
        if len(b)<9:
            t=t+1
            e = list(str(k*t))
            b = b + e
        elif len(b)==9:
            q = ''.join(b)
            w = int(q)
            if ifPandigital(w)==1:
                if w>MAX:
                    MAX=w
                    NUM=k
                    y=1
                else:
                    y=1

            else:
                y=1
        else:
            y=1

print(MAX)
print(NUM)

