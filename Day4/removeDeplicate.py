
def removeDuplicates(nums):
    tmp=[]
    map=dict()
    for i in nums:
        if map.get(i)==None:
            tmp.append(i)
            map[i]=True
    return tmp
def removeDuplicatesPartTwo(nums):
    tmp=[]
    for i in nums:
        if tmp.count(i)==0:
            tmp.append(i)
    return tmp
nums=list(map(int,input("Enter the numbers of array: ").split(' ')))
print(nums)
arrayAfterDuplicateRemoval=removeDuplicates(nums)

print(arrayAfterDuplicateRemoval)