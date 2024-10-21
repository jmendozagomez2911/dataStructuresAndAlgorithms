from typing import List


# https://leetcode.com/problems/two-sum/

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Outer loop: iterate over the elements excluding the last one using nums[:-1]
        # We use nums[:-1] to avoid checking the last element since there's no element after it
        for i, element_i in enumerate(nums[:-1]):

            # Inner loop: iterate over the elements starting from index i+1
            # nums[i+1:] gives us the sublist of elements after the current element_i
            # The start=i+1 ensures that the index j aligns with the index of the original list 'nums'
            # without resetting to 0, as it normally would without the 'start' argument.
            for j, element_j in enumerate(nums[i + 1:], start=i + 1):

                # If the sum of the two elements is equal to the target, return their indices
                if element_i + element_j == target:
                    return [i, j]


def main():
    # Example input
    nums = [2, 7, 11, 15]
    target = 9

    # Create an instance of Solution and call the twoSum method
    solution = Solution()
    result = solution.twoSum(nums, target)

    # Output the result
    if result:
        print(f"Indices of the two numbers that add up to {target}: {result}")
    else:
        print(f"No two numbers add up to {target}")


if __name__ == "__main__":
    main()
