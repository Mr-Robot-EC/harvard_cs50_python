message = """
Welcome to the Math Calculator!

1) choose your two numbers
2) choose your operation
3) see the result
"""

# welcome message
print(message)
is_on = True
is_script_running = True

#login (functions)
def choose_number(is_active):
    while is_active:

        asterisk = "*"

        for i in range(15):
            asterisk += "*"

        print(asterisk)

        number_one = input("Enter number one: ")
        number_two = input("Enter number two: ")

        try:
            if type(float(number_one)) == type(float(number_two)):
                break
            else:
                print("Incorrect input. Try again.")

        except Exception as e:
            print(f"The following exception happened: {e}")


    return number_one, number_two


def choose_operation(number_one_param, number_two_param, is_active):
    while is_active:
        operation = input(
            "\nChoose your operation: \nType =>\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division\n 5 for reminder\n 6 for converting them in integers \n===> ")
        if operation == "1":
            result = float(number_one_param) + float(number_two_param)
            print(f"{number_one_param} + {number_two_param} = {result}")
            break

        elif operation == "2":
            result = float(number_one_param) - float(number_two_param)
            print(f"{number_one_param} - {number_two_param} = {result}")
            break
        elif operation == "3":
            result = float(number_one_param) * float(number_two_param)
            print(f"{number_one_param} * {number_two_param} = {result}")
            break
        elif operation == "4":
            result = float(number_one_param) / float(number_two_param)
            print(f"{number_one_param} / {number_two_param} = {result}")
            break
        elif operation == "5":
            result = float(number_one_param) % float(number_two_param)
            print(f"{number_one_param} % {number_two_param} = {result}")

            if result == 0:
                print("Even.")
            else:
                print("Odd.")

            break

        elif operation == "6":
            print(f" n-one: {int(number_one_param)}\n n-two: {int(number_two_param)}\n")

        else:
            print("Incorrect input. Try again.")


# script
while is_script_running:
    n1, n2 = choose_number(is_on)
    choose_operation(n1, n2, is_on)

    answer = input("\nDo you want to continue? (y/n): ")

    if answer == "y":
        continue
    elif answer == "n":
        print("Bye bye")
        is_on = False
        is_script_running = False
    else:
        print("Incorrect input. Try again.")