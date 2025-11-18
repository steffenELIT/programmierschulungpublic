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
1. "lizard" und "spock" hinzufügen
2. Programm loopen bis man "quit" eingibt.
3. unerlaubten input verweigern

"""
