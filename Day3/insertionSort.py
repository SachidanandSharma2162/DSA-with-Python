
def insertionSort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key



nums=[1,5,4,3,7,9,2]
print(nums)
insertionSort(nums)
print(nums)