"""
Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example:

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)

Time Complexity: O(n) - We iterate through both tuples once, where n is the length of the tuples.
Space Complexity: O(n) - We create a new tuple to store the result, which requires space proportional to the size of the input tuples.
"""


def tuple_elementwise_sum(t1, t2):
    """
    Takes two tuples and returns a tuple containing the element-wise sum.
    If tuples have different lengths, truncates the longer one.
    """
    min_length = min(len(t1), len(t2))  # Find the length of the shorter tuple

    # Perform element-wise sum using zip and tuple comprehension, truncating the longer tuple
    result = tuple(a + b for a, b in zip(t1[:min_length], t2[:min_length]))
    return result


# Example usage
if __name__ == "__main__":
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)

    output_tuple = tuple_elementwise_sum(tuple1, tuple2)
    print(f"Element-wise sum of {tuple1} and {tuple2} is {output_tuple}")
