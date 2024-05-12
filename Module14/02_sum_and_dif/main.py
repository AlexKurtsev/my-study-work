# TODO здесь писать код
def is_summ_digits(sum_num):
    summ_num = 0
    while sum_num > 0:
        summ_num += sum_num % 10
        sum_num //= 10
    return summ_num


def is_count_digits(cont_num):
    count = 0
    while cont_num > 0:
        cont_num //= 10
        count += 1
    return count


number = int(input('Введите число: '))
kol_dig = is_count_digits(number)
sum_dig = is_summ_digits(number)
print(f'\nСумма чисел: {sum_dig}')
print(f'Количество цифр в числе: {kol_dig}')
print(f'Разность суммы и количества цифр: {sum_dig - kol_dig}')
