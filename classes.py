import skills
import character

class Baseclass():
    classname = ""
    healthmodifier = 0
    magicmodifier = 0
    staminamodifier = 0
    skills = []
    subclasses = []
    weapons = []
    armor = []
    mainstat = ""


class Adventurer(Baseclass):
    classname = "Adventurer"
    healthmodifier = 0.5
    magicmodifier = 0.5
    staminamodifier = 0.5
    skills = ["Adventurer Skills"]
    subclasses = ["none"]
    weapons = ["dagger",
               "sword",
               "bow",
               "small shield"]
    armor = ["medium",
             "light"]
    mainstat = "luck"


class Mage(Baseclass):
    classname = "Mage"
    magicmodifier = 1
    staminamodifier = 0.5
    skills = ["Mage Skills"]
    subclasses = ["Wizard"]
    weapons = ["wand",
               "staff",
               "small shields"]
    armor = ["medium"]
    mainstat = "intelligence"


class Warrior(Baseclass):
    classname = "Warrior"
    healthmodifier = 1
    staminamodifier = 0.5
    skills = ["Warrior Skills"]
    subclasses = ["Berserker",
                  "Knight"]
    weapons = ["dagger",
               "sword",
               "axe",
               "mace",
               "2handed sword",
               "2handed axe",
               "spear",
               "small shields",
               "large shields"]
    armor = ["medium",
             "light",
             "heavy"]
    mainstat = "strength"


class Merchant(Baseclass):
    healthmodifier = 0.5
    staminamodifier = 1
    classname = "Merchant"
    skills = ["Merchant"]
    subclasses = ["Blacksmith",
                  "Alchemist"]
    weapons = ["mace",
               "axe",
               "2handed axe",
               "small shield"]
    armor = ["medium",
             "light"]
    mainstat = "constitution"


class Cleric(Baseclass):
    magicmodifier = 0.5
    staminamodifier = 1
    classname = "Cleric"
    skills = ["Cleric"]
    subclasses = ["Priest"]
    weapons = ["mace",
               "small shield"]
    armor = ["medium",
             "light"]
    mainstat = "intelligence"


class Archer(Baseclass):
    staminamodifier = 1.5
    classname = "Archer"
    skills = ["Archer"]
    subclases = ["Ranger"]
    weapons = ["dagger",
               "bow"]
    armor = ["medium",
             "light"]
    mainstat = "dexterity"

ad = Adventurer
wa = Warrior
ma = Mage
me = Merchant
cl = Cleric
ar = Archer
classes = {"Adventurer": ad, "Warrior": wa, "Mage": ma, "Merchant": me, "Cleric": cl, "Archer": ar }


def learnskill():
    return ""
