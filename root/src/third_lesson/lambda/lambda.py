import csv
import random

def main():
    print('Welcome')
    add_wizards(4)
    print_wizards()

def add_wizards(n):

    wizards = []

    with open("wizards.csv", "w", newline="") as file:
        fieldnames = ["name", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for _ in range(n):
            name = input("Enter wizard name: ")
            house = house_names()

            writer.writerow({"name": name, "house": house})

    print("CSV file created and populated successfully")



def house_names():
    print("1) Gryffindor, 2) Hufflepuff, 3) Raven Claw, 4) Slytherin")

    houses = ["Gryffindor", "Raven Claw", "Hufflepuff", "Slytherin"]

    choice = input("Insert house number: ")

    match choice:
        case "1":
            return houses[0]
        case "2":
            return houses[2]
        case "3":
            return houses[1]
        case "4":
            return houses[3]
        case _:
            return random.choice(houses)


def print_wizards():
    wizards = []

    # Read CSV file
    with open("wizards.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            wizards.append({"name": row[0], "house": row[1]})

    # Sorting with lambda expression
    sorted_wizards = sorted(wizards, key=lambda wizard: wizard["name"])

    # Print sorted wizards
    for wizard in sorted_wizards:
        print(f'{wizard["name"]} is in {wizard["house"]}')


if __name__ == '__main__':
    main()