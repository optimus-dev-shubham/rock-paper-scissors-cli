import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Mapping choices
choice_map = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

# Winning conditions
win_conditions = {
    ("r", "s"),
    ("p", "r"),
    ("s", "p")
}

# Load responses
with open("win_list_professional.txt", encoding="utf-8") as f1, \
     open("lose_list_professional.txt", encoding="utf-8") as f2:

    win_list = [line.strip() for line in f1.readlines()]
    lose_list = [line.strip() for line in f2.readlines()]

# Score tracking
player_score = 0
computer_score = 0
draws = 0

print(Fore.CYAN + "🎮 Welcome to Rock Paper Scissors")
print(Fore.BLUE + "Type 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit.\n")

while True:
    player_choice = input(Fore.WHITE + "👉 Your move: ").lower()

    if player_choice == "q":
        print(Fore.MAGENTA + "\n👋 Thanks for playing!")
        print(Fore.CYAN + f"Final Score → You: {player_score} | Computer: {computer_score} | Draws: {draws}")
        break

    if player_choice not in ["r", "p", "s"]:
        print(Fore.RED + "⚠️ Invalid input! Please enter 'r', 'p', or 's'.\n")
        continue

    computer_choice = random.choice(["r", "p", "s"])

    print(Fore.YELLOW + f"\nYou chose {choice_map[player_choice]}")
    print(Fore.YELLOW + f"I chose {choice_map[computer_choice]}")

    # Game logic
    if player_choice == computer_choice:
        print(Fore.YELLOW + "🤝 It's a draw! Great minds think alike.\n")
        draws += 1

    elif (player_choice, computer_choice) in win_conditions:
        print(Fore.GREEN + "😎 " + random.choice(win_list) + "\n")
        player_score += 1

    else:
        print(Fore.RED + "💀 " + random.choice(lose_list) + "\n")
        computer_score += 1

    # Show current score
    print(Fore.CYAN + f"📊 Score → You: {player_score} | Computer: {computer_score} | Draws: {draws}\n")