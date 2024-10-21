"""
Conditional Filter
Define a function that takes a dictionary as a parameter and returns a dictionary
with elements based on a condition.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
Output:

{'b': 2, 'd': 4}
"""


def filter_dict(my_dict, condition):
    """
    This function takes a dictionary and a condition (a lambda function or other callable).
    It returns a new dictionary with key-value pairs that satisfy the given condition.
    """
    return {k: v for k, v in my_dict.items() if condition(k, v)}


# Example usage
if __name__ == "__main__":
    # Example dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Filter dictionary with a condition (in this case, values that are even)
    filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)

    # Print the filtered dictionary
    print("Filtered dictionary:", filtered_dict)
