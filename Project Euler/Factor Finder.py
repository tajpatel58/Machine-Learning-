import math

def primefactorfinder(n):
    while n%2==0:
        n=n/2  # we remove all multiples of 2

    for i in range(3,int(n)+1,2):
        while n%i==0:   # Use of a while loop instead of a for loop
                        # is required as might be divisible by i multiple times
                           # for example 27 is divisible by 3 but yielding 9 which is also divisible by 3.
            n=n/i
    print(n) # we should print n as in this case the number will be a prime itself.
primefactorfinder(600851475143)