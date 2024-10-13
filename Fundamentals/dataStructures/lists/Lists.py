# LIST
# In Python, a list is a built-in data type that represents an ordered collection of elements,
# where each element can be accessed by its index.

def main():
    # The variable 'mixed_list' contains different types of elements: integers, floats, strings, and booleans.
    mixed_list = [42, 3.14, "Python", True, "New Element", 99]
    print(f"Initial elements of mixed_list: {mixed_list}")

    # Access and print the first element in the list
    first_element = mixed_list[0]
    print(f"First element: {first_element} (Type: {type(first_element)})")

    # Insert a new element at index 1 (inserting a float)
    mixed_list.insert(1, 7.77)
    print(f"The elements after inserting 7.77 at index 1: {mixed_list}")

    # Check if the list contains a specific element (checking for a string)
    contains_python = "Python" in mixed_list
    print(f"Contains 'Python'? {contains_python}")

    # Get and print the size of the list
    size = len(mixed_list)
    print(f"Size of the list: {size}")

    # Use index to find the position of an element (case-sensitive, with exception handling)
    try:
        index = mixed_list.index("python")  # This will raise ValueError if not found
        print(f"The index of 'python' is: {index}")
    except ValueError:
        print("'python' (lowercase) is not in the list (note: it's case-sensitive)")

    # Remove an element by value (removing an integer if it exists)
    if 42 in mixed_list:
        mixed_list.remove(42)
        print(f"After removing 42: {mixed_list}")

    # Demonstrating the append() method - Adding a single element to the list
    mixed_list.append("Appended Element")
    print(f"After appending 'Appended Element': {mixed_list}")

    # Demonstrating the extend() method - Extending the list with multiple elements
    mixed_list.extend([1, 2, 3])
    print(f"After extending with [1, 2, 3]: {mixed_list}")

    # Demonstrating slicing: accessing a subset of the list
    print(f"\nSlicing the list (from index 1 to 4): {mixed_list[1:5]}")

    # Demonstrating assignment to a slice: changing values in a specific range
    mixed_list[1:4] = ["Replaced", "Values", "Here"]
    print(f"After replacing the slice [1:4]: {mixed_list}")

    # Demonstrating the del statement: deleting an element at index 2
    del mixed_list[2]
    print(f"After using del to delete element at index 2: {mixed_list}")

    # Demonstrating the pop() method: removing the last element
    last_element = mixed_list.pop()
    print(f"After popping the last element '{last_element}': {mixed_list}")

    # Demonstrating pop() with an index: removing the element at index 1
    popped_element = mixed_list.pop(1)
    print(f"After popping element at index 1 ('{popped_element}'): {mixed_list}")

    # Iterating directly over the elements in mixed_list (For-each loop)
    print("\nContents of the mixed_list (direct iteration):")
    for element in mixed_list:
        print(f"Element: {element} (Type: {type(element)})")

    # Iterating over the elements using enumerate (with index)
    print("\nUsing enumerate to iterate over elements with their index:")
    for index, element in enumerate(mixed_list):
        print(f"Element at index {index}: {element} (Type: {type(element)})")

    # Thread safety in Python: lists are not thread-safe, so when working with multiple threads,
    # use thread-safe structures such as `queue.Queue`.

    from queue import Queue

    # Example of a thread-safe list-like structure using Queue
    thread_safe_queue = Queue()

    # Adding elements to a Queue (thread-safe)
    thread_safe_queue.put("Thread-Safe Element 1")
    thread_safe_queue.put("Thread-Safe Element 2")

    # Accessing elements from the Queue (thread-safe)
    while not thread_safe_queue.empty():
        print(f"Element from Queue: {thread_safe_queue.get()}")

if __name__ == "__main__":
    main()
