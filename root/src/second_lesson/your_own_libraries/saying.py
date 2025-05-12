def main():
    hello("Andrea")
    goodbye("Andrea")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

def print_line(length, symbol):
    if type(length) == int and type(symbol) == str:
        print(symbol * length)
    else:
        print("_" * 10)

if __name__ == "__main__":
    main()