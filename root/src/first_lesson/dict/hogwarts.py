# list of dictionaries
students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronous": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronous": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronous": "Jack Russell Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronous": None
    }
]

for student in students:
    print("name: ", student['name'], ", house: ", student['house'], ", patronous: ", student['patronous'], sep="", end="\n" + "*" * 65 + "\n")