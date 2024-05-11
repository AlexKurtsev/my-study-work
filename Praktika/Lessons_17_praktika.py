# Задача 1. Кубы и квадраты
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне.
# Выведите списки на экран. Для генерации используйте list comprehensions (как и в следующих задачах).
#
#
#
# Пример:
#
# Левая граница: 5
#
# Правая граница: 10
#
#
#
# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
#
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

# kub = [i**3 for i in range(5, 11)]
# kvadrat = [j**2 for j in range(5, 11)]

# print(f"Список кубов чисел в диапазоне от 5 до 10: {[i**3 for i in range(5, 11)]}")
# print(f"Список квадратов чисел в диапазоне от 5 до 10: {[j**2 for j in range(5, 11)]}")
##########################################################################################

# Задача 2. Сообщение
# Илья решил безобидно подшутить над другом и написал программу для смартфона,
# которая при отправке сообщения удваивает каждый символ строки и заодно к каждому
# удвоенному добавляет ещё один дополнительный.
#
# Пользователь вводит строку и дополнительный символ. Напишите программу, которая
# генерирует два списка: в первом списке каждый элемент — удвоенная буква первой строки,
# во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа.
#
#
#
# Пример:
#
# Введите строку: привет
#
# Введите дополнительный символ: !
#
#
#
# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
#
# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']

# print(f"Список удвоенных символов: {[i * 2 for i in 'привет']}")
# print(f"Склейка с дополнительным символом: {[i * 2 + '!' for i in 'привет']}")
############################################################################################
# Задача 3. Повышение цен
# Дан список цен на пять товаров с точностью до копейки.
# Так как экономика даёт о себе знать, мы спрогнозировали,
# что через год придётся повышать цены на X процентов,
# а ещё через один год — ещё на Y процентов.
#
# Напишите программу, которая получает на вход список цен на товары
# (вещественные числа, список генерируется также с помощью list comprehensions)
# и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
#
#
# Пример:
#
# Цена на товар: 1.09
#
# Цена на товар: 23.56
#
# Цена на товар: 57.84
#
# Цена на товар: 4.56
#
# Цена на товар: 6.78
#
# Повышение на первый год: 0
#
# Повышение на второй год: 10
#
# Сумма цен за каждый год: 93.83 93.83 103.21


# lst_price = [float(input("Цена на товар: ")) for i in range(5)]
# n = [i + i * 0.1 for i in lst_price]
# print(round(sum(n), 2))
########################################################################################