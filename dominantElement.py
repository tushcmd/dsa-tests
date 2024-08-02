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

    
    # Store the count of each number in a dictionary
    # count a number occurence by iteration 
    # find the number whose count is greater than n/2
    # return it as the majority element
    #

    # dictionary of the count
    count_dict = {}
    n = len(nums)

    # itearate the list
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        

        # return num with count > n/2
        if count_dict[num] > n // 2:
            return num

    # complete function
    return None

# Tests

print(majorityElement([3,2,3]))  # output 3

print(majorityElement([2, 2, 1, 1, 1, 2, 2])) # output 2

print(majorityElement([5]))  # output 5

print(majorityElement([5, 5, 5, 5, 5]))  # output 5


# time complexity linear O(n)

# space complexity linear O(n)




    # Write your code below