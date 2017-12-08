# Hangman Game
# Marc B

def start_screen():
    print("***************")
    print("****Hangman****")
    print("***************")

def show_credits():
    print()
    print("This awesome hangman game was made by Marc.")
    print("      Created on Novemenber 11, 2017         ")
    
def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if (letter).isalpha():
                return letter
            else:
                print("You may only enter one letter at a time!")
            
        else:
            print("You may only enter one letter at a time!")
            
def display_board(solved):
    print(solved)

def show_result(result):
    if result == 0:
        print("You win!")
    else:
        print("You lost!")

def play_again(name):
    while True:
        decision = input("Would you like to play again? (y/n) ")
        print()
        decision = decision.lower()

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            print("Ok, Bye!")
            return False
        
        else:
            print("I don not understand, please enter valid response")
    
def play(name):
    print("Welcome to my hangman game, " + name + "!")
    print("You'll only have 6 tries to get the word")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6
    result = 0
    print(solved)
    gameover = 0

    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes +=1
            print("Letter not in word")
            print("You currently have " + str(strikes) + " strikes")
            print()
            if strikes ==  limit:
                print("You lost" + name + "!")
                result = 1
                gameover = 1
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(result)

#Game Starts
start_screen()
playing = True

while playing:
    print()
    name = input("What is your name? ")
    play(name)
    playing = play_again(name)
show_credits()
