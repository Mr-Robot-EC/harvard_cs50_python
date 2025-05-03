# comparison/relational operators
"""
>
>=
<=
==
!=
"""

# conditional statement
"""
if
"""

# logical operators
"""
or ||
and &&
"""


x = int(input("x value: "))
y = int(input("y value: "))

# more efficient (check the flowchart)

if x > y:
    print(f"{x} is greater then {y}")
elif x < y:
    print(f"{x} is less then {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print("I cannot understand your request.")

# or (logical operator)

r = int(input("r value: "))
s = int(input("s value: "))

#if r > s or r < s:
if r != s:
    print("{0} is not equal to {1}".format(r, s))
else:
    print("{0} is equal to {1}".format(r, s))

