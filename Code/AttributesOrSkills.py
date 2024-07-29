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
        self.minVal = 1

        '''
        AttributeNames = "Strength Dexterity Stamina Charisma Manipulation Appearance Perception Intelligence Wits"
        self.AttributesNamesList = AttributeNames.split()
        '''
        
        super().__init__()
    
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

class Strength(Attribute):
    def __init__(self):
        self.name = "Strength"
        self.attributeCategory = "Physical"

        super().__init__()
        
strength = Strength()
print(strength.name, strength.minVal, strength.maxVal, strength.attributeCategory)

    
# AttributesList = list()



# print(type(AttributesNamesList))