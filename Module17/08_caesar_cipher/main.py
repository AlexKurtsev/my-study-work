def is_Caesar_cipher(message, alphabet, shift):
    encrypted_message = ""
    for i_message in message:
        if i_message in alphabet:
            encrypted_message += alphabet[
                (alphabet.index(i_message) + shift) % len(alphabet)
            ]
        else:
            encrypted_message += i_message
    return encrypted_message


def main_menu():
    message = input("Введите сообщение: ")
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shift = int(input("Введите сдвиг: "))
    print(f"Зашифрованное сообщение: {is_Caesar_cipher(message, alphabet, shift)}")


main_menu()


###############################################################################################
# С использованием list comprehensions:
def is_Caesar_cipher(message, alphabet, shift):
    encrypted_message = [
        (
            alphabet[(alphabet.index(i_message) + shift) % len(alphabet)]
            if i_message in alphabet
            else " "
        )
        for i_message in message
    ]
    return encrypted_message


def main_menu():
    message = input("Введите сообщение: ").lower()
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shift = int(input("Введите сдвиг: "))
    print(
        f"Зашифрованное сообщение: {"".join(is_Caesar_cipher(message, alphabet, shift))}"
    )


main_menu()
