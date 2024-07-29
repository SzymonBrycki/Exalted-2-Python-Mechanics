# Attributes or Skills

class AttributeOrSkill:
    def __init__(self):

        # POOOOTEM!!!
        '''
        if Character.Essence >= 6:
            self.maxVal = Character.Essence

        else:
            self.maxVal = 5
        '''

        self.maxVal = 5

class Attribute(AttributeOrSkill):
    def __init__(self):
        super().__init__()
        self.minVal = 1

        '''
        AttributeNames = "Strength Dexterity Stamina Charisma Manipulation Appearance Perception Intelligence Wits"
        self.AttributesNamesList = AttributeNames.split()
        '''
    
    '''
    def attributeCategory(self, nameOfAttribute):
        if nameOfAttribute in self.AttributesNamesList[0:2]:
            return "Physical"
        elif nameOfAttribute in self.AttributesNamesList[3:5]:
            return  "Social"
        elif nameOfAttribute in self.AttributesNamesList[6:8]:
            return "Mental"
        else:
            raise ValueError
    '''

class Skill(AttributeOrSkill):
    def __init__(self):
        super().__init__()
        self.minVal = 0

#################
#
# ATTRIBUTES
#
#################

class Strength(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Strength"
        self.attributeCategory = "Physical"


class Dexterity(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Dexterity"
        self.attributeCategory = "Physical"

class Stamina(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Stamina"
        self.attributeCategory = "Physical"

class Charisma(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Charisma"
        self.attributeCategory = "Social"

class Manipulation(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Manipulation"
        self.attributeCategory = "Social"

class Appearance(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Appearance"
        self.attributeCategory = "Social"

class Perception(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Perception"
        self.attributeCategory = "Mental"

class Intelligence(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Intelligence"
        self.attributeCategory = "Mental"

class Wits(Attribute):
    def __init__(self):
        super().__init__()
        self.attVal = self.minVal
        self.name = "Wits"
        self.attributeCategory = "Mental"

#################
#
# SKILLS
#
#################

# Dawn

class Archery(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Archery"

class MartialArts(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Martial Arts"

class Melee(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Melee"

class Thrown(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Thrown"

class War(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "War"

# Zenith

class Integrity(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Integrity"

class Performance(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Performance"

class Presence(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Presence"

class Resistance(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Resistance"

class Survival(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Survival"

# Twilight

class Craft(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Craft"

class Investigation(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Investigation"

class Lore(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Lore"

class Medicine(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Medicine"

class Occult(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Occult"

# Night

class Athletics(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Athletics"

class Awareness(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Awareness"

class Dodge(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Dodge"

class Larceny(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Larceny"

class Stealth(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Stealth"

# Eclipse

class Bureaucracy(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Bureaucracy"

class Linguistics(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Linguistics"

class Ride(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Ride"

class Sail(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Sail"

class Socialize(Skill):
    def __init__(self):
        super().__init__()
        self.skillVal = self.minVal
        self.name = "Socialize"

strength = Strength()
print(strength.name, strength.minVal, strength.maxVal, strength.attributeCategory, strength.attVal)

socialize = Socialize()
print(socialize.name, socialize.minVal, socialize.maxVal, socialize.skillVal)
    
# AttributesList = list()

# print(type(AttributesNamesList))