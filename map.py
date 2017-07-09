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


def moveplayer(position):
    if position == "up":
        return
    elif position == "down":
        return
    elif position == "left":
        return
    elif position == "right":
        return
    else:
        print("Try again")


def checkmovement():
    return


def displaymap(mapname):
    for y in mapname:
        print(y)
