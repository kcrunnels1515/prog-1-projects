#!/usr/bin/env python3

class Pakuri:
    def __init__(self, species):
        # initialize class attribs
        self.species = species
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13
    # return pakuri species string
    def get_species(self):
        return self.species
    # return pakuri attack int
    def get_attack(self):
        return self.attack
    # return pakuri defense int
    def get_defense(self):
        return self.defense
    # return pakuri speed int
    def get_speed(self):
        return self.speed
    # set pakuri attack int
    def set_attack(self, new_attack):
        self.attack = new_attack
    # change pakuri stats
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
