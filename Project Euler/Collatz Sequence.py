
# We first need to run a Collatz sequence so that we can then count the number of steps in the chain.

def collatzCounter(n): # n is the number we want to start our collatz sequence on.
    t=1
    while(n!=1):
         # We add 2 for the chain counter to include the starting number and the 1 (ending number)
        if n%2==0:
            n=n/2
            t=t+1
        else:
            n=3*n+1
            t=t+1
    return t

def longestChain():
    MAX = 0
    ValueforMax=0
    for k in range(1,1000000):
        b = collatzCounter(k)
        print(k)
        if b> MAX:
            MAX=b
            ValueforMax = k
        else:
            continue
    return ValueforMax

print(longestChain())

