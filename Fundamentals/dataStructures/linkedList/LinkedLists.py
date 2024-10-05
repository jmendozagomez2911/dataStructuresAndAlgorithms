# Types of LinkedLists in Python: In Python, there isn't a built-in LinkedList data structure like in Java. However,
# we can implement linked lists using classes, or use the deque (double-ended queue) from the collections module for
# efficient insertion and deletion from both ends. Python's built-in list is generally used for most purposes.

from collections import deque


def main():
    # LinkedList (similar to LinkedList in Java)
    # In Python, we can use deque (double-ended queue) from the collections module to handle
    # efficient insertions/removals at both ends.
    fruits3 = deque()

    # Add elements to the deque (acting as a LinkedList in this case)
    fruits3.append("Apple")
    fruits3.append("Banana")
    fruits3.append("Orange")

    # Print the deque
    print(list(fruits3))  # Output: ['Apple', 'Banana', 'Orange']

    # Access an element in the deque (using indexing, although not typical in linked lists)
    second_fruit = list(fruits3)[1]  # Converting to list to access by index
    print(f"Second fruit: {second_fruit}")

    # Using an iterator to go through the deque (similar to using iterator in Java)
    print("Iterating over the deque:")
    for fruit in fruits3:
        print(fruit)

    # Doubly LinkedList (similar to Doubly LinkedList in Java)
    # Deque in collections is actually doubly linked, meaning it allows efficient operations at both ends,
    # which makes it suitable for operations that require forward and backward traversing.

    # Example of inserting at both ends:
    fruits3.appendleft("Grapes")  # Insert at the beginning
    print("\nAfter appending 'Grapes' at the beginning:")
    print(list(fruits3))  # Output: ['Grapes', 'Apple', 'Banana', 'Orange']

    # Removing elements from both ends
    fruits3.pop()  # Remove the last element
    fruits3.popleft()  # Remove the first element
    print("\nAfter removing from both ends:")
    print(list(fruits3))  # Output: ['Apple', 'Banana']


if __name__ == "__main__":
    main()
