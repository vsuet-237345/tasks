inputFile = open('Тимошенко-Родион-Валерьевич_зит-23м_vvod1.txt')
n = int(inputFile.readline())
matrix = []

for i in range(n):
    matrixRow = []
    rowValues = inputFile.readline().split(' ')
    for value in rowValues:
        matrixRow.append(int(value))
    matrix.append(matrixRow)

inputFile.close()

isSymmetricMatrix = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            isSymmetricMatrix = False

outputFile = open('Тимошенко-Родион-Валерьевич_зит-23м_vivod1.txt', 'w')

for i in range(n):
    for j in range(n):
        outputFile.write(str(matrix[i][j]))
        if j != n - 1:
            outputFile.write(' ')
    outputFile.write('\n')

if isSymmetricMatrix:
    outputFile.write('Матрица семметрична')
else:
    outputFile.write('Матрица не семметрична')

outputFile.close()
