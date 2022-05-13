first_name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

if age < 30 and weight in range(51,120):
    print(first_name, second_name, age, 'лет', weight, 'кг', ' - пациент в хорошем состоянии')
elif age in range (30, 40) and (weight < 50 or weight > 120):
    print(first_name, second_name, age, 'лет', weight, 'кг',' - пациенту требуется заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(first_name, second_name, age, 'лет', weight, 'кг',' - пациенту требуется врачебный осмотр')
else:
    print('end')

