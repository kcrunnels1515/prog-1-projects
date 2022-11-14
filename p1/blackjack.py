#!/usr/bin/env python3

import p1_random as p1
# init vars used in main and give_and_describe_card
player_count = 0
rng = p1.P1Random()
# individual game loop var
game_continue = True

def main():
    # initialize vars used through main()
    global player_count
    global dealer_count
    global game_continue
    player_wins = 0
    dealer_wins = 0
    game_count = 0
    tie_count = 0
    # main game loop
    while True:
        # init in-loop vars
        dealer_count = 0
        player_count = 0
        # print the start message
        print(f"START GAME #{game_count + 1}\n")
        # give player first card
        give_and_describe_card()
        # individual game loop
        game_continue = True
        while game_continue:
            # menu for game
            print("1. Get another card")
            print("2. Hold hand")
            print("3. Print statistics")
            print("4. Exit\n")
            # get menu choice
            menu_choice = input("Choose an option: ")
            print()
            # check input for menu items
            if (menu_choice == "1"):
                give_and_describe_card()
                # check for a player hand of 21
                if player_count == 21:
                    player_wins += 1
                    game_count += 1
                    game_continue = False
                    print("BLACKJACK! You win!\n")
                # if the hand is over 21, print losing message
                elif player_count > 21:
                    dealer_wins += 1
                    game_count += 1
                    game_continue = False
                    print("You exceeded 21! You lose.\n")
            elif (menu_choice == "2"):
                # assign dealer hand
                dealer_count = rng.next_int(11) + 16
                # print hand counts
                print(f"Dealer's hand: {dealer_count}")
                print(f"Your hand is: {player_count}\n")
                # checks if dealer hand is in conditions to win
                if dealer_count > player_count and dealer_count <= 21:
                    dealer_wins += 1
                    game_count += 1
                    game_continue = False
                    print("Dealer wins!\n")
                # checks for exceeding 21
                elif dealer_count > 21:
                    player_wins += 1
                    game_count += 1
                    game_continue = False
                    print("You win!\n")
                # checks for matchng scores
                elif dealer_count == player_count:
                    game_count += 1
                    tie_count += 1
                    game_continue = False
                    print("It\'s a tie! No one wins!\n")
                # checks for dealer less than player
                elif player_count > dealer_count:
                    player_wins += 1
                    game_count += 1
                    game_continue = False
                    print("You win!\n")
            # prints statistics about games played
            elif (menu_choice == "3"):
                print(f"Number of Player wins: {player_wins}")
                print(f"Number of Dealer wins: {dealer_wins}")
                print(f"Number of tie games: {tie_count}")
                print(f"Total # of games played is: {game_count}")
                # makes sure smart-ass zybooks or player doesn't crash the game by asking for stats before any games are played
                if game_count == 0:
                    print(f"Percentage of Player wins: 0.0%\n")
                else:
                    print(f"Percentage of Player wins: {(player_wins / game_count) * 100 :.1f}%\n")
            elif (menu_choice == "4"):
                # quit
                quit()
            else:
                # invalid input catching
                print("Invalid input!")
                print("Please enter an integer value between 1 and 4.\n")


def give_and_describe_card():
    # make vars availible in function
    global player_count
    global rng
    # assign player card
    player_card = rng.next_int(13) + 1
    # card matching and score assignment, i'm not commenting all of this
    if (1 < player_card < 11):
        player_count += player_card
        print(f"Your card is a {player_card}!")
    elif player_card == 1:
        player_count += 1
        print("Your card is a ACE!")
    elif player_card == 11:
        player_count += 10
        print("Your card is a JACK!")
    elif player_card == 12:
        player_count += 10
        print("Your card is a QUEEN!")
    elif player_card == 13:
        player_count += 10
        print("Your card is a KING!")
    print(f"Your hand is: {player_count}\n")

main()
