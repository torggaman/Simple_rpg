import character
import classes
import combat
import items
import load
import magic
import map
import menus
import monsters
import npc
import quests
import save
import skills
import dialog

player = character.Playercharacter
play = True
charactercreated = False
# Run a check to see if player has a character

if not charactercreated:
    pc = player
    pc.createcharacter()
    pc.mapname = "Starting"
    print("Welcome to the world")
    charactercreated = True


def playeraction():
    return input("> ")


def quitgame():
    play = False


def actions(action):
    performactions = {"move": moveplayer(),
                      "menu": "TBD",
                      "quit": quitgame()}
    while True:
        if action in performactions:
            performactions[action]
        else:
            print("Please try again")


def moveplayer():
    movement = True
    while movement:
        action = input("What direction?> ").lower()
        map.showmap[character.Playercharacter.mapyposition][character.Playercharacter.mapxposition] = ''
        checking = map.checkmovement(action,
                                     character.Playercharacter.mapyposition,
                                     character.Playercharacter.mapxposition)
        if action == "up" or action == "u":
            if not character.Playercharacter.mapyposition == 0:
                character.Playercharacter.mapyposition = character.Playercharacter.mapyposition - 1
            else:
                print("Cannot move that way")
        elif action == "down" or action == "d":
            if not character.Playercharacter.mapyposition == (len(map.showmap) - 1):
                character.Playercharacter.mapyposition = character.Playercharacter.mapyposition + 1
            else:
                print("Cannot move that way")
        elif action == "left" or action == "l":
            if not character.Playercharacter.mapxposition == 0:
                character.Playercharacter.mapxposition = character.Playercharacter.mapxposition - 1
            else:
                print("Cannot move that way")
        elif action == "right" or action == "r":
            if not character.Playercharacter.mapxposition == (len(map.showmap[character.Playercharacter.mapyposition]) - 1):
                character.Playercharacter.mapxposition = character.Playercharacter.mapxposition + 1
            else:
                print("Cannot move that way")
        elif action == "actions":
            movement = False
            actions(playeraction())
        else:
            print("Try again")
            print("You can type: Up(u), Down(d), Left(l), Right(r), or actions to leave movement")
        map.showmap[character.Playercharacter.mapyposition][character.Playercharacter.mapxposition] = 'P'
        map.displaymap(map.showmap)


while play:
    needmap = True
    if needmap:
        map.createmap(pc.mapyposition, pc.mapxposition, pc.mapname)
        needmap = False
    actions(playeraction())
