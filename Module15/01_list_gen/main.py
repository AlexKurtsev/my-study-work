# TODO здесь писать код


number = int(input('Введите число: '))
odd_number = []

for i in range(1, number + 1, 2):
    odd_number.append(i)

print(odd_number)

# Про списки сам заранее дополнительные материалы посматривал и знаю, что прямо внутри
# объявленного списка  можно  записать. Просто для себя такую форму записи отметил,
# уж больно она оригинальная! Практиковал по мере решения текущих задач в этом модуле! Работает!:)


odd_number = [num for num in range(1, int(input('Введите число: ')) + 1, 2)]
print(odd_number)


