def merge(nums,l,mid,r):
    i=l
    j=mid+1
    tmp=[]
    while i<=mid and j<=r:
        if nums[i]<nums[j]:
            tmp.append(nums[i])
            i+=1
        elif nums[i]>nums[j]:
            tmp.append(nums[j])
            j+=1
    while i<=mid:
        tmp.append(nums[i])
        i+=1
    while j<=r:
        tmp.append(nums[j])
        j+=1
    p=0
    for k in range(l,r+1):
        nums[k]=tmp[p]
        p+=1

def mergeSort(nums,l,r):
    if l<r:
        mid=(l+r)//2
        mergeSort(nums,l,mid)
        mergeSort(nums,mid+1,r)
        merge(nums,l,mid,r)

nums=[1,5,4,3,7,9,2]
print(nums)
mergeSort(nums,0,len(nums)-1)
print(nums)