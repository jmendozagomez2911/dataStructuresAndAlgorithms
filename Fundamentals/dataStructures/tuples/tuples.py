"""
Essential Tuple Operations for DSA Interviews

This program demonstrates the key tuple operations necessary for a Data Structures and Algorithms (DSA) interview.
"""

def main():
    # 1. Creating a Tuple
    tup = (1, 2, 3, 4, 2)
    print(f"Original tuple: {tup}")

    # Tuple with a single element requires a comma
    single_element_tup = (5,)
    print(f"Single element tuple: {single_element_tup}")

    # Tuple using the tuple() constructor
    constructed_tup = tuple([1, 2, 3])
    print(f"Tuple from a list: {constructed_tup}")

    # 2. Accessing Elements (O(1))
    # Access the first element
    first_element = tup[0]
    print(f"First element of tuple: {first_element}")

    # Access the last element using negative indexing
    last_element = tup[-1]
    print(f"Last element of tuple: {last_element}")

    # 3. Tuple Unpacking (O(1)) with a Practical Example
    # Let's use a function that returns multiple values and unpack the results.
    def find_min_max(arr):
        """A function to return both the minimum and maximum values of an array."""
        return min(arr), max(arr)

    # Unpacking the min and max values from the tuple
    min_val, max_val = find_min_max(tup)
    print(f"Unpacked tuple: min_val={min_val}, max_val={max_val}")

    # Unpacking with the star operator
    first, *middle, last = tup
    print(f"First: {first}, Middle: {middle}, Last: {last}")

    # 4. Tuple Comparisons (O(n))
    tup1 = (1, 2, 3)
    tup2 = (1, 2, 4)

    comparison_result = tup1 < tup2  # Lexicographical comparison
    print(f"Tuple comparison result (tup1 < tup2): {comparison_result}")

    # 5. Iteration over Tuples (O(n))
    print("Iterating over tuple elements:")
    for element in tup:
        print(element)

    # 6. Using a Tuple as a Dictionary Key (O(1) for lookup)
    my_dict = {(1, 2): "value", (3, 4): "another_value"}
    dict_lookup = my_dict[(1, 2)]
    print(f"Dictionary lookup with tuple key: {dict_lookup}")

    # 7. Length of a Tuple (O(1))
    tuple_length = len(tup)
    print(f"Length of the tuple: {tuple_length}")

    # 8. Tuple Slicing (O(k), where k is the length of the slice)
    sliced_tup = tup[1:3]
    print(f"Sliced tuple (index 1 to 2): {sliced_tup}")

    # 9. Finding Element (index()) (O(n))
    # Finds the first occurrence of an element and returns its index
    try:
        element_index = tup.index(2)  # Finds the index of the first occurrence of 2
        print(f"Index of element '2': {element_index}")
    except ValueError:
        print("Element not found in the tuple")

    # 10. Using "in" to Check for Element Existence (O(n))
    element_existence = 3 in tup
    print(f"Does the tuple contain 3? {element_existence}")

    # 11. Counting Element Occurrences (count()) (O(n))
    element_count = tup.count(2)  # Counts how many times '2' appears in the tuple
    print(f"Number of times '2' appears in the tuple: {element_count}")

    # 12. Finding Minimum and Maximum Values (min(), max()) (O(n))
    min_value = min(tup)  # Finds the minimum value in the tuple
    max_value = max(tup)  # Finds the maximum value in the tuple
    print(f"Minimum value in the tuple: {min_value}")
    print(f"Maximum value in the tuple: {max_value}")

    # 13. Using zip() to Pair Corresponding Elements from Two Tuples (O(n))
    tup2 = (10, 20, 30, 40, 50)
    paired_tuples = list(zip(tup, tup2))
    print(f"Paired elements from tup and tup2: {paired_tuples}")

    # 14. Summing Corresponding Elements using zip() (O(n))
    summed_elements = [a + b for a, b in zip(tup, tup2)]
    print(f"Summed corresponding elements from tup and tup2: {summed_elements}")

if __name__ == "__main__":
    main()
