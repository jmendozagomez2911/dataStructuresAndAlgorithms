"""
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b
"""


def max_value_key(my_dict):
    """
    This function takes a dictionary as a parameter and returns the key
    with the highest value in that dictionary.
    """
    # Use the max function to get the key with the highest value
    return max(my_dict, key=my_dict.get)


# my_dict.get(k) is a direct method call, where k is a specific key,
# and it will return the value associated with that specific key.

# key=my_dict.get passes the method as an argument to a higher-order function like max().
# The max() function will then call my_dict.get(key) internally
# for each key in the dictionary to determine which key corresponds to the maximum value.


# Example usage
if __name__ == "__main__":
    # Example dictionary
    my_dict = {'a': 5, 'b': 9, 'c': 2}

    # Print the key with the highest value
    print("The key with the highest value is:", max_value_key(my_dict))
