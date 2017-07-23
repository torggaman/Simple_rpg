import character
import combat
import map
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
        map.createmap(map.Playerposition.map_name)
        map.display_map()
        need_map = False
    if pc.state == "looking at menu":
        menus.menuactions()
    elif pc.state == "":
        actions.playeraction()
    elif pc.state == "battle":
        combat.combat_action()
    else:
        print()
