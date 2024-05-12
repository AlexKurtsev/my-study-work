def is_first(nums, num):
    new_lst = []
    count = 0
    for i_num in range(len(nums)):
        if nums != nums[::-1]:
            nums.insert(num, nums[i_num])
            count += 1
            new_lst.append(nums[i_num])
    print(f"Нужно приписать чисел: {count}")
    print(f"Сами числа: {new_lst[::-1]}")
    print(f"Симметричная последовательность: {nums}")


def is_second(nums):

    print(f"{nums} - этом случае ничего добавлять не нужно!")


def main_menu():
    number = int(input("Кол-во чисел: "))
    numbers = []

    for i in range(number):
        numbers.append(int(input("Введите число: ")))
    print(f"\nПоследовательность: {numbers}")
    if numbers != numbers[::-1]:
        is_first(numbers, number)
    else:
        is_second(numbers)


main_menu()
##################################################################################

number = int(input("Кол-во чисел: "))
numbers = []
new_lst = []

for i in range(number):
    numbers.append(int(input("Введите число: ")))
print(f"\nПоследовательность: {numbers}")
count = 0
flag = False

for i_num in range(len(numbers)):
    if numbers != numbers[::-1]:
        flag = True
        numbers.insert(number, numbers[i_num])
        count += 1
        new_lst.append(numbers[i_num])

if flag == True:
    print(f"\nНужно приписать чисел: {count}")
    print(f"Сами числа: {new_lst[::-1]}")
    print(f"Симметричная последовательность: {numbers}")

if flag == False:
    print(f"\n{numbers} - этом случае ничего добавлять не нужно!")
