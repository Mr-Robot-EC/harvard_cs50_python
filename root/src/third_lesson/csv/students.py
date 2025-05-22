#csv
import csv

def main():
    #writing_csv()
    #reading_csv()
    reading_csv_with_split()

def writing_csv():
    data = [
        ["Harry", "Gryffindor"],
        ["Draco", "Slytherin"],
        ["Andrea", "Raven Claw"],
        ["Hermione", "Gryffindor"]
    ]

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV created successfully.")

def reading_csv():
    with open("students.csv", "r") as file:
        for line in file:
            print(line.replace(",", ": ").rstrip())

def reading_csv_with_split():
    with open("students.csv", "r") as file:
        for line in file:
            row = line.rstrip().split(",")
            print(f"{row[0]}: {row[1]}")

def read_csv_split_readable():
    with open("students.csv", "r") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name}: {house}")

if __name__ == "__main__":
    main()