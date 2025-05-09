# PyPI

# packages
"""
third-party libraries == libraries => True

pypy.org -> cmd line, web

pypy.org/project/cowsay
pip -> install packages
"""

#pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    #ASCII art
    cowsay.cow("hello, " + sys.argv[1])
elif len(sys.argv) == 3:
    cowsay.trex("hello, " + sys.argv[1] + sys.argv[2])
else:
    print("pass")

