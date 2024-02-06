# Import the random module to generate random choices for the computer
import random

# Function to get user's choice
# The user is asked to input their choice each time this function is called
def get_user_choice():
    return input("Choose rock, paper, or scissors: ")

# Function to get computer's choice
# The computer's choice is randomly selected from the list ["rock", "paper", "scissors"]
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner of a round
# The function takes the user's choice and the computer's choice as arguments
# The function first checks if the choices are the same, in which case it's a tie
# Then it checks if the user's choice beats the computer's choice according to the game rules
# If the user's choice doesn't beat the computer's choice and it's not a tie, then the computer wins
# The function prints the result of the round and the current score, and returns the scores
def main(user_choice, computer_choice):
    user_score = 0
    computer_score = 0

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("The computer wins!")
        computer_score += 1

    print(f"Score: You - {user_score}, Computer - {computer_score}")
    return user_score, computer_score

# Main game loop
# The game continues as long as the user wants to play again
# Each game consists of rounds that continue until either the user or the computer wins 2 rounds
# The winner of the game is the one who wins 2 rounds first
# After each game, the user is asked if they want to play again
if __name__ == "__main__":
    play_again = 'y'
    while play_again.lower() == 'y':
        user_wins = 0
        computer_wins = 0
        while user_wins < 2 and computer_wins < 2:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"The computer chose: {computer_choice}")
            user_score, computer_score = main(user_choice, computer_choice)
            user_wins += user_score
            computer_wins += computer_score
            print(f"Round Score: You - {user_wins}, Computer - {computer_wins}")
        print("You won the game!") if user_wins > computer_wins else print("The computer won the game!")
        play_again = input("Do you want to play again? (y/n): ")