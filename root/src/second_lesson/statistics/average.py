import statistics

def main():
    grades = add_grades(10)
    average = statistics.mean(grades)
    avg = calculate_avg_(grades)
    print("Average grade:", average)
    print("Average grade:", avg)

def add_grades(iterations):
    grades = []

    while len(grades) < iterations:
        grade = int(input("Enter grade: "))
        grades.append(grade)

    return grades

def calculate_average(numbers):
    return statistics.mean(numbers)

def calculate_avg_(numbers):
    sum_ = 0
    for number in numbers:
        sum_ += number

    return sum_ / len(numbers)

if __name__ == "__main__":
    main()