# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

test_list = []
test_type = [bool, int, float, str, list, dict]

test_list.append(True)
test_list.append(1)
test_list.append(2.2)
test_list.append('3')
test_list.append([7, 8, 9])
test_list.append({'a': 'Phase A', 'b': 'Phase B', 'c': 'Phase C'})

for i in range(0, len(test_list)):
    if type(test_list[i]) is test_type[i]:
        print(f'Элемент списка {test_list[i]} имеет тип {test_type[i]}.')
    else:
        print(f'Элемент списка {test_list[i]} должен иметь тип {test_type[i]}.')
