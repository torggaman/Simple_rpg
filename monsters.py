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

    def check_health(self):
        return self.stats["health"]

    def check_attack(self):
        return self.stats["attack"]

    def check_defense(self):
        return self.stats["defense"]

    def check_type(self):
        return self.stats["type"]

    def check_experience(self):
        return self.stats["experience"]

    def check_money(self):
        return self.stats["money"]

    def check_items(self):
        return self.stats["items"]


class Slime(Basemonster):
    name = "Slime"
    stats = {"health": 10,
             "attack": 1,
             "defense": 1,
             "type": "slime",
             "experience": 500,
             "money": 5,
             "items": {},
             "attack_speed": 1,
             "attack_range": 1,
             "movement_speed": 1}


class Speedslime(Slime):
    name = "Speed Slime"
    stats = {"health": 20,
             "attack": 2,
             "defense": 2,
             "type": "",
             "experience": 1000,
             "money": 10,
             "items": {},
             "attack_speed": 1,
             "attack_range": 1,
             "movement_speed": 2}



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


s = Slime()
ss = Speedslime()
bs = Bossslime()

list_of_monster = {"Slime": s,
                   "Speed Slime": ss,
                   "Boss Slime": Bossslime}
