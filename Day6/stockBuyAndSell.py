def stockBuySell(arr):
    # code here
    profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            profit+=(arr[i]-arr[i-1])
    return profit

def maxProfit(self, arr):
    profit=0
    mini=arr[0]
    for i in range(1,len(arr)):
        res=arr[i]-mini
        profit=max(profit,res)
        mini=min(arr[i],mini)
    return profit
nums=list(map(int,input("Enter the numbers in array: ").split()))
print(nums)

profit=stockBuySell(nums)
print(profit)