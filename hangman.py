import random

# Predefined list of words for the game
WORDS = ["python", "intelligence", "hangman", "algorithm", "machine", "learning", "neural", "network", "analysis"]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    # Select a random word from the list
    word = random.choice(WORDS)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 5  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        # Display the current state of the word
        print("\nCurrent word:", display_word(word,     guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {attempts}")

        # Get user input
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is in the word
        if guess in word_letters:
            print("Correct guess!")
            word_letters.remove(guess)
        else:
            print("Incorrect guess!")
            attempts -= 1

        # Check if the word is fully guessed
        if not word_letters:
            print("\nCongratulations! You guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Run the Hangman game
hangman_game()
