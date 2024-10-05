# Arrays
# Data Structure that can store a fixed-size collection of elements of the same data type

def main():
    # Step 1: Declare an array (list in Python)
    numbers = []

    # Step 2: Initialize the array (list) with a fixed size
    numbers = [0] * 5  # Creates a list with 5 elements initialized to 0

    # Step 3: Populate the array (list) with values
    numbers[0] = 10  # Assign value to the first element
    numbers[1] = 20  # Assign value to the second element
    numbers[2] = 30  # Assign value to the third element
    numbers[3] = 40  # Assign value to the fourth element
    numbers[4] = 50  # Assign value to the fifth element

    # Step 4: Access and print elements of the array (list)
    print("Accessing individual elements:")
    print(f"First element: {numbers[0]}")
    print(f"Second element: {numbers[1]}")

    # Step 5: Modify elements of the array (list)
    numbers[2] = 35  # Change the third element to 35

    # Step 6: Iterate through the array (list) using a for loop
    print("\nIterating through the array:")
    for i in range(len(numbers)):
        print(f"Element at index {i}: {numbers[i]}")

    # Step 7: Using a for-each loop (enhanced for loop in Java)
    print("\nUsing for-each loop:")
    for num in numbers:
        print(num)

    # Step 8: Find the length of the array (list)
    print(f"\nLength of the array: {len(numbers)}")

    # Step 9: Combined declaration, initialization, and population
    more_numbers = [5, 10, 15, 20, 25]
    print("\nCombined declaration and initialization:")
    for num in more_numbers:
        print(num)


if __name__ == "__main__":
    main()
