"""
Problem:
Find the maximum element in a given array.

Example:
Input: [3, 7, 2, 9, 4]
Output: 9
"""

def find_max(arr):
    max_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num

    return max_element


# Test case
array = [3, 7, 2, 9, 4]
print("Maximum element:", find_max(array))
