import unittest
from main import main, get_computer_choice

class TestMain(unittest.TestCase):

    def test_all_possible_outcomes(self):
        # Test all possible outcomes
        outcomes = [
            ("rock", "scissors", 1, 0),
            ("rock", "paper", 0, 1),
            ("rock", "rock", 0, 0),
            ("paper", "rock", 1, 0),
            ("paper", "scissors", 0, 1),
            ("paper", "paper", 0, 0),
            ("scissors", "rock", 0, 1),
            ("scissors", "paper", 1, 0),
            ("scissors", "scissors", 0, 0),
        ]
        for user_choice, computer_choice, expected_user_score, expected_computer_score in outcomes:
            user_score, computer_score = main(user_choice, computer_choice)
            self.assertEqual(user_score, expected_user_score)
            self.assertEqual(computer_score, expected_computer_score)

    def test_invalid_input(self):
        # Test invalid input from the user
        user_choice = "invalid"
        computer_choice = get_computer_choice()
        user_score, computer_score = main(user_choice, computer_choice)
        # The game should return 0 for both scores when the user input is invalid
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 0)

    def test_multiple_rounds(self):
        # Test multiple rounds
        user_choices = ["rock", "rock", "scissors"]
        computer_choices = ["scissors", "paper", "rock"]
        expected_user_scores = [1, 0, 0]
        expected_computer_scores = [0, 1, 1]
        for i in range(3):
            user_score, computer_score = main(user_choices[i], computer_choices[i])
            self.assertEqual(user_score, expected_user_scores[i])
            self.assertEqual(computer_score, expected_computer_scores[i])

if __name__ == '__main__':
    unittest.main()