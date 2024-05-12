def add_lst_digits(num):
    return [1 if i_num % 2 == 0 or i_num == 0 else i_num % 5 for i_num in range(num)]


num = int(input("Введите длину списка: "))
print(f"\nРезультат: {add_lst_digits(num)}")
###########################################################################


def change_numbers():
    print(
        f'Результат: {
        [
            1 if i_num % 2 == 0 else i_num % 5
            for i_num in range(int(input("Введите длину списка: ")))
        ]
    }'
    )


change_numbers()
