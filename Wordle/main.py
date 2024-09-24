import random

def choose_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def main():
    
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
            if attempts == 0:
                print("\nGame over! The word was:", word)
                break

if __name__ == "__main__":
    main()
