# SPlit turns string into a list after removing the element of choice, strip just removes and leaves a string.
# You can sort a list where each element is a string if the ordering is trivial.
import time
start = time.time()

with open('names.txt') as f:
    a = f.read()

a = a.replace('"', '')
a = a.split(',')
a.sort()

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

SUM = 0
for i in range(0,len(a)):
    p = enum(a[i])
    SUM = SUM + p*(i+1)

print(SUM)



end = time.time()
print(end-start)