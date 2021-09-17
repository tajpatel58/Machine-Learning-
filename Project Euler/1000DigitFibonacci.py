# n here is defined as the index of the first number with n digits. NOTE THE RETURNED VALUE WILL BE THE INDEX OF THE FIRST N DIGIT NUMBER.
def fibonacci(n):
    a=1
    b=2
    t=3 # NOTE: t=3 as b which is equal to 2 is the 3rd Fibonacci number.
    while(len(list(str(b)))!=n):
        t+=1
        c=a
        a=b
        b=a+c
    print(b)
    return t

print(fibonacci(1000))

