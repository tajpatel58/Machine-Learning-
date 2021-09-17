
# Our goal is to find the last 10 digits of 1^1 + 2^2 + .... + 1000^1000

SUM = 0
for k in range(1, 1000):
    SUM = SUM + k**k

b = []
a = list(str(SUM))
for j in range(len(a)-10,len(a)) :
    b.append(a[j])

c = ''.join(b)
print(c)
print(len(b))
