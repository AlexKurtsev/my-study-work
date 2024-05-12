import random


def is_winners_competition():
    team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
    team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
    winners = [
        team_1[i_num] if team_1[i_num] > team_2[i_num] else team_2[i_num]
        for i_num in range(20)
    ]
    print(team_1)
    print(team_2)
    print(winners)


is_winners_competition()
