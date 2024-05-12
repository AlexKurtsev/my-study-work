# TODO здесь писать код
def is_min_devider(number):
    for i in range(2, number):
        if number % i == 0: return i


number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {is_min_devider(number)}.')

# Еще такой вариант:

import math


def min_devider(n):
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0: return i
    i += 1
  return n

print(f'Наименьший делитель, отличный от единицы: {min_devider(int(input('Введите число: ')))}.')
