import math
def countDigit(num):
    return int(math.log10(num)+1)
def checkArmstrong(num):
    tmp=num
    sum=0
    dig=countDigit(num)
    while tmp>0:
        digit=tmp%10
        sum=sum+(digit**dig)
        tmp//=10
    if sum==num:
        return True
    else:
        return False


n=int(input("Enter n: \n"))
if checkArmstrong(n)==True:
    print("Armstrong: ",n)
else:
    print("Not Armstrong")

