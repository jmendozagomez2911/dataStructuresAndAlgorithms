"""
Set Operations Example Program
This program demonstrates the use of set operations such as union, intersection, and difference using two input tuples.
"""


def main():
    # Define two example tuples
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 5, 6, 7, 8)

    # Convert tuples to sets
    set1 = set(tuple1)
    set2 = set(tuple2)

    # 1. Union of sets: combines all unique elements from both sets
    # The union of two sets contains all the elements present in either set.
    union_result = set1 | set2  # Same as set1.union(set2)
    print(f"Union of {set1} and {set2}: {union_result}")

    # 2. Intersection of sets: elements that are present in both sets
    # The intersection of two sets contains only the elements that are present in both sets.
    intersection_result = set1 & set2  # Same as set1.intersection(set2)
    print(f"Intersection of {set1} and {set2}: {intersection_result}")

    # 3. Difference of sets: elements that are in the first set but not in the second set
    # The difference between two sets contains elements that are only in the first set and not in the second.
    difference_result = set1 - set2  # Same as set1.difference(set2)
    print(f"Difference of {set1} - {set2}: {difference_result}")

    # 4. Symmetric Difference: elements in either set1 or set2 but not in both
    # The symmetric difference contains elements that are in either set1 or set2 but not in both.
    symmetric_difference_result = set1 ^ set2  # Same as set1.symmetric_difference(set2)
    print(f"Symmetric difference between {set1} and {set2}: {symmetric_difference_result}")


if __name__ == "__main__":
    main()
