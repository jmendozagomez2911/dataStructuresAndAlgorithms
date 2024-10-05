# LIST
# In Python, a list is a built-in data type that represents an ordered collection of elements,
# where each element can be accessed by its index.

def main():
    # The variable 'fruits' is of type list
    # In Python, lists are mutable and can hold a collection of elements, such as strings in this case.
    fruits = ["Apple", "Banana", "Orange"]

    # Add elements to the list

    # Access elements in the list
    first_fruit = fruits[0]
    print(f"First fruit: {first_fruit}")

    # Insert a new element at index 1
    fruits.insert(1, "Grapes")

    # Check if the list contains an element
    contains_banana = "Banana" in fruits
    print(f"Contains Banana? {contains_banana}")

    # Get the size of the list
    size = len(fruits)
    print(f"Size of the list: {size}")

    # Use index to find the position of an element (case-sensitive)
    try:
        index = fruits.index("banana")  # Will raise ValueError if not found
        print(f"The index of banana is: {index}")
    except ValueError:
        print("Banana is not in the list (note: 'banana' is case-sensitive)")

    # Remove an element by value
    if "Banana" in fruits:
        fruits.remove("Banana")

    # Use for-each loop (equivalent to Java's foreach) to print each element
    print("Contents of the fruits list:")
    for fruit in fruits:
        print(fruit)

    # Another list of fruits using a combined declaration and initialization
    frutas = ["banana", "cherry", "orange"]

    # Use for-each loop to print each element
    print("Contents of the frutas list:")
    for fruta in frutas:
        print(fruta)

    # Thread safety in Python: lists are not thread-safe, so when working with multiple threads,
    # use thread-safe structures such as `queue.Queue`.
    # For example, if multiple threads attempt to modify the same list, you should manage thread safety manually.

    # Lists in Python are not inherently thread-safe like Java's Vector, so when working with multiple threads,
    # Python provides options like the `queue.Queue` for thread-safe operations.
    from queue import Queue

    # Example of a thread-safe list-like structure using Queue
    fruits2 = Queue()

    # Adding elements to a Queue (thread-safe)
    fruits2.put("Apple")
    fruits2.put("Banana")

    # Accessing elements from the Queue (thread-safe)
    while not fruits2.empty():
        print(f"Element from Queue: {fruits2.get()}")


if __name__ == "__main__":
    main()
