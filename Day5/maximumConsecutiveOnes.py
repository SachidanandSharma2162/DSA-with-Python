
def countMaximumConsecutiveOnes(nums):
    count=0
    max_count=0
    for i in nums:
        if i==1:
            count+=1
        else:
            max_count=max(count,max_count)
            count=0
    return max_count

nums=list(map(int,input("Enter the array elements: ").split()))
print(nums)

countOfOnes=countMaximumConsecutiveOnes(nums)

print(countOfOnes)