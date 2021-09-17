def sumOfSquares(val):
    sumofsquares =0
    for i in range(1,val+1):
        sumofsquares = sumofsquares+ i*i

    return sumofsquares

def squareOfSum(val):
    x =0
    for i in range(1,val+1):
        x = x + i
    d = x*x
    return d

print(sumOfSquares(100))
print(squareOfSum(100))

print(squareOfSum(100)-sumOfSquares(100))