import sys

from saying import hello, goodbye, print_line

# python personal_library.py Andrea
if len(sys.argv) == 2:
    hello(sys.argv[1])
    print_line(20, "#")
    goodbye(sys.argv[1])
