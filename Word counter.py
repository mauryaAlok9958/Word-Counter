def count_words(text):
    """
    Function to count the number of words in a given text.
    """
    # Split the text into words based on whitespace
    words = text.split()
    # Return the count of words
    return len(words)
def main():
    """
    Main function to prompt user input, count words, and display the result.
    """
    print("Welcome to the Word Counter Program!")
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ").strip()

    # Check if the input text is empty
    if not text:
        print("Error: Empty input. Please enter some text.")
    else:
        # Count the number of words
        word_count = count_words(text)
        # Display the word count
        print(f"Number of words in the text: {word_count}")

if __name__ == "__main__":
    main()
