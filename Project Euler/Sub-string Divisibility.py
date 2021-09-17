
# Our goal in this project is to find the sum of all numbers that are 0-9 pandigital and have the sub-string divisibility as presented in the programme.
import time

start = time.time()
w = range(0, 10)
def if0to9pandigital(n):  # This function tells us if our number n is 0-9 pandigital.
    c = list(str(n))
    if len(c)==10:
        t=0
        for k in range(0,len(w)):
            d = str(w[k])
            if d in c:
                continue
            else:
                t=1
                return 0
        return 1
    else:
        return 0



def substring(n):       # We don't need to check length 10 as this will be checked in the above function.
    a = list(str(n))
    b = [2,3,5,7,11,13,17]
    del a[0]
    counter=0
    while(counter!=7):
        u = a[0] + a[1] + a[2]
        w = ''.join(u)
        if (int(w) % b[0]==0):
            del a[0]
            del b[0]
            counter = counter + 1
        else:
            return 0
    return 1

# A more efficient way to do this would be to list the permutations of (1,2,3,4,5,6,7,8,9,0) WHich is what we do in the following.
# for k in range(1023456789,9876543210):
#     if if0to9pandigital(k)==1 and substring(k)==1:
#         print(k)
#     else:
#         continue


def insertnum(a,b):
    q=[]
    for i in range(0,len(a)):
        c = a[i]
        d = list(c)
        for k in range(0,len(d)+1): # We have a +1 here as we want to also add k into the final position. Ie if we have 120 and we're adding 3 we should definitely have 1203 as a permutation.
            d.insert(k,str(b))
            e = ''.join(d)
            q.append(e)
            d.remove(str(b)) # NOTE: REMOVE ONLY REMOVES THE INSTANCE OF b ONCE! REMOVE b so that we can put b into a diff position in the next iteration.
    return q


def zeroremove(a):
    for i in range(0,len(a)):
        c = a[i]
        d = list(c)
        if int(d[0])==0:
            d.remove('0')
            e = ''.join(d)
            a[i]= e
        else:
            continue
    return a

def permutations(a):
    for k in range(2,10):
        a = insertnum(a,str(k))

    return a

def intarray(a):
    q=[]
    for i in range(0,len(a)):
        q.append(int(a[i]))
    return q


a = ['10','01']
b = permutations(a)
c = zeroremove(b)
d = intarray(c)
f = list(set(d)) # Set will create a set of each element of the array.
total = 0
for k in f:
    if if0to9pandigital(k)==1 and substring(k)==1:
        print(k)
        total = total + k

print(total)

end = time.time()

print(end-start)
