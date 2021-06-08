import random
from utils import ace_checker

class Blackjack:

    ### Global variables
    global cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self):
        self.user_hand = [ace_checker(random.choice(cards), None) for i in range(2)]
        self.computer_hand = [random.choice(cards) for i in range(2)]

    def get_user_hand(self):
        return self.user_hand

    def get_computer_hand(self):
        return self.computer_hand

    def get_user_score(self):
        return sum(self.user_hand)

    def get_computer_score(self):
        return sum(self.computer_hand)

    def check_computer_hand_17(self):
        return sum(self.computer_hand) < 17

    def check_user_hand_21(self):
        return sum(self.user_hand) <= 21

    def add_computer_hand(self):
        pick_card = random.choice(cards)
        self.computer_hand.append(ace_checker(pick_card, self.computer_hand))
        return

    def add_user_hand(self):
        pick_card = random.choice(cards)
        self.user_hand.append(ace_checker(pick_card, self.user_hand))
        return

    def game_over(self):
        if self.get_user_score() > 21 and self.get_computer_score() > 21:
            return "You went over. You lose 😤"
        if self.get_user_score() == self.get_computer_score():
            return "Draw 🙃"
        elif self.get_computer_score() == 21 and len(self.get_computer_hand()) == 2:
            return "Lose, opponent has Blackjack 😱"
        elif self.get_user_score() == 21 and len(self.get_user_hand()) == 2:
            return "Win with a Blackjack 😎"
        elif self.get_user_score() > 21:
            return "You went over. You lose 😭"
        elif self.get_computer_score() > 21:
            return "Opponent went over. You win 😁"
        elif self.get_user_score() > self.get_computer_score():
            return "You win 😃"
        else:
            return "You lose 😤"
