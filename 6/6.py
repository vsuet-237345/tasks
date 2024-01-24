import math

# 3 Вариант

d = []
n = int(input('Ввведите длину массива: '))

for i in range(n):
    currentValue = int(input('Ввведите {0:d} элемент: '.format(i)))
    d.append(currentValue)

print('Исходный массив:', d)

oddIndexesValueAmount = 0
for i in range(n):
    if math.fmod(i, 2):
        oddIndexesValueAmount += d[i]

print('Сумма элементов с нечетными индексами: ', oddIndexesValueAmount)

# Вторая часть задачи

positiveArray = []
negativeArray = []

for value in d:
    if value >= 0:
        positiveArray.append(value)
    else:
        negativeArray.append(value)

print('Массив с положительными числами: ', positiveArray)
print('Массив с отрицательными числами: ', positiveArray)
