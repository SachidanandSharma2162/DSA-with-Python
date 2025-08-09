row,col=map(int,input("Enter rows and columns: ").split())
print(row,col)

matrix=[[0]*row for _ in range(col)]

for i in range(row):
    for j in range(col):
        tmp=int(input())
        matrix[i][j]=tmp

print(matrix)