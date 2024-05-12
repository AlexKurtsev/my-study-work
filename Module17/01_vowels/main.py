def add_vowel_letters(text):
    lst_letters = [i_lets for i_lets in text if i_lets in "аеёиоуыэюя"]
    print(f"\nСписок гласных букв: {lst_letters}")
    print(f"Длина списка: {len(lst_letters)}")


text = input("Введите текст: ")
add_vowel_letters(text)


########################################################################
def add_vowel_letters(text):
    return [i_lets for i_lets in text if i_lets in "аеёиоуыэюя"]


text = input("Введите текст: ")
lst_letters = add_vowel_letters(text)

print(f"\nСписок гласных букв: {lst_letters}")
print(f"Длина списка: {len(lst_letters)}")
