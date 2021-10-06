#%%
def findDuplicates(nums) -> list[int]:
    occurences_dict = {}
    output = []
    for num in nums:
        if num in occurences_dict.keys():
            occurences_dict[num] += 1 
        else:
            occurences_dict[num] = 1 
    for key in occurences_dict.keys():
        if occurences_dict[key] == 2:
            output.append(key)
    return output 

print(findDuplicates([1,1,3,5,6,3,4,6,4,7,8,9,99,87]))