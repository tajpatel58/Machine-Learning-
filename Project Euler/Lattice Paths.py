# I have more of an intuitive answer in an nxn grid to go from top corner to bottom corner you have to make n moves across and n moves down.
# However it doesn't matter what order we make the moves in. So We have to make a total of 2n moves, if you imagine a vector of length 2n
# which consists of 0's and 1's where 0 indicates we move across and 1 indicates we move down. For each vector of 0's and 1's of length 2n if
# it has n 1's and n 0's then its a path from top corner to bottom corner.
# SO the number of ways to distribute the 1's is (2n CHOOSES n) as automatically the 0's will be put into the blank spaces.
import math
def choose(n,c):
    a = math.factorial(n)
    b = math.factorial(n-c)
    d = math.factorial(c)
    e = d*b
    return int(a/e)
print(choose(40,20))

