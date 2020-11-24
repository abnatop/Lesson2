# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

winter = 'Зима'
spring = 'Весна'
summer = 'Лето'
autumn = 'Осень'

seasons_list = [
    winter, winter,
    spring, spring, spring,
    summer, summer, summer,
    autumn, autumn, autumn,
    winter
]

seasons_dict = {
    1: winter,
    2: winter,
    3: spring,
    4: spring,
    5: spring,
    6: summer,
    7: summer,
    8: summer,
    9: autumn,
    10: autumn,
    11: autumn,
    12: winter
}
month_number = int(input('Введите номер месяца от 1 до 12: '))
print(f'Месяц номер {month_number} относится к времени года {seasons_dict[month_number]}')
print(f'Месяц номер {month_number} относится к времени года {seasons_list[month_number - 1]}')
