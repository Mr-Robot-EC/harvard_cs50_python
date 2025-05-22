import random as r
import csv

def main():
    #writing_csv(3)
    #print_wizards()
    #print_wizards_dict()
    print_sort_wizards()

def writing_csv(n):
    data = []
    house_names = ["Gryffindor", "Raven Claw", "Hufflepuff", "Slytherin"]

    for _ in range(n):
        name = input("Enter a name: ")
        house = input("1 > Gryffindor;\n2 > Raven Claw;\n3 > Hufflepuff;\n4 > Slytherin\n")
        match house:
            case "1":
                house = "Gryffindor"
            case "2":
                house = "Raven Claw"
            case "3":
                house = "Hufflepuff"
            case "4":
                house = "Slytherin"
            case _:
                house = r.choice(house_names)

        data.append([name, house])

    with open("wizards.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV created successfully.")


def print_wizards():

    wizards = []

    with open("wizards.csv", "r") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            wizards.append(f"{name}: {house}")

    for wizard in sorted(wizards):
        print(wizard)


def print_wizards_dict():

    wizards_dict = {}

    with open("wizards.csv", "r") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            wizards_dict[name] = house

        for name, house in sorted(wizards_dict.items()):
            print(f"{name}: {house}")


def get_wizard_name(wizard):
    return wizard["name"]


def print_sort_wizards():
    wizards = []

    with open("wizards.csv", "r") as file:
        for _ in file:
            name, house = _.strip().split(",")
            wizard = {"name": name, "house": house}
            wizards.append(wizard)

        # Python feature
        """
        Python allows you to pass [function] as [arguments] into others [functions]
        
        get_wizard_name -> function
        sorted -> function
        
        We are passing [get_wizard_name] 
        to [sorted] 
        as [value] 
        of the [key parameter]
        """
        for wizard in sorted(wizards, key=get_wizard_name):
            print(f"{wizard['name']} -> {wizard['house']}")


if __name__ == "__main__":
    main()