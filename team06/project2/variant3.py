# This is necessary to find the main code
import sys
sys.path.insert(0, '../../Bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../team06')
from clydeML import ClydeML


initial_seed = int(random.random()*500)
num_tries = 1
wins = 0
winning_seeds = []
for i in range(num_tries):
    random.seed(initial_seed+i)
    # Create the game
    g = Game.fromfile('map.txt')

    g.add_monster(SelfPreservingMonster("selfpreserving", # name
                                "S",              # avatar
                                3, 9,             # position
                                1                 # detection range
    ))
    
    g.add_character(ClydeML("me", # name
                                "C",  # avatar
                                0, 0,  # position
                                filename="variant1-3.json"
    ))
    if g.go(1):
        wins += 1
        winning_seeds.append(initial_seed + i)
    # input()

print(f"Guy won {wins} times out of {num_tries} iterations, winning seeds were: {winning_seeds}")
