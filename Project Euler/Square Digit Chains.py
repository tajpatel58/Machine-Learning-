import time

start = time.time()
def chain():
    counter = 0
    for k in range(2, 10_000_000):
        print(k)
        val = k
        list2 = [89, 145, 42, 20, 4, 16, 37, 58]
        list3 = [1, 44, 32, 10, 13]
        list4 = list2 + list3
        list5 = [val]
        while val not in list4:
            list1 = list(str(val))
            sum = 0
            for i in range(0, len(list1)):
                sum += int(list1[i]) ** 2
            val = sum
            list5.append(val)
        if val in list3:
            list3 += list5
        else:
            list2 += list5
            counter += 1
    return counter

print(chain())

end = time.time()

print(end - start) 