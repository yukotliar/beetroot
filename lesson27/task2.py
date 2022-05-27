# Simulation: Hot Potato

from queue import Queue
from random import randint


def hot_potato(players: Queue):
    round = 1
    while players.size() != 1:
        random_number = randint(2, 15)
        for i in range(random_number):
            team_member = players.dequeue()
            players.enqueue(team_member)
        looser = players.dequeue()
        print(f'У {round} колі пробігло {random_number} гравців, на жаль {looser} вибув.')
        round += 1
    winner = players.dequeue()
    print(f'ПЕРЕМОЖЕЦЬ: {winner} ')
    return winner


players = Queue()
players.enqueue('SerhiiM')
players.enqueue('Iryna')
players.enqueue('Sofiya')
players.enqueue('Alexandr')
players.enqueue('Kostyantyn')
players.enqueue('Olena')
players.enqueue('Svyatoslav')
players.enqueue('Yuriy')
players.enqueue('Dmytro')
players.enqueue('Polina')
players.enqueue('Elenka')
players.enqueue('Yaroslava')
players.enqueue('SerhiiS')

hot_potato(players)
