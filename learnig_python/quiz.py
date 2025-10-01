questions =("who trained luffy?",
           "who is the man marked with fire?",
           "why did imu destroyed lucia kingdom?",
           "who killed Vegapunk?")

options =(("A:Copper B:Garp C:Reighley D:Shanks"),
        ("A:Dragon B:Sabo C:Ace D:unknown"),
        ("A:to test mother flame B:people didn't gave him/her shit C:he/she's bitch D:just to have fun"),
        ("A:saturn B:kizaru C:imu D:marine soldiers"))
answers =("C","D","A","B")

guesses = []
score =0
ques_num =0

for question in questions:
    print("---------------------------------------------")
    print(question)

    for option in options[ques_num]:
        print(option, end="")
    print()    
    guess = input("chooses the correct Option : ").upper()  
    guesses.append(guess); 

    if(guess == answers[ques_num]):
        print("correct answer")
        score+=1
    else:
        print(f"you'r wrong {answers[ques_num]}")
    ques_num += 1   
      
    print() 
print("=============================================")
print("Quiz Complete!")
print(f"Your score: {score}/{len(questions)}")  
print("=============================================")     

 