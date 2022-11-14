#!/usr/bin/env python3

import p1_random as p1

dealer_count = 0
player_count= 0
game_counter = 0
game_continue = True
rng = p1.P1Random()

def main():
    while game_continue:
        global game_counter
        game_counter += 1
        print(f"START GAME \#{game_counter}")
        game_loop()
    quit()

# separated game loop for simplicity
def game_loop():
    global dealer_count
    global player_count
    while True:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        menu_choice = input()
        eval_menu(menu_choice)
        if player_count == 21:
            if dealer_count == 21:
                print("It\'s a tie! No one wins!")
            else:
                print("BLACKJACK! You win!")
        elif (player_count > 21):
            print("You exceeded 21! You lose.")
        elif (dealer_count == 21):
            if player_count == 21:
                print("It\'s a tie! No one wins!")
            else:
                print("Dealer wins!")


# gives player and prints player card type
def get_card():
    global player_count
    player_card = rng.next_int(13) + 1
    player_count += player_card
    if (1 < player_card < 11):
        print(f"Your card is a {player_card}!")
    elif player_card == 1:
        print("Your card is an ACE!")
    elif player_card == 11:
        print("Your card is a JACK!")
    elif player_card == 12:
        print("Your card is a QUEEN!")
    elif player_card == 13:
        print("Your card is a KING!")

def print_stats():


# run methods based on menu choice
def eval_menu(menu_choice):
    if (menu_choice == "1"):
        get_card()
    elif (menu_choice == "2"):
        global dealer_count
        dealer_count += rng.next_int(13) + 1
        print(dealer_count)
    elif (menu_choice == "3"):
        print_stats()
    elif (menu_choice == "4"):
        quit()
    #    global game_continue
    #    game_continue = False
    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.")

main()
