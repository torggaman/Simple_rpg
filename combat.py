import character
import monsters
import skills
import magic
import map


class Battlefield:
    fighting = False
    monster = {"name": "", "damage_taken": 0, "x_position": 0, "y_position": 0}
    player = {"previous_map_name": "", "previous_x": 0, "previous_y": 0}


bf = Battlefield()


def clear_battlefield():
    bf.fighting = False
    bf.monster = {"name": "", "damage_taken": 0, "x_position": 0, "y_position": 0}
    bf.player = {"previous_map_name": "", "previous_x": 0, "previous_y": 0}


def create_battlefield():
    monstername = map.maplist[map.position.map_name].monsters[map.position.monster_encountered]["name"]
    map.reset_map()
    mapname = monsters.list_of_monster[monstername].map_name
    monster = bf.monster
    player = bf.player
    player["previous_map_name"] = map.position.map_name
    player["previous_x"] = map.position.map_x_position
    player["previous_y"] = map.position.map_y_position
    monster["name"] = monstername
    monster["x_position"] = map.maplist[mapname].width
    monster["y_position"] = map.maplist[mapname].height
    map.position.map_x_position = 0
    map.position.map_y_position = 0
    map.position.map_name = mapname
    map.createmap(mapname)
    bf.fighting = True
    map.display_map()
    character.display_stats()


directions = ["up", "down", "left", "right"]


def combat_action():
    if not bf.fighting:
        create_battlefield()
    action = input(character.Playercharacter.state + " > ")
    if action == "attack":
        attack()
    elif action == "skill":
        use_skill()
    elif action == "magic":
        use_magic()
    elif action == "item":
        use_item()
    elif action == "turn":
        action = input("What Direction? ")
        map.turn_direction(action)
        map.redraw_character()
        map.display_map()
        character.display_stats()
    elif action in directions:
        map.removeplayer()
        if action == "up":
            map.position.moveplayerup()
        elif action == "down":
            map.position.moveplayerdown()
        elif action == "left":
            map.position.moveplayerleft()
        elif action == "right":
            map.position.moveplayerright()
        map.redraw_character()
        map.display_map()
        character.display_stats()
    else:
        print("Try again")


def attack():
    if check_monster():
        damage = character.calculate_damage()
        print("You swing for %d points of damage" % damage)
        bf.monster["damage_taken"] += damage
        check_monster_death()
        if not bf.monster["name"] == "":
            monster_attack()
            check_player_death()
    else:
        print("Nothing to attack")


def use_skill():
    return


def use_magic():
    return


def use_item():
    return


def check_monster():
    whats_there = map.what_is_in_front()
    print(whats_there)
    if whats_there == "M":
        return True
    else:
        return False


def check_monster_death():
    monster_name = bf.monster["name"]
    if bf.monster["damage_taken"] >= monsters.list_of_monster[monster_name].stats["health"]:
        experience_gained = monsters.list_of_monster[monster_name].stats["experience"]
        money_gained = monsters.list_of_monster[monster_name].stats["money"]
        print(monster_name + " Has Been Defeated\n You gain:\n %d xp \n %d money" % (experience_gained, money_gained))
        character.Playercharacter.experience += experience_gained
        character.Playercharacter.money += money_gained
        character.Playercharacter.levelup()
        end_battle()


def monster_attack():
    monster_name = bf.monster["name"]
    monster_damage = monsters.list_of_monster[monster_name].stats["attack"]
    print("Monster hit you for %d points of damage" % monster_damage)
    character.Playercharacter.damage_taken += monster_damage


def check_player_death():
    if character.Playercharacter.damage_taken >= character.Playercharacter.stats["health"]:
        print("You have died")
        respawn_character()


def respawn_character():
    character.Playercharacter.state = ""
    map.position.map_name = character.Playercharacter.save_location
    map.position.map_x_position = character.Playercharacter.save_location["x_position"]
    map.position.map_y_position = character.Playercharacter.save_location["y_position"]
    clear_battlefield()
    map.reset_map()
    map.createmap(map.position.map_name)
    map.redraw_character()
    map.display_map()
    character.display_stats()


def end_battle():
    character.Playercharacter.state = ""
    map.position.map_name = bf.player["previous_map_name"]
    map.position.map_x_position = bf.player["previous_x"]
    map.position.map_y_position = bf.player["previous_y"]
    clear_battlefield()
    map.reset_map()
    map.createmap(map.position.map_name)
    map.redraw_character()
    map.display_map()
    character.display_stats()
