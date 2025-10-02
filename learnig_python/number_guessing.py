import random
lowest =1
highest =100
answer = random.randint(lowest, highest)
guesses = 0
is_playing = True

print("Welcome to Number Guessing Game")

while is_playing:
    guess = input(f"Enter a number between {lowest} and {highest} : ")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1;

        if guess <lowest or guess > highest:
            print("Your input is Out of Range, Enter valid input ")
        elif guess < answer:
            print("Too Low! Try again!!")   
        elif guess > answer:
            print("Too High! Try again!!")
        else:
            print(f"Correct!! The answer is {answer}")  
            print(f"number of guesses : {guesses}")
            is_playing = False       
    else:
        print("Enter a valid input")

