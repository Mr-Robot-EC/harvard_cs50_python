# from keyword
"""
import specific functions from a module
"""
from random import choice, randint, shuffle

def main():
    cards = shuffle_card()
    sep_line("#", 15)
    print_list(cards)
    sep_line("@", 15)

def sep_line(symbol = "_", length= 10):
    print("\n", symbol * length)

def coin_toss_choice(first_choice= "heads", second_choice= "tails"):
    counters = {first_choice: 0, second_choice: 0}
    for _ in range(100):
        coin = choice([first_choice, second_choice])
        if coin == first_choice:
            counters[first_choice] += 1
        else:
            counters[second_choice] += 1

    for key, value in counters.items():
        print(f"{key} : {value}")

def coin_toss_randint():
    counters = {"heads": 0, "tails": 0}
    for _ in range(100):
        coin = randint(0, 1)
        if coin == 0:
            counters["heads"] += 1
        else:
            counters["tails"] += 1

    for key, value in counters.items():
        print(f"{key} : {value}")

def shuffle_card(deck=None):
    if deck is None:
        deck = ["ace", "jack", "queen", "king"]
        shuffle(deck)
    return deck

def print_list(list_):
    for item in list_:
        if item != list_[-1]:
            print(item + ", ", end=" ",)
        else:
            print(item, end="")


if __name__ == "__main__":
    main()