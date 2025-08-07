
def rightRotateArray(nums,k):
    k=k%len(nums)
    nums[:]= nums[-k:]+nums[:-k]
    return nums
def leftRotateArray(nums,k):
    k=k%len(nums)
    nums[:]= nums[k:]+nums[:k]
    return nums

nums=list(map(int,input("Enter the numbers of array: ").split(' ')))
print(nums)
k=int(input("Enter the value of k: "))
# nums=rightRotateArray(nums,k)
nums=leftRotateArray(nums,k)

print(nums)
