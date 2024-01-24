import math

# 3 Вариант

def rightTriangleHypotenuseCalculate(firstLeg: float, secondLeg: float) -> float:
    return math.sqrt(math.pow(firstLeg, 2) + math.pow(secondLeg, 2))

firstTriangle = []
secondTriangle = []

firstTriangle.append(float(input('Первый катет первого прямоугольного треугольника: ')))
firstTriangle.append(float(input('Второй катет первого прямоугольного треугольника: ')))

secondTriangle.append(float(input('Первый катет второго прямоугольного треугольника: ')))
secondTriangle.append(float(input('Второй катет второго прямоугольного треугольника: ')))

firstHypotenuse = rightTriangleHypotenuseCalculate(firstTriangle[0], firstTriangle[1])
secondHypotenuse = rightTriangleHypotenuseCalculate(secondTriangle[0], secondTriangle[1])

if firstHypotenuse > secondHypotenuse:
    print('Гипотенуза первого треугольника', firstHypotenuse, 'больше второго', secondHypotenuse)
elif secondHypotenuse > firstHypotenuse:
    print('Гипотенуза второго треугольника', secondHypotenuse, 'больше первого', firstHypotenuse)
else:
    print('Гипотенузы равны', firstHypotenuse)

# Вторая часть задания

string = input('Ввведите строку: ')
words = string.split(' ')

for wordIndex in range(len(words)):
    for i in range(len(words[wordIndex])):
        for j in range(len(words[wordIndex])):
            if ord(words[wordIndex][i]) < ord(words[wordIndex][j]):
                tempSymbol = words[wordIndex][j]
                words[wordIndex] = words[wordIndex][:j] + words[wordIndex][i] + words[wordIndex][j + 1:]
                words[wordIndex] = words[wordIndex][:i] + tempSymbol + words[wordIndex][i + 1:]

print(' '.join(words))
