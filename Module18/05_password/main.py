while True:
    password = input("Придумайте пароль: ")
    count = len([i_digit for i_digit in password if i_digit.isdigit()])
    big_letter = len([i_letter for i_letter in password if i_letter.isupper()])

    if (len(password) >= 8) and (count >= 3) and (big_letter >= 1):
        print("Это надёжный пароль!")
        break

    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

#################################################################################


def is_more_simbols():
    print("Пароль должен состоять из 8 символов! Попробуйте ещё раз.")


def invalid_simbol():
    print("Пароль должен состоять только из букв и цифр! Попробуйте ещё раз.")


def is_more_digit():
    print("Пароль должен включать как минимум три цифры. Попробуйте ещё раз.")


def is_more_bigletter():
    print(
        "Пароль должен включать как минимум одну заглавную букву! Попробуйте ещё раз."
    )


def main_menu():
    while True:
        password = input("Придумайте пароль: ")
        count = len([i_digit for i_digit in password if i_digit.isdigit()])
        big_letter = len([i_letter for i_letter in password if i_letter.isupper()])
        if len(password) < 8:
            is_more_simbols()
        elif not password.isalnum():
            invalid_simbol()
        elif count < 3:
            is_more_digit()
        elif big_letter < 1:
            is_more_bigletter()
        else:
            print("Это надёжный пароль!")
            break


main_menu()
