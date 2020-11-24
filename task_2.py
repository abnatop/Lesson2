# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

managed_list = []

while True:
    list_element = input('Введите элемент списка (или END для выхода): ')
    if list_element != 'END':
        managed_list.append(list_element)
    else:
        break

if len(managed_list) < 2:
    print('Кол-во элементов меньше двух, обмен значениями невозможен')
    exit()

print('Исходный список: ', managed_list)

for i in range(0, len(managed_list) - 1, 2):
    j = i + 1
    managed_list[i], managed_list[j] = managed_list[j], managed_list[i]

print('Измененный список: ', managed_list)
