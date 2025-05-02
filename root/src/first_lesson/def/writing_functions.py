import sys

def main():

    print_tree()

    separate_line(15)
    name = input("What is your name? ")
    hello(name)

    separate_line(15)
    hello()

    separate_line(15)

    is_main_running = input("Do you want to stop the main function? (y/n): ")

    if is_main_running == "y":
        print("Exiting main program..")
        sys.exit()
def hello(to="world"):
    print(f"Hello, {to}!")
def separate_line(n):
    print("\n" + "*" * int(n) + "\n")
def print_tree(floors="3", trunk="5"):

    is_print_tree_on = True
    # print a tree
    while is_print_tree_on:

        # checking values (defensive programming)
        try:
            tree_array = input(
                "How many floors and what is the trunk height of your tree? \nplease write your numbers separated by a comma: ").replace(
                " ", "").split(",")
            # len_check = True if len(tree_array) == 2 else False
            # type_check = True if (type(int(tree_array[0])) == int and type(int(tree_array[1])) == int) else False

            len_check = len(tree_array) == 2
            type_check = all(isinstance(int(num), int) for num in tree_array)

            if len_check and type_check:

                floors = int(tree_array[0])
                trunk = int(tree_array[1])

                space = " " * floors
                base = space + "*"
                asterisk = "*"
                trunk_space = (floors - 1) * " "

                for i in range(floors):
                    # floors -= 1
                    space = " " * (floors - i - 1)
                    asterisk += "*" * 2
                    base += ("\n" + space + asterisk)

                print(base)

                for i in range(trunk):
                    print(trunk_space + "**")

                is_print_tree_on = False
            else:
                print("Please enter two numbers separated by a comma")

        except Exception as e:
            print("An exception occurred:", e)


if __name__ == '__main__':
    while True:
        main()
