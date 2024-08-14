goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}

store = {
    "12345": [
        {"quantity": 27, "price": 42},
    ],
    "23456": [
        {"quantity": 22, "price": 510},
        {"quantity": 32, "price": 520},
    ],
    "34567": [
        {"quantity": 2, "price": 1200},
        {"quantity": 1, "price": 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}


for i_key, i_value in goods.items():
    total_price = 0
    total_count = 0

    for i_list in range(len(store[i_value])):

        total_price += (
            store[i_value][i_list]["quantity"] * store[i_value][i_list]["price"]
        )
        total_count += store[i_value][i_list]["quantity"]

    print(f"{i_key} - {total_count} шт., стоимость {total_price} рублей.")
