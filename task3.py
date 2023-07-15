import random
choices = ["rock", "paper", "scissors"]
userchoice = input("Enter your choice (rock, paper, scissors): ")
computerchoice = random.choice(choices)
print("You chose", userchoice)
print("The computer chose", computerchoice)
if userchoice == "rock":
    if computerchoice == "scissors":
        print("You win the game!")
    else:
        print("You lose the game!")
elif userchoice == "paper":
    if computerchoice == "rock":
        print("You win the game!")
    else:
        print("You lose the game!")
elif userchoice == "scissors":
    if computerchoice == "paper":
        print("You win the game!")
    else:
        print("You lose the game!")
else:
    print("Invalid choice.")
