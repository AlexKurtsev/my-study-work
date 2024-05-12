# TODO здесь писать код
# Мы нечто подобное уже решали.
# Ну так как модуль про списки, написал по-разному!

world = input('Введите слово: ')
new_world = ''
for i in world:
    new_world = i + new_world

if new_world == world:
    print(f'Слово "{world}" - палиндром!')

else:
    print(f'Слово "{world}" - не палиндром!')

###


world = [i for i in (input('Введите слово: '))]

new_world = world[:]
new_world.reverse()
palindrom = ''

if world == new_world:
    for i in world:
        palindrom += i
    print(f'Слово "{palindrom}" - палиндром!')

else:
    for i in world:
        palindrom += i
    print(f'Слово "{palindrom}" - не палиндром!')

# В принципе, циклы чтобы выводы привычней глазу смотрелись, можно и без них,
# если выводов достаточно! Просто: либо палиндром, либо нет!

# Ну и вот так ещё:

world = input('Введите слово: ')
new_world = world[::-1]


if new_world == world:
    print(f'Слово "{world}" - палиндром!')

else:
    print(f'Слово "{world}" - не палиндром!')

# Здесь, правда, через строки. Можно через список, просто лишняя строка (world = list(world))
# На Ваше усмотрение, Вячеслав, если все эти решения не то - переделаю!