
def longestConsecutiveSequence(nums):
    ans=1
    for i in nums:
        len=1
        j=i+1
        while True:
            if j in nums:
                len+=1
                j+=1
            else:
                ans=max(len,ans)
                break
    return ans

def longestConsecutiveSequenceSet(nums):
    num_set=set()

    for i in nums:
        num_set.add(i)
    longest=0
    count=0
    for i in num_set:
        if i-1 not in num_set:
            count=1
            x=i
            while x+1 in num_set:
                count+=1
                x+=1
        longest=max(longest,count)
    return longest
nums=list(map(int,input("Enter the array elements: ").split()))

print(nums)
lcs=longestConsecutiveSequenceSet(nums)
print(lcs)