# We want to find the prime <1000000 st it's written as the largest string of primes.

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


def primes(n):  # This function will give an array of the first n primes.
    array = [2]
    q = 3
    while (len(array) != n):
        if primeTest(q) == 1:
            array.append(q)
            q = q + 1
        else:
            q = q +1
    return array



# NOTE: the following function has 80000 which seems random but it's because 80000 primes don't exceed n
# We obviously don't wish to add primes bigger than n.
def primesums(n): # n is the limit, our prime shouldn't exceed n

    array = primes(80000)
    MAX = 0
    PRIME = 0 # Prime is the prime at which we attain this max.
    array2 = [0] * 1000000
    for i in range(0, 80000):
        index = i
        t=1
        a = array[index]
        print(i)
        for k in range(index +1 , 80000):
            a = a + array[k]
            t = t + 1
            if (a < n) and array2[a-1] < t and primeTest(a)==1 and t > MAX:
                MAX = t
                PRIME = a
            if a > n:
                break
    return PRIME


print(primesums(1000000))
