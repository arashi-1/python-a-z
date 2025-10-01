menu={"burger":49,
      "pizza":79,
      "cold-drink":40,
      "cold-coffee":89,
      "chai":15
      }
cart=[];
total=0;

print("--------------- Menu ---------------")
for key, value in menu.items():
    print(f"{key:15} : ₹{value}")
print("------------------------------------")

while True:
    food = input("Choose the food from Menu (press q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+=menu.get(food)
    item = 1
    print(f"{item}: {food}", end=" ")
    item += 1

print()    
print(f"Your total amount is ₹{total}")