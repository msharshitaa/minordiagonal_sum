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
"""