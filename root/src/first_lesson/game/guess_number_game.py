import random as r

player_life = 0

print("""
WELCOME!
You can't survive this game. 
You will have to guess a random number between 0 and 100.
If you fail, shame on you!

1) choose your name
2) choose level of difficulty
3) try to guess the number
""")

# 1) name
name = input("What is your name? ")
print("Hello " + name + " and welcome to this game!\n")

# 2) choose level
while True:
    level = input("What is your level of difficulty? \n1 = easy\n2 = medium\n3 = hard\n")

    if level == "1":
        player_life = 12
        print(f"\nYou have {player_life} lives, let's begin the game.")
        break
    elif level == "2":
        player_life = 8
        print(f"\nYou have {player_life} lives, let's begin the game.")
        break
    elif level == "3":
        player_life = 5
        print(f"\nYou have {player_life} lives, let's begin the game.")
        break
    else:
        print("\nSorry, you can only choose 1, 2 or 3")
        continue

# 3) guess the number
random_number = r.randint(0, 100)

while player_life > 0:

    guess = input("Guess a number between 0 and 100: ")

    try:
        guess = int(guess)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Try again\n")
        continue

    # print(f"{type(guess)} debug")

    if guess > 100 or guess < 0:
            print("Sorry, your guess is out of range\n")
            continue

    if guess == random_number:
        print("\nYou won the game")
        break
    elif guess < random_number:
        print("\nYour guess is too low")
        player_life -= 1
        print(f"You have {player_life} lives left.\n")
        if player_life == 0:
            print("Sorry, you lose")

    elif guess > random_number:
        print("\nYour guess is too high")
        player_life -= 1
        print(f"You have {player_life} lives left.\n")
        if player_life == 0:
            print("\nSorry, you lose")

    else:
        print("\nI cannot understand your guess.")



# Next Ideas
# Verified inputs
# Create a GUI in Python related to the game
# Connect this little program to a DB
# Create a cheating bot
# Crate a program that help simplify Python Documentation
# Create a portfolio website with links (LinkedIn, GitHub, jobs experiences) and update your Flow CV
# Interact with various DBs
# DataScience project