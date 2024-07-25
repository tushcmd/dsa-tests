def duplicate_finder(nums):

    # set of seen numbers
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

#Testung
print(duplicate_finder([]))
print(duplicate_finder([1,2,3,4,1,1]))