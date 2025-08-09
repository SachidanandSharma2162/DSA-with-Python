def transpose(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(0,n):
        for j in range(0,m):
            if i<=j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
    
def copyColumns(matrix):
    n=len(matrix)
    m=len(matrix[0])
    # i=0
    # j=m-1
    # while i<j:
    #     for k in range(0,n):
    #         matrix[k][i],matrix[k][j]=matrix[k][j],matrix[k][i]
    #     i+=1
    #     j-=1
    for i in range(0,n):
        matrix[i].reverse()
    return matrix

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    matrix=transpose(matrix)
    matrix=copyColumns(matrix)
    return matrix


row,col=map(int,input("Enter rows and columns: ").split())
print(row,col)

matrix=[[0]*row for _ in range(col)]

for i in range(row):
    for j in range(col):
        tmp=int(input())
        matrix[i][j]=tmp

print(matrix)

matrix=rotate(matrix)

print(matrix)
