violator_songs = {
    "World in My Eyes": 4.86,
    "Sweetest Perfection": 4.43,
    "Personal Jesus": 4.56,
    "Halo": 4.9,
    "Waiting for the Night": 6.07,
    "Enjoy the Silence": 4.20,
    "Policy of Truth": 4.76,
    "Blue Dress": 4.29,
    "Clean": 5.83,
}
choise_songs = int(input("Сколько песен выбрать?: "))
time_song = 0

for i_song in range(choise_songs):
    name_song = input(f"Название {i_song + 1} песни: ")
    if name_song in violator_songs:
        time_song += violator_songs[name_song]

print(f"\nОбщее время звучания песен: {round(time_song, 2)} мин.")

############################################################################
# Хотел через LC сделать, но PyCharm форматирует так, что, по мне, не очень читабельно!
# Более наглядно выглядит первый вариант! Читающему будет куда проще!
# Я вообще написал еще с использованием get и item, но в качестве тренировок,
# не стал сюда громоздить всё до кучи!

choise_songs = int(input("Сколько песен выбрать?: "))
print(
    "\nОбщее время звучания песен: ",
    round(
        sum(
            [
                violator_songs[input(f"Название {i_song + 1} песни: ")]
                for i_song in range(choise_songs)
            ]
        ),
        2,
    ),
    "мин.",
)
