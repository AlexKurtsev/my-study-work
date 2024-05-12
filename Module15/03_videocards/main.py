# TODO здесь писать код


old_list = [3070, 2060, 3090, 3070, 3090]

new_list = []

for i in range(len(old_list)):
    if old_list[0] >= old_list[i]:
        new_list.append(old_list[i])


print(f'\nСтарый список видеокарт: {old_list}\nНовый список видеокарт: {new_list}')


# Вот такой ещё вариант предложу на Ваш суд:


old_list = [3070, 2060, 3090, 3070, 3090]
old_list_max = max(old_list)
new_list = []

for i in old_list:
    if old_list_max > i:
        new_list.append(i)

print(f'\nСтарый список видеокарт: {old_list}\nНовый список видеокарт: {new_list}')











