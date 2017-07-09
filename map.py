import character


class Basemap:
    name = ""
    width = 0
    height = 0
    type = ""
    monsters = []


class Starting(Basemap):
    name = "Starting Area"
    width = 4
    height = 4
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

def spawnmonster():
    return
