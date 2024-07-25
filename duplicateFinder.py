# In the context of evaluating an inventory list represented by an array of integers, your task is to determine whether any item (number) occurs more than once.

# Your function should return true if at least one item is found in multiple instances, indicating a repeated entry in the inventory.

# Conversely, if each item is unique and no duplicates are present, your function should return false.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

# Constraints:

# The number of items in the inventory (array length) ranges from 1 to 10^5.

# Each item's identifier (integer value) can be between -10^9 and 10^9.


def duplicate_finder(nums):


    # Create an empty set to store unique elements from the list
    seen = set()
    # Iterate over each number in the list 'nums'
    for num in nums:
        
        # Check if the current number is already in the set 'seen'
        if num in seen:
            
            # If the number is found in the set, a duplicate exists, so return True
            return True
        
        
        # Add the current number to the set 'seen' as it's not a duplicate yet
        seen.add(num)
        
    
    # If no duplicates are found in the entire list, return False
    return False

# Test cases
print(duplicate_finder([1,2,3,1]))  # Should return True
print(duplicate_finder([1,2,3,4]))  # Should return False
print(duplicate_finder([1,1,1,3,3,4,3,2,4,2]))  # Should return True

# Additional test cases
print(duplicate_finder([]))  # Should return False (empty array)
print(duplicate_finder([5]))  # Should return False (single element)
print(duplicate_finder([-1, 0, 1]))  # Should return False (negative numbers)
print(duplicate_finder([10**9, -10**9, 10**9]))  # Should return True (large numbers)