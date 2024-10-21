# This example shows that even after setting one variable (original) to None,
# the reference held by another variable (reference) remains intact and still
# points to the original object (integer with value 5).

def main():
    # Step 1: Declare and initialize variables
    original = 5  # 'original' points to an integer object with value 5
    reference = original  # 'reference' points to the same integer object as 'original'

    # Step 2: Print the values to see the references
    print(f"Original value: {original}")   # Should print: Original value: 5
    print(f"Reference value: {reference}") # Should print: Reference value: 5

    # Step 3: Set 'original' to None (Python's equivalent of null)
    original = None

    # Step 4: Print the values again to see the effect
    print(f"Original after setting: {original}")   # Should print: Original after setting: None
    print(f"Reference after setting: {reference}") # Should print: Reference after setting: 5

if __name__ == "__main__":
    main()
