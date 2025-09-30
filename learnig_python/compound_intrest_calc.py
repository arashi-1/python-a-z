p=0
t=0
r=0

while p <=0:
    p = float(input("Enter the principle amount: "))

    if p<=0:
        print("Principle can't be 0 or negative.")

while t<=0:
    t = int(input("Enter the time in years:"))

    if t<=0:
        print("Time can't be 0 or negative.")

while r<=0:
    r = float(input("Enter the Rate of the interest:"))

    if r<=0:
        print("Rate can't be 0 or negative")

ci = p*pow((1+r/100),t)

print(f"The balance amount after {t} years is {round(ci,2)}")