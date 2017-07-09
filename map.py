import character

class Basemap:
    name = ""
    width = 0
    height = 0
    type = ""
    monsters = []


class Starting(Basemap):
    name = "Starting Area"
    width = 10
    height = 10
    type = "beginner"
    monsters = []

maplist = {"Starting": Starting}
showmap = []


def createmap(yposition, xposition, mapname):
    ysize = maplist[mapname].height
    xsize = maplist[mapname].width
    for y in range(ysize):
        showmap.append([])
        for x in range(xsize):
            showmap[y].append([])
            showmap[y][x] = ""
    showmap[yposition][xposition] += "P"
    displaymap(showmap)


def moveplayer():
    movement = True
    while movement:
        action = input("What direction?> ")
        showmap[character.Playercharacter.mapyposition][character.Playercharacter.mapxposition] = ''
        checking = checkmovement(action, character.Playercharacter.mapyposition,character.Playercharacter.mapxposition)
        if action == "up":
            if checking:
                character.Playercharacter.mapyposition -= 1
            else:
                print("Cannot move that way")
        elif action == "down":
            if checking:
                character.Playercharacter.mapyposition += 1
            else:
                print("Cannot move that way")
        elif action == "left":
            if checking:
                character.Playercharacter.mapxposition -= 1
            else:
                print("Cannot move that way")
        elif action == "right":
            if checking:
                character.Playercharacter.mapxposition += 1
            else:
                print("Cannot move that way")
        elif action == "actions":
            movement = False
            return
        elif not checking:
            print("Try again")
            print("You can type: Up, Down, Left, Right, or actions to leave movement")
        else:
            print("try again")
        showmap[character.Playercharacter.mapyposition][character.Playercharacter.mapxposition] = 'P'
        displaymap(showmap)


def checkmovement(movement, currentpositiony, currentpositionx):
    if currentpositiony == 0 and movement is "up":
        return False
    elif currentpositionx == 0 and movement is "left":
        return False
    elif currentpositiony == (len(showmap) - 1) and movement is "down":
        return False
    elif currentpositionx == (len(showmap[currentpositiony]) - 1) and movement is "right":
        return False
    else:
        return True


def displaymap(mapname):
    for y in mapname:
        print(y)
