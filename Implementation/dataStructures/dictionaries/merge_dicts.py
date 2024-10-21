# Common Keys
# Define a function that takes two dictionaries as parameters and merges them,
# summing the values of common keys.

# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:
# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary to avoid modifying the original

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if the key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add the key-value pair if it's not in the first dictionary

    return merged_dict


# APPROACH MORE EFFICIENTLY
# def merge_dicts(dict1, dict2):
#    result = dict1.copy()
#    for key, value in dict2.items():
#       result[key] = result.get(key, 0) + value
#    return result


# Test the function
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    result = merge_dicts(dict1, dict2)
    print(result)  # Output should be: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
