from math import floor


def hello(to="world"):
    print(f"Hello, {to}!")

def print_tree(floors="3", trunk="5"):

    floors = int(floors)
    trunk = int(trunk)

    space = " " * floors
    base = space + "*"
    asterisk = "*"
    trunk_space = (floors - 1) * " "

    for i in range(floors):
        #floors -= 1
        space = " " * (floors - i - 1)
        asterisk += "*" * 2
        base += ("\n" + space + asterisk)

    print(base)

    for i in range(trunk):
        print(trunk_space + "**")


#playing with def functions
name = input("What is your name? ")
hello(name)
hello()

print("\n" + "*" * 10 + "\n")

#print a tree
while True:
    try:
        tree_array = input(
            "How many floors and what is the trunk height of your tree? \nplease write your numbers separated by a comma: ").replace(
            " ", "").split(",")
        # len_check = True if len(tree_array) == 2 else False
        # type_check = True if (type(int(tree_array[0])) == int and type(int(tree_array[1])) == int) else False

        len_check = len(tree_array) == 2
        type_check = all(isinstance(int(num), int) for num in tree_array)

        if len_check and type_check:
            print_tree(tree_array[0], tree_array[1])
            break
        else:
            print("Please enter two numbers separated by a comma")

    except Exception as e:
        print("An exception occurred:", e)


