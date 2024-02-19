import random


class Pokemon:
    def __init__(self, name, level, strength, speed, type):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.type = type
        self.life = 120

    def update_score_speed(self, num):
        self.speed += num


class Player:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons

    def pick_pokemon():
        random_pokemon = random.randint(1, 5)
