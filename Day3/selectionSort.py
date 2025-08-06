def selectionAscendingSort(nums):
    n=len(nums)
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if nums[min_idx]>nums[j]:
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]

def selectionDescendingSort(nums):
    n=len(nums)
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if nums[min_idx]<nums[j]:
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]


nums=[1,5,4,3,7,9,2]
print(nums)
# selectionDescendingSort(nums)
selectionAscendingSort(nums)
# nums.sort()
print(nums)