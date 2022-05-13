number = int(input('Введите число: '))

while number < 0 or number > 10:
    print('введите число от 0 до 10')
    number = int(input('Введите число: '))
print(number ** 2)