# Queues follow the FIFO (First In, First Out) order.
# Principle: The first element added to the collection will be the first one to be removed.
# Queues are often used in scenarios where elements need to be processed in a specific order,
# such as task scheduling, breadth-first search algorithms, etc.

from collections import deque


def main():
    # Initialize a queue using deque (deque is ideal for implementing queues in Python)
    queue = deque()

    # Add elements to the queue
    queue.append("Apple")
    queue.append("Banana")
    queue.append("Orange")
    queue.append("Cherry")

    # Peek: Retrieves, but does not remove, the front element of the queue
    print(f"Front element: {queue[0]}")
    print(f"Size of queue: {len(queue)}")  # Output: 4

    # Remove: Retrieves and removes the front element of the queue (FIFO order)
    print(queue.popleft())  # Output: Apple
    print(queue.popleft())  # Output: Banana

    # Check if the queue is empty
    print(f"Is the queue empty? {len(queue) == 0}")  # Output: False

    print(queue.popleft())  # Output: Orange

    # Check if the queue is empty again
    print(f"Is the queue empty? {len(queue) == 0}")  # Output: False

    # Final removal, now the queue should be empty
    print(queue.popleft())  # Output: Cherry
    print(f"Is the queue empty? {len(queue) == 0}")  # Output: True


if __name__ == "__main__":
    main()
