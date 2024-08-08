# Imagine you have a long piece of text ('haystack') and you are looking for a specific smaller string ('needle') within it.
# Your task is to determine where in the text the smaller string first shows up.
# You should output the starting position of the first occurrence of the 'needle' in the 'haystack'.
# Should the 'needle' not be found within the 'haystack', your program must return -1, indicating its absence.
 
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: The substring "sad" is first found at the start of the "haystack", thus the output is 0.
 
# Example 2:
# Input: haystack = "helloworld", needle = "123"
# Output: -1
# Explanation: Since "123" is not present in "helloworld", we return -1.
 
# Constraints:
# The length of both 'haystack' and 'needle' will be between 1 and 10^4, inclusive.
# Both 'haystack' and 'needle' will contain only lowercase English letters.

def findSubstringStart(haystack, needle):
    # return 0 if string is empty
    if not needle:
        return 0
    
    # iterate through the string
    for i in range(len(haystack) - len(needle) + 1):
        # check substring starting index
        if haystack[i:i+len(needle)] == needle:
            return i
    
    # return -1 if needle is not found
    return -1
