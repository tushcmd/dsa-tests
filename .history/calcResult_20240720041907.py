 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calc_result(cards):
    score = sum(int(card) for card in cards if card.isdigit())
    multiplier = 1
    max_value = max(int(card) for card in cards if card.isdigit())
    
    if 'x10' in cards:
        multiplier *= 10
    
    if '0' in cards:
        score -= max_value
            
    return score * multiplier


print(calc_result(['0', '4', '5', '9', '10x']))