# The following will be an efficient primeTester. THIS IS VERY EFFICIENT! DON'T FORGET THIS FACT ABOUT PRIMES!
import math


def primeTest(n):   # Want to test if n is a prime
    if n % 2 == 0:
        return 0  # 0 indicates a composite number.

    d = int(math.sqrt(n))+1
    for k in range(3, d, 2):  # We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n % k == 0:
            return 0  # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1  # "This return 1" may look awfully strange but what happens is once a return value is set

# it cannot be changed.... so in the event we don't return 0 then we return 1.


def insertnum(a, b):
    w = []
    for i in range(0, len(a)):
        c = list(a[i])
        for j in range(0, len(c)+1):
            c.insert(j, str(b))
            e = ''.join(c)
            w.append(e)
            c = list(a[i])
    return w


def permutation(y):
    array = list(str(y))
    p = [array[0]]
    for u in range(1, len(array)):
        p = insertnum(p, int(array[u]))
    return p


def intarray(arraystring):
    arraynumber = [0] * len(arraystring)
    for o in range(0, len(arraystring)):
        arraynumber[o] = int(arraystring[o])
    return arraynumber


r = []
for k in range(1000, 10000):
    if primeTest(k) == 1:
        r.append(k)


counter = 0  # We create a counter to count the number of triplets we have, only 2 triplets exist.
for i in range(0, len(r)):
    for j in range(2, 3333, 2):
        if primeTest(r[i]+j) == 1 and primeTest(r[i]+2*j) == 1:
            x = intarray(permutation(r[i]))
            if r[i]+j in x and r[i]+2*j in x:
                counter = counter + 1
                f = list(str(r[i]))
                g = list(str(r[i]+j))
                h = list(str(r[i]+2 * j))
                v = ''.join(f+g+h)
                print(int(v))
            if counter ==2:
                break


