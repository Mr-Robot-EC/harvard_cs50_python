# dict
"""
dictionary {key:value}
    words as indexes in this case
"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("_" * 15)

# by design in this case you will see te keys
for student in students:
    print(student)

print("_" * 15)

for student in students:
    print(student, students[student], sep=", ")

print("_" * 15)

for key, value in students.items():
    print(key, value, sep=", ")

print("_" * 15)