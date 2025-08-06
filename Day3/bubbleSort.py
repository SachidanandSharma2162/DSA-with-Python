def bubbleSort(nums):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if nums[j]>nums[j+1]:
                flag=True
                nums[j],nums[j+1]=nums[j+1],nums[j]

def optimizedBubbleSort(nums):
    n=len(nums)
    for i in range(0,n-1):
        flag=False
        for j in range(0,n-1-i):
            if nums[j]>nums[j+1]:
                flag=True
                nums[j],nums[j+1]=nums[j+1],nums[j]
        if flag==False:
            break


nums=[1,2,3,4,5,6,7]
# nums=[1,5,4,3,7,9,2]
print(nums)
bubbleSort(nums)
# nums.sort()
print(nums)