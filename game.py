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
    charactercreated = True


def playeraction():
    return input("> ")

while play:
    print("Welcome to the world")
    map.createmap(pc.mapyposition, pc.mapxposition, pc.mapname)
    playeraction()
    break
