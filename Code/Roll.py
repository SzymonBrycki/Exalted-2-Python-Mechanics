import random

class Roll():
    def __init__(self):
        self.diceMax = 10

    def roll1(self, success=7):
        resultList = list()
        roll = random.randrange(1, self.diceMax)
        if roll >= success:
            resultList.append(1)
            resultList.append(roll)
            return resultList
        elif roll == 10:
            resultList.append(2)
            resultList.append(roll)
        else:
            resultList.append(0)
            resultList.append(roll)
        
        return resultList
        
    def rollX(self, x, success=7):
        succCount = 0
        resultsList = list()
        while x != 0:
            n = Roll.roll1(self)
            if n[0] == 1:
                succCount += 1
                resultsList.append(n[1])
            elif n[0] == 2:
                succCount += 2
                resultsList.append(n[1])
            else:
                resultsList.append(n[1])
            x -= 1

        allList= list()
        allList.append(succCount)
        allList.append(resultsList)
        
        return allList

roll = Roll()

'''
for x in range (1, 10):
    print(roll.roll1())
'''

print(roll.rollX(20))