from WeaponClass import Weapon
from tkinter import Tk
from tkinter import scrolledtext
import tkinter as tk
from tkinter import END

def show_selected_weapons(weaponList):
    '''Shows the selected weapons by the user. It's an scrolled text'''

    showWeaponsFrame = Tk()
    showWeaponsFrame.geometry("765x400")
    showWeaponsFrame.title("Selected weapons")

    text_area = scrolledtext.ScrolledText(showWeaponsFrame,  
                                      wrap = tk.WORD,  
                                      width = 60,  
                                      height = 5,  
                                      font = ("Times New Roman", 
                                              15)) 
  
    text_area.grid(column = 0, pady = 10, padx = 10)

    text_area.focus()

    listSize = len(weaponList)

    for i in range(listSize):
        string = ""

        string += "Weapon name: " + weaponList[i].weaponName + '\n'
        string += "Weapon amount: " + str(weaponList[i].weaponAmount) + '\n'
        string += "Weapon skill level: " + str(weaponList[i].weaponSkillLevel) + '\n'

        text_area.insert(END, string + "\n")

    text_area.configure(state = "disabled")