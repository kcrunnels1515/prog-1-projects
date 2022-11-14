#!/usr/bin/env python3

from pakuri import *

class Pakudex:
    # initialize important attributes
    def __init__(self, capacity=20):
        self.pakuri_array = []
        self.size = len(self.pakuri_array)
        self.capacity = capacity
    # returns pakuri object given a pakuri species
    def ret_from_species(self, species):
        for i in self.pakuri_array:
            if i.get_species() == species:
                return i
        return None
    # return size of pakudex
    def get_size(self):
        return self.size
    # return capacity
    def get_capacity(self):
        return self.capacity
    # unused function to placate zybooks
    def get_species_array(self):
        final = []
        if self.pakuri_array == []:
            return None
        else:
            for i in self.pakuri_array:
                final.append(i.get_species())
            return final
    # actual function used in place of one above
    # returns list of Pakuri species in Pakudex
    def real_get_species_array(self):
        final = []
        for i in self.pakuri_array:
            final.append(i.get_species())
        return final

    # returns list of pakuri stats, if it is in the pakudex
    def get_stats(self, species):
        for i in self.pakuri_array:
            if i.get_species() == species:
                return [i.get_attack(),i.get_defense(),i.get_speed()]
        return None
    # just a bit self-explanatory notation inside sort()
    # provides sort with the attribute to sort by
    def sort_pakuri(self):
        self.pakuri_array.sort(key=lambda pak: pak.species)

    # creates a Pakuri object and adds it to the list
    # of pakuri in the pakudex
    def add_pakuri(self, species):
        if species in self.real_get_species_array():
            return False
        else:
            pakuri = Pakuri(species)
            self.pakuri_array.append(pakuri)
            self.size += 1
            return True
    # if the species is in the pakudex, execute
    # the evolve method for the Pakuri class
    # on the instance
    def evolve_species(self, species):
        if species != None:
            if self.ret_from_species(species) != None:
                self.ret_from_species(species).evolve()
                return True
            else:
                return False
        else:
            return False
