# We start off with the lexicographic permutations of 0,1,2. We then add 3 to every position of the each number. ie we have Lexicographic permutations for 0,1,2 are:
# 012 021 102 120 201 210.... we add 3 to every position of 012 which yields: 3012 0312 0132 0123. and we do this for every number in the collection of lexicographic permutations for
# 0,1,2. Which when output will give us the permutations for 0,1,2,3. Which we need to make a function to order the numbers in.


# Let's do the easy steps first... Lets create a function that given an array of numbers will organise into ascending order.
# To do this we create anither function to find the minimum in the array. I HAVE COMMENTED OUT AS I WILL USE THE PYTHON BUILT IN ONE

# def min(a):
#     min = a[0]
#     for i in range(0,len(a)):
#         if a[i] <min:
#             min = a[i]
#         else:
#             continue
#     return min

# def order(a,p):
#     q = len(a)
#     b = [min(a)]
#     d = min(a)
#     a.remove(d)
#     while(len(a)!=q-p):
#         print(len(a))
#         c = min(a)
#         b.append(c)
#         a.remove(min(a))
#     return b[len(b)-1]


a = ['01','10']

# In the follow a is the list of numbers (in string form) and b is the number we wish to add to these strings.
# this array denoted as q is the array of numbers (Stored as strings) is the array of permutations with b added.
# So what we do here is we add the number b to a particular index to get one of the permutations, then we add the new number to an array


def insertnum(a,b):
    q=[]
    for i in range(0,len(a)):
        c = a[i]
        d = list(c)
        for k in range(0,len(d)+1): # We have a +1 here as we want to also add k into the final position. Ie if we have 120 and we're adding 3 we should definitely have 1203 as a permutation.
            d.insert(k,str(b))
            e = ''.join(d)
            q.append(e)
            d.remove(str(b)) # NOTE: REMOVE ONLY REMOVES THE INSTANCE OF b ONCE!
    return q



# So a is an array in which we want to add certain numbers to get permutations. For example using a as defined above by calling this function upon it
# this function will create an array for permutations 0,1,2,3 (THIS WILL BE FIRST ITERATION OF FOR LOOP) then the second loop will create an array for
# permutations of 0,1,2,3,4 then we keep doing this to get to 9. Which will eventually output an array of all permutations of 0,1,2,3,....,9.

def permutations(a):
    for k in range(2,10):
        a = insertnum(a,str(k))

    return a

# This function will given an array of strings if any of them start with the number 0 we have to remove the 0 in order for python to understand the number. Ie python doesnt understand that 023 is 23.
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

def intarray(a):
    q=[]
    for i in range(0,len(a)):
        q.append(int(a[i]))
    return q

# b = [123,20101,210,201,98,19,382,1928,2326]
# print(order(b,2))

b = permutations(a)
c = zeroremove(b)
e = intarray(c)
f = list(set(e)) # THIS MAKES SENSE WHAT WE DO IS WE CREATE a set from elements in an array and store this set as an array. This is a great way to remove duplicates from an array!
f.sort()
print(f)
print(len(f))
print(f[999999])




















