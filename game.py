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
#Run a check to see if player has a character

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
    performactions = {"move": map.moveplayer(),
               "menu": "TBD",
               "quit": quitgame()}
    while True:
        if action in performactions:
            performactions[action]
        else:
            print("Please try again")

while play:
    needmap = True
    if needmap:
        map.createmap(pc.mapyposition, pc.mapxposition, pc.mapname)
        needmap = False
    actions(playeraction())
