"""
break= used to terminate the loop entirely
continue= skips to the next iteration of the loop
pass= does nothing, acts as a placeholder
"""

def main():
    n = get_int()
    print(n)

    x = get_integer("Provide an integer please: ")
    print(x)

# SyntaxError
def syntax_error():
    try:
        #print("Hello World)
        print("Syntax error")
    except SyntaxError:
        print("Syntax Error")

# Runtime error
def runtime_error():
    # pass a str to cause an error
    # ValueError: invalid literal for int() with base 10: 'cat'
    n = int(input("What's n? "))
    print("n is {0}".format(n))

# Try, Except, ValueError
def try_except():
    try:
        n = int(input("What's n? "))
        print("n is {0}".format(n))
    except ValueError:
        print("n is not an integer")

def name_error():
    # pass a str to raise the exception NameError
    try:
        n = int(input("What's n? "))
    except Exception as e:
        print(e)

    print("n is {0}".format(n))

def try_else():
    try:
        n = int(input("What's n? "))
    except Exception as e:
        print(e)
    else:
        print("n is {0}".format(n))

def print_input_using_while_loop():
    while True:
        try:
            n = int(input("What's n (int)? "))
        except Exception as e:
            print(e)
        else:
            break

    print("n is {0}".format(n))

def get_int():
    while True:
        try:
            return int(input("What's n (int)? "))
        except ValueError:
            print("n is not an integer")

def get_int_gently():
    while True:
        try:
            return int(input("What's n (int)? "))
        except ValueError:
            pass

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

if __name__ == "__main__":
    main()