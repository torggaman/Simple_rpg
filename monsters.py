class Basemonster:
    name = ""
    stats = {"health": 1,
             "attack": 1,
             "defense": 1,
             "type": "",
             "experience": 1,
             "money": 1,
             "items": {},
             "attack_speed": 1,
             "attack_range": 1,
             "movement_speed": 1}
    skills = {}
    spells = {}
    map_name = "Battlefield"


class Slime(Basemonster):
    name = "Slime"
    stats = {"health": 10,
             "attack": 1,
             "defense": 1,
             "type": "slime",
             "experience": 10,
             "money": 5,
             "items": {},
             "attack_speed": 1,
             "attack_range": 1,
             "movement_speed": 1}


class Speedslime(Slime):
    name = "Speed Slime"
    stats = {"attack": 2,
             "attack_speed": 2,
             "movement_speed": 2,
             "experience": 20,
             "money": 10}


class Bossslime(Slime):
    name = "Boss Slime"
    stats ={"health": 50,
            "attack": 10,
            "defense": 5,
            "type": "slime",
            "experience": 100,
            "money": 50,
            "items": {},
            "attack_speed": 1,
            "attack_range": 1,
            "movement_speed": 1}
    map_name = "Big Battlefield"


list_of_monster = {"Slime": Slime,
                   "Speed Slime": Speedslime,
                   "Boss Slime": Bossslime}
