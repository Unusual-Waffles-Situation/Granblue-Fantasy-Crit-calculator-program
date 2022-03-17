def calculate_crit_value(skillLevel, summonState, skillType, summonType, weaponModType, summonElement, weaponElement):
    '''Calculate the crit value of a certain weapon'''

    auraValue = get_aura_value(summonState, summonType, weaponModType, summonElement, weaponElement)
    
    substractionValue = get_subs_value(summonState, skillType, summonType, weaponModType, summonElement, weaponElement)

    decimalPorcentageValue = get_decimal_porcentage_value(skillType)

    critValue = round(((decimalPorcentageValue * skillLevel) + auraValue) - substractionValue, 2)

    return critValue

def get_aura_value(summonState, summonType, weaponModType, summonElement, weaponElement):
    ''' Check if the using a single or double summon, and return the aura value'''

    auraValue = 0

    if summonType == weaponModType and summonElement == weaponElement:
        if summonState == "Single":    # Check if only using a single summon (be it main or support)
            auraValue = 14

        elif summonState == "Double":    # Check if using double summons (main AND support are the same)
            auraValue = 28

    return auraValue

def get_subs_value(summonState, skillType, summonType, weaponModType, summonElement, weaponElement):
    '''Get the substraction value for the formula (if the crit type is Med, return 4.9/9.8. If using Big, returns 0)'''

    substractionValue = 0

    if summonType == weaponModType and summonElement == weaponElement:
        if summonState == "Single" and skillType == "Med":    # Check if only using a single summon (be it main or support)
            substractionValue = 4.9                            # AND if the weapon's crit type is medium

        elif summonState == "Double" and skillType == "Med":    # Check if using double summons (main AND support are the same)
            substractionValue = 9.8                              # AND if the weapon's crit type is medium

    return substractionValue

def get_decimal_porcentage_value(skillType):
    '''Returns the decimal value of a single porcentage, be it Med (0.434) or Big (0.67)'''

    decValue = 0

    if skillType in "Med":
        decValue = 0.434

    elif skillType in "Big":
        decValue = 0.67

    return decValue

def calculate_total_crit_value(critValuesList):
    '''Return the total sum (in porcentage) of all the weapons selected'''

    listLength = len(critValuesList)

    totalSum = 0

    for i in range(listLength):
        totalSum += critValuesList[i]

    return totalSum