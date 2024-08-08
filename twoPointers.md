### Two Pointers Technique Overview

The two pointers technique is a common strategy used in array and string problems, where you operate with two indices (or "pointers") to solve the problem more efficiently than using brute force. The technique is versatile and can be used in different ways depending on the problem, but the core idea is to manipulate two pointers simultaneously to achieve the desired result.

#### When to Use Two Pointers

- **Sorted Arrays:** Often used in problems involving sorted arrays or linked lists.
- **Finding Pairs or Triplets:** Commonly used in problems where you need to find pairs or triplets that satisfy a particular condition.
- **Partitioning:** Useful for problems that involve partitioning an array into different sections.
- **Sliding Window:** Can be combined with a sliding window approach for problems that require finding subarrays or substrings that meet certain criteria.

### Basic Patterns of Two Pointers

1. **Opposite Ends (Converging Pointers):**
   - Start one pointer at the beginning and the other at the end, and move them towards each other until they meet.
   - Common in problems involving finding pairs with certain sums in sorted arrays.

2. **Same Direction (Sliding Window):**
   - Both pointers start at the beginning, with one pointer advancing to find the desired condition while the other pointer lags or follows.
   - Used in problems involving subarrays, substrings, or partitions.

3. **Partitioning:**
   - One pointer moves through the array to partition it based on a condition, and the other pointer is used to swap elements as needed.
   - Often used in problems like partitioning arrays around a pivot (e.g., the Dutch National Flag problem).

### Example Problems

1. **Two Sum (Sorted Array):**

   **Problem:** Given a sorted array of integers, find two numbers such that they add up to a specific target number. Return the indices of the two numbers.

   **Solution:**

   ```python
   def two_sum_sorted(arr, target):
       left, right = 0, len(arr) - 1
       while left < right:
           current_sum = arr[left] + arr[right]
           if current_sum == target:
               return (left, right)
           elif current_sum < target:
               left += 1
           else:
               right -= 1
       return None  # If no pair is found
    ```

2. **Remove Duplicates from Sorted Array:**

   **Problem:** Given a sorted array, remove the duplicates in-place such that each element appears only once and returns the new length.

   **Solution:**

   ```python
   def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
    ```

3. **Container With Most Water:**

   **Problem:** Given an array where each element represents the height of a line drawn from that index, find two lines that together with the x-axis form a container, such that the container contains the most water.

   **Solution:**

   ```python
   def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
    ```

4. **3Sum (Finding Triplets that Sum to Zero):**

   **Problem:** Given an array of integers, find all unique triplets in the array which gives the sum of zero.

   **Solution:**

   ```python
   def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res
    ```

Key Considerations

- Edge Cases: Always consider arrays that are too small (e.g., arrays with 0, 1, or 2 elements).
- Duplicate Handling: If the array can contain duplicates, make sure your solution accounts for it appropriately, especially when finding unique pairs or triplets.
- Efficiency: Two pointers can significantly reduce the time complexity, often turning O(n^2) solutions into O(n) or O(n log n).
