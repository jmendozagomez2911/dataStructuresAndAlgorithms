# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output:
# {'apple': 3, 'orange': 2, 'banana': 1}


# Function to count word frequency
def count_word_frequency(words):
    dictionary = {}
    for i in range(len(words)):
        if words[i] in dictionary:
            pass  # If the word is already counted, skip it
        else:
            conteo = 1  # Initialize count for the current word
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    conteo += 1  # Increment count for matching word
            dictionary[words[i]] = conteo  # Add the word and its count to the dictionary
    return dictionary


# APPROACH MORE EFFICIENTLY
# def count_word_frequency(words):
# word_count = {}
# for word in words:
#    word_count[word] = word_count.get(word, 0) + 1
# return word_count

# Main program
def main():
    # Sample list of words
    words = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi"]

    # Call the function to count word frequency
    word_frequencies = count_word_frequency(words)

    # Print the result
    print(f"Word Frequencies: {word_frequencies}")


if __name__ == "__main__":
    main()
