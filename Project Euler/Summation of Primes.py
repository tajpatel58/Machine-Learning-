# The following will be an efficient primeTester.
import math
def primeTest(n): # Want to test if n is a prime
    if n%2==0:
        return 0 # 0 indicates a composite number.
    t=0
    d = int(math.sqrt(n))+1
    for k in range(3,d,2) :# We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n%k==0:
            return 0 # Again we return 0 in the event that we have a composite number.
            break
        else:
            continue

    return 1 # "This return 1" may look awfully strange but what happens is once a return value is set
             # it cannot be changed.... so in the event we don't return 0 then we return 1.

def sumOfPrimes(n): #Sum the number of primes less than n (FOCUS ON LESS THAN - NOT LESS THAN OR EQUAL TO)
    SUM=0
    for i in range(2,n):
        if primeTest(i)==1:
            SUM=SUM+i
            print(i)
        else:
            continue
    print(SUM)

sumOfPrimes(2000000)
