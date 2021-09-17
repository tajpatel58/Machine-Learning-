import math
import time

start = time.time()


def primeTest(n):   # Want to test if n is a prime
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0  # 0 indicates a composite number.

    d = int(math.sqrt(n))+1
    for k in range(3, d, 2):  # We make the step size 2 as it's not a multiple of 2 no need to check the even numbers.
        if n % k == 0:
            return 0  # Again we return 0 in the event that we have a composite number.
        else:
            continue

    return 1  # "This return 1" may look awfully strange but what happens is once a return value is set


def digitadd(num1, digit):
    list1 = list(str(num1))
    newlist = []
    size = len(list1)
    for i in range(0, size+1):
        list1.insert(i, str(digit))
        for j in range(0, size+1):
            list1.insert(j, str(digit))
            str2 = ''.join(list1)
            num2 = int(str2)
            if primeTest(num2) == 1:
                newlist.append(num2)
                del list1[j]
            else:
                newlist.append(num2)
                del list1[j]
        del list1[i]

    return list(set(newlist))

# This function returns an array of primes which are the result of replacing 2 digits in num1 with 'digit'


def digitreplace(num1, digit):
    list1 = list(str(num1))
    size = len(list1)
    newlist = []
    for i in range(0, size):
        for j in range(0, size):
            if i == j:
                continue
            else:
                store1 = list1[i]
                store2 = list1[j]
                list1[i] = str(digit)
                list1[j] = str(digit)
                str1 = ''.join(list1)
                numreplace = int(str1)
                list1[i] = store1
                list1[j] = store2
                if primeTest(numreplace) == 1:
                    newlist.append(numreplace)
                else:
                    continue

    return list(set(newlist))


def primefamily(n):
    indicator = 0
    num1 = 100
    while indicator != 1:
        if primeTest(num1) == 1:   # We only need to check primes as the prime family arises from editing a prime.
            list1 = list(str(num1))
            size = len(list1)
            for i in range(0, size):
                for j in range(0, size):
                    for v in range(0, size):
                        if i != v and v != j and i != j:
                            newlist = []
                            store1 = list1[i]
                            store2 = list1[j]
                            store3 = list1[v]
                            for k in range(0, 10):
                                list1[i] = str(k)
                                list1[j] = str(k)
                                list1[v] = str(k)
                                str1 = ''.join(list1)
                                numreplace = int(str1)
                                str2 = list(str(numreplace))
                                if len(str2) == size and primeTest(numreplace) == 1:
                                    newlist.append(numreplace)
                                else:
                                    continue
                            list1[i] = store1
                            list1[j] = store2
                            list1[v] = store3
                            nonrepeatlist = list(set(newlist))
                            if len(nonrepeatlist) >= n:
                                print(nonrepeatlist)  # The smallest number in this list is part of the 8 prime family.
                                print(num1)  # Print here gives num1 that when edited gives the prime family of 8.
                                indicator = 1
                                quit()
                            else:
                                continue
        num1 += 1


primefamily(8)
end = time.time()

print(end-start)
