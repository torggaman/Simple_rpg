class Baseclass():
    health_modifier = 0
    magic_modifier = 0
    stamina = 0
    skills = []
    subclasses = []


class Adventurer(Baseclass):
    health_modifier = 0.5
    magic_modifier = 0.5
    stamina_modifier = 0.5
    skills = ["Adventurer Skills"]
    subclasses = ["none"]


class Mage(Baseclass):
    magic_modifier = 1
    stamina_modifier = 0.5
    skills = ["Mage Skills"]
    subclasses = ["Wizard"]


class Warrior(Baseclass):
    health_modifier = 1
    stamina = 0.5
    skills = ["Warrior Skills"]
    subclasses = ["Berserker", "Knight"]


class Merchant(Baseclass):
    skills = ["Merchant"]
    subclasses = ["Blacksmith", "Alchemist"]


class Cleric(Baseclass):
    skills = ["Cleric"]
    subclasses = ["Priest"]



class Archer(Baseclass):
    skills = ["Archer"]
    subclases = ["Ranger"]