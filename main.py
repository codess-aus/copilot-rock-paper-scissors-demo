#Create a rock, paper, scissors game where it is the player vs the computer.
#The computer’s answer will be randomly generated, while the program will ask the user for their input.
#The game will be a best of 3 rounds, and will keep score until the end.
#After each round, it will ask the user if they want to play again.
#If they say yes, it will start over, otherwise it will end the game and print out the scores.
#each function should be clearly commented and have a docstring
#use a main function to run the game
#use a function for each of the following:
#computer’s random choice
#user’s choice
#determine the winner
#keep score
#ask the user if they want to play again
#use a loop to keep the game running
#after each round, print out what the computer chose, what the user chose, and who won
#at the end of the game, print out the final scores and declare who is the champion

# import random module
import random

# define main function
def main():
    # define variables
    player_score = 0
    computer_score = 0
    rounds = 0
    # define loop
    while rounds < 3:
        # call get_player_choice function
        player_choice = get_player_choice()
        # call get_computer_choice function
        computer_choice = get_computer_choice()
        # call determine_winner function
        winner = determine_winner(player_choice, computer_choice)
        # print computer choice
        print("Computer chose " + computer_choice + ".")
        # print player choice
        print("Player chose " + player_choice + ".")
        # print winner
        if winner == "tie":
            print("It's a tie!")
        else:
            print(winner.capitalize() + " wins the round!")
        # call keep_score function
        player_score, computer_score = keep_score(winner, player_score, computer_score)
        # call print_score function
        print_score(player_score, computer_score)
        # add 1 to rounds
        rounds += 1
    # print final scores
    print("Final scores:")
    print("Player score: " + str(player_score))
    print("Computer score: " + str(computer_score))
    print("And the champion is...")
    # define if statements
    if player_score > computer_score:
        print("PLAYER!")
    elif computer_score > player_score:
        print("COMPUTER!")
    else:
        print("IT'S A TIE!")
    # call play_again function
    play_again()

# define get_player_choice function
def get_player_choice():
    # define loop
    while True:
        # ask user for input
        player_choice = input("Rock, paper, or scissors? ")
        # if input is valid, break loop
        if player_choice.lower() == "rock" or player_choice.lower() == "paper" or player_choice.lower() == "scissors":
            break
        # if input is invalid, print error message
        else:
            print("Invalid input. Please try again.")
    # return player_choice
    return player_choice

# define get_computer_choice function
def get_computer_choice():
    # define list of choices
    choices = ["rock", "paper", "scissors"]
    # randomly choose a choice from list
    computer_choice = random.choice(choices)
    # return computer_choice
    return computer_choice

# define determine_winner function
def determine_winner(player_choice, computer_choice):
    # define if statements
    if player_choice.lower() == "rock" and computer_choice.lower() == "scissors":
        winner = "player"
    elif player_choice.lower() == "paper" and computer_choice.lower() == "rock":
        winner = "player"
    elif player_choice.lower() == "scissors" and computer_choice.lower() == "paper":
        winner = "player"
    elif player_choice.lower() == "rock" and computer_choice.lower() == "paper":
        winner = "computer"
    elif player_choice.lower() == "paper" and computer_choice.lower() == "scissors":
        winner = "computer"
    elif player_choice.lower() == "scissors" and computer_choice.lower() == "rock":
        winner = "computer"
    else:
        winner = "tie"
    # return winner
    return winner

# define keep_score function
def keep_score(winner, player_score, computer_score):
    # define if statements
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    # return player_score and computer_score
    return player_score, computer_score

# define print_score function
def print_score(player_score, computer_score):
    # print scores
    print("Player score: " + str(player_score))
    print("Computer score: " + str(computer_score))

# define play_again function
def play_again():
    # define loop
    while True:
        # ask user if they want to play again
        play_again = input("Do you want to play again? ")
        # if input is valid, break loop
        if play_again.lower() == "yes" or play_again.lower() == "no":
            break
        # if input is invalid, print error message
        else:
            print("Invalid input. Please try again.")
    # if user wants to play again, call main function
    if play_again.lower() == "yes":
        main()
    # if user does not want to play again, print goodbye message
    elif play_again.lower() == "no":
        print("Thanks for playing! Goodbye!")

# call main function
main()

# end program