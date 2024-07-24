 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calc_result(cards):
    let score = 0
    let multiplier = 1
    
    for card in cards:
        if card == '10x':
            multiplier = 10
        elif card == '0':
            for card in cards:
                isinstance(card, int) and card.remove(card.max())
                return cards
            print(cards)
            # score = 0
            # multiplier = 1
        else:
            score += int(card) * multiplier
    return score


print(calc_result(['0', '4', '5', '9', '10x']))