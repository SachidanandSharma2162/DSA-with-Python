
def linearSearch(nums,key):
    for i in nums:
        if i==key:
            return True
    return False

nums=list(map(int,input("Enter the numbers in array: ").split()))
print(nums)

key=int(input("Enter key to search: "))
if linearSearch(nums,key)==True:
    print("Present")
else:
    print("Not Present")