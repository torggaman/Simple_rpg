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
        charmove = character.Playercharacter
        charmovex = charmove.mapxposition
        charmovey = charmove.mapyposition
        showmap[charmovey][charmovex] = ''
        if action == "up":
            if checkmovement(action, charmovey, charmovex):
                charmovey -= 1
            else:
                print("Cannot move that way")
        elif action == "down":
            if checkmovement(action, charmovey, charmovex):
                charmovey += 1
            else:
                print("Cannot move that way")
        elif action == "left":
            if checkmovement(action, charmovey, charmovex):
                charmovex -= 1
            else:
                print("Cannot move that way")
        elif action == "right":
            if checkmovement(action, charmovey, charmovex):
                charmovex += 1
            else:
                print("Cannot move that way")
        elif action == "actions":
            movement = False
        else:
            print("Try again")
            print("You can type: Up, Down, Left, Right, or actions to leave movement")
        showmap[charmovey][charmovex] = 'P'
        displaymap(character.Playercharacter.mapname)


def checkmovement(movement, currentpositiony, currentpositionx):
    if showmap[currentpositiony][currentpositionx] == '':
        if str(currentpositiony) is "0" and movement is "up":
            return False
        elif str(currentpositionx) is "0" and movement is "left":
            return False
        elif str(currentpositiony) is str((len(showmap) - 1)) and movement is "down":
            return False
        elif str(currentpositionx) is str((len(showmap[currentpositiony]) - 1)) and movement is "right":
            return False
        else:
            return True
    else:
        return False


def displaymap(mapname):
    for y in mapname:
        print(y)
