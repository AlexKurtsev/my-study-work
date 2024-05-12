# TODO здесь писать код


def sort_nums_lst(lst_nums):
    for i in range(len(lst_nums)):
        for j in range(i, len(lst_nums)):

            if lst_nums[i] > lst_nums[j]:
                temp = lst_nums[j]
                lst_nums[j] = lst_nums[i]
                lst_nums[i] = temp
    return lst_nums


lst_nums = [1, 4, -3, 0, 10]

print(f'Изначальный список: {lst_nums}')
print(f'Отсортированный список: {sort_nums_lst(lst_nums)}')


# Ну и вдруг кто-нибудь захочет создать свой список:


def sort_nums_lst(list_nums):
    for i in range(len(list_nums)):
        for j in range(i, len(list_nums)):

            if list_nums[i] > list_nums[j]:
                temp = list_nums[j]
                list_nums[j] = list_nums[i]
                list_nums[i] = temp

    return list_nums


def get_input_parameters():
    lst_nums = []
    for i in range(int(input('Количество цифр в списке: '))):
        lst_nums.append(int(input(f'Введите {i + 1} число: ')))
    return lst_nums


lst_nums = get_input_parameters()
print(f'Изначальный список: {lst_nums}')
print(f'Отсортированный список: {sort_nums_lst(lst_nums)}')
