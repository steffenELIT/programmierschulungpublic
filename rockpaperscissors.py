import random

moves = ["rock", "paper", "scissors"]

user = input("move: ").strip().lower()
computer = random.choice(moves)

print("computer:", computer)

if user == computer:
    print("draw")
elif (user == "rock" and computer == "scissors") or (user == "rock" and computer == "scissors") or (user == "rock" and computer == "scissors"):
    print("you win")
else:
    print("you lose")

"""
AUFGABEN:
1. Programm loopen bis man "quit" eingibt.
2. "lizard" und "spock" hinzufügen
3. unerlaubten input verweigern
"""