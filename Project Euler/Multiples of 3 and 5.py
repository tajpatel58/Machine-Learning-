import math
def multiples3and5():
    c = list(range(1,1000))
    a = []
    for i in c:
        n = i/3
        k = i/5
        if int(n)==n or int(k)==k:
            a.append(i)
        else:
            continue
    total=0
    for e in a:
        total = e + total
    print(total)

multiples3and5()