def is_biggest_word(enter_string):

    big_word = " "
    for i_word in enter_string:
        if len(i_word) > len(big_word):
            big_word = i_word
        elif len(i_word) == len(big_word):
            big_word = enter_string[0]
    return big_word


enter_string = input("Введите строку: ").split()

print(f"Самое длинное слово: {is_biggest_word(enter_string)}")
print(f"Длина этого слова: {len(is_biggest_word(enter_string))} букв(ы).")

# Но я не успокоился на первом варианте, вот что-то мне в нём не понравилось, как будто двоечник сделал
# и решил покопаться поглубже! И в документации нашёл информацию, более подробную, про функцию max!
# И "О Эврика!!!" Как оказывается всё можно сделать гораздо проще!

enter_string = input("Введите строку: ").split()
biggest_word = max(enter_string, key=len)
print(
    f"Самое длинное слово: {biggest_word}. Длина этого слова: {len(biggest_word)} букв(ы)."
)
