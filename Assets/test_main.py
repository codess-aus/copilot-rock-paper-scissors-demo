# Import the unittest module, which provides tools for constructing and running tests.
import unittest

# Import the main function from the main module (main.py file).
from main import main

# Define a class TestMain that inherits from unittest.TestCase. 
# TestCase is a base class for all test cases in unittest.
class TestMain(unittest.TestCase):

    # Define a test method. Each test method should start with the word 'test'.
    def test_user_wins(self):
        # Call the main function with "rock" as the user's choice and "scissors" as the computer's choice.
        # According to the game rules, the user should win this round.
        user_score, computer_score = main("rock", "scissors")
        # Assert that the user's score is 1 (indicating a win).
        self.assertEqual(user_score, 1)
        # Assert that the computer's score is 0 (indicating a loss).
        self.assertEqual(computer_score, 0)

    # Define another test method to test the scenario where the computer wins.
    def test_computer_wins(self):
        # Call the main function with "rock" as the user's choice and "paper" as the computer's choice.
        # According to the game rules, the computer should win this round.
        user_score, computer_score = main("rock", "paper")
        # Assert that the user's score is 0 (indicating a loss).
        self.assertEqual(user_score, 0)
        # Assert that the computer's score is 1 (indicating a win).
        self.assertEqual(computer_score, 1)

    # Define another test method to test the scenario where there's a tie.
    def test_tie(self):
        # Call the main function with "rock" as both the user's and the computer's choice.
        # According to the game rules, this should result in a tie.
        user_score, computer_score = main("rock", "rock")
        # Assert that both the user's and the computer's scores are 0 (indicating a tie).
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 0)

# This line checks if this script is the main module - that is, if it's being run directly.
# If it is, it calls unittest.main(), which runs the test methods.
if __name__ == '__main__':
    unittest.main()