# functional recursion
def sumOfNaturalNumbers(num):
    if num<=1:
        return num
    else:
        return num + sumOfNaturalNumbers(num-1)

num=int(input("Enter n: "))
sum=sumOfNaturalNumbers(num)

print("Sum: ",sum)