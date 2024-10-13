import array


# Arrays
# Data Structure that can store a fixed-size collection of elements of the same data type

def main():
    # Step 1: Declare an array
    numbers = array.array('i')  # 'i' stands for integer type array

    # Step 2: Initialize the array with a fixed size and populate it with values
    numbers = array.array('i', [10, 20, 30, 40, 50])  # Array of integers

    # Step 3: Access and print elements of the array
    print("Accessing individual elements:")
    print(f"First element: {numbers[0]}")
    print(f"Second element: {numbers[1]}")

    # Step 4: Modify elements of the array
    numbers[2] = 35  # Change the third element to 35

    # Step 5: Iterating through the array by index
    print("\nIterating through the array by index:")
    for i in range(len(numbers)):
        print(f"Element at index {i}: {numbers[i]}")

    # Step 6: Using a for-each loop (enhanced for loop in Java) to iterate over the array
    print("\nUsing for-each loop:")
    for num in numbers:
        print(num)

    # Step 7: Find the length of the array
    print(f"\nLength of the array: {len(numbers)}")

    # Step 8: Combined declaration, initialization, and population of another array
    more_numbers = array.array('i', [5, 10, 15, 20, 25])
    print("\nCombined declaration and initialization:")
    for num in more_numbers:
        print(num)

    # Step 9: Insert a new element in the middle of the array (at index 2)
    print("\nInserting 25 at index 2:")
    numbers.insert(2, 25)  # Inserting at the middle (shifts elements to the right)

    # Step 10: Print the array after insertion
    print("Array after inserting 25 at index 2:")
    for num in numbers:
        print(num)

    # Step 11: Print the length of the array after insertion
    print(f"\nLength of the array after insertion: {len(numbers)}")

    # Step 12: Access an element at a specific index
    index = 3
    print(f"\nAccessing element at index {index}: {numbers[index]}")

    # Step 13: Search index for an element in the array
    search_element = 35
    if search_element in numbers:
        print(f"\nElement {search_element} found at index {numbers.index(search_element)}")
    else:
        print(f"\nElement {search_element} not found in the array")

    # Step 14: Delete an element from the array
    print(f"\nDeleting element {search_element} from the array.")
    numbers.remove(search_element)  # Remove the first occurrence of the element
    print("Array after deletion:")
    for num in numbers:
        print(num)

    # Step 15: Print the length of the array after deletion
    print(f"\nLength of the array after deletion: {len(numbers)}")


if __name__ == "__main__":
    main()
