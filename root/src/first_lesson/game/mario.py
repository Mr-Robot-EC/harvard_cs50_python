# column, row, square
def main():
    print("Welcome to Mario!")
    print("Drawing a square")
    draw_square(5, "+")
    sep_line(5, "*")

    print("Drawing a line")
    draw_row(5)
    sep_line(5, "_")

    print("Drawing a column")
    draw_column(1, 2)
    sep_line(5, "o")

    print("Bubble sort")
    ordered_list = bubble_sort([4, 2, 6, 8, 10, 99, 0, -2, 5, -2, -7, 10, 67, -2, -10, 2])
    print_list_with_separator(ordered_list, "$", 1)
    sep_line(10, "/\\/")

def draw_column(height, width):
    for _ in range(height):
        draw_row(width)

def print_list_with_separator(list_, separator=",", remove_chars_from_end_string=2):
    printed_list = ""
    separator += " "
    for _ in list_:
        printed_list += str(_) + separator

    print(printed_list[:-remove_chars_from_end_string])

def draw_row(width):
    print("#" * width)

def draw_square(size, symbol="#"):
    print((symbol * size + "\n") * size, end="")

def make_square(size):
    for _ in range(size):
        draw_row(size)

def sep_line(n, symbol):
    print(symbol * n)

def bubble_sort(unsorted_list):

    ordered_list = unsorted_list[:]

    for i in range(len(ordered_list)):
        for j in range(len(ordered_list)):
            if ordered_list[i] > ordered_list[j]:
                temp = ordered_list[j]
                ordered_list[j] = ordered_list[i]
                ordered_list[i] = temp

    return ordered_list

if __name__ == "__main__":
    main()