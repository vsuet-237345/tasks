def reverse_number(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + reverse_number(n // 10)

number = int(input('Введите число: '))
reversed_number = int(reverse_number(number))
print(reversed_number)
