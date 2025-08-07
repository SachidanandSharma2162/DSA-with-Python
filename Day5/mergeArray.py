
def merge(nums1,nums2):
    i=0
    j=0
    nums=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            nums.append(nums1[i])
            i+=1
        elif nums1[i]>nums2[j]:
            nums.append(nums2[j])
            j+=1 
        else:
            nums.append(nums1[i])
            i+=1
            j+=1
    while i<len(nums1):
            nums.append(nums1[i])
            i+=1
    while j<len(nums2):
            nums.append(nums2[j])
            j+=1
    return nums

nums1=list(map(int,input("Enter the numbers in array: ").split()))
print(nums1)
nums2=list(map(int,input("Enter the numbers in array: ").split()))
print(nums2)

nums3=merge(nums1,nums2)

print(nums3)