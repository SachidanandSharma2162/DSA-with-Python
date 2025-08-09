def rearrangeArray(nums):
    pos=0
    neg=1
    n=len(nums)
    ans=[0]*(n)
    for i in nums:
        if i<0:
            ans[neg]=i
            neg+=2
        else:
            ans[pos]=i
            pos+=2
    return ans

nums=list(map(int,input("Enter the array elements: ").split()))

print(nums)
nums=rearrangeArray(nums)
print(nums)