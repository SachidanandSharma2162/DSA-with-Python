# Recursive function to reverse array
def reverseArray(i,j,nums):
    if i>j:
        return
    nums[i],nums[j]=nums[j],nums[i]
    reverseArray(i+1,j-1,nums)
num=[1,2,3,4,5]
print(num)
reverseArray(0,len(num)-1,num)
print(num)
