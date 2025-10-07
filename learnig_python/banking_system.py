def show_amount(balance):
    print(f"Your current balance is ${balance:.2f}")
def deposit():
    amount = float(input(f"Enter your amount to be deposited "))
     
    if amount < 0:
        print("Invalid Amount")
        return 0
    else:
        print(f"Amount ${amount} deposited")
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount you want to withdraw "))

    if amount > balance:
        print("Insufficient Amount")
        return 0
    elif amount < 0:
        print("Amount must be Greater than 0")
        return 0
    else:
        print(f"You Withdraw ${amount}")
        return amount       

def main():
    balance = 0
    is_running = True

    while is_running:
        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = input("Choose your choice (1-4) ")

        if choice == '1':
            show_amount(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == "3":
           balance -= withdraw(balance)

        elif choice == "4":
            is_running = False

        else:   
            print("Invalid Choice")   

    print("Thanks! Have a nice day")

if __name__ == "__main__":
    main()