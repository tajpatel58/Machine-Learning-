
def factorial(n): # Compute the factorial of n
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

def sumofDigitsinfactorial(n):
    a = factorial(n)
    b= list(str(a))
    SUM =0  # We define "SUM" to be the sum of the digits in 100 factorial.
    for k in range(0,len(b)):
        SUM = SUM + int(b[k])

    return SUM

print(sumofDigitsinfactorial(100))