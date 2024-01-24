# 3 Вариант

n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))

matrix = []

for i in range(n):
    matrixRow = []
    for j in range(m):
        matrixRow.append(int(input('Введите [{0:d}, {1:d}] элемент: '.format(i, j))))
    matrix.append(matrixRow)

for i in range(n):
    print(matrix[i])

bigItemPosition = [0, 0]
bigItem = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > bigItem:
            bigItem = matrix[i][j]
            bigItemPosition = [i, j]

# move rows
for i in range(m):
    tempItem = matrix[0][i]
    matrix[0][i] = matrix[bigItemPosition[0]][i]
    matrix[bigItemPosition[0]][i] = tempItem

# move columns
for i in range(n):
    tempItem = matrix[i][0]
    matrix[i][0] = matrix[i][bigItemPosition[1]]
    matrix[i][bigItemPosition[1]] = tempItem

print('Матрица после смещения: ')
for i in range(n):
    print(matrix[i])
