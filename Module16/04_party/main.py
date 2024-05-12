def get_guest_in(guests):
    name = input(f"Имя гостя: ").title()
    print(f"Привет, {name}!")
    guests.append(name)


def get_too_many_guest():
    name = input(f"Имя гостя: ").title()
    print(f"Прости, {name}, но мест нет.")


def get_guest_out(guests):
    name = input(f"Имя гостя: ").title()
    print(f"Пока, {name}!")
    guests.remove(name)


def main_menu():
    guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
    while True:
        print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
        answer = input(f"Гость пришёл или ушёл? ").lower()

        if answer == "пора спать":
            print("Вечеринка закончилась, все легли спать.")
            break

        elif answer in ["пришёл", "пришел"] and len(guests) < 6:
            get_guest_in(guests)

        elif answer in ["пришёл", "пришел"] and len(guests) == 6:
            get_too_many_guest()

        elif answer in ["ушёл", "ушел"]:
            get_guest_out(guests)


main_menu()
##############################################################################


def is_guests(guests, guest_behavior):
    name = input(f"Имя гостя: ").title()
    if guest_behavior in ["пришёл", "пришел"] and len(guests) < 6:
        print(f"Привет, {name}!")
        guests.append(name)
        return guests

    if guest_behavior in ["пришёл", "пришел"] and len(guests) == 6:
        print(f"Прости, {name}, но мест нет.")

    if guest_behavior in ["ушёл", "ушел"]:
        print(f"Пока, {name}!")
        guests.remove(name)
        return guests


guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    answer = input(f"Гость пришёл или ушёл? ").lower()
    if answer != "пора спать":
        is_guests(guests, answer)
    else:
        print("Вечеринка закончилась, все легли спать.")
        break
