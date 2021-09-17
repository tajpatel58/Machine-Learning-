successful_attempts = []
with open('Project79.txt', 'r') as f:
    for line in f:
        successful_attempts.append(line)

for i in range(0,len(successful_attempts)):
    successful_attempts[i] = int(successful_attempts[i])

print(successful_attempts)

# So I need to find a number with smallest length that contaians all the numbers below in that precise order.
def subnum(num,sub):
    list_sub = list(str(sub))
    list_num = list(str(num))
