string = input("Введите строку: ")

cipher_list = []
counter = 1

for i_letter in range(len(string)):
    if string[i_letter] == string[i_letter + 1 : i_letter + 2]:
        counter += 1

    else:
        cipher_list.append(string[i_letter] + str(counter))
        counter = 1

print(f"\nЗакодированная строка: {"".join(cipher_list)}")


# Получилось через срез! Первоначально делал: string[i_letter] == string[(i_letter + 1) % len(string)](вариант 2),
# в строке "aaaabbсaa" ну всё видит, кроме последних двух "aa"! Причём, стоит после них поставить другие буквы, например: "aaaabbсaag", считывает всё,
# но в таком варианте ("aaaabbсaa") не видит и всё тут! А другие строки из примеров кодирует! Прямо, действительно, волшебная строка!


# string = input("Введите строку: ")
#
# cipher_list = []
# counter = 1
#
# for i_letter in range(len(string)):
#     if string[i_letter] == string[(i_letter + 1) % len(string)]:
#         counter += 1
#
#     else:
#         cipher_list.append(string[i_letter] + str(counter))
#         counter = 1
#
# print("\nЗакодированная строка:", "".join(cipher_list))
