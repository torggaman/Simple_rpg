from random import randint
import classes as c


class Basecharacter:
    name = ""
    stats = {
        "strength": 1,
        "intelligence": 1,
        "dexterity": 1,
        "constitution": 1,
        "luck": 1,
        "health": 1,
        "magic": 1,
        "stamina": 1,
        "health_regen": 1,
        "magic_regen": 1,
        "stamina_regen": 1}
    stats_modifier = {"health": 1,
                      "magic": 1,
                      "stamina": 1,
                      "strength": 1,
                      "intelligence": 1,
                      "dexterity": 1,
                      "constitution": 1,
                      "luck": 1}
    equipped = {"head": {"name": "", "armor": 0, "special": {}},
                "chest": {"name": "", "armor": 0, "special": {}},
                "hand": {"name": "", "armor": 0, "special": {}},
                "leg": {"name": "", "armor": 0, "special": {}},
                "primary": {"name": "", "attack": 0, "magic_attack": 0, "special": {}, "type": "melee"},
                "off_hand": {"name": "", "attack": 0, "magic_attack": 0, "armor": 0, "special": {}, "type": "melee"}}
    inventory = {}
    damage_taken = 0
    magic_used = 0
    stamina_used = 0
    drop_Rate = 1
    questsTaken = []
    questsComplete = []
    level = 1
    experience = 0
    money = 0
    debt = 0
    characterclass = []
    walkspeed = 1
    attackspeed = 1
    skills_learned = []
    spells_learned = []
    requiredexperience = 1000
    state = ""
    save_location = {"map_name": "Starting", "x_position": 0, "y_position": 0}

    def levelup(self):
        while self.experience >= (self.level * self.requiredexperience):
            self.level += 1
            print("Level: " + str(self.level) + "\n")
            self.stats["strength"] = self.stats["strength"] + (self.level * self.stats_modifier["strength"])
            self.stats["intelligence"] = self.stats["intelligence"] + (self.level * self.stats_modifier["intelligence"])
            self.stats["dexterity"] = self.stats["dexterity"] + (self.level * self.stats_modifier["dexterity"])
            self.stats["constitution"] = self.stats["constitution"] + (self.level * self.stats_modifier["constitution"])
            self.stats["luck"] = self.stats["luck"] + (self.level * self.stats_modifier["luck"])
            print("Strength: %d \n"
                  "Intelligence: %d \n"
                  "Dexterity: %d \n"
                  "Constitution: %d \n"
                  "Luck: %d" % (self.stats["strength"],
                                self.stats["intelligence"],
                                self.stats["dexterity"],
                                self.stats["constitution"],
                                self.stats["luck"]))

    def choosestats(self):
        statpoints = 30
        while statpoints > 0:
            print("Where would you like to put your points? ")
            print("Status Points: %d" % statpoints)
            print("Strength: %d \n "
                  "Intelligence: %d \n "
                  "Dexterity: %d \n "
                  "Constitution: %d \n "
                  "Luck: %d" % (self.stats["strength"],
                                self.stats["intelligence"], 
                                self.stats["dexterity"], 
                                self.stats["constitution"], 
                                self.stats["luck"]))
            answer = input("Choose a stat")
            if answer == "strength":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.stats["strength"] = int(answer)
            elif answer == "intelligence":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.stats["intelligence"] = int(answer)
            elif answer == "dexterity":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.stats["dexterity"] = int(answer)
            elif answer == "constitution":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.stats["constitution"] = int(answer)
            elif answer == "luck":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.stats["luck"] = int(answer)
            else:
                print("Please try again \nMake sure the number is larger than 0 and no higher than 10")

    def create_character(self):
        self.name = input("What is your name? ")
        print("Welcome: %s" % self.name)
        print("Generating Stats")
        self.get_stats()
        self.chooseclass()
        self.get_health()
        self.get_magic()
        self.stats["stamina"] = 100 + (self.stats["dexterity"] * 2)
        self.get_spells()
        self.get_skills()

    def get_health(self):
        base_health = 100
        modified_health = (self.stats["constitution"] * 10)
        self.stats["health"] = (base_health + modified_health) * self.stats_modifier["health"]

    def get_magic(self):
        basemagic = 50
        modifiedmagic = (self.stats["intelligence"] * 5)
        self.stats["magic"] = (basemagic + modifiedmagic) * self.stats_modifier["magic"]

    def get_stats(self):
        minimum = 1
        maximum = 10
        stats = {"strength": 0, "intelligence": 0, "dexterity": 0, "constitution": 0, "luck": 0}
        for stat in stats:
            number = randint(minimum, maximum)
            if number == maximum:
                maximum -= 1
            if number == minimum:
                minimum += 1
            stats[stat] = number
        print("Your stats are:\n"
              "Strength: %d\n"
              "Intelligence: %d\n"
              "Dexterity: %d\n"
              "Constitution: %d\n"
              "Luck: %d" % (stats["strength"],
                            stats["intelligence"],
                            stats["dexterity"],
                            stats["constitution"],
                            stats["luck"]))
        self.stats["strength"] = stats["strength"]
        self.stats["intelligence"] = stats["intelligence"]
        self.stats["dexterity"] = stats["dexterity"]
        self.stats["constitution"] = stats["constitution"]
        self.stats["luck"] = stats["luck"]

    def chooseclass(self):
        choosing = True
        while choosing:
            availableclasses = [c.ad.class_name,
                                c.wa.class_name,
                                c.ma.class_name,
                                c.me.class_name,
                                c.cl.class_name,
                                c.ar.class_name]
            print("What class are you?")
            print("%s[1], %s[2], %s[3], %s[4], %s[5], %s[6]" % (availableclasses[0],
                                                                availableclasses[1],
                                                                availableclasses[2],
                                                                availableclasses[3],
                                                                availableclasses[4],
                                                                availableclasses[5]))
            answer = input("Choose a number > ")
            try:
                answer = int(answer)
                if answer >= 0 & answer <= 6:
                    choosenclass = availableclasses[answer - 1]
                    self.characterclass = availableclasses[answer - 1]
                    self.stats_modifier["health"] += c.classes[choosenclass].healthmodifier
                    self.stats_modifier["magic"] += c.classes[choosenclass].magicmodifier
                    self.stats_modifier["stamina"] += c.classes[choosenclass].staminamodifier
                    if not c.classes[choosenclass].mainstat == "":
                        self.stats_modifier[c.classes[choosenclass].mainstat] += 1
                    choosing = False
            except ValueError:
                print("Please make sure you choose a number 1 - 6")

    def get_spells(self):
        character_spells = c.classes[Playercharacter.characterclass].spells
        if len(character_spells) > 0:
            for spells in character_spells:
                Playercharacter.spells_learned.append(spells)

    def get_skills(self):
        character_skills = c.classes[Playercharacter.characterclass].skills
        if len(character_skills) > 0:
            for skills in character_skills:
                Playercharacter.skills_learned.append(skills)

    def showstats(self):
        print("Name: %s\n"
              "Class: %s\n"
              "Level: %d\n"
              "Health: %d\n"
              "Magic: %d\n"
              "Stamina: %d\n"
              "Strength: %d\n"
              "Intelligence: %d\n"
              "Dexterity: %d\n"
              "Constitution: %d\n"
              "Luck: %d\n" % (self.name,
                              self.characterclass,
                              self.level,
                              self.stats["health"],
                              self.stats["magic"],
                              self.stats["stamina"],
                              self.stats["strength"],
                              self.stats["intelligence"], 
                              self.stats["dexterity"], 
                              self.stats["constitution"], 
                              self.stats["luck"]))


Playercharacter = Basecharacter()


def display_health():
    display = (Playercharacter.stats["health"] - Playercharacter.damage_taken)
    print("HP: %d / %d" % (display, Playercharacter.stats["health"]))


def display_magic():
    display = (Playercharacter.stats["magic"] - Playercharacter.magic_used)
    print("MP: %d / %d" % (display, Playercharacter.stats["magic"]))


def display_stamina():
    display = Playercharacter.stats["stamina"] - Playercharacter.stamina_used
    print("St: %d / %d" % (display, Playercharacter.stats["stamina"]))


def display_exp():
    print("Exp: %d / %d" % (Playercharacter.experience, (Playercharacter.requiredexperience * Playercharacter.level)))


def display_stats():
    print("")
    display_health()
    display_magic()
    display_stamina()
    display_exp()


def set_up_spell_list():
    paging = 1
    number = 0
    known_spells = {}
    for spells in Playercharacter.spells_learned:
        if number == 5:
            paging += 1
            number = 0
        if known_spells[str(paging)]:
            known_spells[str(paging)].append(spells)
            number += 1
        else:
            known_spells[str(paging)] = []
            known_spells[str(paging)].append(spells)
            number += 1


def display_spells(spells):
    displaying = True
    display_page = 1
    while displaying:
        spells_to_display = "Page" + str(display_page) + "/ " + str(len(spells)) + "\n"
        for spell in spells[display_page]:
            spells_to_display = spells_to_display + spell + "/ "
        print(spells_to_display)
        action = input("\"next\" or \"previous\" page \n or \"close\"")
        try:
            if action == "next" and spells[display_page]:
                display_page += 1
            elif action == "previous" and display_page == 1:
                display_page -= 1
            elif action == "close":
                displaying = False
            else:
                print("Please type one of the following: \nnext/ previous/ close")
        except IndexError:
            print("No more pages moving back to first page")
            display_page = 1


def calculate_damage():
    pc = Playercharacter
    weapontype = pc.equipped["primary"]["type"]
    addweapontype = 0
    if weapontype == "melee":
        addweapontype = pc.stats["strength"]
    elif weapontype == "ranged":
        addweapontype = pc.stats["dexterity"]
    elif weapontype == "magic":
        addweapontype = pc.stats["intelligence"]
    total_damage = pc.equipped["primary"]["attack"] + pc.equipped["off_hand"]["attack"] + addweapontype
    return total_damage


def calculate_magic_damage():
    pc = Playercharacter
    pcint = pc.stats["intelligence"]
    total_damage = pcint + pc.equipped["primary"]["magic_attack"] + pc.equipped["off_hand"]["magic_attack"]
    return total_damage
