def fibonacci():
    f=[1,2]
    i=1
    while f[i]<4000000:
        d= f[i]+f[i-1]
        if d<4000000:
            f.append(d)
            i=i+1
        else:
            break
    return f

w = fibonacci()

def sumEvenArray(q):
    l=len(q)
    total =0
    for i in list(range(1,l)):
        d = q[i]/2
        if int(d)==d:
            total = total + q[i]
        else:
            continue
    return total

print(sumEvenArray(w))