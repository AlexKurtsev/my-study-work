def is_counting(mens_list, number):
    start = 0
    for _ in range(len(mens_list) - 1):
        print(f"\nТекущий круг людей {mens_list}")
        start_count = start % len(mens_list)
        start = (start_count + number - 1) % len(mens_list)
        print(f"Начало счёта с номера {mens_list[start_count]}")
        print(f"Выбывает человек под номером {mens_list[start]}")
        mens_list.remove(mens_list[start])
    return mens_list


mens_list = [i for i in range(1, int(input(f"Кол-во человек: ")) + 1)]
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number} - й человек.")
print("\nОстался человек под номером: ", *is_counting(mens_list, number))

# С реализацией решения этой задачи в коде возникла конкретная засада! :)
# Не помню, что мы нечто подобное разбирали! Помогло объяснение одного человека
# на примере часов, и то не всё ясно! Решил методами подбора! :)
