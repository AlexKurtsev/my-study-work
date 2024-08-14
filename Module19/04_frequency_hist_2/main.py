def is_invert_dict(original_text_dict):
    invert_dict = dict()
    for i_sym, value in original_text_dict.items():
        if value not in invert_dict:
            invert_dict[value] = [i_sym]
        else:
            invert_dict[value].append(i_sym)
    return invert_dict


def is_frequency_hyst(string_text):
    text_dict = dict()
    for i_let in string_text:
        if i_let in text_dict:
            text_dict[i_let] += 1
        else:
            text_dict[i_let] = 1
    return text_dict


text = input("Ввeдите текст: ")

hyst = is_frequency_hyst(text)
invert_hyst = is_invert_dict(hyst)

print("\nОригинальный словарь частот: ")
for i_sym in sorted(hyst.keys()):
    print(i_sym, ":", hyst[i_sym])

print("\nИнвертированный словарь частот: ")
for i_key in invert_hyst:
    print(i_key, ":", invert_hyst[i_key])


###################################################################################
# В этом варианте я создал оригинальный словарь через "словарь comprehensions"!


def is_invert_dict(original_text_dict):
    invert_dict = dict()
    for i_sym, value in original_text_dict.items():
        if value not in invert_dict:
            invert_dict[value] = [i_sym]
        else:
            invert_dict[value].append(i_sym)
    return invert_dict


def is_frequency_hyst(string_text):
    return {i_let: string_text.count(i_let) for i_let in string_text}


text = input("Ввeдите текст: ")

hyst = is_frequency_hyst(text)
invert_hyst = is_invert_dict(hyst)

print("\nОригинальный словарь частот: ")
for i_sym in sorted(hyst.keys()):
    print(i_sym, ":", hyst[i_sym])

print("\nИнвертированный словарь частот: ")
for i_key in invert_hyst:
    print(i_key, ":", invert_hyst[i_key])
