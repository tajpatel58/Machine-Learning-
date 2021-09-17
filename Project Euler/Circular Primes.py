
# The following will be an efficient primeTester. THIS IS VERY EFFICIENT! DON'T FORGET THIS FACT ABOUT PRIMES!
import math
def primeTest(n): # Want to test if n is a prime\
    if n==2:
        return 1
    if n%2==0:
        return 0 # 0 indicates a composite number.
    t=0
    d = int(math.sqrt(n))+1
    for k in range(3,d,2) :# We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n%k==0:
            return 0 # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1 # "This return 1" may look awfully strange but what happens is once a return value is set
             # it cannot be changed.... so in the event we don't return 0 then we return 1.

def rotate(n):
    a = list(str(n))
    b = len(a)-1
    c = [0]*b
    for i in range(0,b):
        c[i]=a[i+1]
    c.append(a[0])
    d = ''.join(c)
    return int(d)


def circularPrime(n):
    a = list(str(n))
    b=[0]*len(a)
    t=0
    for i in range(0,len(a)):
        b[i]=int(a[i])

    if 0 in b:
        return 0
    else:
        while(primeTest(n)==1 and t<len(a)):
            n = rotate(n)
            t+=1
    if t==len(a):
        return 1
    else:
        return 0



#This function will count the number of circular primes less than n
def CircularPrimeCounter(n):
    q=0
    for i in range(2,n):
        if circularPrime(i)==1:
            q+=1
            print(i)
        else:
            continue
    return q

print(CircularPrimeCounter(1000000))


