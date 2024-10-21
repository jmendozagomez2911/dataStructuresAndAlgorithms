# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example:
# Input: nums = [1, 2, 3, 1]
# Output: true

def contains_duplicate(nums):
    # Convert the list to a set to remove duplicates
    nums_set = set(nums)

    # If the length of the set is not equal to the length of the list, it means there were duplicates
    return len(nums) != len(nums_set)


def main():
    # Example input
    nums = [1, 2, 3, 1]

    # Call the function to check for duplicates
    result = contains_duplicate(nums)

    # Output the result
    print(f"Does the list contain duplicates? {result}")


if __name__ == "__main__":
    main()

# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(n), due to the space required for the set.
