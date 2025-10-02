import random
option=["stone","paper", "scissors"]
computer = random.choice(option)
is_playing = True
print("Welcome to Stone Paper and Scissors Game")
while is_playing:
    answer = input("enter your choice (stone, paper, scissors): ").lower()
    if answer not in option:
        print("Invalid Choice")
    elif answer == "stone" and computer == "scissors":
        print("You Win")
    elif answer == "paper" and computer == "stone":
        print("You Win")
    elif answer == "scissors" and computer == "stone":
        print("You Win")   
    elif answer == "stone" and computer == "stone" or answer == "scissors" and computer == "scissors" or answer == "paper" and computer == "paper" :
        print("Tie")
    else:
        print("You loose")

    play = input("Play again (y/n): ").lower()
    if "y" not in play:
        is_playing = False

print("Thanks for Playing")