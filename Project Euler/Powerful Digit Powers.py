# We use the fact a number can only be the power of length if its less than 10.

# We add 1 to the final answer as we forgot to check 1 ** 1 == 1


def find_num(length):
    counter = 0
    for i in range(2, 10):
        list1 = list(str(i ** length))
        if len(list1) == length:
            print(i ** length)
            counter += 1
        else:
            continue
    return counter


counter = 0
for k in range(1, 90):
    counter += find_num(k)

print(counter+1)

