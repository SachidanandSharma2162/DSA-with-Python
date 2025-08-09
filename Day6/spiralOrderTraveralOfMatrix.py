def spiralOrder(matrix):
    col=0
    row=0
    m=len(matrix)
    n=len(matrix[0])
    d=m*n
    count=0
    direct=0
    ans_list=[]
    while count<d:
        if direct==0:
            ans_list.append(matrix[row][col])
            matrix[row][col]=float("-inf")
            if col<n-1 and matrix[row][col+1]!=float("-inf"):
                col+=1
            else:
                direct=1
                row+=1
        elif direct==1:
            ans_list.append(matrix[row][col])
            matrix[row][col]=float("-inf")
            if row<m-1 and matrix[row+1][col]!=float("-inf"):
                row+=1
            else:
                direct=2
                col-=1
        elif direct==2:
            ans_list.append(matrix[row][col])
            matrix[row][col]=float("-inf")
            if col>0 and matrix[row][col-1]!=float("-inf"):
                col-=1
            else:
                direct=3
                row-=1
        elif direct==3:
            ans_list.append(matrix[row][col])
            matrix[row][col]=float("-inf")
            if row>0 and matrix[row-1][col]!=float("-inf"):
                row-=1
            else:
                direct=0
                col+=1
        count+=1
    return ans_list

row,col=map(int,input("Enter rows and columns: ").split())
print(row,col)

matrix=[[0]*row for _ in range(col)]

for i in range(row):
    for j in range(col):
        tmp=int(input())
        matrix[i][j]=tmp

print(matrix)

matrixSpiralList=spiralOrder(matrix)

print(matrixSpiralList)
