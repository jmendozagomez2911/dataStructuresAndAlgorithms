"""
Common Elements
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

Example:

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)

Time Complexity: O(n + m) - Where n is the size of tuple1 and m is the size of tuple2.
Space Complexity: O(min(n, m)) - Since we are storing the common elements in a set of size proportional to the smaller tuple.
"""


def common_elements(tuple1, tuple2):
    """
    This function takes two tuples, converts them to sets, and returns a tuple containing the common elements
    using the & operator to find the intersection between the two sets.

    Time Complexity: O(n + m) - Where n is the length of tuple1 and m is the length of tuple2.
    Space Complexity: O(min(n, m)) - Because the set stores only the common elements, its size is proportional to the smaller tuple.
    """

    # Explanation of the & operator:
    # - `set(tuple1) & set(tuple2)` is used to find the intersection between two sets.
    # - The & operator returns a new set that contains only the elements that are present in both sets.
    # - This works because sets in Python support set operations such as union, intersection, and difference.
    # - The resulting set contains the common elements, and we convert it back into a tuple.

    # Convert the tuples to sets and find the intersection using the & operator
    return tuple(set(tuple1) & set(tuple2))


# Example usage
if __name__ == "__main__":
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 5, 6, 7, 8)

    output_tuple = common_elements(tuple1, tuple2)
    print(f"Common elements: {output_tuple}")  # Expected output: (4, 5)
