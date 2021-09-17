
# Pentagon numbers are given by the sequence:n(3n-1)/2

# Through some handwritten work a number k is a pentagon number if there exists n st n(3n-1)/2 == k,
# equiavalently require sqrt(1+24k) mod 6 == 5

import math
import time

start = time.time()


def ispentagon(n):  # This function should test whether or not a number is a pentagon number.
    if math.sqrt(1 + 24 * n) % 6 == 5:
        return 1
    else:
        return 0


def pentagon(m):
    return m * (3 * m - 1)/2


t = 0
q = 10
w = []
while t < 1:
    a = pentagon(q)
    for k in range(1, q):
        c = pentagon(k)
        if ispentagon(a + c) == 1 and ispentagon(a - c) == 1:
            t = t+1
            w.append(int(a - c))
        else:
            continue
    q = q + 1

print(w)

end = time.time()

print(end - start)
