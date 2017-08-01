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
                "previous_y": 0,
                "cast_time": 0}
clean_projectile = {}
directions = ["up", "down", "left", "right"]
list_of_actions = ["attack", "a", "skill", "s", "magic", "m", "item", "i"]


class Battlefield:
    fighting = False
    monster = clean_monster
    player = clean_player
    projectile = clean_projectile

    def clear_battlefield(self):
        self.fighting = False
        self.monster = clean_monster
        self.player = clean_player


bf = Battlefield()


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
    players_spells = character.Playercharacter.spells_learned
    known_spells = "Spells Known: "
    for i in range(len(players_spells)):
        known_spells = known_spells + players_spells[i] + " | "
    # Pick a Spell
    chosen_spell = choose_spell(known_spells, players_spells)
    cast_spell(chosen_spell)
    # check if the monster is in front
    if not check_monster():
        projectile_placement()
        continue_moving = True
        while continue_moving:
            if check_if_hit():
                damage_monster_spell(chosen_spell)
            if len(bf.projectile) < 1:
                continue_moving = False
            else:
                moving_projectile()
    else:
        damage_monster_spell(chosen_spell)
        return
    # If the spell needs to be cast then a cast time starts and the player can't move(Maybe can turn)
    # Spell is cast and effect takes place(Maybe check if a spell needs to move)


def choose_spell(known_spells, players_spells):
    # Display available spells(Have something next to ones when the user doesn't have enough magic to use)
    choosing_spell = True
    while choosing_spell:
        print(known_spells)
        action = input("Choose a spell: ")
        if action in players_spells:
            return action
            choosing_spell = False
        else:
            print("Please choose the number next to the spell you want to cast")


def cast_spell(spell):
    if map.can_place_in_front():
        spell_cast = magic.list_of_spells[spell]
        magic_left = character.Playercharacter.stats["magic"] - character.Playercharacter.magic_used
        if magic_left > spell_cast.magic_cost:
            character.Playercharacter.magic_used += spell_cast.magic_cost
            for projectiles in range(spell_cast.effects["projectile_number"]):
                bf.projectile["p" + str(projectiles)] = {"x_position": 0,
                                                         "y_position": 0,
                                                         "range": spell_cast.effects["range"],
                                                         "duration": spell_cast.effects["linger"],
                                                         "facing": map.position.facing_direction}
            if spell_cast.cast_time > 0:
                bf.player["cast_time"] = spell_cast.cast_time
            print("You cast %s" % spell)
        else:
            print("Not enough magic")
    else:
        print("Not Enough Room to cast")


def projectile_placement():
    facing = map.position.facing_direction
    starting_position = map.in_front_of_player()
    length_of_projectile = len(bf.projectile)
    if length_of_projectile == 1:
        single_projectile_placement()
    elif length_of_projectile > 1:
        projectile_initial_placement(starting_position)


def moving_projectile():
    display_projectiles()
    remove_projectile()
    check_projectile_range()
    projectile_travel()
    display_projectiles()
    check_all_projectiles()


def check_all_projectiles():
    projectiles_to_remove = []
    for items in bf.projectile:
        projectiles = bf.projectile[items]
        if check_edge(projectiles["x_position"], projectiles["y_position"]):
            projectiles_to_remove.append(items)
        else:
            continue
    for names in projectiles_to_remove:
        print(names)
        clear_single_projectile(names)


def clear_single_projectile(projectile_name):
    map.showmap[bf.projectile[projectile_name]["y_position"]][bf.projectile[projectile_name]["x_position"]].replace(projectile_name, "")
    del bf.projectile[projectile_name]


def projectile_movement():
    return


def check_if_hit():
    for items in bf.projectile:
        x_position = bf.projectile[items]["x_position"]
        y_position = bf.projectile[items]["y_position"]
        if map.showmap[y_position][x_position] == "M":
            clear_single_projectile(items)
            return True
        else:
            return False


def projectile_initial_placement(starting_position):
    facing = map.position.facing_direction
    projectile_number = 0
    x_position_start = map.position.map_x_position
    y_position_start = map.position.map_y_position
    for projectile in bf.projectile:
        if facing == "up" or facing == "down":
            y_position_start = starting_position
            projectile["y_position"] = y_position_start
            projectile["x_position"] = x_position_start + projectile_number - 1
            projectile_number += 1
        elif facing == "left" or facing == "right":
            x_position_start = starting_position
            projectile["y_position"] = y_position_start + projectile_number - 1
            projectile["x_position"] = x_position_start
            projectile_number += 1


def single_projectile_placement():
    projectile_name = "p0"
    projectiles = bf.projectile
    facing = map.position.facing_direction
    x_position_start = map.position.map_x_position
    y_position_start = map.position.map_y_position
    if facing == "up":
        y_position_start -= 1
    elif facing == "down":
        y_position_start += 1
    elif facing == "left":
        x_position_start -= 1
    elif facing == "right":
        x_position_start += 1
    place_projectile(projectile_name, x_position_start, y_position_start)


def place_projectile(projectile_name, x_position, y_position):
    projectile = bf.projectile[projectile_name]
    projectile["x_position"] = x_position
    projectile["y_position"] = y_position


def projectile_travel():
    for items in bf.projectile:
        projectiles = bf.projectile[items]
        if projectiles["facing"] == "up":
            projectiles["y_position"] -= 1
        elif projectiles["facing"] == "down":
            projectiles["y_position"] += 1
        elif projectiles["facing"] == "left":
            projectiles["x_position"] -= 1
        elif projectiles["facing"] == "right":
            projectiles["x_position"] += 1


def check_edge(x_position, y_position, facing):
    at_edge = False
    if facing == "left" or facing == "right":
        if x_position == len(map.showmap[y_position])-1 or x_position == 0:
            at_edge = True
    elif facing == "up" or facing == "down":
        if y_position == len(map.showmap)-1 or y_position == 0:
            at_edge = True
    return at_edge


def check_projectile_range():
    for name in bf.projectile:
        if bf.projectile[name]["range"] > 0:
            bf.projectile[name]["range"] -= 1
        else:
            clear_single_projectile(name)


def remove_projectile():
    for items in bf.projectile:
        map.showmap[bf.projectile[items]["y_position"]][bf.projectile[items]["x_position"]] = ""


def display_projectiles():
    for items in bf.projectile:
        map.showmap[bf.projectile[items]["y_position"]][bf.projectile[items]["x_position"]] = items
    map.display_map()


def damage_monster_spell(spell):
    total_damage = character.calculate_magic_damage() + magic.list_of_spells[spell].magic_damage
    bf.monster["damage_taken"] += total_damage
    print("%s deals %d damage to %s" % (spell, total_damage, bf.monster["name"]))


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
    bf.clear_battlefield()
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
    bf.clear_battlefield()
    map.reset_map()
    map.createmap(map.position.map_name)
    map.redraw_character()
    map.display_map()
    character.display_stats()


def generic_use(x, y, z):
    choosing = True
    while choosing:
        print(x)
        action = input("Choose one: ")
        if action in x:
            return
        else:
            continue

