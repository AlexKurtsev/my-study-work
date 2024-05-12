# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):

numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]

# Конкретно для этого списка или аналогичным образом составленного:

for i in range(len(numbers_list) - 1, -1, -1):
    if i % 2 != 0:
        print(numbers_list[i], end=' ')

# Для всех остальных:
# Опробовал этот код на нескольких случайным образом составленных списках...работает!
# В условиях задачи нет требования вывести результат списком, поэтому просто числовой ряд.


numbers_list = [1, 2, 8, 14, 7, 3, 17, 20, 9, 10, 11, 6]
# numbers_list = [1, 2, 8, 13, 15, 3, 17, 20, 9, 41, 27, 6]

count = len(numbers_list)

while count > 0:
    if numbers_list[count - 1] % 2 != 0:
        numbers_list.remove(numbers_list[count - 1])
    count -= 1

for j in range(len(numbers_list) - 1, -1, -1):
    print(numbers_list[j], end=' ')


# А этот вариант с использованием random:


from random import randint

numbers_list = []

for i in range(15):
    numbers_list.append(randint(1, 100))
print(numbers_list)

count = len(numbers_list)

while count > 0:
    if numbers_list[count - 1] % 2 != 0:
        numbers_list.remove(numbers_list[count - 1])
    count -= 1

for j in range(len(numbers_list) - 1, -1, -1):
    print(numbers_list[j], end=' ')












