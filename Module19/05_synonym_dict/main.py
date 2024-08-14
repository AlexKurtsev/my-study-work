# count = int(input("Введите количество пар слов: "))
# dct_word = dict()
#
# for i in range(count):
#     frs_word, scd_word = (
#         input(f"Введите {i + 1} пару (через дефис): ").title().split("-")
#     )
#     dct_word[frs_word] = scd_word
#
# while True:
#     flag = False
#     word = input("Введите слово: ").title()
#     for i_key, i_value in dct_word.items():
#
#         if word == i_key:
#             print(f"Синоним: {i_value}")
#             flag = True
#         elif word == i_value:
#             print(f"Синоним: {i_key}")
#             flag = True
#
#     if not flag:
#         print("Ошибка, такого слова нет в словаре!")
####################################################################################

count = int(input("Введите количество пар слов: "))
dct_word = dict()

for i in range(count):
    frs_word, scd_word = (
        input(f"Введите {i + 1} пару (через дефис): ").title().split("-")
    )
    dct_word[frs_word] = scd_word

while True:

    word = input("Введите слово: ").title()
    for i_key in dct_word:
        if word in dct_word.get(i_key, dct_word[i_key]):
            print("ок")
        else:
            print("Ошибка, такого слова нет в словаре!")
