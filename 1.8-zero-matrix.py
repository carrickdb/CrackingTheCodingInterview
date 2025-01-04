def zeroMatrix(matrix):
    rowHasZero = 0 in matrix[0]
    colHasZero = False
    for row in matrix:
        if row[0] == 0:
            colHasZero = True
            break
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for row in matrix:
                row[j] = 0
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
    if rowHasZero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if colHasZero:
        for row in matrix:
            row[0] = 0

matrix = [
    [1,1,1],
    [1,0,1],
    [0,1,1],
    [6,4,2]
]
# matrix = [[0]]
zeroMatrix(matrix)

for row in matrix:
    print(row)
