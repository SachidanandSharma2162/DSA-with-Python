def checkPalindrome(l,r,string):
    if l>=r:
        return True
    if string[l] != string[r]:
        return False
    return checkPalindrome(l+1,r-1,string)

string=str(input())
print(checkPalindrome(0,len(string)-1,string))