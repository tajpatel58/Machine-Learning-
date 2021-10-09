
#%%
def binary_search(nums, target):
    index = 0
    original_list = nums 
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    while len(nums) >= 1:
        length = len(nums)
        mid = int(length/2)
        final_num = nums[-1]
        if target == nums[mid]:
            index += mid
            return index
        elif target < nums[mid]:
            nums = nums[:mid]
        else:
            nums = nums[mid+1: ]
            index = index + mid + 1 
    loc_closest = binary_search(original_list, final_num)
    if target > final_num:
        return loc_closest + 1
    else:
        return loc_closest

print(binary_search([0,1,2,3,4,5,6,7,8], 2))

print(binary_search([1,3,5,6,7,9,10],9))

print(binary_search([1,6],9))

print(binary_search([1,2,5,8,10,12,17,22,27], 11))


# %%

