from blackjack import Blackjack
import interface

def start_game():
    print(interface.logo)

def game_play():
    game = Blackjack()
    if game.check_computer_hand_17():
        game.add_computer_hand()
    interface.game_play_reveal(game)
    while game.check_user_hand_21():
        call_user = input("Type 'y' to get another card, type 'n' to pass: ")
        if call_user == 'y':
            game.add_user_hand()
            interface.game_play_reveal(game)
        else:
            break
    interface.final_play_reveal(game)
    print(game.game_over())

def new_game():
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "y":
        interface.cls()
        start_game()
        game_play()
    else:
        return
    new_game()
