# In this challenge we want to find the sum of all amicabble numbers <10000. 2 numbers are ambiccable if:
# if d(a) prints the sum of its divisors, a and b are amiccable if d(a)==d(b)
# So firstly let's construct a function that will return the sum of its divisors.
import math
def sumofDivisors(n):
    SUM=1 # Default the value of SUM to 1 to account for the divisor 1.
    d = math.sqrt(n)
    if int(d)==d:
        SUM = d
    else:
        SUM=1
    for i in range(2,int(d)+1):
        if n%i==0:
            SUM = SUM + i + n/i
        else:
            continue
    return SUM

def sumofAmiccables(n):
    sumofAmiccable=0
    for k in range(1,n):
        for i in range(k+1,n):
            if sumofDivisors(k)==i and sumofDivisors(i)==k:
                sumofAmiccable = sumofAmiccable + k +i
                print(k)
                print(i)
        # NOTE BY USING THIS METHOD WE WILL ADD AMICCABLE NUMBERS TWICE SO DIVIDE BY 2 AT THE END
            else:
                print(i)
                print(k)
                continue
    return sumofAmiccable


print(sumofAmiccables(10000))

