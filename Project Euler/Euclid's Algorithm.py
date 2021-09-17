# First I give some context behind Eucld's Algorithm. It basically says that if we want to find the gcd or hcf (same)
# Then if we denote our 2 numebrs by m,n. (m>n) gcd(m,n) = gcd(m mod n , n ) Then we repeat until the remainder is 0.


def euclids_algorithm(num1, num2):
    if num1 == 0:
        return num2
    return euclids_algorithm(num2 % num1, num1)

