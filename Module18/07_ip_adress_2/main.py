# ip = input("Введите IP: ")
# split_ip = ip.split(".")
# count_1 = 0
# count_2 = 0
# if len(split_ip) < 4:
#     print("Адрес - это четыре числа, разделенные точками")
# else:
#     for i in range(len(split_ip)):
#         if split_ip[i].isdigit():
#             count_2 += 1
#             if int(split_ip[i]) > 255:
#                 count_1 += 1
#                 print(f"{split_ip[i]} превышает 255")
#
#         else:
#             print(f"{split_ip[i]}- не целое число")
#
# if count_1 == 0 and count_2 == 4:
#     print("IP-адрес корректен")


####################################################################

while True:
    ip_address = input("Введите IP - адрес: ")
    ip_list = ip_address.split(".")
    count_digit = 0
    count_elem = 0
    if len(ip_list) == 4:
        for i_elem in range(len(ip_list)):
            if ip_list[i_elem].isdigit():
                count_digit += 1
                if int(ip_list[i_elem]) > 255:
                    count_elem += 1
                    print(
                        f"IP - адрес содержит элемент {ip_list[i_elem]}, "
                        f"он не может быть больше 255!"
                    )

            else:
                print(f"Элемент {ip_list[i_elem]} - не целое число!")

    else:
        print(f"IP - адрес — это четыре числа, разделённые точками.")

    if count_digit == 4 and count_elem == 0:
        print("IP-адрес корректен.")
        break

#######################################################################
# По началу задание показалось не слишком сложным, но по мере вхождения в него неожиданно проявились
# сложности! :) Решений шесть, наверное, перепробовал! Всё бы ничего, но условий слишком разных много!
# Проблема была вывести итоговый результат при корректном введений адреса. Он постоянно дублировался
# с другими принтами. Пробовал использовать флаг,
# но где его "поднять", а где "опустить", так чтобы без сучка и задоринки, так и не получилось!
# В итоге "родил" только вот такой вариант!
# На ваш суд!
