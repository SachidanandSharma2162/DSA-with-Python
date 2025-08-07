
def findMissingFromTheArray(nums):
    n=len(nums)
    sumOfN=int((n*(n+1))/2)
    sumOfA=0
    for i in nums:
        sumOfA+=i
    return sumOfN-sumOfA
nums=list(map(int,input("Enter the numbers in array: ").split()))
print(nums)

missing=findMissingFromTheArray(nums)
print(missing)