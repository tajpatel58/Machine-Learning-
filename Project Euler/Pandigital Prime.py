
import math
def primeTest(n): # Want to test if n is a prime
    if n%2==0:
        return 0 # 0 indicates a composite number.
    t=0
    d = int(math.sqrt(n))+1
    for k in range(3,d,2) :# We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n%k==0:
            return 0 # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1 # "This return 1" may look awfully strange but what happens is once a return value is set
             # it cannot be changed.... so in the event we don't return 0 then we return 1.

def ifnpandigital(n):
    c = list(str(n))
    a = len(c)
    t=0
    w = range(1,a+1)
    for k in range(0,len(w)):
        d = str(w[k])
        if d in c:
            continue
        else:
            t=1
            break
    if t==1:
        return 0
    else:
        return 1  #1 indicates pandigital number

MAX=0
for k in range(2,10000000):
    if ifnpandigital(k)==1 and primeTest(k)==1 and k>MAX:
        MAX=k
        print(k)

print(MAX)
