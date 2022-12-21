# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# Вводим число
num = int(input('Enter number: '))
# создаем пустой список, в него будут добавлятся елементы
num_list = []
# создаем переменную для суммирования элементов
result = 0
# счетчик по перебору элементов до num  заданного числа
for i in range(num):
    # т.к. делить на ноль нельзя .... мы увеличиваем счетчик на 1
    i += 1
    # преобразуем все числа в заданном диапазоне по этой формуле
    variation = (1 + 1/i)**i
    #суммируем получившиеся элементы
    result = result + variation
    # выставляем количество знаков после запятой
    num_list.append(round(variation, 2))
# выводим результаты
print(round(result, 2))
print(num_list)