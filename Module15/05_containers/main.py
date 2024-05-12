# TODO здесь писать код

kol_containers = int(input('Количество контейнеров: '))

containers = []

for i in range(kol_containers):
    weight_containers = int(input('Введите вес контейнера: '))
    while weight_containers > 200:
        print(f'Вес контейнера превышает максимальный вес в 200 кг!')
        weight_containers = int(input(f'Введите вес контейнера еще раз: '))

    containers.append(weight_containers)

new_container = int(input('Введите вес нового контейнера: '))

count = 1  # Здесь сразу присвоил 1, а ниже - в print добавил.
for container in containers:
    if container >= new_container:
        count += 1

print(f'Номер, который получит новый контейнер: {count}')

# count = 0
#
# while count < len(containers) and containers[count] >= new_container:
#     count += 1
#
# print(f'Номер, который получит новый контейнер: {count + 1}')
