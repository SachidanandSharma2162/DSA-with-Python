def checkPalindrome(num):
    tmp=num
    sum=0
    while tmp>0:
        digit=tmp%10
        sum=sum*10+digit
        tmp//=10
    if sum==num:
        return True
    else:
        return False


n=int(input("Enter n: \n"))
if checkPalindrome(n)==True:
    print("Palindrome: ",n)
else:
    print("Not Palindrome")

