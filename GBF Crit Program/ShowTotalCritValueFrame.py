from tkinter import Tk
from tkinter import Label
from WeaponClass import Weapon
from SummonClass import Summon
import CritOperations as co

def show_total_crit_value(summon, weaponList):
    '''Shows the total crit value'''

    critValueFrame = Tk()
    critValueFrame.geometry("350x200")
    critValueFrame.title("Total crit value")

    critValue = calculate_crit(summon, weaponList)

    critText = "The total crit value is " + str(critValue) + "%"

    critValueLabel = Label(critValueFrame, text = critText)
    critValueLabel.place(x = 85, y = 80)

def calculate_crit(summon, weaponList):
    '''Calculate the crit values of all the selected weapons'''

    size = len(weaponList)

    critValueList = []

    for i in range(size):
        skillLevel = weaponList[i].weaponSkillLevel

        summonState = summon[0].summonState

        weaponCritType = weaponList[0].critSkillType

        summonType = summon[0].summonType

        weaponType = weaponList[i].weaponModType

        summonElement = summon[0].summonElement

        weaponElement = weaponList[i].weaponElement

        weaponAmount = weaponList[i].weaponAmount

        critValue = co.calculate_crit_value(skillLevel, summonState, weaponCritType, summonType, weaponType, summonElement, weaponElement)

        critValue = critValue * weaponAmount

        critValueList.append(critValue)

    totalCritValue = co.calculate_total_crit_value(critValueList)

    return totalCritValue