def revers_letters(simbols):
    new_simbols = []
    for i in range(len(simbols)):
        if simbols[i] == "h":
            new_simbols.insert(0, i)
    return simbols[new_simbols[0] - 1 : new_simbols[-1] : -1]


simbols = "hhqwerh"
print(
    f"\nРазвёрнутая последовательность между первым и последним h: {revers_letters(simbols)}"
)

#############################################################################################
# Покопался ещё в методах строк (ведь мы здесь имеем дело со строковым типом данных)
# и вот такое решение получилось!

simbols = "hhqwerh"

simb_first = simbols.index("h")
simb_last = simbols.rindex("h")

print(
    f"\nРазвёрнутая последовательность между "
    f"первым и последним h: {simbols[simb_last - 1 : simb_first : -1]}"
)
