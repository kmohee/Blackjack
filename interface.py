import os

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def game_play_reveal(game):
    print(f"    Your cards: {game.get_user_hand()}, current score: {game.get_user_score()}")
    print(f"    Computer's first card: {game.get_computer_hand()[0]}")

def final_play_reveal(game):
    print(f"    Your final hand: {game.get_user_hand()}, final score: {game.get_user_score()}")
    print(f"    Computer's final hand: {game.get_computer_hand()}, final score: {game.get_computer_score()}")
