# When dealing with 2D arrays or a matrix .... if we wish to create a mxn matrix then we do this by [[0]*n]*m which creates an nxn matrix. Although when it's printed it seems
# dodgy just understand that it's pythons way of storing the data.

# c=[[1,2,3],[4,5,6],[7,8,9]]
# c[0][0]=2
# print(c[1][2])

#We create a function to yield a nxn spiral of numbers.
# n MUST BE ODD!!!!
import math
def spiralin(n):
    k = n*n
    a = [0]*n
    for i in range(0,n):
        a[i]=[0]*n
    d = math.ceil(n/2)-1
    a[d][d]=1
    t=n
    b=0
    u=0
    for j in range(1,t+1):
        a[u][t-j]=k-b
        b+=1
    for j in range(1,t):
        a[j][u] = k-b
        b+=1
    for j in range(1,t):
        a[t-1][j]=k-b
        b+=1
    for j in range(1,t-1):
        a[t-1-j][t-1]=k-b
        b+=1
    u+=1
    t=t-1

    while(k-b!=0):

        for j in range(1,t-u+1):
            a[u][t-j]=k-b
            b+=1
        for j in range(1,t-u):
            a[u+j][u]=k-b
            b+=1
        for j in range(1,t-u):
            a[t-1][u+j]=k-b
            b+=1
        for j in range(2,t-u):
            a[t-j][t-1]=k-b
            b+=1
        u=u+1
        t=t-1


    return a



def printarray(n):
    for i in range(0,n):
        print(spiralin(n)[i])

# The follow function sums both diagonals of the matrix BUT doesn't count the middle number twice.
def sumofbothDiagonal(a):
    b= len(a[0])
    SUM=0
    for i in range(0,b):
        SUM += a[i][i]
    for i in range(1,b+1):
        SUM+= a[b-i][i-1]

    return SUM-1


printarray(11)














