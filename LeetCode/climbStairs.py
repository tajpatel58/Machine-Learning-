
#%% 
import math

def climbStairs(n: int) -> int:
    # individiual can only take 1 or 2 steps.
    max_twos = int(n/2)
    perms = 0
    for num_twos in range(max_twos+1):
        num_ones = n - num_twos * 2
        total_nums = num_ones + num_twos
        perms += math.factorial(total_nums) / (math.factorial(num_ones) * math.factorial(num_twos))
    return int(perms)


# %%
# Testing Example:
# for 4, 1111,121, 211, 22, 112
print(climbStairs(4))
# %%
