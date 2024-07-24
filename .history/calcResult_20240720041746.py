 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calc_result(cards):
    score = 0
    multiplier = 1
    has_zero = '0' in cards
    max_value = 0
    
    for card in cards:
        if card == 'x10':
            multiplier *= 10
        elif card.isdigit():
            value = int(card)
            if has_zero and value > max_value:
                max_value = value
            score += value
    
    if has_zero:
        score = score - max_value
            
            
    return score * multiplier


print(calc_result(['0', '4', '5', '9', '10x']))