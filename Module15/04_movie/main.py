films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

my_films = []
kol_films = int(input('Сколько фильмов хотите добавить? '))

for _ in range(kol_films):
    name_film = input('Введите название фильма: ')

    if name_film not in films:
        print(f'Ошибка: фильма {name_film} у нас нет :(')
    else:
        my_films.append(name_film)

print('\nВаш список любимых фильмов:', end=' ')
for i in my_films:
    print(i, end=' ')


# Или вариант без операторов not и in в условном if:
# Здесь я вывод сделал просто списком. В первом варианте
# я попытался реализовать тот же вывод, что и в примере условия задачи,
# получилось, конечно, коряво. Я изучил этот вопрос, но оставил так, как
# сделал бы на данном этапе.


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorit_films = []
count_films = int(input('Сколько фильмов хотите добавить? '))

for _ in range(count_films):
    name_film = input('Введите название фильма: ')
    flag = False
    for film in films:
        if name_film == film:
            flag = True
            favorit_films.append(name_film)

    if flag == False:
        print(f'Ошибка: фильма {name_film} у нас нет :(')
print('\nВаш список любимых фильмов:', favorit_films, end=' ')
