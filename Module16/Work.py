# [1, 2, 1, 2, 2]


count_numbers = int(input('Введите количество цифр в последовательности: '))
lst_nums = [int(input(f'Введите {i_num + 1} число: ')) for i_num in range(count_numbers)]
count = 0

for j_num in lst_nums:
    if lst_nums != lst_nums[::-1]:
        lst_nums.insert(count_numbers, j_num)
        count += 1
print(lst_nums, lst_nums[::-1], count)


# lst = [1, 2, 1, 2, 2, 1, 2, 1]
# print(lst[::-1])

