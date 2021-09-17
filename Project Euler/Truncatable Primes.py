
import math
def primeTest(n): # Want to test if n is a prime
    if n== 2:
        return 1
    if n % 2 == 0 or n==1:
        return 0  # 0 indicates a composite number.
    t = 0
    d = int(math.sqrt(n)) + 1
    for k in range(3, d, 2):  # We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n % k == 0:
            return 0  # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1  # "This return 1" may look awfully strange but what happens is once a return value is set
    # it cannot be changed.... so in the event we don't return 0 then we return 1.


# This function will tell us if the number n is a truncatable prime... returning 1 if yes and 0 if no.
def truncatablePrime(n):
    a= list(str(n))
    b=[0]*len(a)
    t=0
    w=n
    for i in range(0,len(a)):
        b[i]= int(a[i])
    q = list(str(n))
    c = len(q)
    if 0 in b:
        return 0
    else:
        for i in range(0,c):
            if primeTest(n)==1 and len(a)!=0:
                t+=1
                a.pop(0)
                if len(a)!=0:
                    n=int(''.join(a))
                else:
                    continue
            else:
                break
        if t==c:

            for i in range(0,c):
                if primeTest(w)==1 and len(q)!=0:
                    t+=1
                    q.pop(len(q)-1)
                    if len(q)!=0:
                        w=int(''.join(q))
                    else:
                        break
                else:
                    break
        else:
            return 0
    if t==2*c:
        return 1
    else:
        return 0


def Truncfinder():
    t=0
    N=10
    SUM=0
    while(t!=11 and N>0):
        if truncatablePrime(N)==1:
            t+=1
            SUM+=N
            print(N)
            N+=1
        else:
            N+=1

    return SUM



print(Truncfinder())







