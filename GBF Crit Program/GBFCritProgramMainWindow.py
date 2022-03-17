import SelectSummonFrame as ssf
import SelectWeaponFrame as swf
import ShowSelectedWeaponsFrame as sswf
import ShowTotalCritValueFrame as stcv
from SummonClass import Summon
from WeaponClass import Weapon
from tkinter import Tk
from tkinter import Button
from tkinter import Label

# Variables

mainFrame = Tk()    # Create the main frame window
mainFrame.geometry('1280x720')
mainFrame.title("Crit calculator")

selectedSummon = []    # The summon selected by the user

selectedWeaponsList = []    # List of weapons selected by the user

def main_window():
    '''Creates the main window and all its functions'''

    mainLabel = Label(mainFrame, text = "GBF's crit calculator")
    mainLabel.place(x = 585, y = 25)

    summmonPickLabel = Label(mainFrame, text = "Pick a summon option: ")
    summmonPickLabel.place(x = 50, y = 125)

    singleSummon = "Single"

    singleSummonButton = Button(mainFrame, text = "Single summon", command = lambda: select_summon(singleSummon, mainFrame))
    singleSummonButton.place(x = 75, y = 150)

    doubleSummon = "Double"

    doubleSummonButton = Button(mainFrame, text = "Double summon", command = lambda: select_summon(doubleSummon, mainFrame))
    doubleSummonButton.place(x = 350, y = 150)

    anotherSummonButton = Button(mainFrame, text = "Another summon (like double Huanglong strats, or whatever)", command = lambda: another_summon_option(mainFrame))
    anotherSummonButton.place(x = 625, y = 150)

    addWeaponButton = Button(mainFrame, text = "Add weapon", command = select_weapon_window)
    addWeaponButton.place(x = 75, y = 275)

    deleteWeaponButton = Button(mainFrame, text = "Delete weapon", command = delete_weapon)
    deleteWeaponButton.place(x = 200, y = 275)

    showSelectedWeaponsButton = Button(mainFrame, text = "Show selected weapons", command = show_selected_weapons)
    showSelectedWeaponsButton.place(x = 325, y = 275)

    calculateCritButton = Button(mainFrame, text = "Calculate crit value", command = calculate_crit_value)
    calculateCritButton.place(x = 580, y = 500)

def select_summon(summonState, frame):
    '''Calls the function to pick a magna/primal summon'''

    ssf.select_summon(summonState, frame)

    selectedSummon = ssf.get_selected_summon()

def another_summon_option(frame):
    '''Calls the function to pick a non-magna/primal summon'''

    ssf.another_summon_option(frame)

    selectedSummon = ssf.get_selected_summon()

def select_weapon_window():
    '''Calls the function to add weapons'''

    selectedSummon = ssf.get_selected_summon()

    swf.select_weapon_window(selectedSummon)

def delete_weapon():
    '''Calls the function to delete a weapon'''

    swf.delete_weapon()

def show_selected_weapons():
    '''Calls the function to show the selected weapons'''

    selectedWeaponsList = swf.get_weapon_list()

    sswf.show_selected_weapons(selectedWeaponsList)

def calculate_crit_value():
    '''Calls the function to calculate the total crit value'''

    selectedSummon = ssf.get_selected_summon()

    selectedWeaponsList = swf.get_weapon_list()

    stcv.show_total_crit_value(selectedSummon, selectedWeaponsList)

main_window()

mainFrame.mainloop()