count = int(input("Введите количество заказов: "))
dct_menu = dict()
count_order = ["Первый", "Второй", "Третий", "Четвертый", "Пятый", "Шестой"]

for i in range(count):
    order = input(f"{count_order[i]} заказ: ").title().split()

    if order[0] not in dct_menu:
        dct_menu[order[0]] = {order[1]: int(order[2])}
    elif order[1] not in dct_menu[order[0]]:
        dct_menu[order[0]].update({order[1]: int(order[2])})
    else:
        dct_menu[order[0]][order[1]] += int(order[2])

for i, value in dct_menu.items():
    print(f"{i}:")
    sort_menu = dict(sorted(value.items()))
    for j, kol in sort_menu.items():
        print(f"\t {j}: {kol}")
################################################################################
count = int(input("Введите количество заказов: "))
dct_menu = dict()
count_order = ["Первый", "Второй", "Третий", "Четвертый", "Пятый", "Шестой"]

for i in range(count):
    order = input(f"{count_order[i]} заказ: ").title().split()

    if order[0] in dct_menu:
        if order[1] in dct_menu[order[0]]:
            dct_menu[order[0]][order[1]] += int(order[2])
        else:
            dct_menu[order[0]][order[1]] = int(order[2])
    else:
        dct_menu[order[0]] = {order[1]: int(order[2])}

for elem_1 in sorted(dct_menu):
    print(f"{elem_1}:")
    for elem_2 in sorted(dct_menu[elem_1]):
        print(f"\t {elem_2}: {dct_menu[elem_1][elem_2]}")
