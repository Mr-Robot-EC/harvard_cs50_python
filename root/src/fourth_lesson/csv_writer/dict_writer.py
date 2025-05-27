import csv

def main():
    print("Starting program...")
    dict_writer()

def dict_writer():

    name = input("Declare your name: ")
    home = input("Declare your home: ")

    with open("students.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})

if __name__ == '__main__':
    main()

