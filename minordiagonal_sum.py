def minor_diagonal_sum(matrix, row, col):
    diagonal_sum = 0
    n = len(matrix)
    for i in range(row):
        for j in range(col):
            if ((i + j) == (n - 1)):
                diagonal_sum += matrix[i][j]
    return diagonal_sum
row = int(input())
col = int(input())
matrix = []
for i in range(row):
    matrix.append(list(map(int, input().split())))
print(minor_diagonal_sum(matrix, row, col))

"""
main diagonal means primary
minor means secondary
A00 A01 A02 A03
A10 A11 A12 A13
A20 A21 A22 A23
A30 A31 A32 A33
The primary diagonal is formed by the elements A00, A11, A22, A33. 
Condition for Principal Diagonal: The row-column condition is row = column. 
The secondary diagonal is formed by the elements A03, A12, A21, A30.
Condition for Secondary Diagonal: The row-column condition is row = numberOfRows – column -1.
refer(gfg)
"""
