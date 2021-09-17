
with open('words.txt') as f:
    a = f.read()

a = a.replace('"','')
a = a.split(',')

def enum(n):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k = list(n)
    p = len(k)
    w = [0]*p
    for i in range(0,len(k)):
        t=0
        for s in alphabet:
            t = t+1
            if k[i]==s:
                w[i]= t
            else:
                continue
    SUM=0
    for r in range(0,len(w)):
        SUM = SUM + w[r]
    return SUM

# This function will return the array of triangle numbers of size n.
def trianglenumber(n):
    b = [0]*n
    for k in range(1,n+1):
        b[k-1]= int(0.5*k*(k+1))
    return b

y = [0]*1786   # We create an array to store the enumerated values of the words in the words file. NOTE: 1786 is the size of the file.
for j in range(0,len(a)):
    p = enum(a[j])
    y[j] = p

# We create an array size max(y) si that every enumerated value will be less than the max(c)
c = trianglenumber(max(y))

t=0
for k in range(0,len(y)):
    if y[k] in c:
        t = t + 1
        print(y[k])
    else:
        continue
print(c)
print(t)
