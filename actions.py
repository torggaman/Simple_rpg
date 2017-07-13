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
        m.addplayer()
        m.displaymap()
    elif action == "open menu":
        character.Playercharacter.state = "looking at menu"
    else:
        print("Please Try again")
