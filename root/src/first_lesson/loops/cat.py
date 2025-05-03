#loops

def main():
    print("Starting the program...")
    #do_meow()
    #sep_line()
    #do_meow_for(5)
    #sep_line()
    #do_meow_while(5)
    #sep_line()
    #do_bau_for_pythonic(4)
    #do_bau_for_improved(4)
    choose_num()

def do_meow():
    print("meow")
    print("meow")
    print("meow")

def do_meow_for(n):
    for i in range(n):
        print("{0} meow".format(i))

def do_meow_while(n):
    counter = n
    while counter > 0:
        counter -= 1
        print("{0} meow".format(counter))

def do_bau_for():
    for i in [0, 1, 2]:
        print("bau")

def do_bau_for_improved(n):
    for i in range(n):
        print("{0} bau".format(i))

def do_bau_for_pythonic(n):
    for _ in range(n):
        print("bau")

def do_meow_python(n):
    print("meow\n" * n, end="")

def get_positive_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def choose_num():
    n = get_positive_num()

    for _ in range(n):
        print("Tiger said Grrr")

def sep_line():
    print("\n" + "_" * 10 + "\n")


if __name__ == "__main__":
    main()