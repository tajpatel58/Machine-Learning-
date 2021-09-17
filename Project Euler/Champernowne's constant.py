print(210)


# q=['1']
# for k in range(2,203000):
#     c = list(str(k))
#     q = q +c
#
# print(int(q[0])*int(q[9])*int(q[99])*int(q[999])*int(q[9999])*int(q[99999])*int(q[999999]))
# print(len(q))
# w= ''.join(q)

def nthdigit(n):
    a=[0]*10000000
    j=1
    for k in range(0, len(a)):
        a[k]=j
        j += 1
    q = [0]
    i=2
    while(n>len(q)):
        b = q
        q = q + a[i]
        i = i+1

    e = n - len(b)
    r = list(str(a[i-1]))
    print(r[e-1])

nthdigit(8)
