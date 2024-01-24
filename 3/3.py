import math

# 3 Вариант

bigNumber = input('Введите число: ')
evenNumbers = []
oddNumbers = []

for number in bigNumber:
    if math.fmod(int(number), 2):
        oddNumbers.append(number)
    else:
        evenNumbers.append(number)

print('Четные цифры ', evenNumbers)
print('Нечетные цифры ', oddNumbers)
