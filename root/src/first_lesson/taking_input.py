name = input("What's your name? ")
print(f"Hello {name}")

age = int(input("How old are you? "))
print(f"You are {age} years old")

if age < 18:
    print("You are too young to vote!")
elif 18 <= age <= 30:
    print("You're young, but you can vote!")
else:
    print("You can vote Sir!")