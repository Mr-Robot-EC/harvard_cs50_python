# https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# ask user for their name
name = input("What is your name? ")

# say hello to the use and overriding print
print("Hello, ", end="")
print(name)

surname = input("What is your surname? ")

print(f"Hello, {surname}")