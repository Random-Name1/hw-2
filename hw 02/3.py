# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RI

run_int = RI(1, 1000)
print(run_int)
my_int = (run_int + (run_int % 10)**2)
print(int(my_int))