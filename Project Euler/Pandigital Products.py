# Our number will not be the product of 3 digit times a 3 digit so we will restrict our search to numbers that are the product of a 2 digit and 3 digit

# We are in the search for numbers that are pandigital in terms of product/multiplicand/output i.e 39*186 = 7254 ... each number from 1-9 appears.
# A pandigital number is a number that 1-9 in it, but in this case we will say if it is pandigital in terms of product/multiplicand/output

def PandigitalTest():
    q = [0]*1000000
    for i in range(1,100):
        for k in range(1,10000):
            s = i*k
            a = list(str(i))
            b = list(str(k))
            c = list(str(i*k))
            d = a+b+c
            p = a+b+c
            if len(d)==9:
                for j in range(1,10):
                    e = str(j)
                    if e in d:
                        d.remove(e)
                    else:
                        break
                if len(d)==0:
                    q[s-1]=1
                else:
                    continue
            else:
                continue
    return q
w = PandigitalTest()
SUM=0
for k in range(0,len(w)):
    if w[k]==1:
        a = k+1
        SUM+=a
    else:
        continue
print(SUM)






