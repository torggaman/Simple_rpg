from random import randint
import classes as c


class Basecharacter:
    stats = {
        "strength": 1,
        "intelligence": 1,
        "dexterity": 1,
        "constitution": 1,
        "luck": 1,
        "health": 1,
        "magic": 1,
        "stamina": 1
    }
    magic = 1
    stamina = 1
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
    actionskillslearned = []
    passiveskillslearned = []
    name = ""
    healthmodifier = 1
    magicmodifier = 1
    staminamodifier = 1
    strengthmodifier = 1
    intelligencemodifier = 1
    dexteritymodifier = 1
    constitutionmodifier = 1
    luckmodifier = 1
    requiredexperience = 1000
    state = ""

    def levelup(self):
        while self.experience >= (self.level * self.requiredexperience):
            self.level += 1
            print("Level: " + str(self.level) + "\n")
            self.stats["strength"] = self.stats["strength"] + (self.level * self.strengthmodifier)
            self.stats["intelligence"] = self.stats["intelligence"] + (self.level * self.intelligencemodifier)
            self.stats["dexterity"] = self.stats["dexterity"] + (self.level * self.dexteritymodifier)
            self.stats["constitution"] = self.stats["constitution"] + (self.level * self.constitutionmodifier)
            self.stats["luck"] = self.stats["luck"] + (self.level * self.luckmodifier)
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

    def get_health(self):
        base_health = 100
        modified_health = (self.stats["constitution"] * 10)
        self.stats["health"] = (base_health + modified_health) * self.healthmodifier

    def get_magic(self):
        basemagic = 50
        modifiedmagic = (self.stats["intelligence"] * 5)
        self.stats["magic"] = (basemagic + modifiedmagic) * self.magicmodifier

    def get_stats(self):
        stats = {"strength": 0, "intelligence": 0, "dexterity": 0, "constitution": 0, "luck": 0}
        for stat in stats:
            number = randint(1, 10)
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
        availableclasses = [c.ad.classname,
                            c.wa.classname,
                            c.ma.classname,
                            c.me.classname,
                            c.cl.classname,
                            c.ar.classname]
        print("What class are you?")
        print("%s[1], %s[2], %s[3], %s[4], %s[5], %s[6]" % (availableclasses[0],
                                                            availableclasses[1],
                                                            availableclasses[2],
                                                            availableclasses[3],
                                                            availableclasses[4],
                                                            availableclasses[5]))
        answer = input("Choose a number > ")
        if int(answer) > 0 & int(answer) < 7:
            choosenclass = availableclasses[int(answer)-1]
            self.characterclass = availableclasses[int(answer) - 1]
            for i in range(len(availableclasses)):
                if i == choosenclass:
                    self.healthmodifier += c.i.healthmodifier
                    self.magicmodifier += c.i.magicmodifier
                    self.staminamodifier += c.i.staminamodifier
        else:
            self.chooseclass()

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
    display = int(round((Playercharacter.stats["health"] / 10)))
    print("Hp:[" + "/" * display + "]")


def display_magic():
    display = int(round((Playercharacter.stats["magic"] / 10)))
    print("Mp:[" + "/" * display + "]")


def display_stamina():
    display = int(round((Playercharacter.stats["stamina"] / 10)))
    print("St:[" + "/" * display + "]")


def display_exp():
    print("Exp:[" + "-" * int(Playercharacter.experience / 100) + "]")


def display_stats():
    print("")
    display_health()
    display_magic()
    display_stamina()
    display_exp()
