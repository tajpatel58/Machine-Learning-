def isPalindrome(x):
    if x >= 0:
        list_digits_x = list(str(x))
        digits_of_reverse = []
        size = len(list_digits_x)
        for j in range(0, size):
            digits_of_reverse.append(list_digits_x[size - j - 1])
        reverse_string = "".join(digits_of_reverse)
        reverse = int(reverse_string)
        if reverse == x:
            return "true"
        else:
            return "false"
    else:
        return "false"


print(isPalindrome(-121))