

def primefactorsfinder(num):
    divisorsp = []
    i = 2
    while i < num ** 0.5 or num == 1:
        if num % i == 0:
            divisorsp.append(i)
            num = num/i
            i = i - 1
        i = i + 1
    return len(set(divisorsp)) + 1


j = 10

t = 0
while t != 1:
    set1 = primefactorsfinder(j)
    set2 = primefactorsfinder(j+1)
    set3 = primefactorsfinder(j+2)
    set4 = primefactorsfinder(j+3)
    print(j)

    if set1 == 4 and set2 == 4 and set3 == 4 and set4 == 4:
        t = 1
        print(j)

    else:
        j = j + 1
