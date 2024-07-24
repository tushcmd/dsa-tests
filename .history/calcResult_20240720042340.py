 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calc_result(cards):
    score = sum(int(card) for card in cards if card.isdigit())
    nearest_to_10 = min(abs(int(card) - 10) for card in cards if card.isdigit())
    score -= nearest_to_10
    
    if '10x' in cards:
        score *= 10
    
    return score
            
    return score * multiplier


print(calc_result(['0', '4', '5', '9', '10x']))