import sys
"""
sys (system)
sys.argv -> argv : "argument-vector"

definition: In Python, sys.argv is a list that 
            stores command-line arguments passed to a script 
            when it is executed. 
            It is part of the sys module and allows you 
            to access arguments provided by the user.
"""

# example
"""
python .\command_line_arguments.py Andrea Edson
Hello, my name is  Andrea
"""

line = "_" * 20

# defensive programming with -> if
# we check != 3 and not 2 because the first argv is always the name of the script
if len(sys.argv) != 3:
    print("Example of defensive programming. I need 2 args.")
else:
    print("Example of defensive programming. Thank you for your cooperation.")

# defensive programming with try, except, else
try:
    print("Hello, my name is ", sys.argv[1])
    print("My surname is ", sys.argv[2])
    print(line)
    print("sys.argv[0] -> ", sys.argv[0])
    print(line)
    print("sys.argv[1] -> ", sys.argv[1])
    print(line)
    print("sys.argv[2] -> ", sys.argv[2])
except IndexError:
    print("IndexError -> provide two args.")
