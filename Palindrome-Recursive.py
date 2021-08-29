
# Define a palindrome number test using recursion. A Number is recursive iff, start and end are equal and middle is
# palindrome

# number input should be a string.
def is_palindrome(number):
    list_num = list(number)
    length = len(list_num)
    if length == 1:
        return 1
    if length == 2 and int(list_num[0]) == int(list_num[-1]):
        return 1
    elif list_num[0] == list_num[-1]:
        sub_num_list = list_num[1:-1]
        sub_num = ''.join(sub_num_list)
        return is_palindrome(sub_num)
    else:
        return 0

