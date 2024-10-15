# DICTIONARY
# In Python, a dictionary is a built-in data type that represents an unordered collection
# of key-value pairs, where keys are unique.

def main():
    # Initializing a dictionary with mixed types of values
    mixed_dict = {
        "name": "Alice",
        "age": 30,
        "is_student": False,
        "grades": [88, 92, 95],
        "address": {"city": "Wonderland", "zip": "12345"}
    }
    print(f"Initial dictionary: {mixed_dict}")

    # Accessing a value by key
    name = mixed_dict["name"]
    print(f"Accessed 'name': {name} (Type: {type(name)})")

    # Adding a new key-value pair to the dictionary
    mixed_dict["favorite_color"] = "blue"
    print(f"Dictionary after adding 'favorite_color': {mixed_dict}")

    # Modifying an existing value
    mixed_dict["age"] = 31
    print(f"Dictionary after modifying 'age': {mixed_dict}")

    # Checking if a key exists in the dictionary
    has_grades = "grades" in mixed_dict
    print(f"Contains 'grades' key? {has_grades}")

    # Get the value of a key with a default (to avoid KeyError)
    nickname = mixed_dict.get("nickname", "No nickname")
    print(f"Value for 'nickname': {nickname}")

    # Removing a key-value pair using `del`
    # del doesn't return anything.
    del mixed_dict["is_student"]
    print(f"Dictionary after deleting 'is_student': {mixed_dict}")

    # Removing a key-value pair using `pop`
    # pop() returns the value of the removed key
    removed_value = mixed_dict.pop("favorite_color", None)
    print(f"Dictionary after popping 'favorite_color': {mixed_dict}")
    print(f"Popped value: {removed_value}")

    # Getting all keys in the dictionary
    keys = mixed_dict.keys()
    print(f"Keys in the dictionary: {keys}")

    # Getting all values in the dictionary
    values = mixed_dict.values()
    print(f"Values in the dictionary: {values}")

    # Getting all key-value pairs as tuples using `items()`
    items = mixed_dict.items()
    print(f"Key-value pairs: {items}")

    # Iterating over the dictionary keys
    print("\nIterating over the dictionary keys:")
    for key in mixed_dict:
        print(f"Key: {key}")

    # Iterating over the dictionary values
    print("\nIterating over the dictionary values:")
    for value in mixed_dict.values():
        print(f"Value: {value}")

    # Iterating over key-value pairs
    print("\nIterating over key-value pairs:")
    for key, value in mixed_dict.items():
        print(f"Key: {key}, Value: {value}")

    # Merging two dictionaries (use the `update()` method)
    additional_info = {"hobby": "chess", "favorite_food": "pizza"}
    mixed_dict.update(additional_info)
    print(f"Dictionary after update with additional info: {mixed_dict}")

    # Dictionary comprehension: Create a new dictionary with only integer values
    int_values_dict = {key: value for key, value in mixed_dict.items() if isinstance(value, int)}
    print(f"Dictionary with only integer values: {int_values_dict}")

    # Clearing all key-value pairs from the dictionary
    mixed_dict.clear()
    print(f"Dictionary after clearing all elements: {mixed_dict}")


if __name__ == "__main__":
    main()
