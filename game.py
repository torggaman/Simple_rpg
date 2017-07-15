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
character_created = False
need_map = True
# Run a check to see if player has a character

def quitgame():
    return

while play:
    if not character_created:
        pc.create_character()
        map.Playerposition.map_name = "Starting"
        print("Welcome to the world")
        character_created = True
    if need_map:
        map.createmap(map.Playerposition.map_y_position, map.Playerposition.map_x_position, map.Playerposition.map_name)
        need_map = False
    action = input(pc.state + " > ")
    if pc.state == "looking at menu":
        menus.menuactions(action)
    elif pc.state == "":
        actions.playeraction(action)
    else:
        print()
