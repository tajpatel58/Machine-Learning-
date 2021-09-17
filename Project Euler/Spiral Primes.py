import math


def primeTest(n):  # Want to test if n is a prime
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


# We notice that if we consider each ring of the matrix the bottom right element is an odd square.
# This is useful as we can generate the numbers on the diagonals by taking away the length of the side.
# If the ring is the 3rd one, the bottom right is 49. Length will be the square root so 7.
# So the 4 corners of the ring are 49 itself ofcourse,  49 - 7, 49 - 7 -7, 49 - 7 - 7 - 7.
def diagonal_generator(n):
    list_diagonal = []
    counter = n ** 2
    index = n - 1
    for j in range(1, 5):
        list_diagonal.append(counter)
        counter = counter - index

    return list_diagonal


# This function will find the length of the side for which the number of primes in the diagonals / number of points
# in this diagonal < n. In this problem we needed the answer for n = 0.1
def proportion(n):
    indicator = 0
    prime_counter = 0
    index = 1
    length_of_side = 0
    num_of_diagonals = 1
    while indicator != 1:
        index += 2
        counter = 0
        diagonal = diagonal_generator(index)
        length_of_side = index
        for i in range(0, len(diagonal)):
            if primeTest(diagonal[i]) == 1:
                prime_counter += 1
                counter += 1
            else:
                continue
        num_of_diagonals += 4
        if prime_counter / num_of_diagonals < n:
            indicator = 1
        else:
            continue
    return length_of_side


print(proportion(0.1))
