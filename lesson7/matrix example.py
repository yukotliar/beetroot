matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
matrix1 = [[j for j in range(1 + 4 * i, 5 + 4 * i)] for i in range(3)]
print(matrix)
print(matrix1)
matrix = []
for i in range(3):
    matrix_insert = []
    for j in range(1 + 4 * i, 5 + 4 * i):
        matrix_insert.append(j)
    matrix.append(matrix_insert)

matrix[1][1]