# Create a game for the user to guess the secret word.
# You will propose a secret word and give the possibility for the user to enter only one letter.
# 
# When the user enters a letter, you will check if the entered letter is in the secret word.
#   - If the entered letter is in the secret word; display the letter;
#   - If the entered letter is not in the secret word; display '*'
#
# Keep count of the user's attempts.

import os # To clear the terminal
import sys # To exit the program

# VARIABLE DEFINITION  
SECRET_WORD = "COMPUTER"
word_formed = len(SECRET_WORD) * "*"

letters_unraveled = ""
letters_tried = SECRET_WORD
entered_letter = ""

won_game = False

# INITIAL GAME INSTRUCTIONS
print("HELLO, WELCOME TO GUESS THE WORD GAME")
print("- Only enter one letter at a time.")
print("- Number of attempts is unlimited.")
print("- You win by guessing the word.\n")
start_game = input("Start? [Y] Yes or [N] No: ").upper()

if start_game == 'N':
    sys.exit() # Program terminates

# GAME BEGINS
print(f"\nSecret word: {word_formed}")

while won_game == False:
    entered_letter = input("Enter a letter: ")
    entered_letter = entered_letter.upper() # Standard : Upper

    if len(entered_letter) > 1: # Validation, doesn't count as an attempt
        print("Only ONE LETTER at a time is accepted. Please try again!")
        print(f"Secret word: {word_formed}\n")
        continue
    
    if entered_letter in letters_tried: # Doesn't count as an attempt.
        print("You already entered this letter before.")
        print(f"Secret word: {word_formed}\n")
        continue
    else:
        letters_tried += entered_letter

    if entered_letter in SECRET_WORD:
        letters_unraveled += entered_letter

    word_formed = "" # Clear variable and check again.
    for secret_letter in SECRET_WORD:
        word_formed += secret_letter if secret_letter in letters_unraveled else "*"

        # Another option:
        # word_formed = "".join([secret_letter if secret_letter in letters_unraveled else '*' for secret_letter in SECRET_WORD])

    if word_formed == SECRET_WORD:
        won_game = True
        continue
    
    print(f"Secret word: {word_formed}\n")
else: # GAME ENDS
    os.system('cls') # Or 'clear', it depends on the OS
    print("CONGRATULATIONS! YOU GUESSED THE SECRET WORD!")
    print(f"The secret word was: {SECRET_WORD}")
    print(f"You guessed it in: {len(letters_tried)} attempts")
    sys.exit()
