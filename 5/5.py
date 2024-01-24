# 3 Вариант

string = input('Введите строку с символами ".": ')
mutatedString = ''
deletedDotsCount = 0

for i in range(len(string)):
    if string[i] == '.':
        deletedDotsCount += 1
    else:
        mutatedString += string[i]

print(mutatedString)
print('Удалено', deletedDotsCount, 'точек')
