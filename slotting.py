"""
Debater class:
Name (string)
Skill (int)
PartnerSkillHistory (list)
PositionHistory (Dict, Pos:#)
LastPartner (debater)
def getPSH(self)

Sort list of attendees by PSH+Skill
Top+Bottom pairings into teams
Protect last partner
Sort teams by combined skill
Quadrant brackets into rooms
Room positions based on best ratio
"""    
import math       
class Debater():
    '''
    Each UADS member is a debater
    '''
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.partnerSkillHistory = []
        self.positionHistory = {}
        self.lastPartner = None

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def getPSH(self):
        try:
            return sum(self.partnerSkillHistory)/len(self.partnerSkillHistory)
        except ZeroDivisionError:
            return 0
def slotRound(selection):
    today = [debater for debater in selection]
    today.sort(key = lambda x: x.getPSH())#+x.skill)
    split = len(today)//2
    # Protect last partner pairing
    for i in range(split):
        if today[i].lastPartner == today[len(today)-i-1]:
            if i == split-1:
                today[i], today[i-1] = today[i-1], today[i]
            else:
                today[i], today[i+1] = today[i+1], today[i]
    teams = []
    for i in range(split):
        teams.append((today[i], today[len(today)-i-1]))
    for t in teams:
        t[0].partnerSkillHistory.append(t[1].skill)
        t[0].lastpartner = t[1]
        t[1].lastpartner = t[0]
        t[1].partnerSkillHistory.append(t[0].skill)
    teams.sort(key = lambda x: x[0].skill + x[1].skill)
    print(teams)

def newRound(selection):
    numdeb = len(selection)
    history = [debater for debater in selection]
    history.sort(key = lambda x: -1 * x.getPSH())
    skills = [debater for debater in selection]
    skills.sort(key = lambda x: x.skill)
    split = numdeb//2
    # Protect last partner pairing
    for i in range(numdeb):
        if history[i] == skills[i]:
            if i == numdeb-1:
                history[i], history[i-1] = history[i-1], history[i]
            else:
                history[i], history[i+1] = history[i+1], history[i]
    teams = []
    for i in range(numdeb):
        teams.append((history[i], skills[i]))
    for t in teams:
        t[0].partnerSkillHistory.append(t[1].skill)
        t[0].lastpartner = t[1]
        t[1].lastpartner = t[0]
        t[1].partnerSkillHistory.append(t[0].skill)
    teams.sort(key = lambda x: x[0].skill + x[1].skill)
    print(teams)

def splitRound(selection):
    numdeb = len(selection)
    indeb = numdeb//2 -1
    skills = [debater for debater in selection]
    skills.sort(key = lambda x: x.skill)
    b1 = []
    b2 = []
    for i in range(indeb+1):
        b1.append(skills.pop())
    for i in range(indeb+1):
        b2.append(skills.pop())
    b1.sort(key = lambda x: x.getPSH())
    split = numdeb//2
    # Protect last partner pairing
    for i in range(indeb):
        if b1[i] == b2[i].lastPartner:
            if i == indeb:
                b1[i], b1[i-1] = b1[i-1], b1[i]
            else:
                b1[i], b1[i+1] = b1[i+1], b1[i]
    teams = []
    for i in range(len(b1)):
        teams.append((b1[i], b2[i]))
    for t in teams:
        t[0].partnerSkillHistory.append(t[1].skill)
        t[0].lastPartner = t[1]
        t[1].lastPartner = t[0]
        t[1].partnerSkillHistory.append(t[0].skill)
    teams.sort(key = lambda x: x[0].skill + x[1].skill)
    print(teams)

def testSlot():
    import random
    even = [i for i in range(8, 37, 2)]
    teams = []
    for i in range(40):
        teams.append(Debater(str(i), random.randint(1, 10)))
    for i in range(50):
        splitRound(random.sample(teams, random.sample(even, 1)[0]))
    teams.sort(key = lambda x: x.skill)
    for x in teams:
        print(x.skill, " ", x.getPSH())

a = Debater("Anne", 3)
b = Debater("Bob", 5)
c = Debater("Carol", 7)
d = Debater("Iain", 9)
e = Debater("Sue", 2)
f = Debater("Larry", 4)
g = Debater("Tom", 9)
h = Debater("Dude", 6)

