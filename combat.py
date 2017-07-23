import character
import monsters
import skills
import magic
import map
from random import randint

clean_monster = {"name": "",
                 "damage_taken": 0,
                 "x_position": 0,
                 "y_position": 0,
                 "facing": "up"}
clean_player = {"previous_map_name": "",
                "previous_x": 0,
                "previous_y": 0}
directions = ["up", "down", "left", "right"]
list_of_actions = ["attack", "a", "skill", "s", "magic", "m", "item", "i"]


class Battlefield:
    fighting = False
    monster = clean_monster
    player = clean_player


bf = Battlefield()


def clear_battlefield():
    bf.fighting = False
    bf.monster = clean_monster
    bf.player = clean_player


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
    monster["x_position"] = map.maplist[mapname].width - 1
    monster["y_position"] = map.maplist[mapname].height - 1
    map.position.map_x_position = 0
    map.position.map_y_position = 0
    map.position.map_name = mapname
    map.createmap(mapname)
    bf.fighting = True
    map.display_map()
    character.display_stats()


def combat_action():
    if not bf.fighting:
        create_battlefield()
    print("Action: attack/[a], skill/[s], magic/[m], item/[i]")
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
    elif action in directions:
        move_player(action)
    else:
        print("Try again")
    check_monster_death()
    if not bf.monster["name"] == "":
        decide_monster_attack()
        check_player_death()
        map.display_map()
        character.display_stats()


def move_player(action):
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


def player_nearby(default_range=1):
    target = ""
    y_position = bf.monster["y_position"]
    x_position = bf.monster["x_position"]
    try:
        if not y_position == 0:
            target = map.showmap[y_position - default_range][x_position]
        if not y_position == len(map.showmap) - 1:
            target = target + map.showmap[y_position + default_range][x_position]
        if not x_position == 0:
            target = target + map.showmap[y_position][x_position - default_range]
        if not x_position == len(map.showmap[y_position]) - 1:
            target = target + map.showmap[y_position][x_position + default_range]
        if not target == "":
            return True
        else:
            return False
    except IndexError:
        return False


def monster_movement():
    player_y = map.position.map_y_position
    player_x = map.position.map_x_position
    monster_y = bf.monster["y_position"]
    monster_x = bf.monster["x_position"]
    direction_to_move = []
    if monster_y < player_y:
        direction_to_move.append("higher")
    if monster_x < player_x:
        direction_to_move.append("left_of")
    if monster_y > player_y:
        direction_to_move.append("lower")
    if monster_x > player_x:
        direction_to_move.append("right_of")
    if len(direction_to_move) != 0 and not player_nearby():
        choosen_move_direction = randint(0, len(direction_to_move) - 1)
        remove_monster()
        move_monster(direction_to_move[choosen_move_direction])
        monster_combat_redraw()


def move_monster(move):
    if move == "higher":
        bf.monster["y_position"] += 1
        bf.monster["facing"] = "down"
    elif move == "lower":
        bf.monster["y_position"] -= 1
        bf.monster["facing"] = "up"
    elif move == "right_of":
        bf.monster["x_position"] -= 1
        bf.monster["facing"] = "left"
    elif move == "left_of":
        bf.monster["x_position"] += 1
        bf.monster["facing"] = "right"
    else:
        print("Monster doesn't Move")


def monster_combat_redraw():
    facing = bf.monster["facing"]
    x_position = bf.monster["x_position"]
    y_position = bf.monster["y_position"]
    icon = "M"
    if facing == "up":
        map.showmap[y_position][x_position] = icon
    elif facing == "down":
        map.showmap[y_position][x_position] = icon
    elif facing == "left":
        map.showmap[y_position][x_position] = icon
    elif facing == "right":
        map.showmap[y_position][x_position] = icon
    else:
        map.showmap[y_position][x_position] = icon


def remove_monster():
    x_position = bf.monster["x_position"]
    y_position = bf.monster["y_position"]
    map.showmap[y_position][x_position] = ""


def attack():
    if check_monster():
        damage = character.calculate_damage()
        print("You swing for %d points of damage" % damage)
        bf.monster["damage_taken"] += damage
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


def decide_monster_attack():
    # depending on where the monster is located and type of monster they should
    # provide a weight to know what to use
    # if a monster has spells or skills they will be weighted lower than standard attack
    if player_nearby():
        chance = randint(0, 100)
        weight = 0
        if chance >= 30:
            monster_attack()
        elif chance >= 10:
            monster_skill()
        elif chance >= 0:
            monster_spell()
        else:
            print("Did nothing")
    else:
        monster_movement()


def monster_attack():
    monster_name = bf.monster["name"]
    monster_damage = monsters.list_of_monster[monster_name].stats["attack"]
    print("Monster hit you for %d points of damage" % monster_damage)
    character.Playercharacter.damage_taken += monster_damage


def monster_skill():
    print("Tried to Use a Skill")


def monster_spell():
    print("Tried to Cast a Spell")


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
