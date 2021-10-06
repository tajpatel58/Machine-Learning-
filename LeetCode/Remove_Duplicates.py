#%%

def removeDuplicates(nums) -> int:
    length_list = len(nums)
    k = 0
    end = length_list - 1 
    index = 0
    while index != length_list:
        val = nums[index]
        index += 1 
        while index != length_list and nums[index] == val:
            nums[index] = 101
            index += 1 
        k += 1
    nums.sort() 
    return k

print(removeDuplicates([0,1,1,2]))

# %%
