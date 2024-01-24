import math

# 3 Вариант

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

if b >= a:
    print('A должно быть больше B')
    exit()

print('Нечётные числа:')
for i in range(b, a):
    if math.fmod(i, 2):
        print(i)
