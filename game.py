import character
import classes
import combat
import items
import load
import magic
import map
import monsters
import npc
import quests
import save
import skills
import dialog
import actions
import menus


pc = character.Playercharacter
play = True
charactercreated = False
needmap = True
# Run a check to see if player has a character

def quitgame():
    return

while play:
    if not charactercreated:
        pc.createcharacter()
        map.Playerposition.mapname = "Starting"
        print("Welcome to the world")
        charactercreated = True
    if needmap:
        map.createmap(map.Playerposition.mapyposition, map.Playerposition.mapxposition, map.Playerposition.mapname)
        needmap = False
    action = input(pc.state + " > ")
    if pc.state == "looking at menu":
        menus.menuactions(action)
    elif pc.state == "":
        actions.playeraction(action)
    else:
        print()
