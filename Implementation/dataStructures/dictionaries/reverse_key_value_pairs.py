"""
Reverse Key-Value Pairs
Define a function which takes a dictionary as a parameter and returns a dictionary in which
the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output:

{1: 'a', 2: 'b', 3: 'c'}
"""


def reverse_dict(my_dict):
    """
    This function takes a dictionary as a parameter and returns a new dictionary
    where the keys and values are reversed.
    """
    return {v: k for k, v in my_dict.items()}


# Example usage
if __name__ == "__main__":
    # Example dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Print the reversed dictionary
    print("Reversed dictionary:", reverse_dict(my_dict))
