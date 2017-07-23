import character
from random import randint


class Playerposition:
    map_x_position = 0
    map_y_position = 0
    map_name = ""
    room_name = ""
    facing_direction = "down"
    monster_encountered = ""

    def moveplayerup(self):
        if not self.map_y_position == 0:
            if walk_check((self.map_y_position - 1), self.map_x_position):
                self.map_y_position = self.map_y_position - 1
            self.facing_direction = "up"
        else:
            turn_direction("up")
            print("Cannot move that way")

    def moveplayerleft(self):
        if not self.map_x_position == 0:
            if walk_check(self.map_y_position, (self.map_x_position - 1)):
                self.map_x_position = self.map_x_position - 1
            self.facing_direction = "left"
        else:
            turn_direction("left")
            print("Cannot move that way")

    def moveplayerright(self):
        if not self.map_x_position == (len(showmap[self.map_x_position]) - 1):
            if walk_check(self.map_y_position, (self.map_x_position + 1)):
                self.map_x_position = self.map_x_position + 1
            self.facing_direction = "right"
        else:
            turn_direction("right")
            print("Cannot move that way")

    def moveplayerdown(self):
        if not self.map_y_position == (len(showmap) - 1):
            if walk_check((self.map_y_position + 1), self.map_x_position):
                self.map_y_position = self.map_y_position + 1
            self.facing_direction = "down"
        else:
            turn_direction("down")
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
    monsters = {}
    npc = {}
    objects = {
        "wall": {},
        "door": {},
        "chest": {},
        "trap": {},
        "exit": {}}


class Starting(Basemap):
    name = "Starting Area"
    width = 4
    height = 4
    type = "beginner"
    objects = {
        "wall": {"1": {"xposition": 1, "yposition": 1, "secret": False},
                 "2": {"xposition": 1, "yposition": 2, "secret": True}},
        "door": {"1": {"xposition": 1, "yposition": 0, "locked": False, "open": False},
                 "2": {"xposition": 1, "yposition": 3, "locked": False, "open": True}},
        "chest": {},
        "trap": {},
        "exit": {"1": {"xposition": 3, "yposition": 3, "map": "Starting2", "player_x": 3, "player_y": 1}}
    }
    monsters = {"1": {"name": "Slime"}}


class Starting2(Basemap):
    name = "Starting Area2"
    width = 4
    height = 4
    type = "beginner"
    objects = {
        "wall": {},
        "door": {},
        "chest": {},
        "trap": {},
        "exit": {"1": {"xposition": 3, "yposition": 0, "map": "Starting", "player_x": 3, "player_y": 2}}
    }
    monsters = {"1": {"name": "Slime"}}


class Battlefield(Basemap):
    name = "Battlefield"
    width = 5
    height = 5


class Bigbattlefield(Basemap):
    name = "Big Battlefield"
    width = 10
    height = 10


position = Playerposition()
maplist = {"Starting": Starting,
           "Starting2": Starting2,
           "Battlefield": Battlefield,
           "Big Battlegfield": Bigbattlefield}
showmap = []


def createmap(mapname):
    yposition = position.map_y_position
    xposition = position.map_x_position
    ysize = maplist[mapname].height
    xsize = maplist[mapname].width
    for y in range(ysize):
        showmap.append([])
        for x in range(xsize):
            showmap[y].append([])
            showmap[y][x] = ""
    place_objects(mapname)
    showmap[yposition][xposition] += "P"
    spawn_monster(mapname)
    if character.Playercharacter.state == "battle":
        showmap[maplist[mapname].height - 1][maplist[mapname].width - 1] = "M"


def display_map():
    print("Current Map: " + maplist[position.map_name].name)
    for y in showmap:
        print(y)


def redraw_character():
    facing = position.facing_direction
    x_position = position.map_x_position
    y_position = position.map_y_position
    if facing == "up":
        showmap[y_position][x_position] = "^"
    elif facing == "down":
        showmap[y_position][x_position] = "v"
    elif facing == "left":
        showmap[y_position][x_position] = "<"
    elif facing == "right":
        showmap[y_position][x_position] = ">"
    else:
        showmap[y_position][x_position] = "P"


def turn_direction(direction):
    if direction == "north" or direction == "up":
        if position.map_y_position == 0:
            print("Nothing that way")
        position.facing_direction = "up"
    elif direction == "south" or direction == "down":
        if position.map_y_position == len(showmap) - 1:
            print("Nothing that way")
        position.facing_direction = "down"
    elif direction == "west" or direction == "left":
        if position.map_x_position == 0:
            print("Nothing that way")
        position.facing_direction = "left"
    elif direction == "east" or direction == "right":
        if position.map_x_position == len(showmap[position.map_y_position]) - 1:
            print("Nothing that way")
        position.facing_direction = "right"
    else:
        print("Please try: up, down, left, right \n or north, south, east, west")


def removeplayer():
    xposition = position.map_x_position
    yposition = position.map_y_position
    showmap[yposition][xposition] = ""


def spawn_monster(mapname):
    if len(maplist[mapname].monsters) > 0:
        for m in maplist[mapname].monsters:
            x_maximum = maplist[mapname].width - 1
            y_maximum = maplist[mapname].height - 1
            x_position = 0
            y_position = 0
            while not showmap[y_position][x_position] == "":
                x_position = randint(0, x_maximum)
                y_position = randint(0, y_maximum)
            showmap[y_position][x_position] = "M" + str(m)


def what_is_in_front():
    if position.facing_direction == "up":
        if position.map_y_position == "0":
            return False
        else:
            return showmap[position.map_y_position - 1][position.map_x_position]
    elif position.facing_direction == "down":
        if position.map_y_position == len(showmap) - 1:
            return False
        else:
            return showmap[position.map_y_position + 1][position.map_x_position]
    elif position.facing_direction == "left":
        if position.map_x_position == "0":
            return False
        else:
            return showmap[position.map_y_position][position.map_x_position - 1]
    elif position.facing_direction == "right":
        if position.map_x_position == len(showmap[position.map_y_position]) - 1:
            return False
        else:
            return showmap[position.map_y_position][position.map_x_position + 1]


def walk_check(y_position, x_position):
    position_to_move = showmap[y_position][x_position]
    position_to_move_list = list(position_to_move)
    if "D" in position_to_move_list:
        number = position_to_move.replace("D", "")
        if maplist[position.map_name].objects["door"][number]["open"]:
            return True
        else:
            print("The door appears to be closed")
            return False
    elif position_to_move == "C":
        print("Something is Blocking the path")
        return False
    elif "T" in position_to_move_list:
        return True
    elif "X" in position_to_move_list:
        number = position_to_move.replace("X", "")
        move_to_map(number)
        return False
    elif "W" in position_to_move_list:
        number = position_to_move.replace("W", "")
        if maplist[position.map_name].objects["wall"][number]["secret"]:
            return True
        else:
            print("Something is Blocking the path")
            return False
    elif "M" in position_to_move_list:
        if not character.Playercharacter.state == "battle":
            character.Playercharacter.state = "battle"
            print(position_to_move)
            position.monster_encountered = str(position_to_move.replace("M", ""))
        return False
    else:
        return True


def check_door(door_number):
    door = maplist[position.map_name].objects["door"][door_number]
    if door["locked"]:
        # have an if statement for if the user has a key to unlock the door
        print("The door appears to be locked")
    else:
        if not door["open"]:
            door["open"] = True
            print("Door Opened")
    return


def check_chest():
    return


def check_trap(trap_number):
    trap = maplist[position.map_name].objects["trap"][trap_number]
    if not trap["disarmed"]:
        print("You activated the trap!")


def check_in_front():
    what_is_it = what_is_in_front()
    if not what_is_it:
        print("There is nothing")
    else:
        what_is_it_list = list(what_is_it)
        if "D" in what_is_it_list:
            check_door(what_is_it.replace("D", ""))
        elif "M" in what_is_it_list:
            if not character.Playercharacter.state == "battle":
                character.Playercharacter.state = "battle"
                position.monster_encountered = str(what_is_it.replace("M", ""))
        else:
            print("Nothing to check")


def reset_map():
    global showmap
    showmap = []


def move_to_map(number):
    map = maplist[position.map_name].objects["exit"][number]
    position.map_name = map["map"]
    position.map_x_position = map["player_x"]
    position.map_y_position = map["player_y"]
    reset_map()
    createmap(position.map_name)


def place_objects(mapname):
    map = maplist[mapname]
    if len(map.objects["wall"]) > 0:
        mapw = map.objects["wall"]
        for walls in mapw:
            showmap[mapw[walls]["yposition"]][mapw[walls]["xposition"]] = "W" + str(walls)
    if len(map.objects["door"]) > 0:
        mapd = map.objects["door"]
        for doors in mapd:
            showmap[mapd[doors]["yposition"]][mapd[doors]["xposition"]] = "D" + str(doors)
    if len(map.objects["chest"]) > 0:
        mapc = map.objects["chest"]
        for chests in mapc:
            showmap[mapc[chests]["yposition"]][mapc[chests]["xposition"]] = "C" + str(chests)
    if len(map.objects["trap"]) > 0:
        mapt = map.objects["trap"]
        for traps in mapt:
            showmap[mapt[traps]["yposition"]][mapt[traps]["xposition"]] = "T" + str(traps)
    if len(map.objects["exit"]) > 0:
        mapexit = map.objects["exit"]
        for exits in mapexit:
            showmap[mapexit[exits]["yposition"]][mapexit[exits]["xposition"]] = "X" + str(exits)
