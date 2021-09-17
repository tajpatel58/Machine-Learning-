def primeTest(n):
    t=0
    for i in range(2,n):
        if n%i==0:
            t=t+1
        else:
            continue
    if t==0:
        return 1 # returning 1 tells us the number is prime
    else:
        return 0# returning 0 tells us the number is composite

def nTHprime(n): # For relatively small n. Otherwise adjust the value in the range.m
    k=0
    prime=0
    for i in range(2,10000000):
        if primeTest(i)==1 and k<n-1:
            k=k+1
            print(k)
        elif primeTest(i)==1 and k==n-1:
            prime = i
            break
        else:
            continue
    return prime

print(nTHprime(10001))



