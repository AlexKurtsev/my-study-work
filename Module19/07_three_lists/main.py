array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]

print(
    "\nРешение без множеств: ", *[i for i in array_1 if i in array_2 and i in array_3]
)
print(
    "Решение без множеств: ",
    *[i for i in array_1 if i not in array_2 and i not in array_3]
)


print("\nРешение со множествами: ", *set(array_1).intersection(array_2, array_3))
print("Решение со множествами: ", *set(array_1).difference(array_2, array_3))

#########################################################################################


def is_not_array(array_1, array_2, array_3):
    return [i for i in array_1 if i in array_2 and i in array_3], [
        i for i in array_1 if i not in array_2 and i not in array_3
    ]


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
solution_1, solution_2 = is_not_array(array_1, array_2, array_3)

print("\nРешение без множеств: ", *solution_1)
print("Решение без множеств: ", *solution_2)


def is_array(array_1, array_2, array_3):
    return set(array_1).intersection(array_2, array_3), set(array_1).difference(
        array_2, array_3
    )


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
solution_1, solution_2 = is_array(array_1, array_2, array_3)

print("\nРешение с множествами: ", *solution_1)
print("Решение с множествами: ", *solution_2)

##########################################################################################


def is_not_array(array_1, array_2, array_3):
    sol_1 = [i for i in array_1 if i in array_2 and i in array_3]
    sol_2 = [i for i in array_1 if i not in array_2 and i not in array_3]
    sol_3 = set(array_1).intersection(array_2, array_3)
    sol_4 = set(array_1).difference(array_2, array_3)

    print("\nРешение без множеств (1): ", *sol_1)
    print("Решение без множеств (2):  ", *sol_2)
    print("\nРешение с множествами (1): ", *sol_3)
    print("Решение с множествами (2): ", *sol_4)


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


is_not_array(array_1, array_2, array_3)
