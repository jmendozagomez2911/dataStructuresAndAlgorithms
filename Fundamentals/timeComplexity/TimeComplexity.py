# TimeComplexity
# This program demonstrates the basic usage of arrays and explains time complexity and memory complexity.

def main():
    # Arrays in Python (lists) Python lists are dynamic, meaning you can modify their size. However, they can still
    # behave similarly to arrays in other languages like Java. In low-level languages like C or Java, arrays are not
    # dynamic structures. Once created, their size is fixed. For example, if it's an array of ints in Java,
    # each element typically occupies 4 bytes. In the case of objects, each element holds a reference.

    int_array = [0] * 7  # Create an array (list) of size 7 in Python, initialized to zeros.

    # Initializing array values
    int_array[0] = 20
    int_array[1] = 35
    int_array[2] = -15
    int_array[3] = 7
    int_array[4] = 55
    int_array[5] = 1
    int_array[6] = -22

    # Iterating through the array and printing elements
    for i in range(len(int_array)):
        print(f"element {i}: {int_array[i]}")

    # Time complexity and memory complexity
    print("\nThere are two types of complexity:")
    print("1. Time complexity: Number of steps involved to run an algorithm (measured using Big O notation).")
    print("2. Memory complexity: Amount of memory it takes to run an algorithm (measured in terms of space usage).")

    # Note: In modern systems, memory is often less of a constraint, so time complexity tends to be more critical.


if __name__ == "__main__":
    main()
