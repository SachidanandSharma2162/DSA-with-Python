# when a fucntion calls itself it is called as Recursion

# Factorial of number
def Factorial(num):
    # base condition
    if num==0:
        return 1
    return num*Factorial(num-1)

# Print number count times
def printNumber(count,num):
    # base condition
    if count==0:
        return
    printNumber(count-1,num+1)
    print(num)

print(Factorial(5))
printNumber(10,1)


