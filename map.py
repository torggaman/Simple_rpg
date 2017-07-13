class Playerposition:
    mapxposition = 0
    mapyposition = 0
    mapname = ""
    roomname = ""

    def moveplayerup(self):
        if not self.mapyposition == 0:
            self.mapyposition = self.mapyposition - 1
        else:
            print("Cannot move that way")

    def moveplayerleft(self):
        if not self.mapxposition == 0:
            self.mapxposition = self.mapxposition - 1
        else:
            print("Cannot move that way")

    def moveplayerright(self):
        if not self.mapxposition == (len(showmap[self.mapxposition]) - 1):
            self.mapxposition = self.mapxposition + 1
        else:
            print("Cannot move that way")

    def moveplayerdown(self):
        if not self.mapyposition == (len(showmap) - 1):
            self.mapyposition = self.mapyposition + 1
        else:
            print("Cannot move that way")

    def checksurroundings(self):
        surrounding = {}


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


position = Playerposition()
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
    displaymap()


def displaymap():
    for y in showmap:
        print(y)


def removeplayer():
    xposition = position.mapxposition
    yposition = position.mapyposition
    showmap[yposition][xposition] = ""


def addplayer():
    xposition = position.mapxposition
    yposition = position.mapyposition
    showmap[yposition][xposition] = "P"


def spawnmonster():
    return
