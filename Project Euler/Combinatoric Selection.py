# The problem is rather simple hence efficiency wasn't a factor when I coded this programme.
import math


def choose(n, c):
    a = math.factorial(n)
    b = math.factorial(n-c)
    d = math.factorial(c)
    e = d*b
    return int(a/e)


counter = 0
for m in range(2, 101):
    for r in range(2, m):
        if choose(m, r) > 1_000_000:
            counter += 1
        else:
            continue


print(counter)
