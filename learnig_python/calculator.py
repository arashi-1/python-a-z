opr = input("Enter the operation you want to perform(+, -,*,/,%) :")
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

if opr == "+":
    print(f"the sum of {num1} and {num2} is {num1+num2}")
elif opr == "-":
    print(f"the substraction of {num1} and {num2} is {num1-num2}")
elif opr == "*":
    print (f"the multiplication of {num1} and {num2} is {round(num1*num2, 2)}")
elif opr == "/":
    if num2 != 0:
        print (f"the division of {num1} and {num2} is {round(num1/num2,2)}")
    else:
        print("Error: Division by zero is not allowed.")    
elif opr == "%":
    print(f"the modules of {num1} and {num2} is {num1%num2}")    
else:
    print(f"Invalid Operation")