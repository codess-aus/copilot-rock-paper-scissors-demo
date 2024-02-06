# Import the random module to generate random choices for the computer
import random

# Get user's choice
def get_user_choice():
    return input("Choose rock, paper, or scissors: ")

# Get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Determine the winner
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