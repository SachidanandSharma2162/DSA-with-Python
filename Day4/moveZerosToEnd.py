
def moveZerosToEnd(nums):
    idx=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[i],nums[idx]=nums[idx],nums[i]
            idx+=1
            
        

nums=list(map(int,input("Enter the numbers of array: ").split(' ')))
print(nums)
moveZerosToEnd(nums)

print(nums)