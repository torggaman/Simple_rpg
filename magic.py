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


class Fireball(Basicspell):
    name = "Fireball"
    magic_cost = 10
    magic_damage = 5
    element = "fire"
    level = 1
    max_level = 5
    effects = {"knockback": 1,
               "projectile_type": "ball",
               "linger": 0,
               "projectile_number": 1,
               "range": 2}


class Iceball(Basicspell):
    name = "Iceball"
    magic_cost = 10
    magic_damage = 3
    element = "ice"
    level = 1
    max_level = 3
    effects = {"knockback": 0,
               "projectile_type": "ball",
               "linger": 3,
               "projectile_number": 1,
               "range": 1}


list_of_spells = {"fireball": Fireball, "iceball": Iceball}
