# Stack
# A stack is like a pile of items where you can only add or remove items from the top,
# following the LIFO principle (Last-In, First-Out).
# Principle: The last element added to the collection will be the first one to be removed.
# Stacks are commonly used for tasks like tracking function calls, undo operations, and evaluating expressions.

def main():
    # In Python, we can use a list to simulate stack behavior (LIFO)
    stack = ["Apple", "Banana", "Orange"]

    # Push elements onto the stack (using append, which adds to the end of the list)

    # Peek: Get the top element without removing it
    print(f"Top element: {stack[-1]}")  # Output: Orange

    # Pop elements from the stack (removes and returns the top element)
    print(stack.pop())  # Output: Orange
    print(stack.pop())  # Output: Banana

    # Check if the stack is empty
    print(f"Is the stack empty? {len(stack) == 0}")  # Output: False

    # Pop the remaining element
    print(stack.pop())  # Output: Apple

    # Check if the stack is empty again
    print(f"Is the stack empty? {len(stack) == 0}")  # Output: True


if __name__ == "__main__":
    main()
