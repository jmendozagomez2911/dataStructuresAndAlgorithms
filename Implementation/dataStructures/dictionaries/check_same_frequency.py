"""
Same Frequency
Define a function which takes two lists as parameters and checks if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False

Time Complexity: O(n)
Space Complexity: O(n)
"""


def check_same_frequency(list1, list2):
    """
    This function takes two lists and checks if they have the same frequency of elements.
    It creates two dictionaries to store the frequency of elements in each list and
    compares the dictionaries to determine if the lists have the same frequency.

    Time Complexity:
    - Counting the frequency of elements in both lists takes O(n), where n is the number of elements in the lists.
      We iterate through both lists once, making the time complexity O(n).
    - The comparison of two dictionaries also takes O(n) because we have to check each key-value pair.

    Space Complexity:
    - We use two dictionaries, and in the worst case, we store all elements in them.
      This results in O(n) space complexity, where n is the number of unique elements in the lists.
    """
    dict1 = {}
    dict2 = {}

    # If the lists have different lengths, they can't have the same frequency of elements
    if len(list1) != len(list2):
        return False

    # Count frequency of elements in list1
    for element in list1:
        dict1[element] = dict1.get(element, 0) + 1

    # Count frequency of elements in list2
    for element in list2:
        dict2[element] = dict2.get(element, 0) + 1

    # Compare the frequency dictionaries
    return dict1 == dict2


# Example usage
if __name__ == "__main__":
    # Example lists
    list1 = [1, 2, 3, 2, 1]
    list2 = [3, 1, 2, 1, 3]

    # Check if the two lists have the same frequency of elements
    print("Do the lists have the same frequency of elements?", check_same_frequency(list1, list2))
