# docs.python.org/3/library/csv.html
import csv

def main():
    #wizards = read_csv("wizards.csv")
    wizards = read_dict_csv("wizards.csv")
    sort_print_wizards(wizards, "name")


def read_csv(file_name):
    wizards = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            wizards.append({"name": row[0], "house": row[1], "age": row[2]})

    return wizards

def read_dict_csv(file_name):
    wizards = []

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            wizards.append({"name": row["name"], "house": row["house"], "age": row["age"]})

    return wizards


def sort_print_wizards(list_, order_by):
    sorted_wizards = sorted(list_, key=lambda wizard: wizard[order_by])

    for wizard in sorted_wizards:
        print(f"{wizard['name']} is {wizard['age']} old. The house is {wizard['house']}.")


if __name__ == "__main__":
    main()