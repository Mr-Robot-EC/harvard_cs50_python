def main():
    num = int(input("Enter a number: "))
    print("Number squared is", square(num))

def square(num):
    return num * num

if __name__ == "__main__":
    main()