# The following will be an efficient primeTester. THIS IS VERY EFFICIENT! DON'T FORGET THIS FACT ABOUT PRIMES!
import math
def primeTest(n): # Want to test if n is a prime
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


def quadraticprimes():
    q=[]
    MAX=0
    A=0
    B=0
    for a in range(-999,1000):
        for b in range(0,1001):
            c = b
            t=0
            n=0
            while(c>0 and primeTest(c)==1):
                t=t+1                     # NOTE t is the number of consecutive numbers starting from n=0 st when substituted into the quadratic we get a prime number.
                n=n+1
                c= n*n+a*n+b
            q.append(t)
            if t>MAX:
                MAX=t
                A=a
                B=b
            else:
                continue
            q.append(t)
    return A*B

print(quadraticprimes())