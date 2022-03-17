import OperationsWithJSON as owj
import CritOperations as co
from WeaponClass import Weapon
from tkinter import Tk
from tkinter import StringVar
from tkinter import Button
from tkinter import BOTTOM
from tkinter import Label
from tkinter import ttk
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter import RIGHT

# Variables

testFrame = Tk()
testFrame.state("withdrawn")

selectedWeaponsList = []    # List of weapons selected by the user

numberOfWeaponsInGrid = []    # The numbers of weapon that are currently in the grid.
                              # Used to control the user from selecting more than 10 weapons

weaponAmountIV = StringVar()    # Save the desired amount of the selected weapon
weaponSkillLevelIV = StringVar()    # Save the skill level of the selected weapon

magnaWeaponsList = []    # List of weapons containing all the information of the magna-type weapons
primalWeaponsList = []    # List of weapons containing all the information of the primal-type weapons

magnaWeaponsList = owj.get_magna_weapons()
primalWeaponsList = owj.get_primal_weapons()

testFrame.destroy()

def get_combobox_value(ComboVal):
    '''Return the option selected in the Combobox'''

    selectedOption = "" + str(ComboVal.get())

    return selectedOption

def get_scale_value(scaleVal):
    '''Return the option picked in the Scale'''

    selectedOption = int(scaleVal.get())

    return selectedOption

def get_weapon_list():
    '''Return the weapon list'''

    return selectedWeaponsList

def is_weapon_list_empty():
    '''Check if the there are any weapons added on the list. Used to check if a weapon can be deleted'''

    amount = len(selectedWeaponsList)

    if amount == 0:
        return True    # Return True if the list is empty
    
    else:
        False    # Return False if the list is not empty

def select_weapon_window(summon):
    '''Frame for selecting a weapon'''

    selectWeaponFrame = Tk()
    selectWeaponFrame.geometry("600x400")
    selectWeaponFrame.title("Select a weapon")

    selectWeaponLabel = Label(selectWeaponFrame, text = "Select a weapon: ")
    selectWeaponLabel.place(x = 50, y = 50)

    weaponsCB = ttk.Combobox(selectWeaponFrame, state = "readonly")
    weaponsCB.place(x = 75, y = 100)

    weaponNameList = []
    magnaWeaponAmount = len(magnaWeaponsList)
    primalWeaponAmount = len(primalWeaponsList)

    for i in range(magnaWeaponAmount):
        weaponNameList.append(magnaWeaponsList[i].weaponName)

    for k in range(primalWeaponAmount):
        weaponNameList.append(primalWeaponsList[k].weaponName)
    
    weaponsCB["values"] = weaponNameList
    
    weaponOptionButton = Button(selectWeaponFrame, text = "Choose weapon options", command = lambda: weapon_options(weaponsCB, magnaWeaponAmount, primalWeaponAmount, selectWeaponFrame, summon)).pack(side = BOTTOM)

def weapon_options(weaponCB, magnaAmount, primalAmount, weaponFrame, summon):
    '''Show the selected weapon options (weapon amount and weapon skill level)'''

    weaponName = get_combobox_value(weaponCB)

    selectedWeapon = get_selected_weapon_info(weaponName, magnaAmount, primalAmount)

    selectedWeaponAmountLabel = Label(weaponFrame, text = "Select the amount of weapons: ")
    selectedWeaponAmountLabel.place(x = 75, y = 150)

    weaponsSelected = len(selectedWeaponsList)

    if weaponsSelected > 0:
        weaponsSelected = numberOfWeaponsInGrid[0]

    maximumNumberOfWeapons = 10 - weaponsSelected

    selectedWeaponAmountScale = Scale(weaponFrame, variable = weaponAmountIV, orient = HORIZONTAL, from_ = 1, to = maximumNumberOfWeapons)
    selectedWeaponAmountScale.place(x = 75, y = 200)

    selectedWeaponSkillLevelLabel = Label(weaponFrame, text = "Select the weapon skill level: ")
    selectedWeaponSkillLevelLabel.place(x = 350, y = 150)

    selectedWeaponMaxSkillLevel = selectedWeapon.weaponSkillLevel

    selectedWeaponSkillLevelScale = Scale(weaponFrame, variable = weaponSkillLevelIV, orient = HORIZONTAL, from_ = 1, to = int(selectedWeaponMaxSkillLevel))
    selectedWeaponSkillLevelScale.place(x = 350, y = 200)

    nextButton = Button(weaponFrame, text = "Next", command = lambda: add_weapon(weaponFrame, selectedWeapon, selectedWeaponAmountScale, selectedWeaponSkillLevelScale, summon)). pack(side = RIGHT)    

def add_weapon(weaponFrame, weapon, amountScale, skillScale, summon):
    '''Add the selected weapon (with its options) to the weapon list and calculate the crit value'''

    weaponAmount = get_scale_value(amountScale)

    skillLevel = get_scale_value(skillScale)

    weapon.weaponAmount = weaponAmount

    weapon.weaponSkillLevel = skillLevel

    selectedWeaponsList.append(weapon)

    reduce_grid_capacity(weaponAmount)

    weaponFrame.destroy()

def get_selected_weapon_info(selectedWeaponName, magnaAmount, primalAmount):
    '''Return a weapon-type object for the selected summon name'''

    weaponName = ""
    weaponCritType = ""
    weaponModType = ""
    weaponElement = ""
    weaponSkillLevel = ""
    weaponAmount = ""

    weapon = Weapon(weaponName, weaponCritType, weaponModType, weaponElement, weaponSkillLevel, weaponAmount)

    for i in range(magnaAmount):
        if selectedWeaponName in magnaWeaponsList[i].weaponName:
            weaponName = magnaWeaponsList[i].weaponName
            weaponCritType = magnaWeaponsList[i].critSkillType
            weaponModType = magnaWeaponsList[i].weaponModType
            weaponElement = magnaWeaponsList[i].weaponElement
            weaponSkillLevel = magnaWeaponsList[i].weaponSkillLevel

            weapon.weaponName = weaponName
            weapon.critSkillType = weaponCritType
            weapon.weaponModType = weaponModType
            weapon.weaponElement = weaponElement
            weapon.weaponSkillLevel = weaponSkillLevel

            return weapon

    for k in range(primalAmount):
        if selectedWeaponName in primalWeaponsList[k].weaponName:
            weaponName = primalWeaponsList[k].weaponName
            weaponCritType = primalWeaponsList[k].critSkillType
            weaponModType = primalWeaponsList[k].weaponModType
            weaponElement = primalWeaponsList[k].weaponElement
            weaponSkillLevel = primalWeaponsList[k].weaponSkillLevel

            weapon.weaponName = weaponName
            weapon.critSkillType = weaponCritType
            weapon.weaponModType = weaponModType
            weapon.weaponElement = weaponElement
            weapon.weaponSkillLevel = weaponSkillLevel

            return weapon

    return weapon

def reduce_grid_capacity(amount):
    '''Function to control how many weapons has the user selected'''

    totalWeapons = len(numberOfWeaponsInGrid)

    if totalWeapons == 0:
        numberOfWeaponsInGrid.append(amount)

    else:
        totalWeapons = numberOfWeaponsInGrid[0]
        totalWeapons += amount

        numberOfWeaponsInGrid[0] = totalWeapons

def increase_grid_capacity(amount):
    '''Function to increase the grid capacity. It's used when the user deletes a weapon'''

    totalWeapons = len(numberOfWeaponsInGrid)

    if totalWeapons > 0:
        totalWeapons = numberOfWeaponsInGrid[0]
        totalWeapons -= amount

        numberOfWeaponsInGrid[0] = totalWeapons


def delete_weapon():
    '''Delete the last weapon added'''

    lastWeaponIndex = len(selectedWeaponsList)
    lastWeaponIndex -= 1

    if lastWeaponIndex >= 0:
        weaponAmount = selectedWeaponsList[lastWeaponIndex].weaponAmount

        increase_grid_capacity(weaponAmount)

        selectedWeaponsList.pop()