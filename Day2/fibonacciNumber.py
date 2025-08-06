# Recursive Function to find the Nth fibonacci number
def findFibonacci(n,dp):
    if n==0:
        return dp[0]
    if n==1:
        return dp[1]
    dp[n]=findFibonacci(n-1,dp)+findFibonacci(n-2,dp)
    return dp[n]

n=int(input("Enter Nth fibonacci Number: "))
dp=[-1]*(n+1)
dp[0]=0
dp[1]=1
print(findFibonacci(n,dp))