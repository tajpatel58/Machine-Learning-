# The following will be an efficient primeTester. THIS IS VERY EFFICIENT! DON'T FORGET THIS FACT ABOUT PRIMES!
import math


def primeTest(n):  # Want to test if n is a prime
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


def euler_totient_function(n):
    prod = n;
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            vec =[i, n/i]
            if i == n/i:
                prod = prod * (1-1/i)
            else:
                for d in vec:
                    if primeTest(d) == 1:
                        prod = prod * (1-1/d)
                    else:
                        continue
    return prod


max_value = 0
max_arg = 1

for j in range(1, 1000000):
    if j/euler_totient_function(j) > max_value:
        max_value = j/euler_totient_function(j)
        max_arg = j
    else:
        continue

print(max_arg)