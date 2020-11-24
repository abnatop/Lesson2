# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

REC_POS = 1 # индекс словаря в записи

database = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 2000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 2, 'ед': 'ед.'}),
    (4, {'название': 'принтер', 'цена': 8000, 'количество': 4, 'ед': 'шт.'})
]
product_card = {}
product_name = 'название'
product_price = 'цена'
product_count = 'количество'
product_unit = 'ед'

# counter = 1
# while True:
#     name = input('Введите название товара (или END для выхода): ')
#     if name == 'END':
#         break
#     price = input('Введите цену товара: ')
#     count = input('Введите количество товара: ')
#     unit = input('Введите единицу измерения товара: ')
#
#     product_card = {
#         product_name: name,
#         product_price: price,
#         product_count: count,
#         product_unit: unit
#     }
#     database.append(tuple((counter, product_card)))
#     counter += 1

product_names = []
product_prices = []
product_counts = []
product_units = []

for product in database:

    name = product[REC_POS][product_name]
    if name not in product_names:
        product_names.append(name)

    price = product[REC_POS][product_price]
    if price not in product_prices:
        product_prices.append(price)

    count = product[REC_POS][product_count]
    if count not in product_counts:
        product_counts.append(count)

    unit = product[REC_POS][product_unit]
    if unit not in product_units:
        product_units.append(unit)

print(product_names)
print(product_prices)
print(product_counts)
print(product_units)


