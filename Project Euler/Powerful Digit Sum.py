
def digital_sum(num):
    list_num = list(str(num))
    val = 0
    for i in range(0, len(list_num)):
        val += int(list_num[i])

    return val

def max():
    max = 0
    for i in range(0,100):
        for j in range(0,100):
            test = digital_sum(i ** j)
            if test > max:
                max = test
            else:
                continue
    return max

print(max())