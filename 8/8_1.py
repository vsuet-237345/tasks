# 3 Вариант

n = int(input('Введите размер квадратной матрицы: '))

matrix = []

for i in range(n):
    matrixRow = []
    for j in range(n):
        matrixRow.append(int(input('Введите [{0:d}, {1:d}] элемент: '.format(i, j))))
    matrix.append(matrixRow)

isSymmetricMatrix = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            isSymmetricMatrix = False

for i in range(n):
    print(matrix[i])

if isSymmetricMatrix:
    print('Матрица семметрична')
else:
    print('Матрица не семметрична')
