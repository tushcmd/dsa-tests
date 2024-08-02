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

def
 
majorityElement
(
nums
)
:

    
# Initialize the count for the current candidate to 0

    count 
=
 
0

    
# Initialize the candidate to an arbitrary value, here 0

    candidate 
=
 
0

    
# Loop through each number in the input array

    
for
 num 
in
 nums
:

        
# If the count is 0, we pick the current number as the new candidate.

        
# This happens when we're starting or when the previous candidate's count has been fully neutralized

        
# by different numbers encountered in the array.

        
if
 count 
==
 
0
:

            candidate 
=
 num
        
# If the current number is the same as the current candidate, increment the count.

        
# This means we found another instance of our candidate.

        
if
 num 
==
 candidate
:

            count 
+=
 
1

        
# Otherwise, decrement the count.

        
# This represents a vote against the current candidate by a different number.

        
else
:

            count 
-=
 
1

    
# After the loop, the candidate variable holds the majority element.

    
# This works because if a majority element exists, it will be the candidate when the loop finishes.

    
# The algorithm effectively pairs off different elements and removes them from consideration,

    
# ensuring the majority element remains at the end.

    
return
 candidate
