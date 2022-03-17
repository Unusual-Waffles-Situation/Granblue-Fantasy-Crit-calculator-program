import json
from SummonClass import Summon
from WeaponClass import Weapon

# Variables

summonsJSON = "Summons.json"    # Invoke the JSON which contains all the summons
weaponsJSON = "Weapons.json"    # Invoke the JSON which contains all the weapons

def get_magna_summons():
    '''Return a list with the information of all the magna summons'''

    with open(summonsJSON) as json_file:
        data = json.load(json_file)

    summonList = []

    summonType = "Magna"

    for i in data[summonType]:
        name = i["Name"]
        element = i["Element"]
        state = ""
        
        summon = Summon(name, summonType, element, state)

        summonList.append(summon)

    return summonList

def get_primal_summons():
    '''Return a list with the information of all the primal summons'''

    with open(summonsJSON) as json_file:
        data = json.load(json_file)

    summonList = []

    summonType = "Primal"

    for i in data[summonType]:
        name = i["Name"]
        element = i["Element"]
        state = ""

        summon = Summon(name, summonType, element, state)

        summonList.append(summon)

    return summonList

def get_magna_weapons():
    '''Return a list with the information of all the magna weapons'''

    with open(weaponsJSON) as json_file:
        data = json.load(json_file)

    weaponList = []

    weaponType = "Magna"

    for i in data[weaponType]:
        name = i["Name"]
        critType = i["Crit type"]
        element = i["Element"]
        maxSkillLevel = i["Maximum skill level"]
        amount = ""

        weapon = Weapon(name, critType, weaponType, element, maxSkillLevel, amount)

        weaponList.append(weapon)

    return weaponList

def get_primal_weapons():
    '''Return a list with the information of all the primal weapons'''

    with open(weaponsJSON) as json_file:
        data = json.load(json_file)

    weaponList = []

    weaponType = "Primal"

    for i in data[weaponType]:
        name = i["Name"]
        critType = i["Crit type"]
        element = i["Element"]
        maxSkillLevel = i["Maximum skill level"]
        amount = ""

        weapon = Weapon(name, critType, weaponType, element, maxSkillLevel, amount)

        weaponList.append(weapon)

    return weaponList    