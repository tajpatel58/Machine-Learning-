# The final objective is to create an array of numbers than can be written as the sum of 2 abundant numbers.
#Note from the brief all numbers greater than 28123 can be written as the sum of 2 abundant numbers.

import math
def sumofDivisors(n):
    SUM=1 # Default the value of SUM to 1 to account for the divisor 1.
    d = math.sqrt(n)
    if int(d)==d:
        SUM = d+1
        for i in range(2,int(d)):
            if n%i==0:
                SUM = SUM + i + n/i
            else:
                continue
    else:
        for i in range(2,int(d)+1):
            if n%i==0:
                SUM = SUM + i + n/i
            else:
                continue
    return int(SUM)

# This next function returns a list of abundant numbers less than n
# The reason we reduce to find abundant numbers less than n is because the sum of any 2 abundant numbers will be
# less than n.
def listofabundant(n):
    a = [] # 12 is the first abundant number
    for k in range(2,n+1):
        b = sumofDivisors(k)
        if b>k:
            a.append(k) # k is abundant if the sum of its divisors is greater than itself.
        else:
            continue

    return a

# This function given an array will return another array that is the sum of any 2 numbers of number in the input array.
# Note in this case we ammend the function so that n no number in the array can be bigger than n,
# NOTE THE FOLLOWING IS A CHUNK OF INEFFICIENT CODE!! KEPT IT SO YOU KNOW HOW TO IMPROVE
# def sumofpairs(a,n):
#     b=[]
#     print(len(a))
#     for i in range(0,len(a)):
#         for k in range(i,len(a)):
#             print(i)
#             c = a[i]+a[k]
#             if c < n:
#                 if c in b :
#                     continue
#                 else:
#                     b.append(c)
#             else:
#                 continue
#     return b



# The following function will accept an array of integers (a) and another integer (b)
# This function will aim to sum the numbers that aren't in the array a and less than b.
# The use of this function in our problem is to input an array with numbers that can be written as the sum of
# 2 abundant numbers and from this we can sum the numbers less than 28123 that's not in the array.

# def sumofnonabundant(a,b):
#     SUM=0
#     for k in range(1,b+1):
#         if k in a:
#             print(k)
#             continue
#         else:
#             print(SUM)
#             SUM=SUM+k
#     return SUM

# So this function does the same as written above, given an array input which in this case is labelled 'a' we output another array that is a
# combination of 0's and 1's. If in the ith position of the array there is a 1 then that means i (WHICH IS AN INTEGER) is the result
# of the sum of 2 numbers in the array 'a'. So the use of this function in our problem is by giving it an array of abundant numbers
# the output of the function will be an array of 0's and 1's where 1 indicates the number is the sum of 2 abundant numbers.


def sumofpairs(a):
    b = [0]*28123 # We default the length of the array to be 28123 as we know that for any number greater than 28123 it is the sum of 2 abundant numbers
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            c=a[i]+a[j]
            if c<=28123:
                b[c-1]=1 # We have written c-1 as we need to account for how indexing arrays work.
            else:
                continue
    return b

# The follow function will be used to sum the numbers that cannot be written as the sum of 2 abundant numbers.
# We do this by inputting an array from the function above ie. should be of the form of 0's and 1's which we sum all the indexes with 0.
def sumofnonabundant(a):
    SUM=0
    for i in range(0,len(a)):
        if a[i]==0:
            d=i+1
            SUM += d  # WE ADD ONE TO ACCOUNT FOR THE INDEX. a[20]==0 then that means 21 cannot be written as the sum of 2 abundant numbers.
            print(i+1)
        else:
            SUM=SUM
    return SUM

d= listofabundant(28123)
print(d)
e= sumofpairs(d)
print(e)
print(sumofnonabundant(e))
