
def twoSum(nums,target):
    map={}
    for i in nums:
        res=target-i
        if map.get(res):
            return True
        else:
            map[i]=True
        
    return False



nums=list(map(int,input("Enter the array elements: ").split()))

print(nums)

target=int(input("Enter the target sum: "))
targetExist=twoSum(nums,target)

if targetExist==True:
    print("Found")
else:
    print("Not Found")