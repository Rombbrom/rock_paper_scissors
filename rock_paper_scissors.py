from random import randint

choice = ["rock", "paper", "scissors"]
computer_choice = choice[randint(0, 2)]
print("Let's play Rock, Paper, Scissors!")
user_choice = input("Enter rock, paper, or scissors: ").lower()
if user_choice not in choice:
    print("Invalid choice. Please try again.")
else:
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
