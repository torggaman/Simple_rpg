import map as m
import character

directions = ["up", "down", "left", "right"]

def playeraction(action):
    if action in directions:
        m.removeplayer()
        if action == "up":
            m.position.moveplayerup()
        elif action == "down":
            m.position.moveplayerdown()
        elif action == "left":
            m.position.moveplayerleft()
        elif action == "right":
            m.position.moveplayerright()
        m.redraw_character()
        character.display_stats()
    elif action == "open menu":
        character.Playercharacter.state = "looking at menu"
    elif action == "turn":
        direction = input("What direction?> ")
        m.turn_direction(direction)
        m.removeplayer()
        m.redraw_character()
        character.display_stats()
    else:
        print("Please Try again")
