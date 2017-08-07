class Basicspell:
    name = ""
    magic_cost = 0
    magic_damage = 0
    element = ""
    level = 1
    max_level = 1
    experience = 0
    cast_time = 0
    effects = {"knockback": 0,
               "projectile_type": "",
               "linger": 0,
               "projectile_number": 1,
               "range": 1}

    def check_spell_type(self):
        return self.effects["projectile_type"]

    def check_spell_range(self):
        return self.effects["range"]

    def check_knock_back(self):
        return self.effects["knockback"]

    def check_element(self):
        return self.element


class Fireball(Basicspell):
    name = "Fireball"
    magic_cost = 10
    magic_damage = 2
    element = "fire"
    level = 1
    max_level = 5
    effects = {"knockback": 2,
               "projectile_type": "ball",
               "linger": 0,
               "projectile_number": 1,
               "range": 2}



class Icewall(Basicspell):
    name = "Icewall"
    magic_cost = 10
    magic_damage = 3
    element = "ice"
    level = 1
    max_level = 3
    effects = {"knockback": 0,
               "projectile_type": "wall",
               "linger": 3,
               "projectile_number": 1,
               "range": 1}

fb = Fireball()
iw = Icewall()

list_of_spells = {"fireball": fb, "icewall": iw}
