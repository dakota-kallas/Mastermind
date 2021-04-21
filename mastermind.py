#
# A Python version of the Mastermind game.
#
# Author: Dakota Kallas
# Date: April 21, 2021
#

import random

# Class to represent an instance of the Mastermind game
class Mastermind():
    # Instance variable used to preset the peg pattern
    GRADING = False

    # Function to initialize an instance of the Mastermind class
    def __init__(self):
        self.guesses = []
        self.results = []
        self.target_pattern = []
        # Dictionaries of colors used in game [Black, White, Red, Green, Purple, Orange]
        self.colors = {0:'B', 1:'W', 2:'R', 3:'G', 4:'P', 5:'O'}
        self.valid = {'B':0, 'W':1, 'R':2, 'G':3, 'P':4, 'O':5}

    # Function used to play the game
    def play(self):
        # Print a beginning message to the user
        print("Welcome to the game of Mastermind!\n")
        solved = False
        
        Mastermind.ask_directions(self)

        # Generate the random peg pattern
        if self.GRADING == False:
            guess = []
            for index in range(0,4):
                random_color = random.randint(0,5)
                guess.append(self.colors.get(random_color))
            self.target_pattern = guess
        # If GRADING is true, preset the peg pattern
        else:
            self.target_pattern = ['W', 'G', 'W', 'O']

        # Have the user guess until they guess correctly
        while solved == False:
            guess = Mastermind.get_guess(self)

            # If the input is valid, evaluate the guess
            self.guesses.append(guess)
            correctness = Mastermind.evaluate_guess(self, guess)
            self.results.append(correctness)
            if correctness[0] == 4:
                solved = True
            else:
                print("Incorrect Guess.")
                Mastermind.print_board(self)

        print("You guess correctly! Congragulations on being a Mastermind!\n")

    # Parameters: none
    # Returns: a valid game pattern, indicating the user’s guess, in your chosen representation
    def get_guess(self):
        valid = False
        while valid == False:
            # Get input from the user
            guess = input('Enter your guess: ')
            guess = guess.strip().split()
            valid = True

            # Check to see if the input is valid
            if len(guess) == 4:
                for e in guess:
                    if e not in self.valid.keys():
                        valid = False
                        print("Invalid input.\n")
                        break
            else:
                valid = False
                print("Invalid input.\n")

        # Return the guess once it is valid
        return guess

    # Parameters: a valid game pattern – guess, a valid game pattern – target
    # Returns: sequence of pegs indicating correctness of the guess, in your chosen
    #          representation
    def evaluate_guess(self, guess):
        black = 0
        white = 0
        # Array used to check if a peg has already been sued to compare to
        compared = [0, 0, 0, 0]

        # Iterate through the guess to determine its correctness
        for i in range(0,4):
            # Determine when it should have a black peg of correctness
            if guess[i] == self.target_pattern[i]:
                black += 1
                if compared[i] == 1:
                    white -= 1
                compared[i] = 1
            # Determine when it should have a white peg of correctness
            else:
                for p in range(0,4):
                    if guess[i] == self.target_pattern[p] and compared[p] == 0:
                        white += 1
                        compared[p] = 1
                        break
        return [black, white]

    # Parameters: a valid game board
    # Returns: none
    def print_board(self):
        for i in range(0, len(self.guesses)):
            g = self.guesses[i]
            r = self.results[i]
            print("[#{}] Guess: {} {} {} {}   |   Results: b={} w={}".format(i, g[0], g[1], g[2], g[3], r[0], r[1]))
        print()

    def ask_directions(self):
        valid = False
        answer = input("Would you like to know how to play? (Y or N): ")
        while valid == False:
            answer = answer.strip().split()

            if len(answer) == 1:
                if answer[0] == 'N' or answer[0] == 'Y':
                    valid = True
                else:
                    print("Invalid input.\n")
                    answer = input("Would you like to know how to play? (Y or N): ")
            else:
                print("Invalid input.\n")
                answer = input("Would you like to know how to play? (Y or N): ")

        if answer[0] == 'Y':
            print("\nYou must guess the 4 peg pattern by entering 4 upper-case letters")
            print("that represent the peg colors seperated by spaces. (Ex. B O W R)")
            print("Green = G | Purple = P | Orange = O | Black = B | Red = R | White = W\n")
            print("The results of your guess are return as either black (b) or white (w).")
            print("Black represents that you guessed the correct color and posistion for a peg,")
            print("while white represents you guessed the correct color but incorrect position")
            print("for a single peg.")
            print("Tip: You can use this pattern to help find the correct answer!\n")


        