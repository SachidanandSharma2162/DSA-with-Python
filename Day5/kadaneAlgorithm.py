
def findMaximumSubArraySum(nums):
    sum=0
    maxSum=float("-inf")
    for i in nums:
        sum+=i
        maxSum=max(maxSum,sum)
        if sum<0:
            sum=0
    return maxSum

nums=[-2,1,-3,4,-1,2,1,-5,4]
maxSum=findMaximumSubArraySum(nums)

print(maxSum)   