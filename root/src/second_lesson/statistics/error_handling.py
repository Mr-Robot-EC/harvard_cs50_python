import sys

if len(sys.argv) != 3:
    print("Example of defensive programming. I need 2 args.")
    sys.exit()

print("Hello, my name is", sys.argv[1], sys.argv[2])

print("*" * 20)

for i in range(len(sys.argv)):
    print(f"sys.argv[{i}] ->", sys.argv[i])

# slices
"""
In Python, a slice is a way to extract 
a portion of a sequence 
(such as a list, tuple, or string) 
using the start:stop:step syntax.
"""

list_ = []

for _ in range(100):
    list_.append(_)

print("10:20 ->",list_[10:20])
print("0:10 ->",list_[0:10])
print("90: ->", list_[90:])
print(":5 ->", list_[:5]) # from the beginning
print("::10 ->", list_[::10]) # every ten element
print("-1 ->", list_[-1]) # last value
print("-5: ->", list_[-5:]) # last 5 values
print("-10::2 ->", list_[-10::2]) # last 10 values, skipping every second element

print("\nfor cycle")
for arg in sys.argv[1:]:
    print(arg)

print("\nfor cycle")
for arg in sys.argv[1:-1]:
    print(arg)