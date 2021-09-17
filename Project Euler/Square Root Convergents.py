# Note this sequence can be generated. Take a/b to be a member, then (a+2b)/(a+b) is the next term.
def fraction(num):
    iterations = 0
    numerator = 7
    denominator = 5
    counter = 0
    while iterations != num:
        numerator_duplicate = numerator
        numerator = numerator + 2 * denominator
        denominator = numerator_duplicate + denominator
        iterations += 1
        list_numerator = list(str(numerator))
        list_denominator = list(str(denominator))
        if len(list_numerator) > len(list_denominator):
            counter += 1
        else:
            continue
    return counter


print(fraction(1000))
