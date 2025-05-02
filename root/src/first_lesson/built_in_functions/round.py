import random as r

x = float(input("What's x: "))
y = float(input("What's y: "))

print(f"rounded x: {round(x)}")
print(f"rounded y: {round(y)}")

random_number = r.randint(1, 2)

if random_number == 1:
    z = round(x + y)
    print(f"{z:,} = round(x + y)")

elif random_number == 2:
    z = round(x) + round(y)
    print(f"{z:,} = round(x) + round(y)")



x = 2
y = 3
z = x / y
# 2 digits after the comma with the round function
print(round(x / y, 2))
# 2 digits after the comma with format strings
print(f"{z:.2f}")
