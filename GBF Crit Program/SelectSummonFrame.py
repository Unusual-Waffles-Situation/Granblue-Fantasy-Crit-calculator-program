import OperationsWithJSON as owj
from SummonClass import Summon
from tkinter import Tk
from tkinter import Button
from tkinter import BOTTOM
from tkinter import Label
from tkinter import ttk

# Variables

selectedSummonList = []    # The selected summon

magnaSummonsList = []    # List of summons containing all the information of the magna-type summons
primalSummonsList = []    # List of summons containing all the information of the primal-type summons

magnaSummonsList = owj.get_magna_summons()
primalSummonsList = owj.get_primal_summons()

def another_summon_option(mainFrameVar):
    '''When selecting the "Another summon" option'''

    selectedSummonInfoText = "Selected summon: Non magna/primal summon"

    selectedSummonInfoLabel = Label(mainFrameVar, text = selectedSummonInfoText)
    selectedSummonInfoLabel.place(x = 50, y = 200)

    summon = Summon("", "", "", "")

    check_summon_list(summon)

def select_summon(selectedSummonOption, mainFrameVariable):
    '''Create a frame for selecting the summon'''

    summonState = selectedSummonOption

    summonSelectionFrame = Tk()
    summonSelectionFrame.geometry('600x400')
    summonSelectionFrame.title("Summon selection")

    selecSummonLabel = Label(summonSelectionFrame, text = "Select a summon: ")
    selecSummonLabel.place(x = 50, y = 50)

    summonsCB = ttk.Combobox(summonSelectionFrame, state = "readonly")
    summonsCB.place(x = 75, y = 100)

    summonNameList = []
    summonAmount = len(magnaSummonsList)

    for i in range(summonAmount):
        summonNameList.append(magnaSummonsList[i].summonName)

    for k in range(summonAmount):
        summonNameList.append(primalSummonsList[k].summonName)
    
    summonsCB["values"] = summonNameList

    nextButton = Button(summonSelectionFrame, text = "Next", command = lambda: save_summon_info(summonsCB, summonSelectionFrame, summonState, mainFrameVariable)).pack(side = BOTTOM)

def save_summon_info(summonCB, summonFrame, summonState, mainFrameVar):
    '''Save the selected summon. This will be the selected summon used for the operations'''

    selectedSummonName = get_combobox_value(summonCB)

    selectedSummon = get_summon(selectedSummonName, summonState)

    summonFrame.destroy()

    selectedSummonInfoText = "Selected summon: " + selectedSummonName + " (" + summonState + ")."

    selectedSummonInfoLabel = Label(mainFrameVar, text = selectedSummonInfoText)
    selectedSummonInfoLabel.place(x = 50, y = 200)

    check_summon_list(selectedSummon)

def check_summon_list(summon):
    '''Check if there's already a selected summon or not'''

    isListEmpty = len(selectedSummonList)

    if isListEmpty == 0:
        selectedSummonList.append(summon)

    else:
        selectedSummonList[0].summonName = summon.summonName
        selectedSummonList[0].summonType = summon.summonType
        selectedSummonList[0].summonElement = summon.summonElement
        selectedSummonList[0].summonState = summon.summonState

def get_summon(selectedSummonName, sumState):
    '''Return a summon-type object for the selected summon name. This will be the selected summon used for the operations'''

    summonName = ""
    summonType = ""
    summonElement = ""
    state = ""

    summon = Summon(summonName, summonType, summonElement, state)

    summonAmount = len(magnaSummonsList)

    for i in range(summonAmount):
        if selectedSummonName in magnaSummonsList[i].summonName:    # Check if the name of the summon is in the magna summon list
            summonName = magnaSummonsList[i].summonName
            summonType = magnaSummonsList[i].summonType
            summonElement = magnaSummonsList[i].summonElement
            state = sumState

            summon.summonName = summonName
            summon.summonType = summonType
            summon.summonElement = summonElement
            summon.summonState = state

            return summon

    for k in range(summonAmount):
        if selectedSummonName in primalSummonsList[k].summonName:    # Check if the name of the summon is in the primal summon list
            summonName = primalSummonsList[k].summonName
            summonType = primalSummonsList[k].summonType
            summonElement = primalSummonsList[k].summonElement
            state = sumState

            summon.summonName = summonName
            summon.summonType = summonType
            summon.summonElement = summonElement
            summon.summonState = state

            return summon

    return summon

def get_combobox_value(ComboVal):
    '''Return the option selected in the Combobox'''

    selectedOption = "" + str(ComboVal.get())

    return selectedOption

def get_selected_summon():
    '''Return the selected summon by the user'''
    
    return selectedSummonList