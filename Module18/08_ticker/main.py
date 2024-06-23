string_first = input("Первая строка: ")
string_second = input("Вторая строка: ")
shift = 0
flag = False

for i_letter in range(len(string_first)):

    if string_first != string_second:
        string_second = string_second[-1] + string_second[:-1]
        if string_second == string_first:
            flag = True

        shift += 1

if flag:
    print(f"\nПервая строка получается из второй со сдвигом {shift}.")
else:
    print("\nПервую строку нельзя получить из второй с помощью циклического сдвига.")
########################################################################################

string_first = input("Первая строка: ")
string_second = input("Вторая строка: ")
shift = 0

for i_letter in range(len(string_first)):

    if string_first != string_second:
        string_second = string_second[-1] + string_second[:-1]
        shift += 1
    elif string_first == string_second:
        print(f"\nПервая строка получается из второй со сдвигом {shift}.")
        break

else:
    print("\nПервую строку нельзя получить из второй с помощью циклического сдвига.")
#######################################################################################


def is_ticker(string_first, string_second):
    shift = 0
    for i_letter in range(len(string_first)):

        if string_first != string_second:
            shift += 1
            string_second = string_second[-1] + string_second[:-1]

        else:
            print(f"\nПервая строка получается из второй со сдвигом {shift}.")
            break

    else:
        print(
            "\nПервую строку нельзя получить из второй с помощью циклического сдвига."
        )
    return shift


def main_menu():
    string_first = input("Первая строка: ")
    string_second = input("Вторая строка: ")
    is_ticker(string_first, string_second)


main_menu()
