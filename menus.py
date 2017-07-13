import character

listofactions = ["close", "inventory", "stats"]


def menuactions(action):
    if action in listofactions:
        if action == "close":
            character.Playercharacter.state = ""
        elif action == "inventory":
            print("Inventory")
        elif action == "stats":
            print("stats")
    else:
        print("Please try again")