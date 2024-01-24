inputFile = open('Тимошенко-Родион-Валерьевич_зит-23м_vvod2.txt')
n = int(inputFile.readline())
m = int(inputFile.readline())

matrix = []

for i in range(n):
    matrixRow = []
    rowValues = inputFile.readline().split(' ')
    for value in rowValues:
        matrixRow.append(int(value))
    matrix.append(matrixRow)

inputFile.close()
outputFile = open('Тимошенко-Родион-Валерьевич_зит-23м_vivod2.txt', 'w')

for i in range(n):
    for j in range(m):
        outputFile.write(str(matrix[i][j]))
        if j != m - 1:
            outputFile.write(' ')
    outputFile.write('\n')

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

outputFile.write('Матрица после смещения:\n')
for i in range(n):
    for j in range(m):
        outputFile.write(str(matrix[i][j]))
        if j != m - 1:
            outputFile.write(' ')
    outputFile.write('\n')

outputFile.close()
