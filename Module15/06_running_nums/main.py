# TODO здесь писать код

# Изначально я сделал вариант решения №2. Так как мы в этом модуле не проходили срезы,
# упор был на индексы, то я и сосредоточился в решении именно через них!
# Но тут возникла проблема: если нужно сделать именно бегущую строку, а не просто сдвинуть элементы списка,
# то при сдвиге равном 1, это реально (для меня), но вот когда сдвиг больше, то выходишь за диапазон и ошибка!
# В телеграмм-чате все решают через срезы, я, как-бы, поверхностно знал о их существовании,
# немного поизучал этот вопрос и сделал используя этот способ. Не знаю, имел право или нет на данном этапе...
# Срезы, конечно, упростили всё!


kol_el = int(input('Введите количество элементов в списке: '))
lst_numbers = []

for i in range(kol_el):
    element = int(input(f'Ведите {i + 1} элемент списка: '))
    lst_numbers.append(element)

coefficient = int(input('Введите коэффициент сдвига: '))

print('\nИзначальный список:', lst_numbers)
print('\nСдвинутый список: ')

for i in range(len(lst_numbers)):
    lst_numbers = lst_numbers[-coefficient:] + lst_numbers[:-coefficient]
    print(lst_numbers)



# Вариант № 2:



kol_el = int(input('Введите количество элементов в списке: '))
lst_numbers = []

for i in range(kol_el):
    element = int(input(f'Ведите {i + 1} элемент списка: '))
    lst_numbers.append(element)

coefficient = int(input('Введите коэффициент сдвига: '))
count = 0
iteration = kol_el - coefficient

print('\nИзначальный список: ', *lst_numbers)
print(f'\nСдвинутый список: ')

while count < iteration:

    for index, i in enumerate(lst_numbers):
        index -= coefficient

        print(f'{lst_numbers[index]}', end=' ')
    coefficient += 1
    count += 1
    print()



# Вот мой вариант с бегущей строкой, если только сдвиг равен 1.



kol_el = int(input('Введите количество элементов в списке: '))
lst_numbers = []

for i in range(kol_el):
    element = int(input(f'Ведите {i + 1} элемент списка: '))
    lst_numbers.append(element)

coefficient_two = coefficient = int(input('Введите коэффициент сдвига: '))
count = 0

print('\nИзначальный список: ', *lst_numbers)
print(f'\nСдвинутый список: ')

while count < 15:  # Здесь разумеется можно while True и count'ы убрать за ненадобностью.

    for index, i in enumerate(lst_numbers):
        index -= coefficient
        if -index == kol_el:
            coefficient = 0
            index -= coefficient

        print(f'{lst_numbers[index]}', end=' ')
    coefficient += coefficient_two
    count += 1
    print()
