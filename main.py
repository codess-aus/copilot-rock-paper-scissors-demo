# Import the random module to generate random choices for the computer
import random

# Function to get the user's choice
def get_user_choice():
    # Prompt the user to enter their choice
    user_choice = input("Choose rock, paper, or scissors: ")
    # Return the user's choice
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    # Define the possible choices
    choices = ["rock", "paper", "scissors"]
    # Let the computer make a random choice
    computer_choice = random.choice(choices)
    # Return the computer's choice
    return computer_choice

# Main function to determine the winner
def main(user_choice, computer_choice):
    # Initialize scores for user and computer
    user_score = 0
    computer_score = 0
    # Check if both choices are the same
    if user_choice == computer_choice:
        print("It's a tie!")
    # Check if the user chose rock
    elif user_choice == "rock":
        # Check if the computer chose paper
        if computer_choice == "paper":
            print("The computer wins!")
            # Increase the computer's score
            computer_score += 1
        else:
            print("You win!")
            # Increase the user's score
            user_score += 1
    # Check if the user chose paper
    elif user_choice == "paper":
        # Check if the computer chose scissors
        if computer_choice == "scissors":
            print("The computer wins!")
            # Increase the computer's score
            computer_score += 1
        else:
            print("You win!")
            # Increase the user's score
            user_score += 1
    # Check if the user chose scissors
    elif user_choice == "scissors":
        # Check if the computer chose rock
        if computer_choice == "rock":
            print("The computer wins!")
            # Increase the computer's score
            computer_score += 1
        else:
            print("You win!")
            # Increase the user's score
            user_score += 1
    else:
        print("That's not a valid choice!")
    # Print the current scores
    print(f"Score: You - {user_score}, Computer - {computer_score}")
    # Return the scores
    return user_score, computer_score

# Check if this script is the main program
if __name__ == "__main__":
    # Initialize the play again variable
    play_again = 'y'
    # Keep playing as long as the user wants to play again
    while play_again.lower() == 'y':
        # Initialize the round wins for user and computer
        user_wins = 0
        computer_wins = 0
        # Keep playing rounds until someone wins 2 rounds
        while user_wins < 2 and computer_wins < 2:
            # Get the user's and computer's choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            # Print the computer's choice
            print(f"The computer chose: {computer_choice}")
            # Get the scores for this round
            user_score, computer_score = main(user_choice, computer_choice)
            # Update the round wins based on the scores
            if user_score > computer_score:
                user_wins += 1
            elif computer_score > user_score:
                computer_wins += 1
            # Print the round scores
            print(f"Round Score: You - {user_wins}, Computer - {computer_wins}")
        # Check who won the game
        if user_wins > computer_wins:
            print("You won the game!")
        else:
            print("The computer won the game!")
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")