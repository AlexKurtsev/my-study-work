# Задача 1. Список чётных чисел
# Пользователь вводит два числа: А и В. Реализуйте код,
# который генерирует список из чётных чисел в диапазоне от А до B.
# Используйте list comprehensions (как и в следующих задачах).


n = [i for i in range(10) if i % 2 == 0]
print(n)

###############################################################################
# Задача 2. Магазин
# У нас есть вот такой список цен на некоторые товары из магазина:
#
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#
# В этом списке также хранятся цены на товары, которые уже давно не продаются.
# По какой-то причине система, вместо того чтобы их занулить, просто
# приписала к ним минус. Нам нужно это исправить.
#
# Напишите программу, которая генерирует новый список из первого списка,
# заменяя все отрицательные числа на ноль.
#
#
#
# Результат:
#
# [1.25, 0, 10.22, 3.78, 0, 1.16]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
duble_prices = [0 if i < 0 else i for i in original_prices]
print(duble_prices)
#######################################################################################

# Задача 3. Отряды
# Мы продолжаем пробовать себя в качестве разработчика игр.
# Теперь нужно написать небольшую логику поведения некоторых отрядов,
# а также их урон. Есть два отряда, в каждом по 10 монстров.
# В первом отряде у каждого монстра урон абсолютно случайный и
# колеблется от 50 до 80, а во втором — от 30 до 60. Оба отряда
# вместе напали на третий, также из 10 юнитов. Юнит третьего отряда
# погибает, если сумма урона от двух монстров больше 100.
#
# Напишите программу, которая генерирует случайные значения в первых
# двух списках в заданных диапазонах, а также генерирует список,
# состоящий из фраз «Погиб» или «Выжил». Выведите все списки на экран.
#
#
#
# Пример:
#
# Урон первого отряда: [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
#
# Урон второго отряда: [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
#
# Состояние третьего отряда: ['Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб',
# 'Погиб', 'Выжил', 'Погиб', 'Погиб', 'Выжил']
import random

squad_1 = [random.randint(50, 80) for i in range(10)]
print(squad_1)
squad_2 = [random.randint(30, 60) for j in range(10)]
print(squad_2)
squad_3 = [("Погиб" if squad_1[i] + squad_2[i] > 100 else "Выжил") for i in range(10)]
print(squad_3)
