import from_keyword as r

# libraries == modules => True
"""
With the Python interpreter
You have some modules
ex. random
"""

def main():
    count_random_numbers(1000000000)

def random_choice(list_=None):
    if list_ is None:
        list_ = [1, 2, 3, 4, 5, 6]
    return r.choice(list_)

def random_int_within_a_range(min_value = 0, max_value = 100):
    return r.randint(min_value, max_value)

def print_dict(dict_):
    for key, value in dict_.items():
        print("{}: {}".format(key, value))

def count_random_numbers(limit):
    counters = {"zero":0, "one":0, "two":0, "three":0, "four":0}

    i = 0

    while i < limit:
        i += 1
        # print(i)
        random_number = r.randint(0, 9)

        match random_number:
            case 0:
                counters["zero"] += 1
            case 1:
                counters["one"] += 1
            case 2:
                counters["two"] += 1
            case 3:
                counters["three"] += 1
            case 4:
                counters["four"] += 1

    return  print_dict(counters)

if __name__ == "__main__":
    main()
