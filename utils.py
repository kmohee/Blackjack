def ace_checker(card, hand):
    if hand != None:
        if card == 11:
            if sum(hand)>10:
                return 1
    return card
