
def ifSorted(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True

nums=list(map(int,input("Enter the numbers of array: ").split(' ')))
print(nums)
if ifSorted(nums)==True:
    print("Sorted")
else:
    print("Not Sorted")