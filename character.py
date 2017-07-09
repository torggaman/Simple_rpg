from random import randint
import classes as c


class Basecharacter:
    strength = 1
    intelligence = 1
    dexterity = 1
    constitution = 1
    luck = 1
    health = 0
    magic = 0
    stamina = 0
    dropRate = 1
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
    mapxposition = 0
    mapyposition = 0
    mapname = ""
    roomname = ""

    def levelup(self):
        while self.experience >= (self.level * self.requiredexperience):
            self.level += 1
            print("Level: " + str(self.level) + "\n")
            self.strength = self.strength + (self.level * self.strengthmodifier)
            self.intelligence = self.intelligence + (self.level * self.intelligencemodifier)
            self.dexterity = self.dexterity + (self.level * self.dexteritymodifier)
            self.constitution = self.constitution + (self.level * self.constitutionmodifier)
            self.luck = self.luck + (self.level * self.luckmodifier)
            print("Strength: %d \n"
                  "Intelligence: %d \n"
                  "Dexterity: %d \n"
                  "Constitution: %d \n"
                  "Luck: %d" % (self.strength, self.intelligence, self.dexterity, self.constitution, self.luck))

    def choosestats(self):
        statpoints = 30
        while statpoints > 0:
            print("Where would you like to put your points? ")
            print("Status Points: %d" % statpoints)
            print("Strength: %d \n "
                  "Intelligence: %d \n "
                  "Dexterity: %d \n "
                  "Constitution: %d \n "
                  "Luck: %d" % (self.strength,
                                self.intelligence,
                                self.dexterity,
                                self.constitution,
                                self.luck))
            answer = input("Choose a stat")
            if answer == "strength":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.strength = int(answer)
            elif answer == "intelligence":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.intelligence = int(answer)
            elif answer == "dexterity":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.dexterity = int(answer)
            elif answer == "constitution":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.constitution = int(answer)
            elif answer == "luck":
                answer = input("How many points? ")
                if int(answer) < 11 & int(answer) > statpoints & int(answer) > 0:
                    self.luck = int(answer)
            else:
                print("Please try again \nMake sure the number is larger than 0 and no higher than 10")

    def createcharacter(self):
        self.name = input("What is your name? ")
        print("Welcome: %s" % self.name)
        print("Generating Stats")
        self.getstats()
        self.chooseclass()
        self.gethealth()
        self.magic = 50 + (self.intelligence * 5)
        self.stamina = 100 + (self.dexterity * 2)

    def gethealth(self):
        basehealth = 100
        modifiedhealth = (self.constitution * 10)
        self.health = (basehealth + modifiedhealth) * self.healthmodifier

    def getstats(self):
        stats = {"strength": 0, "intelligence": 0, "dexterity": 0, "constitution": 0, "luck": 0}
        for stat in stats:
            stats[stat] = self.generatestats()
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
        self.strength = stats["strength"]
        self.intelligence = stats["intelligence"]
        self.dexterity = stats["dexterity"]
        self.constitution = stats["constitution"]
        self.luck = stats["luck"]

    def generatestats(self):
        minimum = 1
        maximum = 10
        number = randint(minimum, maximum)
        if number == minimum:
            minimum += 1
            number = randint(minimum, maximum)
        return number

    def chooseclass(self):
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
                              self.health,
                              self.magic,
                              self.stamina,
                              self.strength,
                              self.intelligence,
                              self.dexterity,
                              self.constitution,
                              self.luck))

Playercharacter = Basecharacter()
