# Here what we are doing is counting the number of divisors a number has... in particular a "Triangle Number"
# Now the idea is we only need to count the divisors not actually know what they are.
# We can count the number of divisors by using the idea for every divisor of n less than root(n) we have another root
# greater than root(n). Then we also add one in the event that the triagnle number is a perfect square.


import math

def triangleNumberwithNdivisors(n): # n is the number st the triangle number we seek has >n divisors.
    TRIANGLE=6
    e=6
    t=2 # t is the number of divisors... we have 2 already as we count 1 and the number itself.
    for i in range(4,1000000000):
        TRIANGLE=TRIANGLE+i
        # Now for the triangle number we need to count the number of divisors.
        e = math.sqrt(TRIANGLE)
        d=int(e)
        for k in range(2,d):
            if TRIANGLE%k==0:
                t=t+2 # For every divisor less than the root we have one above the root.
            else:
                continue
        if t>n:
            return TRIANGLE
        else:
            t=2 # Reset t=2 so that the next triangle number has 2 divisors.

print(triangleNumberwithNdivisors(500))

