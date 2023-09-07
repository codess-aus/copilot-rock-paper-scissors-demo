# Write a rock, paper, scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input.
# The game will end after one player wins best out of three.
# Then ask the player if they want to play again.
# After each round, print who won that round and the overall score.

import random

def game():
    print("Welcome to rock, paper, scissors!")
    user_score = 0
    computer_score = 0
    while user_score < 3 and computer_score < 3:
        user_choice = input("Please choose rock, paper, or scissors: ").lower()
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            computer_choice = "rock"
        elif computer_choice == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"
        if user_choice == "rock" and computer_choice == "rock":
            print("You chose rock, the computer chose rock. It's a tie!")
        elif user_choice == "rock" and computer_choice == "paper":
            print("You chose rock, the computer chose paper. You lose this round!")
            computer_score += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You chose rock, the computer chose scissors. You win this round!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You chose paper, the computer chose rock. You win this round!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "paper":
            print("You chose paper, the computer chose paper. It's a tie!")
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You chose paper, the computer chose scissors. You lose this round!")
            computer_score += 1
        elif user_choice == "scissors" and computer_choice == "rock":
            print("You chose scissors, the computer chose rock. You lose this round!")
            computer_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You chose scissors, the computer chose paper. You win this round!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "scissors":
            print("You chose scissors, the computer chose scissors. It's a tie!")
        else:
            print("Please enter a valid choice.")
    if user_score == 3:
        print("You won best out of three!")
    else:
        print("You lost best out of three!")
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")

game()

# Path: main.py


