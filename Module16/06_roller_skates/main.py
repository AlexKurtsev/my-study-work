def is_count_people(skate_size, foot_size):
    count = 0
    for j in foot_size:
        for i in skate_size:
            if i == j:
                count += 1
                skate_size.remove(i)
    return count


def main_menu():
    skate_size = []
    foot_size = []
    for s_size in range(int(input(f"Кол-во коньков: "))):
        skate_size.append(int(input(f"Размер {s_size + 1} пары: ")))

    for f_size in range(int(input(f"\nКол-во людей: "))):
        foot_size.append(int(input(f"Размер ноги {f_size + 1} человека: ")))
    print(
        f"Наибольшее кол-во людей, которые могут взять ролики: {is_count_people(skate_size, foot_size)}"
    )


main_menu()
