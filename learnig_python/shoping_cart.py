foods=[]
prices=[]
total=0

while True:
    food = input(f"Enter a food to buy (press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = input(f"enter price of {food}: ")
        foods.append(food)
        prices.append(price)

print("-------Your Cart--------")

for food in foods:
    print(food)


for price in prices:
    total += int(price)
print()

print(f"you total amount is {total}")