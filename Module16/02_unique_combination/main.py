# TODO здесь писать код


# Пример использования:


def merge_sorted_lists(list1, list2):
    for i_elem in list1:
        for j_elem in list2:
            if i_elem == j_elem:
                list2.remove(j_elem)
    list1.extend(list2)
    return sorted(list1)


def main():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10, 5]
    merged = merge_sorted_lists(list1, list2)
    print(merged)


main()


def merge_sorted_lists(list1, list2):
    merged = []
    for i_elem in list1:
        if i_elem not in merged:
            merged.append(i_elem)

    for j_elem in list2:
        if j_elem not in merged:
            merged.append(j_elem)
    return merged


def main():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10, 5]
    merged = merge_sorted_lists(list1, list2)
    print(merged)


main()


def merge_sorted_lists(lst_first, lst_second):
    lst_first.extend(lst_second)
    merged = []
    for i_elem in lst_first:
        if i_elem not in merged:
            merged.append(i_elem)

    return sorted(merged)



list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10, 5]
merged = merge_sorted_lists(list1, list2)
print(merged)



