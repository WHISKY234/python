matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix1=[[7,8,9],[1,2,3],[4,5,6]]
sum=0
sum1=0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i==j or i+j==2:
            sum+=matrix[i][j]
for i1 in range(len(matrix1)):
    for j1 in range(len(matrix1)):
        if i1==j1 or i1+j1==2:
            sum1+=matrix[i1][j1]
sum0=sum+sum1
print("")
print("对角线元素之和为%d"%sum0)