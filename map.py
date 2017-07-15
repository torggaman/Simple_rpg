class Playerposition:
    map_x_position = 0
    map_y_position = 0
    map_name = ""
    room_name = ""
    facing_direction = ""

    def moveplayerup(self):
        if not self.map_y_position == 0:
            self.map_y_position = self.map_y_position - 1
            self.facing_direction = "up"
        else:
            print("Cannot move that way")

    def moveplayerleft(self):
        if not self.map_x_position == 0:
            self.map_x_position = self.map_x_position - 1
            self.facing_direction = "left"
        else:
            print("Cannot move that way")

    def moveplayerright(self):
        if not self.map_x_position == (len(showmap[self.map_x_position]) - 1):
            self.map_x_position = self.map_x_position + 1
            self.facing_direction = "right"
        else:
            print("Cannot move that way")

    def moveplayerdown(self):
        if not self.map_y_position == (len(showmap) - 1):
            self.map_y_position = self.map_y_position + 1
            self.facing_direction = "down"
        else:
            print("Cannot move that way")

    def checksurroundings(self):
        if self.facing_direction == "up":
            return showmap[(self.map_y_position - 1)][self.map_x_position]
        elif self.facing_direction == "down":
            return showmap[(self.map_y_position + 1)][self.map_x_position]
        elif self.facing_direction == "left":
            return showmap[self.map_y_position][(self.map_x_position - 1)]
        elif self.facing_direction == "right":
            return showmap[self.map_y_position][(self.map_x_position + 1)]


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


def redraw_character():
    if position.facing_direction == "up":
        showmap[position.map_y_position][position.map_x_position] = "^"
    elif position.facing_direction == "down":
        showmap[position.map_y_position][position.map_x_position] = "v"
    elif position.facing_direction == "left":
        showmap[position.map_y_position][position.map_x_position] = "<"
    elif position.facing_direction == "right":
        showmap[position.map_y_position][position.map_x_position] = ">"
    else:
        showmap[position.map_y_position][position.map_x_position] = "P"
    displaymap()


def turn_direction(direction):
    if direction == "north" or direction == "up":
        if position.map_y_position == 0:
            print("Nothing that way")
        else:
            position.facing_direction = "up"
    elif direction == "south" or direction == "down":
        if position.map_y_position == len(showmap) - 1:
            print("Nothing that way")
        else:
            position.facing_direction = "down"
    elif direction == "west" or direction == "left":
        if position.map_x_position == 0:
            print("Nothing that way")
        else:
            position.facing_direction = "left"
    elif direction == "east" or direction == "right":
        if position.map_x_position == len(showmap[position.map_y_position]) - 1:
            print("Nothing that way")
        else:
            position.facing_direction = "right"
    else:
        print("Please try: up, down, left, right \n or north, south, east, west")


def removeplayer():
    xposition = position.map_x_position
    yposition = position.map_y_position
    showmap[yposition][xposition] = ""


def spawnmonster():
    return
