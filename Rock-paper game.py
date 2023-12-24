#####################################################################
# ---------------------CodeSoft Internship--------------------------#
# Created: 5/12/2023 9:25:34 PM                                     #
# Author: Salah Eldeen Mohamed Hemdan                               #
# Project: Rock Paper Scissors Game                                 #
#####################################################################

############################ Import Section ################################
import random

############################ Function Section ################################
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '4':
            print("\nFinal Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing. Goodbye!")
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ('1', '2', '3'):
            user_choice = choices[int(user_choice) - 1]

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

############################ Program Section ################################
if __name__ == "__main__":
    play_game()
