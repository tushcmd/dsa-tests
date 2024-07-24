 
# Create a function to calculate the score in a card game as above.
# For example
# Function culcResult ([‘0’, ‘4’, ‘5’, ‘9’, ‘10x’]) -> 90pt


def calcResult(cards):
    # Separate numeric cards and check for '10x'
    numeric_cards = [int(card) for card in cards if card.isdigit()]
    has_multiplier = '10x' in cards
    
    if numeric_cards:
        # Find the number closest to 10
        closest_to_10 = min(numeric_cards, key=lambda x: abs(10 - x))
        
        # Remove the closest number to 10 (equivalent to replacing it with 0)
        numeric_cards.remove(closest_to_10)
    
    # Sum the remaining numbers
    total = sum(numeric_cards)
    
    # Apply multiplier if '10x' is present
    if has_multiplier:
        total *= 10
    
    return total

print(calcResult(['0', '4', '5', '9', '10x']))  # Output: 90
print(calcResult(['1', '4', '5', '10x', '9']))  # Output: 100
print(calcResult(['1', '4', '5', '9', '2']))    # Output: 12
print(calcResult (['1', '4', '5', '9', '2']))