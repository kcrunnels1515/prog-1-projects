#!/usr/bin/env python3

from pakudex import *

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    cont = True
    # capacity setter, checks for non positive integer inputs
    # also displays capacity of Pakudex once set
    while cont:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity < 0:
                raise ValueError
            print(f"The Pakudex can hold {capacity} species of Pakuri.")
            myP = Pakudex(capacity)
            cont = False
        except ValueError:
            print("Please enter a valid size.")
    while True:
        # display main menu
        print('''
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
''')
        # get menu option
        option = input("What would you like to do? ")
        # if pakudex has pakuri, prints pakuri and their index
        # in the pakudex
        if option == "1":
            if myP.get_species_array() == None:
                print("No Pakuri in Pakudex yet!")
                continue
            else:
                if myP.get_species_array() != None:
                    print("Pakuri In Pakudex:")
                    for index, value in enumerate(myP.get_species_array()):
                        print(f"{index + 1}. {value}")
        # if pakuri is in pakudex, print its stats\
        elif option == "2":
            name = input("Enter the name of the species to display: ")
            if myP.get_species_array() != None:
                if name in myP.get_species_array():
                    stats = myP.get_stats(name)
                    print(f"Species: {name}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")
                else:
                    print("Error: No such Pakuri!")
            else:
                print("Error: No such Pakuri!")
        # add pakuri object to pakudex, if it has space and does not
        # contain a duplicate
        elif option == "3":
            if myP.size == myP.capacity:
                print("Error: Pakudex is full!")
                continue
            name = input("Enter the name of the species to add: ")
            if myP.add_pakuri(name):
                print(f"Pakuri species {name} successfully added!")
            else:
                print("Error: Pakudex already contains this species!")
        # if pakuri exists in pakudex, evolve it
        elif option == "4":
            name = input("Enter the name of the species to evolve: ")
            if myP.get_species_array() != None:
                if name in myP.get_species_array():
                    myP.evolve_species(name)
                    print(f"{name} has evolved!")
                else:
                    print("Error: No such Pakuri!")
            else:
                print("Error: No such Pakuri!")
        # sort pakuri in pakudex
        elif option == "5":
            myP.sort_pakuri()
            print("Pakuri have been sorted!")
        # quit program
        elif option == "6":
            print("Thanks for using Pakudex! Bye!")
            quit()
        # error catching for weird input
        else:
            print("Unrecognized menu selection!")

if __name__ == '__main__':
    main()
