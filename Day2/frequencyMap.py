nums=[1,2,3,4,5,1,1,1,2,3,4,5,1,2,3,4,5]

dictMap={}
for i in nums:
    # if i in dictMap:
    #     dictMap[i]+=1
    # else:
    #     dictMap[i]=1
    dictMap[i]=dictMap.get(i,0)+1
print(nums)
print(dictMap)