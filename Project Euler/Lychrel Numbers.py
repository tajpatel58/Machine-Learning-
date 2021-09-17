import time

start = time.time()


def palindrome_tester(num):
    listnum = list(str(num))
    listnum.reverse()
    reverse_num = int(''.join(listnum))
    return 1 if num - reverse_num == 0 else 0


def lychrel_tester(num):
    iterations = 0
    initial_list = list(str(num))
    initial_list.reverse()
    val = num + int(''.join(initial_list))
    while iterations != 50:
        iterations += 1
        if palindrome_tester(val) == 1:
            return 0
        else:
            list_val = list(str(val))
            list_val.reverse()
            val = val + int(''.join(list_val))

    return 1


def lychrel_counter(n):
    counter = 0
    for i in range(10, n+1):
        if lychrel_tester(i) == 1:
            counter += 1
        else:
            continue
    return counter


print(lychrel_counter(10_000))

end = time.time()

print(end-start)
