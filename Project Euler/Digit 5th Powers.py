sum=0
for k in range(2,1000000):
    b = list(str(k))
    sumK=0
    for i in range(0,len(b)):
        sumK = sumK + int(b[i])**4
    if k==sumK:
        sum = sum + k # sum is the sum of all numbers who can be written as the sum of the powers of its digits.

    else:
        continue

print(sum)