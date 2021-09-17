
import math

def primeTest(n):   # Want to test if n is a prime
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0  # 0 indicates a composite number.

    d = int(math.sqrt(n))+1
    for k in range(3, d, 2):  # We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n % k == 0:
            return 0  # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1  # "This return 1" may look awfully strange but what happens is once a return value is set

t = 0
q = 35
while t != 1:
    print(q)
    if primeTest(q) == 0:
        squarecounter = 0
        maxsquare = math.floor(math.sqrt(q/2))
        for k in range(1, maxsquare+1):
            num = q - 2*(k ** 2)
            if primeTest(num)==1:
                q = q + 2  # Make step size 2 as we only want odd numbers
                break
            else:
                squarecounter = squarecounter + 1 # if we try every square and none of num are prime then we're done.

        if squarecounter == maxsquare:
            t = 1
        else:
            continue

    else:
        q = q + 2

