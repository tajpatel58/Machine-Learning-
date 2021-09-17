# if 10^k is congruent to 1 mod d then this implies 1/d is recurring and the smallest k st this holds
#     is the length of recurring part. This is because 10^k == 1 mod d then this implies
#     10^k ( 1/ d) - 1/d is an integer. if 1/d is not recurring then no such k exists. That's what's beautiful.
#     if such a k exists then this implies recurring and the smallest k removes the recurring part.
#     similar to how we obtain the rational form of a recurring decimal.

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

def lengthofrecurring(n):
    for k in range(1,n+1):
        if (10 ** k) % n == 1:
            return k
    else:
        return 0

MAX = 0
# for k in range(1,10000):
#     print(k)
#     a = lengthofrecurring(k)
#     if a > 0:
#         if a == 10:
#             print(k)
#         else:
#             continue
print(lengthofrecurring(481))