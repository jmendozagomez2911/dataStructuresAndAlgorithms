# SortAlgorithms
# This class contains two sorting algorithms: selection sort and insertion sort.
# Each of these algorithms is explained in the comments along with their time complexity and characteristics.

def selection_sort(arr):
    """
    Selection Sort Algorithm:
    - In-place sorting algorithm
    - Time complexity: O(n^2) (quadratic)
    - Unstable sort
    - It selects the smallest element from the unsorted portion of the list
      and swaps it with the element at the current index.
    """
    for i in range(len(arr) - 1):
        lowest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j  # Searching for the lowest index
        # Swap the found minimum element with the element at the current index
        smaller_number = arr[lowest_index]
        arr[lowest_index] = arr[i]
        arr[i] = smaller_number


def insertion_sort(arr):
    """
    Insertion Sort Algorithm:
    - In-place sorting algorithm
    - Time complexity: O(n^2) (quadratic)
    - Stable sort
    - It works by building a sorted portion of the list one element at a time,
      by inserting each new element in its correct position relative to the already sorted portion.
    """
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        # Move elements of arr[0,...,i], that are greater than key, to one position ahead of their current position
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


def main():
    # Selection Sort Example
    print("Selection Sort:")
    arr1 = [9, 14, 3, 2, 43, 11, 58, 22]
    print("Before Selection Sort:")
    print(arr1)

    selection_sort(arr1)
    print("After Selection Sort:")
    print(arr1)

    # Insertion Sort Example
    print("\nInsertion Sort:")
    arr2 = [9, 14, 3, 2, 43, 11, 58, 22, 33]
    print("Before Insertion Sort:")
    print(arr2)

    insertion_sort(arr2)
    print("After Insertion Sort:")
    print(arr2)


if __name__ == "__main__":
    main()
