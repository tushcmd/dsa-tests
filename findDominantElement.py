# For this mock interview, you will go through four phases: Prompt, Plan, Code, & Test.
# Prompt: Understand the problem.
# Plan: Outline your approach.
# Code: Implement your solution.
# Test: Verify your solution works.

# Here is the problem that you will be solving:
# Imagine you have a list of numbers, referred to as 'nums', with a total length of 'n'.
# Your task is to identify the dominant element in this list.
# The dominant element is defined as the one that appears more than half the time (n / 2) in the list.
# It is guaranteed that such an element exists in the list.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
 
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# - The length of 'nums' is equal to 'n'.
# - 'n' ranges from 1 to 50,000.
# - Each element in 'nums' can be any integer between -1,000,000,000 and 1,000,000,000.


def majorityElement(nums):
    # Plan:
    # 1. Use Boyer-Moore Voting Algorithm
    # 2. Initialize candidate and count
    # 3. Iterate through the list, updating candidate and count
    # 4. Return the final candidate
    
    # Code:
    candidate = None
    count = 0
    
    # Iterate through each number in the list
    for num in nums:
        # If count is 0, set the current number as the candidate
        if count == 0:
            candidate = num
        
        # If the current number is the same as the candidate, increase count
        # Otherwise, decrease count
        count += 1 if num == candidate else -1
    
    # The final candidate is guaranteed to be the majority element
    return candidate

# Test:
# Test case 1
print(majorityElement([3,2,3]))  # Expected output: 3

# Test case 2
print(majorityElement([2,2,1,1,1,2,2]))  # Expected output: 2

# Additional test case
print(majorityElement([1]))  # Expected output: 1