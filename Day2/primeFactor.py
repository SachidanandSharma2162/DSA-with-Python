def findFactorsInOptimalWay(num):
    # T(n) = O(root(n))
    factor=set()
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            factor.add(i)
            factor.add(num//i)
    return list(factor)


def findFactors(num):
    # T(n) = O(n)
    factor=[]
    for i in range(1,num+1):
        if num%i==0:
            factor.append(i)
    return factor
n=(int(input("Enter n: ")))

factor=findFactorsInOptimalWay(n)
print(factor)
