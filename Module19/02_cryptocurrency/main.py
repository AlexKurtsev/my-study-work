data = {
    "address": "0x544444444444",
    "ETH": {"balance": 444, "total_in": 444, "total_out": 4},
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False,
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0,
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False,
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0,
        },
    ],
}


# Задание № 1:

print(list(data.keys()))
print(list(data.values()))

# Или:

for i_keys, i_values in data.items():
    print(i_keys)
    print(i_values)

# Задание № 2:

data["ETH"]["total_diff"] = 100

# Или:

data["ETH"].update({"total_diff": 100})


# Задание № 3:

data["tokens"][0]["fst_token_info"]["name"] = "doge"

# Задание № 4:

data["ETH"]["total_out"] += data["tokens"][0].pop("total_out") + data["tokens"][1].pop(
    "total_out"
)

# Или:

count = 0
for i_elem in data["tokens"]:
    for j_elem in i_elem:
        if j_elem == "total_out":
            data["ETH"]["total_out"] += data["tokens"][count][j_elem]
            count += 1


for i in range(len(data["tokens"])):
    data["tokens"][i].pop("total_out")

# Задание № 5:

data["tokens"][0]["fst_token_info"]["total_price"] = data["tokens"][0][
    "fst_token_info"
].pop("price")

#######################

data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1][
    "sec_token_info"
].pop("price")
