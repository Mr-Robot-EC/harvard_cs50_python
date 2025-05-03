# arithmetic operators
"""
    + addition
    - subtraction
    * multiplication
    / division
    % modulo/reminder
"""

def main():

    line_separator()
    num = int(input("Enter a number: "))
    odd_or_even_tree(num)

    line_separator()
    val = int(input("Enter a number: "))
    if is_even(val):
        print("{0} is even".format(val))
    else:
        print("{0} is odd".format(val))

def odd_or_even_tree(n=0):
    for i in range(n):
        if i % 2 == 0:
            print(f"{i} even")
        else:
            print(f"{i} odd")

def line_separator():
    print("-" * 15)

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()