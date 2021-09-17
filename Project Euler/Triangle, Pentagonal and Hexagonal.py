
# This function will return an array of triangle numbers whose index is less than or equal to n
def triangle(n):
    a = [0]*n
    for k in range(1,n+1):
        a[k-1] = int(k*(k+1)*0.5)
    return a

def pentagonal(n):
    a = [0]*n
    for k in range(1,n+1):
        a[k-1] = int(k*(3*k - 1)*0.5)
    return a


def hexagonal(n):
    a = [0]*n
    for k in range(1,n+1):
        a[k-1] = int(k*(2*k - 1))
    return a

a = triangle(100000)
b = pentagonal(100000)
c = hexagonal(100000)

t=0
for k in a:
    if k in b and k in c:
        t = t +1
        if t==3:
            print(k)
            break
        else:
            continue

