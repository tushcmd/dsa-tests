 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calc_result(cards):
    score = 0
    multiplier = 1
    
    for card in cards:
        if card == '10x':
            multiplier *= 2
        elif card.isdigit():
            score += int(card)
            
            
    return score * multiplier


print(calc_result(['0', '4', '5', '9', '10x']))