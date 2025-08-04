# n=12345
# count=0
# while n>0:
#     count+=1
#     n//=10

# print("number of digits: ",count)
import math
def countDigit(num):
    # return int(math.log10(num)+1)
    n=num
    count=0
    while n>0:
        count+=1
        n//=10
    return count

n=int(input("Enter n: "))
print(countDigit(n))