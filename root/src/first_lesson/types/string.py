# user name
name = input("What is your name? ")
# remove whitespace from str
name = name.strip()
# capitalize user's name
name = name.capitalize()

# combined functions
surname = input("What is your surname? ").strip().title()
print(f"Hello, {name} {surname}")

line = "*"

for i in range(10):
    line += "*"

print("\n" + line, end="\n\n")

# split

full_name = input("What is your full name? ")

first, last = full_name.split()

print(f"Hello, {first}, or do you prefer I call you {last}?")