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
print("Hello " + name + " and welcome to this game!")

# 2) choose level
while True:
    level = int(input("What is your level of difficulty? \n1 = easy\n2 = medium\n3 = hard\n"))
    if level == 1:
        player_life = 12
        print(f"You have {player_life} lives, let's begin the game.")
        break
    elif level == 2:
        player_life = 8
        print(f"You have {player_life} lives, let's begin the game.")
        break
    elif level == 3:
        player_life = 5
        print(f"You have {player_life} lives, let's begin the game.")
        break
    else:
        print("Sorry, you can only choose 1, 2 or 3")
        continue

# 3) guess the number
random_number = r.randint(0, 100)

while player_life > 0:
    guess = int(input("Guess a number between 0 and 100: "))

    if guess == random_number:
        print("You won the game")
        break
    elif guess < random_number:
        print("Your guess is too low")
        player_life -= 1
        continue
    elif guess > random_number:
        print("Your guess is too high")
        player_life -= 1
        continue
    elif player_life == 0:
        print("You lose! Fatality")


# Next Ideas
# Verified inputs
# Create a cheating bot
# Crate a program that help simplify Python Documentation
# Create a portfolio website with links (LinkedIn, GitHub, jobs experiences) and update your Flow CV
# Interact with various DBs