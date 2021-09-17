

with open('Project18.txt', 'r') as f:
    array = []
    for line in f:
        array.append(line)

array2 = [i.strip('\n').split(' ') for i in array]
intarray = [[int(n) for n in i] for i in array2]

# This function combines 2 row vectors by taking one vector then deciding which path yields a bigger result. 
def maxarray(vectorup,vectorlow):  # Assume len(vector2)-len(vector1) = 2
    len1 = len(vectorup)
    len2 = len(vectorlow)
    vectorcombine = []
    for i in range(0, len1):
        sum1 = vectorup[i] + vectorlow[i]
        sum2 = vectorup[i] + vectorlow[i+1]
        if sum1 >= sum2:
            vectorcombine.append(sum1)
        else:
            vectorcombine.append(sum2)

    return vectorcombine

# This functions combines the bottom 2 rows of a triangle array and returns the new triangle array.
def trianglecombine(matrix):
    length = len(matrix)
    bottomrow = matrix[length-1]
    secondbottomrow = matrix[length-2]
    newbottom = maxarray(secondbottomrow,bottomrow)
    matrix.pop(length-1)
    matrix.pop(length-2)
    matrix.append(newbottom)
    return matrix

t = 0
while( t!= len(intarray)):
    intarray = trianglecombine(intarray)
    t =+ 1

print(intarray)























