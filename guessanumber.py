import os
import random

print("This is a number guessing game. Enter the range from which a number will be picked randomly.\n\
The goal is to find the number with minimal amount of guesses.")

def game():
    amount_of_guesses = 0

    while(True): # catching input errors, retrying if necessary 
        
        try:
            lower = int(input("Set lower bound: ")) 
            upper = int(input("Set upper bound: "))
            the_number = random.randint(lower,upper)
            break
        
        except ValueError:
            print("Only integers are accepted. Try again:")
            
    # handling guesses quitting after right guess
    while(True):

        guess = int(input("Enter your guess: "))

        if(guess == the_number):
            if(amount_of_guesses == 0):
                print(f'\nYou guessed the correct num1ber with a single guess!!')
            else:
                print(f'\nYou guessed the correct number with {amount_of_guesses+1} guesses.' )
            break
        
        else:
            amount_of_guesses += 1
            if (guess > the_number):
                print("The number we are looking for is lower")
            else:
                print("The number we are looking for is higher")

game() # starting the first game

# game continues while user inputs 1
while(True):
    try:
        g = int(input("Do you want to play again?\n1 Yes\n0 Quit\n"))
        if (g == 1):
            game()
        else:
            break

    except ValueError:
        print("Only 1 or 0 are accepted")

