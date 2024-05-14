nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]

print(
    [
        third_level
        for first_level in nice_list
        for second_level in first_level
        for third_level in second_level
    ]
)
#####################################################################################

def is_third_level(second_level):
    for third_level in second_level:
        new_list.append(third_level)


def is_second_level(first_level):
    for second_level in first_level:
        is_third_level(second_level)


def is_first_level(nice_list):
    for first_level in nice_list:
        is_second_level(first_level)


new_list = []
nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]
is_first_level(nice_list)
print(new_list)