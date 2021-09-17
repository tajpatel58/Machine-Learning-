import math
def samedigits(num1, num2):
    list1 = list(str(num1))
    list2 = list(str(num2))
    for i in list1:
        if i in list2:
            list2.remove(i)
    return 1 if len(list2) == 0 else 0


tenth1, tenth2 = (10, 100)
indicator = 0
a = [2,3,4,5,6]
while(indicator != 1):
    for k in range(tenth1, math.floor(tenth2/6)):
        counter = 0
        for i in a:
            if samedigits(k, i*k) == 1:
                counter += 1
            else:
                break

        if counter == 5:
            indicator = 1
            print(k)
            break
        else:
            continue
    tenth1 = tenth1 * 10
    tenth2 = tenth2 * 100








