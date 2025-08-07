
def largest(nums):
    large=-1
    for i in nums:
        if i>large:
            large=max(i,large)
    return large

nums=[8,4,1,99,33,54,78]
print("largest of array: ",largest(nums))