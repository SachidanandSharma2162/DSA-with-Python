
def findSecondLargest(nums):
    first=float("-inf")
    second=float("-inf")
    for i in nums:
        if i>first:
            second=first
            first=i
        elif i>second:
            second=i
    return first,second

nums=list(map(int,input("Enter the numbers of array: ").split(' ')))
print(nums)
first,secLargest=findSecondLargest(nums)

print(first,secLargest)