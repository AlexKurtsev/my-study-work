# Задача 1. Задачи компаний
# Одна IT-компания решила расшириться и взяла под своё
# крыло ещё три таких же, но поменьше. Конечно же, все
# выполненные и невыполненные задачи этих компаний
# перетекли в основную компанию.
#
# Даны четыре списка компаний, в которых для каждой задачи
# написано, выполнена (1) она или нет (0):
#
#
#
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#
# first_company = [0, 0, 0]
#
# second_company = [1, 0, 0, 1, 1]
#
# third_company = [1, 1, 1, 0, 1]
#
#
#
# Напишите программу, которая расширяет список main элементами
# остальных списков, выведите итоговый список, а также
# выведите количество невыполненных задач.
#
#
#
# Результат работы программы:
#
#
#
# Общий список задач: [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
#
# Кол-во невыполненных задач: 10
#######################################################################

# def is_total_task(a, b, c, d):
#     count = 0
#     a.extend(b)
#     a.extend(c)
#     a.extend(d)
#     for i_task in a:
#         if i_task == 0:
#             count += 1
#     print(f"\nКол-во невыполненных задач: {count}")
#     return a
#
#
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
#
# print(
#     f"Общий список задач: {is_total_task(main, first_company, second_company, third_company)}"
# )

##########################################################################################
# Задача 2. Вредоносное ПО
# Гера решил попрактиковаться в программировании и захотел
# написать небольшой скрипт, который после двух сообщений
# отправляет ещё одно на основе первых двух.
#
# Пользователь вводит две строки. В каждой из них есть какое-то
# количество специальных символов ! и ?. Напишите программу,
# которая считает количество этих символов отдельно в первой
# строке и отдельно во второй. Если в первой строке их больше,
# чем во второй, то на экран выводится первая строчка,
# объединённая со второй, а иначе — вторая с первой. При равном
# количестве символов в строках выводится «Ой».
#
#
#
# Пример 1:
#
# Первое сообщение: Привет!
#
# Второе сообщение: Как дела? Что делаешь?
#
#
#
# Третье сообщение: Как дела? Что делаешь? Привет!
#
#
#
# Пример 2:
#
# Первое сообщение: Хм!!
# Второе сообщение: ?
# Третье сообщение: Хм!!?
##########################################################################

# def concatenate_rows(fm, sm):
#     m = fm.count("!") + fm.count("?")
#     n = sm.count("!") + sm.count("?")
#     print(m, n)
#     if m < n:
#         third_message = sm + " " + fm
#     if m > n:
#         third_message = fm + " " + sm
#
#     return f"{third_message}"
#
#
# first_message = "Хм!!"
# second_message = "?"
# print(concatenate_rows(first_message, second_message))
###########################################################################

# Задача 3. Пакеты
# При работе с сервером мы кодируем сообщение и отправляем
# его в виде пакетов информации. Их количество равно N.
# Допустим, каждый пакет содержит четыре числа, каждое из
# которых равно нулю или единице. Эти числа называются битами.
# Иногда в кодировке сообщения встречаются ошибки, и в пакете
# эта ошибка обозначается числом -1. Если таких ошибок не
# больше одной, то этот пакет мы целиком добавляем в список
# для декодирования, а иначе отбрасываем.
#
# Напишите программу, которая будет обрабатывать полученные
# пакеты и выведет на экран итоговое сообщение для декодирования,
# а также количество ошибок в нём и количество необработанных пакетов.
#
#
#
# Пример:
# Кол-во пакетов: 3
#
#
# Пакет номер 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1
#
#
# Пакет номер 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Много ошибок в пакете.
#
#
# Пакет номер 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1
#
#
# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Кол-во ошибок в сообщении: 1
# Кол-во потерянных пакетов: 1


def examination_pakets(new_paket, lost_lst):

    m = new_paket.count(-1)
    if m <= 1:
        received_message.extend(new_paket)
    if m > 1:
        print(f"Много ошибок в пакете.")
        lost_lst += 1
    return lost_lst


def main(kol_pakets):

    for i_paket in range(kol_pakets):
        print(f"\nПакет номер {i_paket + 1}:")
        new_paket = []
        for i_bit in range(4):
            new_paket.append(int(input(f"{i_bit + 1} бит: ")))
        examination_pakets(new_paket, lost_lst)


lost_lst = 0
received_message = []
kol_pakets = int(input("Введите количество пакетов: "))

main(kol_pakets)

print(f"Полученное сообщение: {received_message}")
print(f"Кол-во ошибок в сообщении: {received_message.count(-1)}")
print(f"Кол-во потерянных пакетов: {lost_lst}")
