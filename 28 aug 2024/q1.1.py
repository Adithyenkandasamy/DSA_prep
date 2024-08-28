nums = [1, 2, 3]
nums_copy = nums[::-1]

nums_copy[1]=10  # This reassigns nums to a new reversed list
print(nums)        # Output: [3, 2, 1]
print(nums_copy)   # Output: [1, 2, 3] (unchanged)

nums = [1, 2, 3]
nums_copy = nums

nums[:] = nums[::-1]  # This reverses the list in place
print(nums)           # Output: [3, 2, 1]
print(nums_copy)      # Output: [3, 2, 1] (also reversed)
