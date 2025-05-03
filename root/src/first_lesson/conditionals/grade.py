# and (logical operator)

grade = int(input("Enter grade: "))

# if grade >= 90 and grade <= 100:
if 90 <= grade <= 100:
    print("Grade is A")
elif grade >= 80:
    print("Grade is B")
elif grade >= 70:
    print("Grade is C")
elif grade >= 60:
    print("Grade is D")
else:
    print("Grade is F")
