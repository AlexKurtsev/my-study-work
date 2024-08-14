# while True:
#
#     user_string = input("Введите строку: ").lower()
#
#     dct_str = {
#         letter: user_string.count(letter)
#         for letter in user_string
#         if (ord(letter) >= 1072 and ord(letter) <= 1103)
#         or (ord(letter) >= 97 and ord(letter) <= 122)
#     }
#     print(dct_str)
#
#     set_letter = set()
#
#     for i_letter in dct_str:
#
#         if dct_str[i_letter] % 2 == 1:
#             set_letter.add(i_letter)
#
#     if len(set_letter) > 1:
#         print("Нельзя сделать палиндромом", set_letter)
#     else:
#         print("Можно сделать палиндромом", set_letter)


###############################################################################################
# def is_palindrom(dct_str):
#     set_letter = set()
#     for i_letter in dct_str:
#         if dct_str[i_letter] % 2 == 1:
#             set_letter.add(i_letter)
#
#     if len(set_letter) > 1:
#         print("Нельзя сделать палиндромом!")
#     else:
#         print("Можно сделать палиндромом!")
#
#
# def checking_conditions(user_string):
#     dct_str = {
#         letter: user_string.count(letter)
#         for letter in user_string
#         if (ord(letter) >= 1072 and ord(letter) <= 1103)
#         or (ord(letter) >= 97 and ord(letter) <= 122)
#     }
#     is_palindrom(dct_str)
#
#
# user_string = input("Введите строку: ").lower()
# checking_conditions(user_string)
#############################################################################
def print_display(set_letter):
    if len(set_letter) > 1:
        print("Нельзя сделать палиндромом!")
    else:
        print("Можно сделать палиндромом!")


def is_palindrom(dct_str):
    set_letter = set()
    for i_letter in dct_str:
        if dct_str[i_letter] % 2 == 1:
            set_letter.add(i_letter)
    print_display(set_letter)


def checking_conditions(user_string):
    dct_str = {
        letter: user_string.count(letter)
        for letter in user_string
        if (ord(letter) >= 1072 and ord(letter) <= 1103)
        or (ord(letter) >= 97 and ord(letter) <= 122)
    }
    is_palindrom(dct_str)


user_string = input("Введите строку: ").lower()
checking_conditions(user_string)

#############################################################################
# lst_1 = [chr(random.choice(range(1072, 1103))) for _ in range(10)]
# print(lst_1)
# Генерация 10 случайных букв русского алфавита
