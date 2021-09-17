


def palindromicTest(a):
    c = list(str(a))
    d = ['']*len(c)
    for k in range(0,len(c)):
        d[k]= c[len(c)-1-k]
    q = ''.join(d)
    if a - int(q)==0:
        return 1        # 1 Indicates a palindromic Number
    else:
        return 0 # 0 indicates a non palindromic number.

print(bin(585))

def remprefix(a):
    c = list(str(a))
    del(c[0])
    del(c[0])
    d = ''.join(c)
    return int(d)

SUM=0

for k in range(1,1000000):
    a = bin(k)
    b = remprefix(a)
    if palindromicTest(k)==1 and palindromicTest(b)==1:
        print(k)
        print(b)
        print(a)
        SUM+=k
    else:
        continue

print(SUM)


