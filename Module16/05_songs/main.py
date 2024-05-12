def choose_songs():
    for i_song in violator_songs:
        if my_choose == i_song[0]:
            my_songs_lst.append(i_song[1])
    return my_songs_lst


violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83],
]
my_songs_lst = []

for i in range(int(input(f"Сколько песен выбрать? "))):
    my_choose = input(f"Название {i + 1} песни: ")
    choose_songs()
print(f"\nОбщее время звучания песен: {round(sum(my_songs_lst), 2)} минуты")
