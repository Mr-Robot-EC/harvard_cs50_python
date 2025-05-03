# match keyword

grf = "Gryffindor"
hf = "Hufflepuff"
rc = "Ravenclaw"
sly = "Slytherin"

house_names = [grf, hf, rc, sly]

screening_questions = {"kind_smart":
                           "Is it better to be kind or smart? ",
                       "wise_brave":
                           "Is it better to be wise or brave? ",
                       "generous_ambitious":
                           "Is it better to be generous or ambitious? ",
                       "knowledge_power":
                           "What is better? Knowledge or power? "
                       }

combinations = {
            "Gryffindor": {
                "1100",  # Brave, Brave, Generous, Knowledge
                "1101",  # Brave, Brave, Generous, Power
                "1110",  # Brave, Brave, Ambitious, Knowledge
                "0100",  # Kind, Brave, Generous, Knowledge
                "0101",  # Kind, Brave, Generous, Power
                "0110"  # Kind, Brave, Ambitious, Knowledge
            },
            "Hufflepuff": {
                "0000",  # Kind, Wise, Generous, Knowledge
                "0001",  # Kind, Wise, Generous, Power
                "0010"  # Kind, Wise, Ambitious, Knowledge
            },
            "Ravenclaw": {
                "1000",  # Smart, Wise, Generous, Knowledge
                "1001",  # Smart, Wise, Generous, Power
                "1010",  # Smart, Wise, Ambitious, Knowledge
                "1011"  # Smart, Wise, Ambitious, Power
            },
            "Slytherin": {
                "1111",  # Brave, Brave, Ambitious, Power
                "0111",  # Kind, Brave, Ambitious, Power
                "0011"  # Kind, Wise, Ambitious, Power
            }
        }

hogwarts_houses = {
    grf: {
        "Founder": "Godric Gryffindor",
        "Values": ["Courage", "Determination", "Nobility"],
        "Symbol": "Lion",
        "Colors": ["Red", "Gold"],
        "Description":
            """
            Founded by Godric Gryffindor, this house values courage, 
            determination, and nobility. 
            Its symbol is a lion, representing bravery and strength, 
            and its colors are red and gold. 
            Gryffindors are known for their daring spirit 
            and willingness to stand up for what's right, 
            even in the face of danger.
            """

    },
    hf: {
        "Founder": "Helga Hufflepuff",
        "Values": ["Loyalty", "Kindness", "Hard Work"],
        "Symbol": "Badger",
        "Colors": ["Yellow", "Black"],
        "Description":
            """
            Created by Helga Hufflepuff, this house rewards loyalty, 
            kindness, and hard work. 
            Its emblem is a badger, symbolizing persistence and 
            dedication, and its colors are yellow and black. 
            Hufflepuffs are known for their fairness, strong sense 
            of community, and ability to see the good in others.
            """
    },
    rc: {
        "Founder": "Rowena Ravenclaw",
        "Values": ["Intelligence", "Creativity", "Wisdom"],
        "Symbol": "Eagle",
        "Colors": ["Blue", "Bronze"],
        "Description":
            """
            Founded by Rowena Ravenclaw, this house is home to those who 
            excel in intelligence, creativity, and wisdom. 
            Its symbol is an eagle, representing soaring intellect, and 
            its colors are blue and bronze. 
            Ravenclaws are celebrated for their wit, curiosity, and 
            pursuit of knowledge.
            """
    },
    sly: {
        "Founder": "Salazar Slytherin",
        "Values": ["Ambition", "Cunning", "Determination"],
        "Symbol": "Snake",
        "Colors": ["Green", "Silver"],
        "Description":
            """
            Established by Salazar Slytherin, this house values ambition, 
            cunning, and determination. 
            Its emblem is a serpent, symbolizing cleverness and 
            adaptability, and its colors are green and silver. 
            Slytherins are known for their resourcefulness, strategic 
            thinking, and strong leadership qualities.
            """
    }
}


name = input("What is your name? ")

if name == "Harry":
    print("""
    - Where do I put you? In what house?
    - Not Slytherin .. not slytherin..
    - Are you sure? They are powerful, and great!
    - Not Slytherin .. not slytherin.. please
    - All right then..\n
    """)

match name:
    case "Hermione" | "Ron" | "Neville":
        print(grf, "!")
        print(hogwarts_houses[grf]["Description"])
    case "Draco":
        print(sly, "!")
        print(hogwarts_houses[sly]["Description"])
    case "Jinn":
        print(hf, "!")
        print(hogwarts_houses[hf]["Description"])
    case "Andrea":
        print(rc, "!")
        print(hogwarts_houses[rc]["Description"])
    case _:
        is_hat_thinking = True

        while is_hat_thinking:
            print("Please answer the following questions: type 0 or 1 to choose your option\n"
                  "For example in the first question 0 => kind and 1 => smart\n")
            first_param = input(screening_questions["kind_smart"]).replace(" ", "")
            second_param = input(screening_questions["wise_brave"])
            third_param = input(screening_questions["generous_ambitious"])
            fourth_param = input(screening_questions["knowledge_power"])
            counter = 0

            combined_params = f"{first_param}{second_param}{third_param}{fourth_param}"

            for key, value in combinations.items():
                for el in value:

                    counter += 1
                    print("______ debug")
                    print(type(el))
                    print(type(combined_params))
                    print("______ debug")
                    if el == combined_params:
                        print(key, "!")
                        print(hogwarts_houses[key]["Description"])
                        is_hat_thinking = False
                        break
                    elif counter == 20:
                        print("Enough! It seems clear to me!!\n"
                              "After asking twenty times, you think you can have fun of the hat!\n"
                              "I know where to put you.")
                        print(sly, "!")
                        print(hogwarts_houses[sly]["Description"])
                        is_hat_thinking = False
                        break


