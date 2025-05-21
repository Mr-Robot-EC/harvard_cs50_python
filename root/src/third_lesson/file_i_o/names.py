def main():
    #append_names(4)
    #print_names()
    #print_indexes()
    print_reversed_names()

def print_names():
    names = []

    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello {name}")

#open
"""
read/write a file
docs.python.org/3/library/functions.html#open
"""

def append_names(n=10):
    # "a" => append
    for _ in range(n):
        with open("names.txt", "a") as file:
            file.write(input("Enter name: ") + "\n")
            #file.close()
            #we don't need to close the file using the keyword 'with'


def print_indexes():
    with open("names.txt") as file:
        for index, line in enumerate(file):
            print(index, "Hello", line.rstrip(), sep=" ")

def print_reversed_names():
    file = open("names.txt", "r")
    # readlines() add an extra \n at the end of every line, that's why after we use strip() to remove it
    names = file.readlines()
    file.close()

    for name in sorted(names, reverse=True):
        print(f"Hello {name.strip()}")


if __name__ == "__main__":
    main()
