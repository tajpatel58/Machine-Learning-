
for k in range(10,100):
    for j in range(k+1,100):
        a = list(str(k))
        b = list(str(j))
        q= k/j
        c = int(a[0])
        d = int(a[1])
        e = int(b[0])
        f = int(b[1])
        if c!=0 and d!=0 and e!=0 and f!=0:
            if c == e and d/f==q:
                print(k)
                print(j)
            if c == f and d/e==q:
                print(k)
                print(j)
            if d == e and c/f==q:
                print(k)
                print(j)
            if  d == f and c/e==q:
                print(k)
                print(j)
        else:
            continue


