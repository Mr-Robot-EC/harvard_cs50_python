def main():
    #read_lines()
    #line_rstrip()
    #sort_names()
    sort_names_pythonic()

def read_lines():
    with open("names.txt", "r") as file:
        #read the lines and return them as a list
        lines = file.readlines()

    for line in lines:
        print("Hello ", line)

def line_rstrip():
    with open("names.txt", "r") as file:
        for line in file:
            print("Hello ", line.rstrip())

def sort_names():
    with open("names.txt", "r") as file:
        names = file.readlines()

        for name in sorted(names):
            print("Hello ", name.rstrip())

def sort_names_pythonic():
    with open("names.txt", "r") as file:
        for line in sorted(file):
            print("Hello ", line.rstrip())


# sorted()
"""
sorted(iterable, /, *, key=None, reverse=False)
"""

if __name__ == '__main__':
    main()