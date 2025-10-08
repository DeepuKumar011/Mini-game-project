import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 's' and computer == 'w') or \
         (user == 'w' and computer == 'g') or \
         (user == 'g' and computer == 's'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
    print("Type: 's' for Snake, 'w' for Water, 'g' for Gun")
    print("Type 'exit' to quit the game anytime.\n")

    choices = ['s', 'w', 'g']

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("👋 Thanks for playing! See you next time.")
            break
        elif user_choice not in choices:
            print("⚠️ Invalid input! Please choose 's', 'w', or 'g'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")

# Run the game
play_game()
