def split(nums,l,h):
    p=l+1
    q=h
    tmp=nums[l]
    while True:
        while p <= q  and nums[q]>tmp:
            q-=1
        while p <= q  and nums[p]<tmp:
            p+=1
        if q>p:
            nums[p],nums[q]=nums[q],nums[p]
        else:
            break
    nums[l],nums[q]=nums[q],nums[l]
    return q
    


def quickSort(nums,l,h):
    if l<h:
        i=split(nums,l,h)
        quickSort(nums,l,i-1)
        quickSort(nums,i+1,h)

nums=[9,8,7,6,5,4,3,2,1]
print(nums)
quickSort(nums,0,len(nums)-1)
print(nums)